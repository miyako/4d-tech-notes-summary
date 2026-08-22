# Tech Note 15-05: DataAnalyzer V1.0

**Author:** Jean-Pierre Ribreau (JPR) – 4D Trainer and Consultant
**Published:** March 9, 2015 | **Product/Version:** 4D v14.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77253
**Download:** https://kb.4d.com/DLTN/TN/2015/15-05_DataAnalyzerV1R2.zip

## Proposition
This note introduces DataAnalyzer v1.0, a standalone 4D-built tool that opens 4D and Wakanda data files directly (bypassing the database engine) and renders their internal block/address-table structure as color maps, statistics, and a raw hex viewer, aimed at both 4D support engineers debugging DB4D and developers investigating file-level issues.

## Key Points
- **Shared file format:** 4D data/index/structure files and Wakanda data/index files use the same underlying DB4D block structure (since 4D v11), organized in fixed 128-byte blocks.
- **Five structural parts:** every data file consists of Header(s), Block Allocation Tables, Record Address Table trees, BLOB Address Table trees, and the actual records.
- **Address table trees scale to ~1 billion records** per table via a 3-level paged tree (1024 → 1024×1024 → 1024×1024×1024 entries).
- **Visual 'maps':** DataAnalyzer draws color-coded Block Allocation and Blocks maps so developers can spot anomalies (fragmentation, inconsistent blocks) at a glance.
- **Record-size distribution graph** helps assess fragmentation risk for tables with highly variable record sizes.
- **Raw Hex View page** lets an engineer read individual records byte-by-byte, decode timestamps/checksums/record numbers, and jump between related addresses via a history menu — explicitly described as a last-resort, expert-only tool.
- **Scope limited to v1.0:** only .4DD and .waData files are supported in this release; index and structure file analysis were promised for future versions.

## Featured Technology
- DB4D low-level file format (.4DD/.waData)
- Block Allocation Table
- Record/BLOB Address Tables
- Hex viewer
- Data-file integrity diagnostics

## Context / Positioning
Written in 2015 for 4D v14.3, in the classic Design-Mode era where 4D and Wakanda (4D's now-discontinued JavaScript/HTML5 platform) shared the same DB4D storage engine. This is an engine-internals tool for advanced troubleshooting, not an application-development technique, so it sits outside the later Project Mode/ORDA evolution entirely.

## Historical Commentary
**Status:** Partially Superseded

As a byte-level forensic tool for a storage engine, DataAnalyzer's relevance has narrowed: Wakanda was discontinued years ago, and while 4D's .4DD data file format has continued (with changes across versions), most developers today never need to hand-inspect raw blocks — 4D Server's built-in Verify Database, corruption diagnostics, and structure export tools cover the vast majority of real-world needs.

The note is still an interesting historical artifact for understanding how DB4D actually stores data, and the underlying troubleshooting mindset (when something's wrong, look at the raw bytes) remains valid, but the specific tool and file-format details described are dated and Wakanda-specific portions are now purely historical.
