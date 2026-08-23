# Tech Note: 4D View Helper (Source Code, Part II)

- **Asset ID:** 31181
- **Tech Note #:** 04-04
- **Published:** January 31, 2004
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Melinda Gallo (routines written by Dave Batton)
- **Page URL:** https://kb.4d.com/assetid=31181
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_01-04_(JAN)/04-04_4D_View_Helper.hqx

## Overview

Part II of the "4D View Helper" documentation set provides full reference documentation — parameters, types, descriptions, and source code — for a small routine library built to simplify common operations (row selection, column sizing, font/row-height control) on 4D View spreadsheet-style plug-in areas, following an earlier Tech Note that introduced the example database.

## Key Points

- `PV_GetSelectedRow(PlugInArea)` and `PV_GetSelectedRows(PlugInArea; ptrLongintArray)` wrap `PV GET SELECTED RANGES LIST` to return the first selected row number, or populate an array with every selected row number, looping the returned selection ranges.
- `PV_SetColumnWidths(PtrPlugInArea; Width{;Width2;...;WidthN})` auto-detects whether widths are percentages (if they sum to 100) or pixels, computes the usable area width via `GET OBJECT RECT` minus 15px for the scrollbar, and applies widths with `PV SET COLUMNS WIDTH`, hiding columns whose width is 0 via `PV EXECUTE COMMAND` — restoring the prior selection afterward via `PV_SetSelectedRows`.
- `PV_SetFont(PlugInArea; FontName; FontSize; FontStyle)` sets font name/size/style on the area's "Cells" style sheet using `PV SET STYLE PROPERTY` with the `pv style text font/size/face` properties, defaulting to the system font (`Font name(0)`) if FontName is empty.
- `PV_SetRowHeight(PlugInArea; Height)` checks the row count via `PV Get document property(area; pv row count)` and applies a uniform height with `PV SET ROWS HEIGHT`; the note candidly flags "this method does not always work as expected."
- `PV_SetSelectedRow(PlugInArea; Row)` and `PV_SetSelectedRows(PlugInArea; ptrLongintArray)` select one or many rows via `PV SELECT ROWS` / `PV SELECT RANGES LIST`, temporarily disabling the area's `pv on selection changed` callback with `PV ON EVENT` so programmatic selection doesn't re-trigger user selection-change logic; passing Row=0 deselects all rows (worked around since `PV SELECT ROWS` rejects 0 directly).
- Positions this as pure API reference material — each routine is a self-contained, reusable wrapper intended to save developers from re-deriving selection/sizing/font logic against the lower-level `PV_` command set each time.

## Featured Technology

- 4D View plug-in area commands (PV_ family)
- PV GET SELECTED RANGES LIST / PV SELECT RANGES LIST for row selection
- PV SET COLUMNS WIDTH with percentage-to-pixel translation
- PV SET STYLE PROPERTY for font name/size/style on the Cells style sheet
- PV SET ROWS HEIGHT and PV Get document property
- PV ON EVENT callback suppression during programmatic selection changes

## Historical Commentary

**Status:** Obsolete

This note is Part II of the '4D View Helper' reference, documenting a small routine library (PV_GetSelectedRow, PV_GetSelectedRows, PV_SetColumnWidths, PV_SetFont, PV_SetRowHeight, PV_SetSelectedRow, PV_SetSelectedRows) that wraps 4D View's native PV_ plug-in commands to make selecting rows, sizing columns, and setting fonts in a 4D View spreadsheet area easier. Since 4D View itself was discontinued and replaced by 4D View Pro (introduced in 4D v16 R6/2018) with an entirely different object-based API, these specific helper routines and the underlying PV_ command set are now obsolete for current development, though the general pattern of wrapping low-level grid/area commands in convenience routines for row selection, column sizing, and font control is still how developers work with 4D View Pro today.

References to newer/updated information:
- 4D View was superseded by 4D View Pro (introduced 2018), which replaces the PV_ command family with a completely different, object/collection-based API
- Selecting rows, sizing columns, and setting fonts in a spreadsheet-style area today would be done with 4D View Pro's newer object methods and formatting APIs rather than this PV_-based helper library
