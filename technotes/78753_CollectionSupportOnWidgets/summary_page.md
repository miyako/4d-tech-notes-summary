# Tech Note 21-12: Collection Support on Popup Dropdown List, Combo Box, and Tab Control

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** July 29, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78753
**Download:** https://kb.4d.com/DLTN/TN/2021/21-12_CollectionSupportOnWidgets.zip

## Proposition
Before v19, pop-up/drop-down lists, combo boxes, and tab controls required arrays for programmatic value population. This note shows the new object/collection-based data source, comparing it directly with the classic array approach and explaining why collections are the better default going forward.

## Key Points
- **New object data source shape:** `{ values: Collection, index: Integer, currentValue: Any }` bound to a Form/process variable via Object expression type.
- **Classic comparison:** the array-based approach requires choosing 1 of 11 typed `ARRAY` declaration commands and manually indexing entries, including a `{0}` placeholder trick.
- **Placeholders:** with collections, set `currentValue` to the placeholder text and `index` to `-1` (combo boxes ignore `index`).
- **Declaration flexibility:** collections declared via `C_COLLECTION` or the `var` keyword support mixed types and don't require knowing the size up front.
- **Richer API surface:** collections expose roughly double the methods of arrays, e.g. `collection.map()`, `.join()`, `.push()`, `.sort()`.
- **Cross-process data sharing:** collection-based form data can be passed cleanly via `DIALOG(formName; $formdata_o)`, avoiding process/interprocess variables that array-based objects require.
- **Widget-specific nuances:** tab controls use `index` (with `FORM GOTO PAGE` to sync the visible page); combo boxes ignore `index` entirely; drop-downs use both `index` and `currentValue`.

## Featured Technology
- Collections (`New collection`, `.push()`, `.sort()`, `.map()`, `.join()`)
- Form data objects passed via `DIALOG`
- Classic ARRAY TEXT / array-based widget data sources (for comparison)

## Best Practices Highlighted
1. Prefer collection/object data sources over arrays for new form widget development.
2. Use Form variables (not process variables) to bind collection-based widget data, enabling clean data transfer via `DIALOG`.
3. Remember combo boxes don't use the `index` property, unlike drop-downs and tab controls.

## Context / Positioning
This note is part of 4D's broader, multi-release push (parallel to ORDA's rollout) to replace array/pointer-based idioms with collections and objects throughout the language and the form engine — extending that shift specifically into widget data sources for the first time in v19.

## Historical Commentary
**Status:** Current

This collection-based technique is still exactly how 4D recommends populating these widgets today — nothing has superseded it, and it remains fully valid and commonly used. The classic array-based approach documented here for comparison still works (arrays haven't been removed), but it's firmly the legacy pattern; new form development in 2026 should default to the object/collection data source shown in this note, consistent with 4D's ongoing preference for collections and classes over arrays and pointers across the whole language.
