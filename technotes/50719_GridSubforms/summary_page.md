# Tech Note 08-29: Bridging Your Grids: Web 2.0 Subforms

**Author:** Tim Kaufman, Technical Services Team Member, 4D Inc.
**Published:** August 13, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_28-31_(AUG)/08-29_4DAF_Subforms.zip

## Overview
When designing web forms in the 4D Ajax Framework, one frequently needs to display related records from a child table while editing a parent record—a classic subform pattern. The Data Grid alone is not sufficient for this use case; the Bridge object (the communication backbone of the 4DAF) must be enlisted to manage the orchestration of parent-child queries, record additions/edits, and event-driven synchronization. This note walks through eight progressively complex examples showing how to weave together Data Grid queries, JavaScript event listeners, and Bridge API calls to build a fully functional web subform that maintains data integrity across add/edit/delete operations.

## Key Points
- **Data Grid + Bridge synergy:** The Data Grid provides the list rendering and row-level events; the Bridge provides the data operations and metadata (table/field information).
- **Parent-child query strategy:** The parent form's grid uses `queryAllRecords()` to load all department records; the child form's grid uses a filtered query (e.g., `Depts.ID = currentDeptID`) to show only related employees.
- **Event-driven selection:** Clicking a parent grid row fires `onDataRowClick`, from which the grid's row metadata (record ID) is extracted via JavaScript to identify and filter the child query.
- **Record manipulation:** Bridge methods `dax_bridge.addRecord()`, `dax_bridge.modifyRecord()` are called directly from JavaScript to write changes to 4D without requiring a separate Data Grid refresh infrastructure.
- **Metadata access:** `dax_getTable()` and `dax_getField()` functions allow JavaScript to inspect field names and types, enabling dynamic form field generation and validation.
- **Sample progression:** Eight examples scale from a static dual-grid layout, through event binding, to a full input form with inline editing, field-level save logic, and multi-record transactions.

## Featured Technology
- 4D Ajax Framework (version 11.2 Release 2)
- Data Grid object (querying, events, row/cell click handlers)
- Bridge 2.0 object (record CRUD, metadata queries)
- JavaScript (DOM manipulation, event listeners, AJAX-style calls)
- 4D Web 2.0 Pack subscription model

## Historical Context
Published in mid-2008 as the 4D Ajax Framework ecosystem matured, this note reflects the era when Web 2.0–style interactivity in 4D meant hand-crafting JavaScript interactions with framework components. The Bridge object and its API were the primary tool for any custom web logic; later, 4D's shift toward REST APIs (v12+), then ORDA (v18+), and eventually Qodly (2020s) rendered the Bridge and the entire 4DAF obsolete. However, the underlying problem—relating parent and child records in a web UI—remains perennially relevant; only the implementation has fundamentally changed.

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework, including the Bridge object and Data Grid as described here, was sunset by 4D Inc. This note's specific code patterns and API calls (e.g., `dax_bridge.addRecord()`, `dax_getTable()`) no longer exist in modern 4D. A developer looking to build parent-child web forms today would use 4D Web Components, Qodly (the modern 4D low-code web platform, GA 2021+), or a custom REST/ORDA backend with a modern JavaScript framework (React, Vue, etc.). The conceptual challenges—filtering child records, handling multi-record persistence, maintaining UI/database synchronization—remain, but the 4DAF's opinionated, JavaScript-heavy approach is now a historical reference point only.
