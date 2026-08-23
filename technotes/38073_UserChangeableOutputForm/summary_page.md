# Tech Note: User Changeable Output Form

- **Asset ID:** 38073
- **Tech Note #:** 05-25
- **Published:** July 18, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Larry Sharpe
- **Page URL:** https://kb.4d.com/assetid=38073
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_25-27_(JUL)/05-25_ChangeableOutputForm.hqx

## Overview

Larry Sharpe (Infoservice) opens his example-database Tech Note series by showing how to give end users runtime control over an output form's columns — which field populates each column, its header text, its Date/Time/Number/Boolean format, and its alignment — using four layout variables per column and a single Output_Columns project method.

## Key Points

- Six columns each use four parallel variables — `sColumnNameN`, `sColumnValueN`, `asColumnPopupN`, `oColumnSplitterN` — moved and resized horizontally (never vertically) by code at form load time.
- User interactions: pick a field from each column's popup; Control-click a header to choose its Date/Time/Number/Boolean format; Option-click to set Left/Centered/Right alignment; Command-click to rename the header; click or right-click to sort/reverse-sort.
- The Output_Columns project method dispatches via `Case of ($command=...)` on: Startup, DefaultColumns (the single section to edit for a different table/column count), OnLoadForm, OnUnloadForm, OnDisplayRow, HeaderClicked, and PopupSelected.
- OnUnloadForm saves the user's column/format/alignment choices only to an interprocess array (in-memory for the running session) — explicitly not yet persisted to the data file, a gap the next Tech Note ("User Preferences") fills.
- OnDisplayRow is deliberately kept lightweight since 4D re-evaluates it only for newly scrolled-into-view rows, not the entire list, so slow code here would visibly lag scrolling.
- Demonstrates 4D 2004's new form-layer "Views" feature, placing decorative boxes/lines, labels, live column variables, and Add/Delete buttons on four separate view levels to simplify selecting and editing related objects.
- The [People] table's Trigger method uses `Sequence number` on the "On Saving New Record" event to assign a unique, invisible, non-modifiable, indexed ID field.

## Featured Technology

- Runtime-configurable output form columns via layout variables
- Output_Columns project method (Case of $command dispatch)
- Modifier-click header interactions (Control/Option/Command/right-click)
- 4D 2004 form Views (layered form objects)
- Sequence number trigger for unique IDs
- In-memory (non-persisted) session preferences

## Historical Commentary

**Status:** Superseded

This note demonstrates a resourceful runtime-customization technique for classic output forms, built entirely from layout variables, popups, and modifier-click gestures, with an explicit plan to add persistence in a follow-up note. The end-user goal — customizable column layout in list views — remains a common requirement, but current 4D development would typically implement it with the List Box object's built-in column/data-source configuration APIs rather than classic output form layout variables and manual positioning code. The follow-up note in this same series ("User Preferences", 05-28) extended this exact technique with BLOB-based persistence, which has itself since been superseded by JSON/object-based settings storage.

**References to newer/updated information:**
- Modern dynamic/user-configurable tabular views in 4D are generally built with the List Box object's programmatic column and data-source APIs (introduced/expanded well after 2005) rather than classic output form layout variables
- The direct follow-up Tech Note "User Preferences" (05-28) extended this technique to persist choices to a table — a persistence approach that has itself since been superseded by JSON/object-based settings storage
