# Tech Note: Spreadsheet to 4D 101

- **Asset ID:** 32313
- **Tech Note #:** 04-16
- **Published:** April 22, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Sati Hillyer, 4D Technical Support Engineer
- **Page URL:** https://kb.4d.com/assetid=32313
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_16-20_(APR)/04-16_Spreadsheet_to_4D_101.hqx

## Overview

Sati Hillyer surveys the ways 4D 2003/2004 can import Microsoft Excel spreadsheet data -- manually via the built-in Import Dialog, programmatically via IMPORT DATA/SYLK/DIFF, into the 4D View plug-in, or via ODBC -- aimed at users migrating existing Excel-based workflows into a proper 4D database.

## Key Points

- Excel files must first be saved into an importable format: Comma-Separated (.csv), Tab-Delimited (.txt), SYLK (.slk), or DIFF (.dif); a feature matrix documents which capabilities (create table, use header row as field names, import into existing table, import into 4D View) each format supports both manually and programmatically.
- Scenario 1 (new table): manually via the 4D Import Dialog (name the table, set field names/types, choose Header/Delimiters options) or programmatically via `IMPORT DATA`, which can auto-create the table and prompt for default input/output forms; table creation only works in interpreted mode, not compiled.
- Scenario 2 (import into existing table): CSV/TXT can only be imported programmatically when not creating a new table (otherwise it falls back to the manual Import Dialog); SYLK/DIFF files support programmatic import directly into a chosen existing table via `IMPORT SYLK`/`IMPORT DIFF`.
- Scenario 3 (4D View): Tab-Delimited and SYLK files can be opened directly inside a 4D View plug-in area's File > Open menu; alternatively, Database > Import Field lets users map specific table fields into 4D View columns, manually or via a programmatic table-selection dropdown.
- Scenario 4 (ODBC, Windows only): requires the Microsoft Excel ODBC driver, a configured System DSN pointing at the workbook, and a named range in Excel (via Insert > Name > Define) acting as the source table; 4D's ODBC plug-in then imports matching-field-count data into an existing 4D table via a simple two-parameter dialog.
- Under the hood, the sample database maintains an interprocess array of table pointers (`mStartup`, `LoadRecords`) and dispatches to `IMPORT DATA`/`IMPORT SYLK`/`IMPORT DIFF` from a central `ImportData` method that first resolves the structure file's path via `GetStructurePath`.

## Featured Technology

- 4D Import Dialog (manual import of CSV/TXT/SYLK/DIFF)
- IMPORT DATA / IMPORT SYLK / IMPORT DIFF commands
- 4D View plug-in for spreadsheet-like display
- ODBC import from Excel via 4D's ODBC plug-in (Windows only)
- Automatic table/form creation from imported data
- ARRAY POINTER-based table iteration (mStartup/LoadRecords)

## Historical Commentary

**Status:** Partially superseded

This tutorial-style note walks through the many ways 4D 2003/2004 can bring Excel spreadsheet data into a 4D database: manual and programmatic import of CSV/TXT/SYLK/DIFF files (with or without automatic table creation), loading data into a 4D View spreadsheet-like area, and pulling data directly from Excel via ODBC on Windows. It's a solid beginner-oriented survey of the era's import capabilities and their format-by-format feature matrix (e.g., which formats support auto table creation vs. import into an existing table). The native `IMPORT DATA`/`SYLK`/`DIFF` commands and the 4D Import Dialog remain part of current 4D, so the core import techniques are still usable, but modern 4D developers increasingly favor CSV/JSON import via newer commands and ORDA-based data loading, and the 4D View plug-in and Windows-only Excel ODBC workflow described are legacy-specific paths less commonly used today.

**References to newer/updated information:**
- 4D's native IMPORT DATA and related import commands remain part of current 4D, though modern workflows often use CSV/JSON-based import or ORDA for bulk data loading
- The 4D View plug-in and the Windows-only Excel ODBC import path described are legacy techniques, less central to current cross-platform 4D development
- 4D has since added broader native support for structured data formats (e.g. JSON), reducing reliance on SYLK/DIFF-era spreadsheet interchange formats
