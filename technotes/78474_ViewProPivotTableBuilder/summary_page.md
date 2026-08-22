# Tech Note 20-08: 4D View Pro Pivot Table Builder

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** May 26, 2020 | **Product/Version:** 4D View Pro v18 R2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78474
**Download:** https://kb.4d.com/DLTN/TN/2020/20-08_ViewProPivotTable.zip

## Proposition
Large flat data tables are hard to interpret without summarization. This note builds a basic pivot table tool from scratch — letting a user pick a table, rows field, columns field, and aggregated value, then procedurally generating the pivot in a View Pro document — using ORDA for data access and new v18R2 View Pro commands for spreadsheet manipulation.

## Key Points
- **Cascading dropdown UI**: table → rows → columns → values, each populated dynamically and reset when an earlier selection changes.
- **ORDA data access**: `ds[$selected_table]` retrieves the dataclass; `.all()` loads the entity selection once for reuse across the builder's logic.
- **`OB GET PROPERTY NAMES`**: enumerates field names on the dataclass/entity for populating rows/columns dropdowns.
- **Aggregation typing**: numeric fields are summarized as "Sum of X"; non-numeric fields as "Count of X", decided by checking `table_data[$prop].type`.
- **`VP DELETE COLUMNS` / `VP INSERT COLUMNS`**: used instead of `VP NEW DOCUMENT` to refresh only the affected region, allowing multiple pivot tables on different sheets of the same document.
- **Collections over arrays**: collections (`New collection`, `.push()`) manage intermediate data due to their richer built-in methods, then converted to arrays where needed for legacy dropdown APIs.

## Featured Technology
- 4D View Pro (v18 R2 command set)
- ORDA (datastore `ds`, dataclass, entity selection)
- 4D Collections

## Best Practices Highlighted
1. Load an entity selection once per table selection and reuse it, rather than re-querying for each pivot recalculation.
2. Use targeted `VP DELETE/INSERT COLUMNS` instead of clearing the whole document, preserving other sheets/data.
3. Reset dependent UI selections whenever an upstream selection (table, rows) changes to avoid stale/invalid pivot configurations.

## Context / Positioning
Published alongside other v18R2 View Pro tech notes, this piece showcased how ORDA (4D's then-newer, more modern data access layer) could be combined with View Pro's expanding command set to build genuinely useful business tools — a pivot table — entirely within 4D, without third-party BI software or manual spreadsheet exports.

## Historical Commentary
**Status:** Partially superseded

ORDA usage shown here (`ds[table].all()`, entity selections, `OB GET PROPERTY NAMES`) remains exactly how modern 4D data access is done — that part of the note is fully current. However, 4D View Pro has since added a native, built-in Pivot Table feature (a Pivot Panel/Pivot Table object directly configurable in the interface and API), which now covers most of what this hand-rolled builder implements manually. For new projects, a developer today should generally reach for 4D View Pro's built-in pivot table support rather than reimplementing the cascading-dropdown pattern shown here; this tech note is best read now as a useful illustration of ORDA + View Pro scripting technique rather than the recommended way to add pivot tables to a modern app.
