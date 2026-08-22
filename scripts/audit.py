# -*- coding: utf-8 -*-
"""
Audit the technotes/ folder against the master asset list, and report
completeness / quality stats. Safe, read-only -- never modifies anything.

Usage:
    python3 scripts/audit.py                       # uses technotes/all_technotes.json
    python3 scripts/audit.py --master /tmp/all_technotes.json

Prints a plain-text report to stdout covering:
  - folder count vs. master list count (missing / extra asset IDs)
  - JSON validity of every meta.json
  - content_source tally (full_pdf / teaser_only / missing key)
  - historical_commentary.status value tally (flags spelling drift)
  - year-by-year teaser_only rate (useful for spotting archive-era bias)
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TECHNOTES_DIR = os.path.join(REPO_ROOT, "technotes")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default=os.path.join(TECHNOTES_DIR, "all_technotes.json"))
    args = ap.parse_args()

    master_ids = set()
    if os.path.exists(args.master):
        master = json.load(open(args.master))
        master_ids = {int(a.get("assetid") or a.get("id")) for a in master}
    else:
        print(f"WARNING: master list not found at {args.master}; "
              f"skipping missing/extra-ID check.\n"
              f"(Regenerate it with scripts/fetch_all_technotes.py)", file=sys.stderr)

    folders = sorted(
        d for d in os.listdir(TECHNOTES_DIR)
        if os.path.isdir(os.path.join(TECHNOTES_DIR, d)) and re.match(r"^\d+_", d)
    )
    folder_ids = {int(d.split("_", 1)[0]) for d in folders}

    print(f"Folders on disk: {len(folders)}")
    if master_ids:
        print(f"Master list total: {len(master_ids)}")
        missing = master_ids - folder_ids
        extra = folder_ids - master_ids
        print(f"Missing (in master, not on disk): {len(missing)} {sorted(missing)[:20]}")
        print(f"Extra (on disk, not in master): {len(extra)} {sorted(extra)[:20]}")

    bad_json = []
    missing_files = []
    content_source = Counter()
    status_values = Counter()
    year_teaser = Counter()
    year_total = Counter()

    for d in folders:
        folder = os.path.join(TECHNOTES_DIR, d)
        needed = ["meta.json", "subject.txt", "summary_paragraph.md", "summary_page.md"]
        for fn in needed:
            if not os.path.exists(os.path.join(folder, fn)):
                missing_files.append(f"{d}/{fn}")

        meta_path = os.path.join(folder, "meta.json")
        if not os.path.exists(meta_path):
            continue
        try:
            meta = json.load(open(meta_path))
        except Exception as e:
            bad_json.append((d, str(e)))
            continue

        cs = meta.get("content_source", "<missing key>")
        content_source[cs] += 1

        status = (meta.get("historical_commentary") or {}).get("status", "<missing>")
        status_values[status] += 1

        year = None
        pub = meta.get("published_date") or meta.get("date") or ""
        m = re.search(r"(19|20)\d{2}", pub)
        if m:
            year = m.group(0)
        else:
            m = re.search(r"(19|20)\d{2}", d)
            if m:
                year = m.group(0)
        if year:
            year_total[year] += 1
            if cs == "teaser_only":
                year_teaser[year] += 1

    print(f"\nInvalid JSON: {len(bad_json)}")
    for d, err in bad_json[:20]:
        print(f"  {d}: {err}")
    print(f"\nMissing expected files: {len(missing_files)}")
    for f in missing_files[:20]:
        print(f"  {f}")

    print("\ncontent_source tally:")
    for k, v in content_source.most_common():
        print(f"  {k}: {v}")

    print("\nhistorical_commentary.status tally (watch for spelling drift):")
    for k, v in status_values.most_common():
        print(f"  {k!r}: {v}")

    print("\nyear-by-year teaser_only rate:")
    for y in sorted(year_total):
        t = year_teaser.get(y, 0)
        n = year_total[y]
        print(f"  {y}: {t}/{n} teaser_only ({100*t/n:.0f}%)")


if __name__ == "__main__":
    main()
