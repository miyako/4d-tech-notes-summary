# Tech Note 15-02: GET DATABASE MEASURES

**Author:** Not specified
**Published:** January 12, 2015 | **Product/Version:** 4D v14 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77205
**Download:** https://kb.4d.com/DLTN/TN/2015/15-02_GetDatabaseMeasures_2.zip

## Proposition
(Only the KB teaser text for this Tech Note could be retrieved — the full PDF was unavailable.) Based on the abstract, this note explains the `GET DATABASE MEASURES` command introduced in 4D v14 R3, which surfaces detailed internal engine metrics (memory usage, disk exchanges, query and sort activity), and supplies graphical tooling to make the otherwise complex raw output easier to interpret.

## Key Points
- **New in v14 R3:** `GET DATABASE MEASURES` reports on nearly every internal aspect of the 4D engine's runtime behavior.
- **Covers memory, disk I/O, queries, and sorts** — the abstract explicitly calls out these categories of returned measures.
- **Output described as complex**, motivating the note's stated purpose of decoding the results in detail.
- **Graphic tools included** (per the abstract) to visualize the measures rather than reading raw numeric output.
- *(Further specifics on structure/interpretation of the returned data are not available since only the teaser text was recoverable.)*

## Featured Technology
- `GET DATABASE MEASURES` command
- 4D engine internal performance counters (memory, disk I/O, queries, sorts)

## Context / Positioning
Published in January 2015 for 4D v14 R5 (command added in v14 R3), this is a classic-era engine-diagnostics note from before ORDA, Project Mode, or 4D's later expanded monitoring/analytics tooling existed.

## Historical Commentary
**Status:** Still Relevant

Because only the short web teaser survived extraction, a detailed historical assessment isn't possible here; however, `GET DATABASE MEASURES` remains a supported low-level 4D command in current versions, so the core subject matter is not obsolete, even though better/newer performance-monitoring options (and possibly refined measure codes) have since been added.

Treat this summary as necessarily hedged: it reflects the abstract only, not the full worked examples or measure-by-measure breakdown the original PDF likely contained.
