# -*- coding: utf-8 -*-
"""
Download and extract the full text of one or more scanned Tech Note assets.

Prerequisites:
  - `unar` (The Unarchiver CLI) must be installed and on PATH:
        brew install unar
    This is REQUIRED for old (pre-2006) Tech Notes, whose download links are
    Windows self-extracting .exe or Mac BinHex .hqx files. Despite the
    extension, these are internally StuffIt 5 archives -- `unar` is the only
    common tool that transparently recognizes and extracts both.
  - `pdftotext` (from poppler) must be installed and on PATH:
        brew install poppler

Usage:
    export KB4D_COOKIE="4DSID_KBv20=<value>"
    python3 scripts/scan_asset.py 51814 > /tmp/scan.json
    python3 scripts/extract_asset.py /tmp/scan.json --outdir /tmp/extracted

Input: a JSON array as produced by scan_asset.py (must have "id" and "link").
Output: for each asset, writes <outdir>/<id>.txt (full text if recoverable,
otherwise the on-page teaser paragraph) and prints a manifest JSON array to
stdout with an added "content_source" field:
    "full_pdf"    - text extracted from the real downloaded document
    "teaser_only" - only the short on-page teaser could be recovered, and why:
        NO_DOWNLOAD_LINK   - the asset page has no download link at all
        NO_PDF_IN_ARCHIVE  - link downloaded but no PDF was found inside
                             (very common for pre-2006 .exe installers that
                             are not simple self-extracting archives)
        DOWNLOAD_FAILED    - the link could not be fetched (timeout / dead)
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import fetch_url


def download(url, dest, timeout=180):
    try:
        data = fetch_url(url, timeout=timeout)
        with open(dest, "wb") as f:
            f.write(data)
        return os.path.getsize(dest) > 0
    except Exception as e:
        print(f"  download failed: {url}: {e}", file=sys.stderr)
        return False


def find_pdf(root):
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.lower().endswith(".pdf"):
                return os.path.join(dirpath, fn)
    return None


def process(entry, outdir):
    aid = entry["id"]
    link = entry.get("link")
    result = dict(entry)
    txt_path = os.path.join(outdir, f"{aid}.txt")

    def fallback(reason):
        teaser = entry.get("teaser", "")
        with open(txt_path, "w") as f:
            f.write(teaser)
        result["content_source"] = "teaser_only"
        result["error_reason"] = reason
        result["text_file"] = txt_path

    if not link:
        fallback("NO_DOWNLOAD_LINK")
        return result

    ext = link.rsplit(".", 1)[-1].lower()
    raw_path = os.path.join(outdir, f"{aid}_raw.{ext}")
    if not download(link, raw_path):
        fallback("DOWNLOAD_FAILED")
        return result

    if ext == "pdf":
        pdf_path = raw_path
    else:
        extract_dir = os.path.join(outdir, f"{aid}_extract")
        os.makedirs(extract_dir, exist_ok=True)
        try:
            subprocess.run(["unar", "-f", "-o", extract_dir, raw_path],
                            capture_output=True, timeout=120)
        except Exception as e:
            print(f"  unar failed for {aid}: {e}", file=sys.stderr)
        pdf_path = find_pdf(extract_dir)

    if not pdf_path:
        fallback("NO_PDF_IN_ARCHIVE")
        return result

    try:
        subprocess.run(["pdftotext", pdf_path, txt_path], capture_output=True, timeout=60)
    except Exception as e:
        print(f"  pdftotext failed for {aid}: {e}", file=sys.stderr)

    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 20:
        result["content_source"] = "full_pdf"
        result["error_reason"] = None
        result["text_file"] = txt_path
    else:
        fallback("NO_PDF_IN_ARCHIVE")

    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scan_json", help="JSON file produced by scan_asset.py")
    ap.add_argument("--outdir", default="/tmp/kb_extract")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    entries = [e for e in json.load(open(args.scan_json)) if e.get("type") == "technote"]

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(process, e, args.outdir): e["id"] for e in entries}
        done = 0
        for fut in as_completed(futs):
            results.append(fut.result())
            done += 1
            if done % 25 == 0:
                print(f"  processed {done}/{len(entries)}", file=sys.stderr)

    results.sort(key=lambda e: -e["id"])
    full = sum(1 for r in results if r.get("content_source") == "full_pdf")
    print(f"Done: {len(results)} total, {full} full_pdf, {len(results)-full} teaser_only",
          file=sys.stderr)
    json.dump(results, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
