# -*- coding: utf-8 -*-
"""
Regenerate technotes/index.md, a single markdown table listing every
Tech Note folder with its year, version, author, historical status, and a
relative link into its summary_page.md. Run this after adding new assets.

Usage:
    python3 scripts/rebuild_index.py
"""
import json
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TECHNOTES_DIR = os.path.join(REPO_ROOT, "technotes")


def main():
    folders = sorted(
        d for d in os.listdir(TECHNOTES_DIR)
        if os.path.isdir(os.path.join(TECHNOTES_DIR, d)) and re.match(r"^\d+_", d)
    )

    rows = []
    for d in folders:
        meta_path = os.path.join(TECHNOTES_DIR, d, "meta.json")
        if not os.path.exists(meta_path):
            continue
        try:
            meta = json.load(open(meta_path))
        except Exception:
            continue

        aid = meta.get("id") or int(d.split("_", 1)[0])
        title = meta.get("title", "")
        pub = meta.get("published_date") or meta.get("date") or ""
        ym = re.search(r"(19|20)\d{2}", pub) or re.search(r"(19|20)\d{2}", d)
        year = ym.group(0) if ym else "?"
        version = meta.get("product_version") or meta.get("version") or ""
        author = meta.get("author") or ""
        status = (meta.get("historical_commentary") or {}).get("status", "")
        rows.append((aid, title, year, version, author, status, d))

    rows.sort(key=lambda r: -r[0])

    lines = [
        "# 4D Tech Notes Index",
        "",
        f"Total Tech Notes: {len(rows)}",
        "",
        "Full corpus (1996-2026), scanned via the kb.4d.com search API "
        "(see scripts/fetch_all_technotes.py) and cross-checked against the "
        "site's asset-ID space. See ../README.md for the processing "
        "methodology, completeness tally, and known limitations.",
        "",
        "| Asset ID | Title | Year | Version | Author | Status | Link |",
        "|---|---|---|---|---|---|---|",
    ]
    for aid, title, year, version, author, status, d in rows:
        title_c = title.replace("|", "\\|")
        author_c = author.replace("|", "\\|")
        lines.append(
            f"| {aid} | {title_c} | {year} | {version} | {author_c} | {status} "
            f"| [page](./{d}/summary_page.md) |"
        )

    with open(os.path.join(TECHNOTES_DIR, "index.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote index.md with {len(rows)} entries.")


if __name__ == "__main__":
    main()
