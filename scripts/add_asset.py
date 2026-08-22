# -*- coding: utf-8 -*-
"""
Scaffold the 4-file folder for one new Tech Note, ready for an LLM
(you, an agent, or a human) to fill in the actual summary content.

This does NOT write the summaries for you -- summarizing requires reading
and understanding the extracted document, which is a judgment call best
made by an LLM/human, not a fixed script. What this script DOES do:
  1. Scan the asset page (metadata + download link).
  2. Download + extract the full text (or fall back to the teaser).
  3. Create technotes/<id>_<ShortSlug>/ with:
       - meta.json           (pre-filled with id/title/version/author/date/
                               download_url/content_source; summary fields
                               left as TODO placeholders)
       - source_text.txt     (the extracted full text, for the summarizer
                               to read -- NOT part of the final 4-file set,
                               delete it once meta.json/subject.txt/
                               summary_paragraph.md/summary_page.md are done)

Usage:
    export KB4D_COOKIE="4DSID_KBv20=<value>"
    python3 scripts/add_asset.py 80106
    # then open technotes/80106_.../source_text.txt, read it, and hand-write:
    #   subject.txt, summary_paragraph.md, summary_page.md, and fill in
    #   meta.json's summary/historical_commentary fields.
    # finally: rm technotes/80106_.../source_text.txt
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import fetch_asset_page, parse_asset_page
from extract_asset import process

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TECHNOTES_DIR = os.path.join(REPO_ROOT, "technotes")


def slugify(title):
    words = re.sub(r"[^A-Za-z0-9 ]", "", title or "").split()
    slug = "".join(w[:1].upper() + w[1:] for w in words if w)
    return slug[:40] if slug else "Untitled"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("assetid", type=int)
    ap.add_argument("--force", action="store_true", help="overwrite existing folder")
    args = ap.parse_args()

    html_body = fetch_asset_page(args.assetid)
    parsed = parse_asset_page(args.assetid, html_body)
    if parsed is None:
        print(f"Asset {args.assetid} is not a valid Tech Note "
              f"(not found, or a Tech Tip / other resource type). Skipping.")
        sys.exit(1)

    print(f"Found: {parsed['title']}  ({parsed['meta']})")
    result = process(parsed, outdir="/tmp/kb_add_asset")

    slug = slugify(parsed["title"])
    folder_name = f"{args.assetid}_{slug}"
    folder = os.path.join(TECHNOTES_DIR, folder_name)
    if os.path.exists(folder) and not args.force:
        print(f"ERROR: {folder} already exists. Use --force to overwrite.")
        sys.exit(1)
    os.makedirs(folder, exist_ok=True)

    # meta.split "PRODUCT: 4D | VERSION: 21 | PLATFORM: Mac & Win"
    version = ""
    m = re.search(r"VERSION:\s*([^|]+)", parsed["meta"])
    if m:
        version = m.group(1).strip()

    meta = {
        "id": args.assetid,
        "title": parsed["title"],
        "url": f"https://kb.4d.com/assetid={args.assetid}",
        "download_url": parsed.get("link"),
        "published_date": parsed.get("date", "").replace("Published On:", "").strip(),
        "product_version": version,
        "author": "TODO - extract from document text",
        "content_source": result.get("content_source"),
        "error_reason": result.get("error_reason"),
        "summary": {
            "subject": "TODO - one-line subject",
            "paragraph": "TODO - one paragraph summary",
        },
        "featured_technology": ["TODO"],
        "historical_commentary": {
            "status": "TODO - one of: still_relevant / partially_superseded / "
                      "superseded / obsolete / historical_interest_only",
            "notes": "TODO - what changed since publication, references to "
                     "newer/updated 4D features that replace or update this",
        },
    }
    with open(os.path.join(folder, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)

    for fn, content in [
        ("subject.txt", "TODO: one-line subject\n"),
        ("summary_paragraph.md", "TODO: one paragraph summary\n"),
        ("summary_page.md", "# TODO: one page summary\n"),
    ]:
        with open(os.path.join(folder, fn), "w") as f:
            f.write(content)

    text_file = result.get("text_file")
    if text_file and os.path.exists(text_file):
        with open(text_file) as f:
            src = f.read()
        with open(os.path.join(folder, "source_text.txt"), "w") as f:
            f.write(src)

    print(f"Scaffolded: {folder}")
    print("Next: read source_text.txt, then fill in meta.json/subject.txt/"
          "summary_paragraph.md/summary_page.md, then delete source_text.txt.")


if __name__ == "__main__":
    main()
