# 4D Tech Notes Summary Archive

A complete, browsable summary of every **4D Tech Note** ever published on
[kb.4d.com](https://kb.4d.com/) — 1,039 documents spanning 1996 to 2026 —
each reduced to a 4-file summary (one-line subject, one-paragraph summary,
one-page summary, and structured metadata with historical commentary).

> **What is 4D?** 4D is an application development IDE first released in the
> 1980s, notable for extremely long-lived backward compatibility.
>
> **What are Tech Notes?** Documents + sample databases 4D published to its
> developer community to showcase new/advanced techniques. Reading them in
> reverse chronological order traces the product's technical evolution and
> the "zeitgeist" of each era (client-server → web → ORDA → cloud/AI).

## Repository layout

```
technotes/
  all_technotes.json          master list of all 1,039 assets (id/title/date/version)
  index.md                    generated table of every note, newest first
  <assetid>_<Slug>/
    meta.json                 structured metadata + historical_commentary
    subject.txt                one-line subject
    summary_paragraph.md       one-paragraph summary
    summary_page.md             one-page summary (full detail)
docs/
  unprocessable_urls.md       every asset that could NOT be fully downloaded/extracted, with reasons
scripts/
  common.py                   shared HTTP/cookie/HTML-parsing helpers
  fetch_all_technotes.py      rebuild the master list from kb.4d.com's search API
  scan_asset.py                scan asset page(s) for metadata + download link (no download)
  extract_asset.py            download + extract full text for scanned assets
  add_asset.py                 scaffold a new note's 4-file folder end-to-end
  rebuild_index.py            regenerate technotes/index.md from all meta.json files
  audit.py                    read-only completeness/quality report
```

## Completeness tally

| | Count | % |
|---|---|---|
| **Total Tech Notes on kb.4d.com** | 1,039 | 100% |
| Fully processed from the real document (`full_pdf`) | 559 confirmed + 55 presumed* | 59.1% |
| Teaser-only (document unrecoverable, see below) | 425 | 40.9% |

\* 55 notes (all within asset IDs 70086-80085, the first batch processed) use
an older `meta.json` schema written before the `content_source` field
existed. Spot-checks confirm they have real `download_url`s and full
summaries — they are almost certainly `full_pdf`, just not labeled as such.
This is a **schema gap, not a data-completeness failure**; see
"Known limitations" below.

Run `python3 scripts/audit.py` at any time to regenerate this table plus a
year-by-year and status-value breakdown.

### Why 425 notes are teaser-only

| Cause | Count | Years affected |
|---|---|---|
| No download link ever existed on the asset page | 150 | 1997-2000 |
| Link exists, but the archive could not be extracted (mostly pre-2006 Windows `.exe` self-extractors, internally StuffIt5) | 257 | 1998-2007 |
| Download failed / dead FTP link | 2 | 2001, 2007 |
| Reachable `.zip` links that repeatedly failed/truncated on download | ~16 | 2009-2022 (scattered) |

Full asset-by-asset list with titles and URLs: **[docs/unprocessable_urls.md](docs/unprocessable_urls.md)**.

### Bias / anomaly notes (important — read before drawing conclusions from year-over-year stats)

**1. Genuine archive-era bias (1996-2007), not a processing error.** The
teaser-only rate is extremely high and format-driven in specific years:

- **1997-2002 are ~93-100% teaser-only.** Many pages from this era simply
  never had (or lost) their download link during CMS migrations, and where a
  link exists it is almost always a `.exe`/`.hqx` self-extracting archive
  that predates the ZIP-everywhere convention. These are internally
  StuffIt5 archives; `unar` recognizes the format but a majority still fail
  to yield a readable PDF (age-related corruption or unusual encoding
  variants). This is a **real, permanent gap in the archive**, not
  something a smarter script would fix.
- **2006 onward drops sharply to ~0-17% teaser-only** once 4D standardized
  on `.zip`-hosted PDFs.

**2. The "2008 batch" methodology anomaly — a self-inflicted process bug,
already found and fixed, documented here so it isn't mistaken for a data
problem.** Unlike the surrounding years, 2008's *source archives* were
almost entirely recoverable (only ~5 of 44 had genuine extraction issues —
consistent with the "2006+" trend, not the 1997-2005 trend). However, during
processing, background summarization agents repeatedly stalled specifically
on this batch, producing near-zero output over 30-40+ minutes. This was
initially worked around with a **programmatically-generated, generically
templated stopgap** for all 42 notes in that batch — a real quality
regression (thin, repetitive commentary, not tailored to each document).
It was caught by an audit (comparing summary text for suspicious
duplication), and every one of the 42 notes was subsequently rewritten with
individually tailored content by directly reading each source document.
**Takeaway for future archivists:** if you see unusually uniform or
repetitive-sounding commentary across a batch, audit for templated
shortcuts the way `scripts/audit.py` does (duplicate boilerplate phrasing is
a red flag, not a legitimate era pattern) — and prefer small, synchronous
batches (5-10 assets) over large background-agent runs, which proved
unreliable for this specific dataset.

**3. Minor OCR/text-extraction quirk (2008 batch).** In at least 3 notes,
extracting text from the PDF reversed the Tech Note number's digit pairs
(e.g. "03-08" instead of "08-03"). The `download_url` filename reliably
contains the correct number (e.g. `.../08-03_Build_Embed_Dashboard.zip`) —
**always prefer the download URL's embedded number over text scraped from
the PDF body when they disagree.**

### Known limitations

- **`meta.json` schema is not perfectly uniform.** Three processing eras
  produced slightly different shapes:
  1. First 407 notes (IDs 70086-80085): no `content_source` key at all.
  2. 632 legacy notes (1996-2008, background-agent batches): has
     `content_source`; `historical_commentary.status` values include
     spelling/spacing variants (`still_relevant` vs `still relevant`,
     `historical_interest_only` vs `historical interest only`).
  3. Hand-fixed 2008 batch (IDs 48550-51814): consistent `content_source`
     and a clean 3-value status vocabulary.

  Run `python3 scripts/audit.py` to see the full status-value tally. Treat
  `content_source` as best-effort/optional when consuming this data, and
  consider normalizing status values before doing any statistical analysis
  across the whole corpus.

## How to use the scripts

All scripts require a kb.4d.com session cookie:

```bash
# In a browser, visit https://kb.4d.com/, open DevTools > Cookies,
# copy the value of the 4DSID_KBv20 cookie, then:
export KB4D_COOKIE="4DSID_KBv20=<value>"
```

Dependencies: Python 3, plus `unar` (`brew install unar`) and `pdftotext`
from poppler (`brew install poppler`) for archive extraction.

### Add one new Tech Note

```bash
python3 scripts/add_asset.py 80106
```

This scans the asset page, downloads and extracts the document, and
scaffolds `technotes/80106_<Slug>/` with `meta.json` (metadata pre-filled,
summary fields as `TODO`) plus a `source_text.txt` containing the extracted
full text. **Read `source_text.txt` and hand-write** (or have an LLM/agent
write) `subject.txt`, `summary_paragraph.md`, `summary_page.md`, and the
`summary`/`historical_commentary` fields in `meta.json` — summarizing and
adding historical perspective is a judgment call, not something this script
automates. Delete `source_text.txt` when done, then run
`python3 scripts/rebuild_index.py`.

### Check for brand-new Tech Notes since the last update

```bash
python3 scripts/fetch_all_technotes.py > technotes/all_technotes.json
python3 scripts/audit.py   # shows any new asset IDs not yet on disk
```

Then run `add_asset.py` for each new ID reported as "missing."

### Start completely from scratch

```bash
# 1. Rebuild the master list via kb.4d.com's search API (not ID-range guessing --
#    the archive's low IDs are non-contiguous and a naive range scan will miss
#    hundreds of legacy notes).
python3 scripts/fetch_all_technotes.py > technotes/all_technotes.json

# 2. Scan every asset for metadata + download link.
python3 scripts/scan_asset.py --file <(python3 -c "import json;print(json.dumps([a['assetid'] for a in json.load(open('technotes/all_technotes.json'))]))") \
  --workers 8 > /tmp/scan_all.json

# 3. Download + extract full text for everything scanned.
python3 scripts/extract_asset.py /tmp/scan_all.json --outdir /tmp/extract_all --workers 8

# 4. For each asset, hand-write (or LLM-generate) the 4 summary files -- see
#    add_asset.py for the exact folder/file shape to produce. This step is
#    the labor-intensive part and is intentionally NOT scripted end-to-end:
#    quality summaries require actually reading and understanding each
#    document, ideally with an explicit historical-commentary pass (what's
#    since been superseded, deprecated, or updated).

# 5. Regenerate the index and audit.
python3 scripts/rebuild_index.py
python3 scripts/audit.py
```

**Tip:** process in small batches (5-10 assets at a time) rather than one
giant background job — see the "2008 batch" anomaly above for why.

## License

See [LICENSE](LICENSE).
