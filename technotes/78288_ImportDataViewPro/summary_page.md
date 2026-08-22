# Tech Note 19-13: Importing Data to 4D View Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 19, 2019 | **Product/Version:** 4D v17 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78288
**Download:** https://kb.4d.com/DLTN/TN/2019/19-13_4DVPImportData.zip

## Proposition
4D View Pro, 4D's native SpreadJS-based spreadsheet feature, is a strong target for exporting query results into a formattable, shareable document (XLS/PDF). This note shows the object-range API for locating an insertion point and populating cells from an entity selection.

## Key Points
- **`VP Get active cell`** returns a View Pro range object identifying the sheet/row/column of the current selection, used as the import's top-left anchor.
- **No native row/column-add command (as of v17R5):** two workarounds are offered — modifying the exported document object (`VP Export to object`, adjusting `rowCount`/`columnCount`, which resets the view) or calling SpreadJS's JS API directly via `WA Evaluate JavaScript`.
- **`VP Cell`** creates a range object for a specific cell; **`VP SET VALUE`** writes a value object (`value`, `time`, or `format` properties) into that range.
- **Import loop:** iterates entity-selection records/fields, calling `VP SET VALUE` per cell — sequential and can be slow for large datasets.
- **Handling existing content:** shifting/overwrite behavior is easier to implement via JS (`addColumns()`/`addRows()`) than via the document-object approach.
- Five demos progress from basic import to sheet resizing, data shifting, formatted import, and custom field selection/ordering.

## Featured Technology
- 4D View Pro (SpreadJS-based Web Area)
- `VP Get active cell`, `VP Cell`, `VP SET VALUE`, `VP Export to object`
- `WA Evaluate JavaScript` (SpreadJS JS API), ORDA entity selections

## Best Practices Highlighted
1. Prefer the JavaScript-based row/column resize approach when a jarring full-view reload is undesirable.
2. Keep large imports in mind — cell-by-cell `VP SET VALUE` calls don't scale well to very large record/field counts.
3. Watch document width — too many imported fields can run off the visible/printable area of a View Pro sheet.

## Context / Positioning
Published as part of 4D's mid-2019 R-release wave highlighting 4D View Pro's growing native command set, this note reflects the broader move to make classic spreadsheet-and-reporting workflows (previously handled by external plugins or 4D View) achievable natively with object notation and ORDA entity selections.

## Historical Commentary
**Status:** Partially superseded

4D View Pro remains the current, actively developed native spreadsheet feature (fully replacing the legacy 4D View plugin), and the object/range-based API (`VP Get active cell`, `VP Cell`, `VP SET VALUE`) described here is still standard practice today. However, the specific limitation motivating the JavaScript workaround — no native way to resize rows/columns — has been addressed in later 4D versions with additional native View Pro commands, so a developer working in a current 4D version would likely have simpler native alternatives to the `WA Evaluate JavaScript`/SpreadJS-API technique shown here for sheet resizing.
