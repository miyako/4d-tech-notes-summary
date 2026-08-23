# Tech Note: Creating a quick Report Wizard (part II)

- **Asset ID:** 27706
- **Tech Note #:** 03-22
- **Published:** May 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon, 4D Inc. Q.A. Manager
- **Page URL:** https://kb.4d.com/assetid=27706
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_21-25_(MAY)/03-22_Create_QR_Wizard_II.hqx

## Overview

Jean-Yves Fock-Hoon follows up his first Tech Note on building a custom Quick Report wizard (which covered list-format reports) by extending the same wizard framework to 4D 2003's new cross-tab report mode, using the `[Invoice Lines]` table as the working example and reusing much of the earlier list-report wizard's page-navigation logic.

## Key Points

- Introduces a 3x3 cell-naming convention for cross-tab reports (cells A-I across three columns and three rows) used throughout to specify which column number and break level a given QR command call needs -- e.g., cell F requires column 3, break level 2.
- The wizard's first page selects report kind (`QR SET REPORT KIND`) and target table (`QR SET TABLE`), navigated to via `GOTO PAGE(16)`.
- Steps one through three define the three required data sources -- columns, rows, and the cell calculation -- all via `QR SET INFO COLUMN`, with a preceding `QR GET INFO COLUMN` call used to preserve unrelated properties like column width when only the data source changes.
- Step four defines the aggregate calculation (Sum, Count, Min, Max, Average) for the intersecting Data Source cell (cell E, column=2/row=2), settable interactively or via `QR SET TOTALS DATA`.
- Step five defines the optional Total column (cell C = title, cell F = calculation); notably, values in the Total column are computed from the underlying data itself, not by averaging the values already shown in cell E.
- Step six defines the optional Grand Total line (cells G/H/I) with the same "computed from raw data, not from displayed cell values" behavior.
- Step seven covers sorting via `QR SET SORT`, which takes an array of column numbers (1=columns, 2=rows) and ascending/descending flags.
- Step eight covers per-cell-type display formatting using `#`, `0`, `*`, and `^` format characters, applied separately to column titles (cell B), row titles (cell D), and data cells (cell E, which also affects F/H/I).
- Step nine covers per-cell style attributes such as font selection, retrieved via `FONT LIST` and `Font number`.
- Explains internally how a cross-tab report is generated: 4D parses every record, maintains internal arrays keyed by unique column/row values, updates the Data Source array on repeated values, then applies the chosen aggregate function per cell once all records are processed.

## Featured Technology

- Quick Report cross-tab report engine (4D 2003)
- QR SET REPORT KIND / QR SET TABLE commands
- QR SET INFO COLUMN (columns/rows/data-source binding)
- QR SET TOTALS DATA (cell, Total column, Grand Total line calculations)
- QR SET SORT command
- QR GET/SET INFO COLUMN display formatting and cell style attributes

## Historical Commentary

**Status:** Partially superseded

Jean-Yves Fock-Hoon extends the custom Quick Report wizard from Part I to cover 4D 2003's new cross-tab report mode, walking step by step through the nine-cell (A-I) cross-tab model and the QR commands that bind data sources to columns, rows, totals, the Total column, and the Grand Total line. The specific QR commands and the 3x3 cell-naming model described here are still part of current 4D and remain directly usable for building custom report wizards. In practice, however, 4D Write Pro has become the more commonly reached-for tool for building modern, richly formatted reports since its introduction, so this classic Quick Report cross-tab wizard technique, while still functional, is now a less frequently chosen path for new report-building UI.

References to newer/updated information:
- The QR command set (QR SET REPORT KIND, QR SET INFO COLUMN, QR SET TOTALS DATA, QR SET SORT, etc.) shown here remains part of current 4D and continues to work as documented
- 4D Write Pro has since become the more commonly used tool for building modern, richly formatted reports and custom report-building wizards, though the classic Quick Report cross-tab engine described here is still available
