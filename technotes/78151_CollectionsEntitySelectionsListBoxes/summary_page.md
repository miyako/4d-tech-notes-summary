# Tech Note 18-19: Introduction to Using Collections and Entity Selections in List Boxes

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** October 31, 2018 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78151
**Download:** https://kb.4d.com/DLTN/TN/2018/18-19_4DCollectionEntityLB.zip

## Proposition
4D v17's ORDA introduced two new dataset primitives — collections and entity selections — and list boxes were extended to consume them directly. This note introduces both concepts and shows how to bind, format, and interact with list boxes backed by each, alongside classic array/current-selection list boxes.

## Key Points
- **Collections recap:** ordered, mixed-type lists accessed via bracket notation (`myCollection[0]`), zero-based unlike 4D arrays (`myArray{1}`).
- **Entity selections recap:** ORDA's equivalent of a current selection, produced by querying a `DataClass` within the `Datastore` object model, but storable explicitly in a variable rather than only existing as an implicit global selection.
- **Shared "Data Source" property:** setting a list box's Data Source to "Collection or entity selection" repurposes the "Value or expression" property to hold the actual collection/entity-selection expression, evaluated at form load.
- **Only scalar values render:** list boxes display String, Text, Numeric, Date, Picture, and Boolean values only — complex/inconsistent object shapes in a collection produce blank cells or gaps.
- **Consistent object shape matters:** a collection of uniformly-shaped objects (e.g., `{"name":..., "age":...}`) works well because columns can bind to object property names.
- **Row/column identification and in-place editing:** the note covers identifying selected rows/columns and modifying list box data directly.
- **Managing entity selections and drill-down:** includes maintaining an entity selection over time and opening a selected entity into a "detail form."
- **Sample database demos:** separate demos for collection-based list boxes, entity-selection-based list boxes, row/column identification, and entity-selection maintenance.

## Featured Technology
- 4D Collections (bracket/object notation)
- ORDA entity selections, DataClass, Datastore object model
- List box "Data Source: Collection or entity selection" property
- List box column/row APIs for collection- and entity-selection-backed grids

## Best Practices Highlighted
1. Use collections of consistently-shaped objects (same property names) when binding to a multi-column list box to avoid blank/gap cells.
2. Ensure the collection or entity selection expression is available/populated before the form loads, since list box binding occurs at load time.
3. Remember list boxes only render scalar value types — never bind columns directly to nested objects/collections expecting automatic rendering.

## Context / Positioning
Published shortly after ORDA's introduction in 4D v17, this note helped developers bridge classic list box usage (arrays, current selections) into the new object-oriented ORDA world, demonstrating that a familiar, heavily-used form control could adopt collections and entity selections without requiring a wholesale UI rewrite.

## Historical Commentary
**Status:** Still relevant

Binding list boxes to collections and entity selections remains a core, actively used 4D technique today, and the ORDA object model described (`ds` → DataClass → entitySelection → entity) is unchanged in its fundamentals. This note's core guidance — data shape consistency for collections, scalar-only rendering, and the shared Data Source property — is still accurate.

Since 2018, 4D has continued to add more list box features and ORDA capabilities (e.g., richer entity selection manipulation, additional list box column types), so developers should check current documentation for newer options, but nothing in this note has been deprecated or superseded; it remains a solid introductory reference for this pattern.
