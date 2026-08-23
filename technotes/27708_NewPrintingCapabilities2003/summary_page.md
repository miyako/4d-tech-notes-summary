# Tech Note: New Printing Capabilities with 4D 2003

- **Asset ID:** 27708
- **Tech Note #:** 03-24
- **Published:** May 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Gou Yang, 4D Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=27708
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_21-25_(MAY)/03-24_NewPrintCapabilities.hqx

## Overview

Gou Yang introduces the new printing commands added in 4D 2003 -- `PRINTERS LIST`, `SET CURRENT PRINTER`, `Get current printer`, `SET PRINT OPTION`, `GET PRINT OPTION`, and `PRINT OPTION VALUES` -- which for the first time let developers procedurally control most options found in the default print dialog. Using a sample "Print Options" database, the note builds a full custom, cross-platform print-settings dialog with per-user saved preferences, then applies those settings across Print Form, Print Record, and Print Selection.

## Key Points

- Guards against Mac OS 9, since `PRINTERS LIST`, `SET CURRENT PRINTER`, and `GET CURRENT PRINTER` require Mac OS X or Windows 2000/XP; the demo alerts and refuses to run the print dialog on OS 9.
- `PGetPrintSettings` retrieves current values with `GET PRINT OPTION` for option numbers 1 (paper), 3 (scale), 4 (copies), 5 (source), 8 (color), 9 (destination), 10 (resolution), and 11 (double-sided), plus `Get current printer` and `Current user`.
- `PLoadDefaultPref` populates UI pop-ups from `PRINTERS LIST` and `PRINT OPTION VALUES(1;arPaper)` / `PRINT OPTION VALUES(5;arSource)`, using a generic `CheckArray` helper to disable controls when an array comes back empty (avoiding "index out of range" errors).
- Platform-conditional UI: color/black-and-white and double-sided options are Windows-only and hidden on Mac (`arMacColor:="Not Available"`), while destination choices differ (Mac offers PDF/EPS/PS in addition to Printer).
- Per-user preferences are stored in a `[PrintPref]` table, keyed by `Current user`, loaded via `PLoadPrintPref` if a record exists and `[PrintPref]Remember=1`, or created via `PCreatePrintPref` on first run.
- `SetOption` (fired on OK) applies the chosen values with `SET PRINT OPTION`, including `SET CURRENT PRINTER`, copies, orientation (`SET PRINT OPTION(2;1)` for portrait), and destination -- creating a document reference via `Create document` for PDF/EPS/PS paths.
- A generic `CheckSetOption` helper only calls `SET PRINT OPTION` for paper/scale/source if their arrays actually contain a value, avoiding overwriting options with blanks.
- Documents the full `SET PRINT OPTION(option;value1{;value2})` reference table, including option 9 (destination: 1=Printer, 2=File/PS, 3=PDF, 4=EPS) and option 11 (double-sided, Windows only).
- Demonstrates `Print Form`, `Print Record` (via `OUTPUT FORM` + `PRINT RECORD([table];>)`), and `Print Selection` (`ALL RECORDS` + `PRINT RECORD`/`PRINT SELECTION`), explicitly flagging the `>` parameter as required to avoid 4D silently reinitializing (and discarding) the procedurally-set print options.

## Featured Technology

- PRINTERS LIST command
- SET CURRENT PRINTER / Get current printer commands
- SET PRINT OPTION / GET PRINT OPTION commands
- PRINT OPTION VALUES command
- Print Form / Print Record / Print Selection with the '>' (don't reinitialize) parameter
- Cross-platform (Mac/Windows) print dialog design

## Historical Commentary

**Status:** Partially superseded

Gou Yang walks through 4D 2003's then-new procedural printing commands (PRINTERS LIST, SET/GET PRINT OPTION, PRINT OPTION VALUES) by building a custom cross-platform print-settings dialog with per-user saved preferences, and explains the important '>' parameter on PRINT RECORD/PRINT SELECTION that preserves programmatically-set options instead of resetting them. The core command set demonstrated here is still part of current 4D and the general pattern of querying then setting print options procedurally remains valid, so the underlying technique is still usable. However, the specific option numbering, the Mac OS 9 checks, and some UI conventions (e.g., "EPS (PDF for Mac OS X)" as a destination) are dated, and 4D's print architecture has continued to evolve since, so developers should verify current option values and destinations against present-day documentation rather than copying this note's numbers verbatim.

References to newer/updated information:
- The PRINTERS LIST, SET/GET PRINT OPTION, and PRINT OPTION VALUES commands remain part of current 4D, though later versions have added or refined print option numbers and destinations beyond what is listed in this 2003-era note
- Mac OS 9 compatibility checks and OS 9-era destination options (like "EPS (PDF for MAC OS X)") described here are no longer relevant on modern systems
