# Tech Note 20-17: Creating a Custom ORDA Query Editor

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** September 30, 2020 | **Product/Version:** 4D v18 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78557
**Download:** https://kb.4d.com/DLTN/TN/2020/20-17_ORDA_Query_Editor.zip

## Proposition
4D's built-in Query Editor predates ORDA and does not take advantage of its performance benefits. This Tech Note shows how to build a fully custom, ORDA-native query editor form — replicating the classic editor's row-based workflow but generating a `dataClass.query()` call instead of a classic query.

## Key Points
- **Row-based dynamic UI**: each query row bundles a table dropdown, conjunction dropdown, comparison-operator dropdown, table-field hierarchical list, and a value text field.
- **State tracking**: `Form.queryRows`, a collection of integers, tracks which numbered rows are currently active/visible.
- **Dynamic field lists**: selecting a different table refreshes the field hierarchical list via `GET TABLE TITLES`/`GET FIELD TITLES`.
- **Add/remove rows**: the plus button duplicates row objects; the minus button hides a row and updates `Form.queryRows`; both buttons and the conjunction control adapt automatically when only one row remains.
- **Query assembly**: all active rows are combined into a single text query statement, respecting conjunctions (AND/OR), and passed to `dataClass.query()`.
- **Display conversion**: the resulting entity selection is converted to a current selection for display in the output form (for the demo's presentation purposes).

## Featured Technology
- ORDA `dataClass.query()`
- Dynamic dropdown/hierarchical-list form objects
- Form-level collection state (`Form.queryRows`)
- GET TABLE TITLES / GET FIELD TITLES
- Entity selection ↔ current selection conversion

## Best Practices Highlighted
1. Track dynamic UI row state in a Form-level collection rather than relying on hard-coded row counts.
2. Refresh dependent UI (field lists) immediately when an upstream selection (table) changes.
3. Build query strings incrementally and validate/combine them centrally before passing to `dataClass.query()`.

## Context / Positioning
This note exemplifies 4D's mid-2020 push to get developers to fully embrace ORDA even where built-in tooling (the classic Query Editor) hadn't yet been rebuilt around it, encouraging teams to invest in custom, ORDA-first UI components that could take advantage of ORDA's substantial LAN/WAN performance improvements over classic 4D queries.

## Historical Commentary
**Status:** Still relevant

Building a custom UI on top of `dataClass.query()` remains exactly how developers construct dynamic ORDA query builders in 4D today — the technique itself has not been superseded. If anything, the motivating problem has intensified in 4D's favor: ORDA-based data access has become the default and expected approach across the platform, making the "classic 4D Query Editor" this note contrasts against increasingly a legacy holdover rather than a serious alternative. Developers building similar query UIs today would follow essentially the same pattern shown here, possibly combined with more modern typed variable declarations (`var`) and class-based helper functions introduced in slightly later 4D versions.
