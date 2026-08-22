# Tech Note 21-04: Full Data Export and Import

**Author:** Timothy A Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** February 22, 2021 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78654
**Download:** https://kb.4d.com/DLTN/TN/2021/21-04_Export-Import.zip

## Proposition
4D's `EXPORT DATA`/`IMPORT DATA` commands and GUI both operate one table at a time, which is impractical for a full-database export/reimport. This note supplies a single wrapper method that loops over every table in the database to perform a complete export or import in one call.

## Key Points
- **Single entry point:** `export_import_all` prompts (via `CONFIRM`) for export vs. import, a folder (`SELECT FOLDER`), and format (XML text vs. 4D binary).
- **Per-table loop:** iterates `Get last table number`/`Is table number valid`, calling `export_import_one_table` for each valid table.
- **XML project definition:** built dynamically per table with `DOM Create XML Ref`/`DOM Create XML element`, enumerating every valid field to drive `EXPORT DATA`/`IMPORT DATA`.
- **Clean reimport:** the import path `TRUNCATE TABLE`s the destination table before calling `IMPORT DATA`.
- **Performance prep for import:** `ALTER DATABASE DISABLE INDEXES/CONSTRAINTS/TRIGGERS` (SQL) is run first — but only works with Journaling disabled, requiring "Use Log" to be turned off beforehand.
- **Operational checklist:** disable the log file and comment out `STARTUP` stored procedures before running either operation.
- **XML export as a data-quality tool:** exporting to readable XML text exposes raw record content, useful for spotting control characters or other data that would otherwise fail on import.

## Featured Technology
- `EXPORT DATA`, `IMPORT DATA`
- `DOM Create XML Ref`, `DOM Create XML element`
- SQL `ALTER DATABASE DISABLE INDEXES/CONSTRAINTS/TRIGGERS`
- `TRUNCATE TABLE`

## Best Practices Highlighted
1. Disable Journaling ("Use Log") and stored procedures before running a full export/import operation.
2. Use XML (text) format when you need to inspect or sanitize raw data content as part of the process.
3. Truncate the destination table before import to guarantee a clean, duplicate-free reload.

## Context / Positioning
This note fills a longstanding practical gap in 4D's classic export/import tooling (which is inherently per-table) by providing a small reusable component, reflecting 4D Technical Services' pattern of publishing utility components that plug gaps in built-in tooling rather than waiting for a product feature to be added.

## Historical Commentary
**Status:** Still relevant

`EXPORT DATA`/`IMPORT DATA` remain unchanged, fully supported classic 4D commands, and this per-table wrapper technique still works as-is in current 4D versions. While ORDA entities/entity selections are now the default, more idiomatic way to manipulate data day-to-day, they don't replace this note's specific use case — bulk full-database export/import for backup, migration, or disaster recovery — so the classic API pattern shown here remains a legitimate, still-useful specialized technique rather than something superseded by ORDA.
