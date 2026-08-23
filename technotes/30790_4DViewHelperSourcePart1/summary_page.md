# Tech Note: 4D View Helper (Source Code, Part I)

- **Asset ID:** 30790
- **Tech Note #:** 03-55
- **Published:** December 19, 2003
- **Product / Version:** 4D View 2003
- **Platform:** Mac & Win
- **Author:** Melinda Gallo (routines written by Dave Batton)
- **Page URL:** https://kb.4d.com/assetid=30790
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_52-55_(DEC)/03-55_4D_View_Helper.hqx

## Overview

Melinda Gallo documents Part I of the "4D View Helper" component (routines by Dave Batton): a library of `PV_`-prefixed project methods that wrap 4D View's native `PV` command set to make it easy to configure a 4D View spreadsheet area as a clean, read-only, list-style display bound to either 4D arrays or database table fields.

## Key Points

- `PV_ConfigureAsList(PlugInArea)` deletes 4D View's default columns/rows with `PV DELETE COLUMNS`/`PV DELETE ROWS`, calls `PV_DisableMenuShortcuts`, and then uses `PV SET AREA PROPERTY` to hide the menu bar/toolbars, block direct data entry (`pv trigger none`), hide grid lines and row headers, force multi-row selection, and suppress 4D View's save-confirmation dialog.
- `PV_DisableMenuShortcuts` calls `PV SET COMMAND STATUS` roughly two dozen times to turn off File, Edit, View, Insert, Style, and other 4D View menu commands and their keyboard equivalents.
- `PV_NeverBeAButton` sets `pv button width`/`pv button height` to 0 via `PV SET PLUGIN PROPERTY` so the area never renders as a button.
- `PV_SetColumnArrays(PlugInArea; ArrayName{;...})` clears existing columns, sets the column count via `PV SET DOCUMENT PROPERTY`, and binds the named 4D arrays to columns using `PV ADD DYNAMIC ARRAYS`.
- `PV_SetColumnFields(PlugInArea; FieldPtr{;...})` binds table fields instead, via `PV ADD DYNAMIC FIELDS`, using the current record selection and the first field's table as master table; `PV_SetColumnFields2` extends this to allow per-column callback methods in place of a field, at the cost of a hard 10-column limit (documented as a workaround for not being able to use `${2}` directly).
- `PV_SetColumnHeaders(PlugInArea; Title1{;...})` loops through the passed titles and applies them with `PV SET COLUMN HEADER`.
- `PV_FixColWidths(PtrPlugInArea{; DynamicColumnNumber})` recalculates and applies the width of a "dynamic" (by default, last) column whenever the area is resized, using `GET OBJECT RECT` to find available width, subtracting fixed column widths, and calling `PV SET COLUMNS WIDTH` plus `PV REDRAW` only when the width actually changes.
- The note states that routines listed from `PV_FixColWidths` onward (`PV_GetSelectedRow(s)`, `PV_SetColumnWidths`, `PV_SetFont`, `PV_SetRowHeight`, `PV_SetSelectedRow(s)`) are deferred to Part II of the Tech Note.

## Featured Technology

- 4D View plug-in areas
- PV SET AREA PROPERTY / PV SET DOCUMENT PROPERTY
- PV ADD DYNAMIC ARRAYS / PV ADD DYNAMIC FIELDS
- PV SET COMMAND STATUS (menu/shortcut suppression)
- PV_FixColWidths dynamic column resizing

## Historical Commentary

**Status:** Obsolete

This note documents the first half of the "4D View Helper" component, a set of PV_-prefixed wrapper routines (PV_ConfigureAsList, PV_SetColumnArrays, PV_SetColumnFields, PV_SetColumnFields2, PV_SetColumnHeaders, PV_FixColWidths) built on top of 4D View's low-level PV commands to make it easy to configure a 4D View spreadsheet area as a read-only, header-driven list bound to either 4D arrays or table fields. As a reference for the discontinued 4D View plug-in/companion product, this is now of purely historical interest for maintaining legacy databases; any new development would use 4D's built-in list box form object (or web-based grids) instead, both of which provide array/selection binding, column configuration, and read-only display natively without needing this kind of helper library.

**References to newer/updated information:**
- 4D View as a standalone plug-in/companion product has been discontinued in current 4D
- Modern 4D applications use the native list box form object (array-based or selection-based) or web-based grid components instead of 4D View areas for tabular display, with built-in column/header/selection configuration replacing the need for this PV_ helper library
