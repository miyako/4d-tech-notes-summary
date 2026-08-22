# Tech Note 18-20: Mail Merges with 4D Write Pro

**Author:** Timothy Aaron Penner, Technical Services Engineer, 4D Inc.
**Published:** November 16, 2018 | **Product/Version:** 4D Write Pro v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78160
**Download:** https://kb.4d.com/DLTN/TN/2018/18-20_MailMergeswith4DWritePro.zip

## Proposition
Legacy 4D Write mail-merge templates could not run in 64-bit 4D. This note gives developers a complete, format-by-format path for converting legacy 4D Write v6/v7 documents (on disk, in Picture fields, or as blobs) into native 4D Write Pro documents, then rebuilds classic mail-merge functionality using 4D Write Pro's expression system.

## Key Points
- **v6 documents on disk:** must first upgrade to v7 using the 32-bit-only legacy plugin (`WR New offscreen area`, `WR OPEN DOCUMENT`, `WR SAVE DOCUMENT`).
- **v7 documents on disk:** convert directly to native 4D Write Pro (in 32- or 64-bit mode) via `WP Import document()` and `WP EXPORT DOCUMENT(...; wk 4wp)`.
- **Picture-format documents (v6/v7):** require 32-bit legacy plugin conversion to a v7 blob first, using `WR PICTURE TO AREA` and `WR AREA TO BLOB`.
- **v7 documents in blob format:** convert directly (32- or 64-bit) to a native object via `WP New($wrBlob)`.
- **Expressions power the merge:** `ST INSERT EXPRESSION` inserts field/command references (e.g., `[People]Name`) that are computed at processing time.
- **Output paths:** processed documents are printed to paper/PDF or exported to HTML for email delivery.
- **Worked examples:** loyalty discounts, outstanding balances, and order confirmation templates demonstrate complete merge workflows.

## Featured Technology
- 4D Write Pro (`WP` command family: `WP Import document`, `WP EXPORT DOCUMENT`, `WP New`)
- Legacy 4D Write plugin (32-bit only: `WR New offscreen area`, `WR OPEN DOCUMENT`, `WR SAVE DOCUMENT`, `WR PICTURE TO AREA`, `WR AREA TO BLOB`)
- `ST INSERT EXPRESSION`
- HTML export for email-based mail merges

## Best Practices Highlighted
1. Identify which legacy storage format a document is in (disk v6/v7, Picture, or blob) before choosing a conversion path — each requires different steps and some only work in 32-bit mode.
2. Convert legacy documents to native 4D Write Pro format (`.4wp`) as early as possible to avoid ongoing dependence on the deprecated 32-bit plugin.
3. Use expression-based placeholders rather than hardcoded text so templates stay data-driven across output formats (print, PDF, HTML/email).

## Context / Positioning
Published during the peak of 4D's 32-to-64-bit transition, this note served practical continuity needs for long-time 4D customers whose businesses depended on mail-merge document generation — ensuring a clear migration path so a common, high-value legacy feature wasn't lost as 4D Write itself was phased out of 64-bit builds.

## Historical Commentary
**Status:** Partially superseded

4D Write (classic) and its legacy plugin are completely gone from current 64-bit 4D, so the detailed v6/v7 conversion procedures here — especially anything requiring 32-bit mode — are now purely of historical/archival interest, relevant only to organizations still holding very old 4D Write documents that were never migrated. Most active 4D databases completed this migration years ago.

The core mail-merge pattern this note builds toward — embedding expressions in a 4D Write Pro document via `ST INSERT EXPRESSION` (or the modern equivalents) and processing them into print/PDF/HTML output — remains a valid and current 4D Write Pro technique, and 4D Write Pro itself continues to be 4D's actively maintained document engine today.
