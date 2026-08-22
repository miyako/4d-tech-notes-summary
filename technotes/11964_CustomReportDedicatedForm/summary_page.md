# Tech Note: Creating a Custom Report Using a Dedicated Form

**Author:** Not specified in source document
**Published:** May 1, 2000 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11964
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a guide to designing custom output forms and Break-level code for printing structured reports in classic 4D.

## Key Points
- Its central proposition is to explain report design specifically around the BREAK LEVEL and ACCUMULATE commands, deliberately excluding other Break-initiation techniques so the guidance applies broadly across different applications and 4D versions of the era.
- A key caveat highlighted in the note is that failing to use BREAK LEVEL/ACCUMULATE properly to initiate Break processing will cause a compiled application to behave incorrectly, underscoring the importance of understanding the compiler's expectations around report structure.
- The featured technology is squarely 4D's classic print/report engine: output forms, Break-level definitions, and the accumulation of totals or subtotals as records are processed in sorted order.
- The note's approach — explaining both the conceptual side (how many levels, why) and the mechanical side (object placement, associated code) — makes it a practical primer rather than a deep-dive into a single example.
- This kind of Break-level, control-line based reporting was the standard 4D reporting technique throughout the v6.x era and remained widely used well beyond it for structured, grouped/subtotaled reports.
- Developers relying on this technique needed a solid mental model of how 4D processes sorted selections record-by-record and triggers break events at each level boundary.

## Featured Technology
- BREAK LEVEL
- ACCUMULATE
- Output forms
- Report printing
- Compiled mode considerations

## Historical Context
This note documents 4D's classic report-printing model built around output forms, Break levels, and the BREAK LEVEL/ACCUMULATE command pair — core language features that predate any reporting add-ons and remain part of the 4D language today, unlike most other technology in this era's notes. The specific guidance about compiled-mode behavior with Break processing is a period-accurate caveat, since compiler behavior nuances of that vintage may differ from later releases. The fundamental concepts (choosing break levels, laying out control lines, associating per-level totals) are still conceptually valid for classic-form-based reporting in 4D today, even though many modern reporting needs are now met by List Box printing, 4D Write Pro, or QR/label tools rather than hand-built Break-level output forms. Related updates since: 4D Write Pro and List Box-based reporting have become common modern alternatives to hand-built Break-level output forms for many reporting tasks; The BREAK LEVEL/ACCUMULATE language commands themselves remain part of the current 4D language for classic form-based reports. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
