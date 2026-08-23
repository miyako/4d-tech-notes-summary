# -*- coding: utf-8 -*-
"""
Recover full text for legacy Tech Notes whose Windows .exe archive fails to
extract, by trying their Mac .hqx alternate download instead.

Background: most pre-2006 Tech Note pages list both a Windows self-extracting
.exe archive and a Mac BinHex .hqx alternate. When the .exe fails to yield a
PDF via `unar` (age-related corruption, unusual StuffIt encoding variants),
the Mac .hqx alternate often still works. The raw ftp://ftp.4d.com/... URL
printed on the page is dead, but kb.4d.com mirrors it over HTTPS at a
predictable path: swap "Windows" for "MacOS" in the archive's
/DLTN/TN/<year>/... path. This script tries that automatically.

This technique recovered 215 of 257 previously-teaser-only legacy notes in
one archival pass (see docs/unprocessable_urls.md for the full writeup).

Usage:
    export KB4D_COOKIE="4DSID_KBv20=<value>"
    # Recover every currently-teaser_only note that has a Mac .hqx alternate:
    python3 scripts/recover_mac_alternate.py --all
    # Or just a specific asset:
    python3 scripts/recover_mac_alternate.py --asset-id 32313
    # Or a scan_asset.py-style JSON file of {id, all_links / links} entries:
    python3 scripts/recover_mac_alternate.py --file /tmp/scan_all.json

Output: for each successfully recovered asset, writes the extracted PDF text
to <outdir>/<id>.txt (default outdir: /tmp/mac_recovery) and a
recovery_manifest.json summarizing successes/failures. This script does NOT
touch technotes/ folders directly -- feed the recovered text into
add_asset.py-style hand (or LLM-assisted) summarization afterwards, same as
any other newly-extracted full text.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import fetch_url, KB_BASE  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TECHNOTES_DIR = os.path.join(REPO_ROOT, "technotes")


def mac_url_from_links(links):
    """Given a list of hrefs scraped from an asset page, find/construct the
    kb.4d.com-hosted Mac .hqx mirror URL, or None if no alternate exists."""
    for l in links or []:
        if ".hqx" not in l.lower():
            continue
        if l.startswith(f"{KB_BASE}/"):
            return l  # already a direct, well-formed mirror URL
        # malformed "https://kb.4d.com/ftp://ftp.4d.com/..." or plain
        # "ftp://ftp.4d.com/..." forms -- extract the path after the host
        # and rebuild against the kb.4d.com/DLTN/TN/ mirror.
        m = re.search(r"ftp://[^/]*/(.*)$", l)
        if m:
            path = m.group(1)
            path = re.sub(r"^ACI_TECHNICAL_NOTES/", "", path, flags=re.I)
            return f"{KB_BASE}/DLTN/TN/{path}"
    return None


def find_pdf(root):
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.lower().endswith(".pdf"):
                return os.path.join(dirpath, fn)
    return None


def recover_one(entry, outdir):
    aid = entry["id"]
    mac_url = mac_url_from_links(entry.get("all_links") or entry.get("links"))
    result = {"id": aid, "mac_url": mac_url, "success": False}
    if not mac_url:
        result["reason"] = "NO_MAC_URL_CONSTRUCTED"
        return result

    raw_path = os.path.join(outdir, f"{aid}.hqx")
    try:
        data = fetch_url(mac_url, timeout=90)
        with open(raw_path, "wb") as f:
            f.write(data)
    except Exception as ex:
        result["reason"] = f"DOWNLOAD_FAILED: {ex}"
        return result

    extract_dir = os.path.join(outdir, f"{aid}_extract")
    os.makedirs(extract_dir, exist_ok=True)
    try:
        subprocess.run(
            ["unar", "-f", "-o", extract_dir, raw_path],
            capture_output=True, timeout=120,
        )
    except Exception as ex:
        result["reason"] = f"UNAR_FAILED: {ex}"
        return result

    pdf_path = find_pdf(extract_dir)
    if not pdf_path:
        result["reason"] = "NO_PDF_IN_EXTRACT"
        return result

    txt_path = os.path.join(outdir, f"{aid}.txt")
    try:
        subprocess.run(["pdftotext", pdf_path, txt_path], capture_output=True, timeout=60)
    except Exception as ex:
        result["reason"] = f"PDFTOTEXT_FAILED: {ex}"
        return result

    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 20:
        result["success"] = True
        result["text_file"] = txt_path
        result["pdf_file"] = pdf_path
    else:
        result["reason"] = "EMPTY_TEXT"
    return result


def teaser_only_entries():
    """Find every technotes/*/meta.json currently marked teaser_only, and
    pull its all_links from the asset page (re-scanned live) so we have
    something to search for a .hqx alternate in."""
    from common import fetch_url as _fetch  # noqa: F401
    import scan_asset  # local helper module in this folder

    entries = []
    for meta_path in glob.glob(os.path.join(TECHNOTES_DIR, "*", "meta.json")):
        meta = json.load(open(meta_path))
        if meta.get("content_source") != "teaser_only":
            continue
        aid = meta.get("asset_id")
        if not aid:
            continue
        scanned = scan_asset.scan_one(aid)
        entries.append({"id": aid, "all_links": scanned.get("all_links", [])})
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                     help="recover every technotes/*/meta.json currently marked teaser_only")
    ap.add_argument("--asset-id", type=int, help="recover a single asset id")
    ap.add_argument("--file", help="JSON file of [{id, all_links|links}, ...] entries")
    ap.add_argument("--outdir", default="/tmp/mac_recovery")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    if args.file:
        entries = json.load(open(args.file))
    elif args.asset_id:
        import scan_asset
        scanned = scan_asset.scan_one(args.asset_id)
        entries = [{"id": args.asset_id, "all_links": scanned.get("all_links", [])}]
    elif args.all:
        entries = teaser_only_entries()
    else:
        ap.error("pass one of --all, --asset-id, or --file")
        return

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(recover_one, e, args.outdir): e["id"] for e in entries}
        done = 0
        for fut in as_completed(futs):
            r = fut.result()
            results.append(r)
            done += 1
            status = "OK" if r["success"] else r.get("reason", "FAIL")
            print(f"[{done}/{len(entries)}] {r['id']}: {status}")

    success = [r for r in results if r["success"]]
    print(f"\n=== {len(success)} / {len(entries)} recovered via Mac .hqx alternate ===")
    manifest_path = os.path.join(args.outdir, "recovery_manifest.json")
    json.dump(results, open(manifest_path, "w"), indent=2)
    print(f"Manifest written to {manifest_path}")
    print(
        "\nNext step: for each successful recovery, read <outdir>/<id>.txt and "
        "hand-write (or LLM-generate) the note's 4 summary files, same as with "
        "any freshly-extracted full text -- see add_asset.py's workflow."
    )


if __name__ == "__main__":
    main()
