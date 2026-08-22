# Tech Note 06-07: Generic Full Data Export-Import Routine

**Author:** Thomas Maul, General Manager, 4D Germany.
**Published:** February 17, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41862
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_05-08_(FEB)/06-07_Generic_Full_Data_v2.zip

## Overview
This note provides a single generic 4D method, "ExportImport," that exports or imports an entire database — all tables, subtables, pictures, and BLOBs — to/from XML, intended for long-term archiving and for repairing/defragmenting damaged or fragmented data files.

## Key Points
- One method handles both directions; installed by copy-pasting into a method named exactly "ExportImport" (or updating references if renamed).
- Compiled databases using "All variables are typed" need a few extra type declarations added to a Compiler method.
- A process variable, `ExportImport_Stop`, allows cancelling an in-progress export/import from another process (e.g., via `ON EVENT CALL`).
- Callable interactively from User mode (prompts for direction and folder) or programmatically: `ExportImport("Export";"C:\myxmlfolder")` / `ExportImport("Import";"C:\myxmlfolder")`.
- Exports one XML file per table; auto-segments files at 1.5GB to avoid known Mac OS issues even though Windows XP supports files over 2GB; pictures/BLOBs are Base64-encoded.
- On import, existing records are deleted, indexes are dropped and rebuilt for speed/defragmentation, and sequence numbers are automatically restored (intended for use against an empty, newly created data file).
- Table/field names are sanitized into XML-safe tags (diacritics and leading digits replaced with underscores).
- References an earlier, more complex component-based approach from TN 01-43 (4D 6.7 era), which this method simplifies and extends with subtable and sequence number support.

## Featured Technology
- Full-database XML export/import
- Base64 encoding of BLOB/picture fields
- Data file defragmentation via export/reimport
- Index drop-and-rebuild for import performance
- Single-method, copy-paste component distribution style

## Historical Context
Published in 2006 for 4D 2004, this note reflects an era before 4D had more comprehensive built-in backup, data-file verification, and XML tooling, and before its native SQL engine (v11, 2007). The full-export/full-import approach to defragmenting and repairing a data file remains conceptually sound and is still occasionally used today, but 4D has since added more robust native tools for data file maintenance, and the specific 1.5GB file-segmentation workaround reflects mid-2000s Mac OS file-size limitations that no longer apply.

## Status
**Superseded** — the archiving/repair concept persists, but 4D's later built-in data-file maintenance and XML tooling reduce the need for this specific single-method implementation.
