# -*- coding: utf-8 -*-
"""
Scan one or more kb.4d.com asset IDs and report their metadata + best
download link, WITHOUT downloading/extracting anything. Use this first to
see what you're dealing with before running extract_asset.py.

Usage:
    export KB4D_COOKIE="4DSID_KBv20=<value>"
    python3 scripts/scan_asset.py 80085 79100 51814
    python3 scripts/scan_asset.py --file ids.json      # JSON array of ints
    python3 scripts/scan_asset.py --range 80085 70086  # inclusive, descending

Output: JSON array of scan results (one dict per asset, or a
{"id": ..., "type": "not_found"} / {"id": ..., "type": "tech_tip_or_other"}
placeholder for non-Tech-Note / invalid IDs), printed to stdout.
"""
import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import fetch_asset_page, parse_asset_page


def scan_one(assetid):
    try:
        html_body = fetch_asset_page(assetid)
    except Exception as e:
        return {"id": assetid, "type": "error", "error": str(e)}

    parsed = parse_asset_page(assetid, html_body)
    if parsed is None:
        if "Requested asset cannot be found" in html_body:
            return {"id": assetid, "type": "not_found"}
        return {"id": assetid, "type": "tech_tip_or_other"}
    return parsed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", type=int, help="asset IDs to scan")
    ap.add_argument("--file", help="JSON file containing an array of asset IDs")
    ap.add_argument("--range", nargs=2, type=int, metavar=("FROM", "TO"),
                     help="scan an inclusive descending range, e.g. --range 80085 70086")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    ids = list(args.ids)
    if args.file:
        ids.extend(json.load(open(args.file)))
    if args.range:
        hi, lo = args.range
        ids.extend(range(hi, lo - 1, -1))

    if not ids:
        ap.error("no asset IDs given (positional args, --file, or --range)")

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(scan_one, i): i for i in ids}
        done = 0
        for fut in as_completed(futs):
            results.append(fut.result())
            done += 1
            if done % 50 == 0:
                print(f"  scanned {done}/{len(ids)}", file=sys.stderr)

    results.sort(key=lambda r: -r["id"])
    technotes = [r for r in results if r.get("type") == "technote"]
    print(
        f"Scanned {len(results)}: {len(technotes)} Tech Notes, "
        f"{len(results) - len(technotes)} skipped (not found / not a Tech Note)",
        file=sys.stderr,
    )
    json.dump(results, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
