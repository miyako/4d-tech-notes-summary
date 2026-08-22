# Tech Note 14-15: Dynamic Interface using Object Set Data Source

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** October 9, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77158
**Download:** https://kb.4d.com/DLTN/TN/2014/14-15_DynamicInterface.zip

## Proposition
This note explains 4D v14's new `OBJECT SET DATA SOURCE` capability — previously, a form object's Data Source was fixed at design time — and demonstrates it by building a form with a Control Tab object where each tab dynamically loads and displays a different set of a table's fields at runtime, using popup lists and generated field-set buttons rather than one static form per table.

## Key Points
- **Design-time limitation removed:** prior to v14, an object's bound field/variable Data Source could not be changed once the form was running; v14 lifts this restriction.
- **Object-by-object behavior differs:** hierarchical lists, list boxes, buttons, and hierarchical popups each respond somewhat differently when their data source is reassigned at runtime.
- **Worked example:** a Control Tab object dynamically creates field-set tabs, each populated by choosing fields from a popup list rather than being pre-built per table.
- **Auto-growing tab control** expands automatically as more field sets are added by the user.
- **Navigation aids:** Previous/Next buttons let the user step through the dynamically created field sets.
- **Reduces per-table form duplication:** a single generic form can serve many tables instead of building a bespoke form for each.

## Featured Technology
- OBJECT SET DATA SOURCE command
- Control Tab / Tab Control object
- Runtime rebinding of form object data sources

## Context / Positioning
Published October 2014 for 4D v14.0, documenting a then brand-new command in the classic binary Design Mode era, well before ORDA introduced object/entity-attribute-based dynamic data binding as an alternative mechanism for building generic, data-driven forms.

## Historical Commentary
**Status:** Still Relevant

`OBJECT SET DATA SOURCE` is still part of 4D's command set in current versions, so this technique remains directly usable; it hasn't been deprecated, just supplemented by newer entity/collection-based dynamic UI approaches introduced with ORDA.

For teams already on ORDA and Project Mode, dynamic UI generation today might lean more on binding list boxes to entity selections/collections and iterating attributes programmatically, but for classic field-by-field dynamic forms, this v14-era command-based technique is still a valid and reasonably current approach.
