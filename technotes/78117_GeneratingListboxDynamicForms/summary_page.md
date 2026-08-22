# Tech Note 18-16: Generating a Listbox using Dynamic forms

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** September 4, 2018 | **Product/Version:** 4D v17 (feature introduced v16R6) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78117
**Download:** https://kb.4d.com/DLTN/TN/2018/18-16_DynamicListbox.zip

## Proposition
List boxes can be built either the conventional way — placed in a form editor and bound via property list/code — or entirely through a JSON Dynamic Form definition. This note walks through both approaches for all four list box data-source types (current selection, array, collection, entity selection) so developers can compare and choose the right technique.

## Key Points
- **Conventional current/named-selection list box:** columns bound to field expressions (e.g., `[Table_1]ID`); data populated via `QUERY`/`ALL RECORDS`.
- **Conventional array-based list box:** columns bound to array variable names; populated with `ARRAY TEXT`/`APPEND TO ARRAY`.
- **Conventional collection/entity-selection list box:** columns reference object properties via the `This` keyword on a collection or ORDA object variable; collections built with `New collection(New object(...))`, entity selections with `ds.Table_1.all()`.
- **Opening conventional forms:** typically via `Open form window` or `Open window`.
- **Dynamic approach:** no form editor step — a JSON definition (literal or built with `New object`/`New collection`) is passed directly to `Open form window` to generate a fully configured, data-bound list box purely from code.
- **Same four data-source types supported dynamically:** the note documents JSON properties for selection-, array-, collection-, and entity-selection-based dynamic list boxes.
- **Sample database:** demonstrates and compares all four calling patterns plus their generated JSON definitions, including display via subform.

## Featured Technology
- 4D Dynamic Forms / JSON form definitions
- List box data sources: current/named selection, array, collection, entity selection
- `Open form window`, `OBJECT SET SUBFORM`
- ORDA `ds.Table.all()`

## Best Practices Highlighted
1. Choose the list box data-source type (selection, array, collection, entity selection) based on whether the underlying data is record-based, memory-array-based, or ORDA-based, before deciding on conventional vs. dynamic construction.
2. Use collection/entity-selection-based list boxes with the `This` keyword when binding to object properties, rather than reworking data into flat arrays.
3. Prefer the JSON Dynamic Form approach when list box structure needs to be determined at runtime (e.g., generic/metadata-driven forms).

## Context / Positioning
Published as Dynamic Forms matured from their v16R6 introduction into broader v17 usage, this note reinforced that a workhorse form object like the list box could be fully generated via code, supporting 4D's push toward more flexible, runtime-configurable UIs alongside the parallel rise of ORDA-based data access.

## Historical Commentary
**Status:** Still relevant

Generating list boxes via JSON Dynamic Forms remains a fully supported, current 4D capability, and all four data-source types described (current selection, array, collection, entity selection) are still valid today. Nothing here has been deprecated.

The main shift since 2018 is emphasis rather than mechanics: collection- and entity-selection-based list boxes (ORDA-driven) have become the more commonly recommended modern pattern for new development compared to classic current-selection or array-based binding, since most new 4D applications are built around ORDA. Developers today would still recognize and could directly reuse the JSON definitions and code patterns shown in this note.
