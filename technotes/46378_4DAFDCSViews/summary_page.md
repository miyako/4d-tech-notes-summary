# Tech Note 07-18: 4D Ajax Framework: Working with DCS Views

**Author:** Tom Fitch, Technical Support Engineer, 4D Inc.
**Published:** May 9, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46378
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_17-21_(MAY)/07-18_4DAF_DCS_Views.zip

## Overview
This note explains Developer Created Selections (DCS) Views, a 4D Ajax Framework (4DAF) feature that lets developers programmatically define grid-style Views appearing in the 4DAF Portal, backed entirely by arrays rather than directly by 4D table records, so data can come from any source (or combination of sources) the developer chooses.

## Key Points
- DCS Views appear and behave like normal 4DAF Control-Panel-created Views, but are populated from arrays; because of heavy array use, the note recommends compiled applications for best performance.
- Four developer hooks must all be implemented: `DAX_DevHook_DCS_ViewAdd`, `DAX_DevHook_DCS_SetSelection`, `DAX_DevHook_DCS_RecordSave`, and `DAX_DevHook_DCS_RecordDelete`.
- `DAX_DevHook_DCS_ViewAdd` (called once by `DAX_Dev_Initialize`) defines each View's shape via `DAX_Dev_DCS_AddCustomView`, passing view name, column titles, column types, and unique/mandatory/non-enterable/non-modifiable flag arrays.
- `DAX_DevHook_DCS_SetSelection` (called on View access/refresh) populates the View via `DAX_Dev_DCS_SetSelection`, taking a Longint array of arbitrary unique record IDs plus one type-compatible data array per column.
- `DAX_DevHook_DCS_RecordSave` (called on create/edit) receives the view name, record ID (or "new record" constant), and arrays of only the modified field names/values, returning the resulting record ID.
- `DAX_DevHook_DCS_RecordDelete` (called on delete) receives the view name and record ID, returning a Boolean that determines whether the View refreshes or an error is shown.
- The example database implements all four hooks via matching `A_DCS_*` Project methods against [Actors] and [M_LineItem] tables, including using `GOTO RECORD()` for simple ID-to-record-number mapping on deletion.

## Featured Technology
- 4D Ajax Framework (4DAF) Developer Created Selections (DCS) Views
- `DAX_DevHook_DCS_*` developer hooks and `DAX_Dev_DCS_*` framework calls
- 4D Web 2.0 Pack

## Historical Context
Published May 2007, this note documents an advanced, array-driven data-binding pattern within the 4D Ajax Framework, aimed at surfacing non-table or composite data sources through the same View mechanism used for ordinary 4DAF Views. It predates 4D v11's native SQL engine (later 2007), Project Mode (2018), and ORDA (2018).

## Historical Commentary
**Status:** Obsolete

The architectural idea of binding a UI grid/View to arbitrary array-populated data through a small set of well-defined hooks (add view, populate, save, delete) remains a sensible abstraction in principle, but its concrete realization here is entirely dependent on the discontinued 4D Ajax Framework and 4D Web 2.0 Pack. None of the `DAX_DevHook_DCS_*` hooks or `DAX_Dev_DCS_*` calls exist in any current 4D product; developers today would use modern list-box, collection, or entity-selection-based UI objects instead.
