# Tech Note: 4D View Helper

- **Asset ID:** 29736
- **Tech Note #:** 03-36
- **Published:** August 29, 2003
- **Product / Version:** 4D View
- **Platform:** Mac & Win
- **Author:** Melinda Gallo
- **Page URL:** https://kb.4d.com/assetid=29736
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_36-39_(AUG)/03-36_4D_View_Helper.hqx

## Overview

Melinda Gallo documents the 4D View Helper component, a set of 13 project methods (prefixed PV_) that wrap the lower-level 4D View plug-in commands to make common list/grid tasks — populating columns from arrays, records, or callback-computed values, configuring the area to behave like a plain list rather than a full spreadsheet, setting fonts and row heights, and reading/restoring the current row selection — dramatically simpler to use from a form.

## Key Points

- PV_ConfigureAsList(PlugInArea) turns a full 4D View spreadsheet area into a plain list by disabling menus, keyboard shortcuts, tool palettes, and cell borders in a single call
- PV_SetColumnArrays populates columns directly from named 4D arrays; PV_SetColumnFields populates columns directly from field pointers, for simple 1:1 record-to-column mapping
- PV_SetColumnFields2 supports per-column callback methods for computed values — demonstrated concatenating First_Name + uppercase(Name) into a synthesized 'full name' column not backed by a single field
- PV_SetColumnHeaders and PV_SetColumnWidths (percentages that must sum to 100, 0 to hide a column) control header text and column layout
- PV_SetFont applies a font/size/style to the whole area, with style expressed as a bitmask (Bold=1, Italic=2, Underline=4, Outline=8, Shadow=16, Condensed=32, Extended=64)
- PV_GetSelectedRow / PV_GetSelectedRows read the current cell selection (first row, or all selected rows into an array); PV_SetSelectedRow / PV_SetSelectedRows restore a selection, with 0 selecting all rows
- Notes that programmatically setting the selection via PV_SetSelectedRow(s) does not fire any configured callback method — the developer must invoke it explicitly if downstream logic depends on it

## Featured Technology

- 4D View Helper component (PV_ helper routines)
- PV_SetColumnArrays / PV_SetColumnFields
- PV_SetColumnFields2 with callback methods
- PV_ConfigureAsList (list-mode 4D View)
- PV_GetSelectedRow(s) / PV_SetSelectedRow(s)
- PV_SetFont / PV_SetRowHeight / PV_SetColumnWidths

## Historical Commentary

**Status:** Obsolete

The 4D View Helper component solved a real 2003-era pain point — the raw 4D View plug-in API was verbose for simple list display — by wrapping it in a friendlier set of PV_ routines. Since then, the 4D View plug-in itself has been discontinued in favor of the native List Box form object, which natively supports array- and collection-backed columns, computed/formula columns, font/style control, and row selection without needing any helper component at all, making both the raw 4D View API and this helper library obsolete for new development.

**References to newer/updated information:**
- The 4D View plug-in that this helper component wraps has been discontinued and replaced by the native List Box form object
- Current List Box objects natively support array/collection-backed columns, computed columns, and selection handling that this helper component had to build by hand on top of 4D View
