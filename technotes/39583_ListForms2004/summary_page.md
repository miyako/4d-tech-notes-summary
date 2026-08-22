# Tech Note 05-33: List Forms in 2004

**Author:** Daniel Do – 4D Technical Support
**Published:** October 3, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=39583
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_30-33_(SEP)/05-33_List_Forms.pdf

## Overview
This note covers using list (output) forms in 4D 2004 to browse, select, edit, and print records as a list, focusing on the `DISPLAY SELECTION` and `MODIFY SELECTION` commands and their shared parameters.

## Key Points
- `DISPLAY SELECTION` shows records read-only; `MODIFY SELECTION` allows in-list editing — both switch the table's mode and restore it afterward.
- Shared parameters: `selectMode` (No Selection / Single Selection / Multiple Selection, default Multiple), `enterList` (enables "Enter in List" editing without opening the input form), and two optional `*` flags controlling single-record display behavior.
- A single-record selection displays in the input form by default (overridable via the `*` parameters).
- The `UserSet` automatically captures user-highlighted records and remains accessible to the calling method after the command completes — useful for chained actions like printing a selection.
- Exiting is handled via custom Accept/Cancel buttons or the platform Escape key.
- 2004-era UI updates: no scrolling past the last record; a "Double-click on Empty Line" compatibility property for pre-2004 upgrades (discouraged for new work); removal of the blinking subform-focus triangle in favor of standard OS focus cues.

## Featured Technology
- DISPLAY SELECTION / MODIFY SELECTION commands
- List (Output) forms vs Detail (Input) forms
- UserSet
- Enter in List mode

## Historical Context
These commands still exist and function in current 4D versions, including Project Mode databases, so the core technique remains valid. However, the List Box form object (introduced starting with 4D v11 SQL and greatly expanded since, including full object/collection-driven list boxes) has become the standard, far more flexible way to present and edit tabular data in modern 4D applications, making the plain list-form approach documented here a legacy but still-functional pattern.
