# Tech Note: Included Lists with 4D View

- **Asset ID:** 33905
- **Tech Note #:** 04-36
- **Published:** September 9, 2004
- **Product / Version:** 4th Dimension 2004
- **Platform:** Mac & Win
- **Author:** Bertrand Soubeyrand
- **Page URL:** https://kb.4d.com/assetid=33905
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_36-40_(AUG)/04-36_Included_Lists.hqx

## Overview

Written by Bertrand Soubeyrand, this note explains how to use a 4D View area -- the spreadsheet-like plug-in available since 4D v6.8 -- as an alternative to a true subform for displaying a related-records 'included list,' offering advantages such as non-contiguous multi-row selection, resizable columns, per-cell font/color/alignment control, and Up/Down-key row navigation. The note details preparing the area with PV SET AREA PROPERTY calls (disabling the modification-saving dialog, restricting selection to single rows, hiding toolbars/menus/scrollbars to mimic a subform look), then wiring the area to related records with PV SET DOCUMENT PROPERTY for row/column counts and PV ADD DYNAMIC FIELDS, which establishes a live, synchronized-array-driven link between three columns and their corresponding table fields (including a computed/callback column via FormuleChampPV). It then shows how to intercept user interaction through PV ON EVENT handlers for double-click (creating and displaying a new related record via a temporary set) and single-click on column headers (sorting the underlying selection with ORDER BY and recoloring the sorted column via View_ColumnColor), concluding that 4D View can be programmed to behave much like a fully interactive subform with modest code.

## Key Points

- PV SET AREA PROPERTY with constants like pv saving dialog, pv select mode (pv select single row), and pv show *toolbar/*header/*scrollbar flags configures the View area to visually mimic a subform.
- PV ADD DYNAMIC FIELDS links three synchronized arrays (table numbers, field numbers, callback method names) so the area's columns display live related-record data, including a computed column driven by a callback method (FormuleChampPV).
- PV ON EVENT registers background handlers for pv on double clicked and pv on clicked, each receiving area reference, event, modifier, column, row, and key-code parameters, with the handler's $0 result controlling whether the click is 'consumed'.
- Double-clicking a header row in the demo creates a new related record via CREATE SET/ADD RECORD/ADD TO SET/GOTO SELECTED RECORD, then refreshes the area with PV UPDATE DYNAMIC AREA.
- Single-clicking a column header sorts the related selection using ORDER BY (ascending or descending based on the Shift-key modifier) and recolors the sorted column via a View_ColumnColor helper using PV SET CELL PROPERTY.
- PV GET CELL FIELD and PV SELECT RANGE are used to map a clicked cell back to its underlying table/field and to programmatically re-select ranges of cells after data changes.

## Featured Technology

- 4D View plug-in (available since 4D v6.8)
- PV SET AREA PROPERTY / PV ADD DYNAMIC FIELDS
- 4D View used as a subform-style 'included list' area
- PV ON EVENT click/double-click event handling
- PV SELECT RANGE / PV UPDATE DYNAMIC AREA / ORDER BY-driven column sorting

## Historical Commentary

**Status:** Obsolete

This note shows a clever workaround for the era: using the general-purpose 4D View spreadsheet plug-in, driven entirely through PV-prefixed commands, as a stand-in for a true subform to gain per-cell formatting and multi-row selection that subforms of the time lacked. The original 4D View plug-in has long been discontinued, and its capabilities were absorbed first by 4D's built-in List Box form object and later, for full spreadsheet functionality, by the separate 4D View Pro product introduced in 2018, making this specific PV-command-based technique obsolete even though its underlying goal -- an interactive, cell-formatted tabular subform -- is now handled natively.

**References to newer/updated information:**
- The legacy 4D View plug-in and its PV-prefixed command set used throughout this note have been discontinued and are not part of current 4D
- 4D's native List Box form object now provides subform-like tabular display with per-cell styling and multi-row selection without a separate plug-in
- 4D View Pro (introduced in 4D v17, 2018) is a modern, unrelated spreadsheet component that replaced 4D View's grid capabilities going forward
