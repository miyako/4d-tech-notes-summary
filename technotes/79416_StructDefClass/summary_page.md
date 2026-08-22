# Tech Note 24-06: Developer Tool: Structure Definition Class

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** April 30, 2024 | **Product/Version:** 4D v20 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79416
**Download:** https://kb.4d.com/DLTN/TN/2024/24-06_StructDefClass.zip

## Proposition
Developers frequently need to answer ad-hoc questions about a database's structure — e.g., which fields are indexed with Cluster B-tree, or which tables are excluded from the log file. Prior to 4D 20 R4, EXPORT STRUCTURE only produced XML, which required XPath knowledge and inconsistently listed properties. This note shows how to leverage the new HTML export format to build a fully queryable, in-memory structure model.

## Key Points
- **HTML export as data source:** `EXPORT STRUCTURE` (or File > Export > Structure definition to HTML) now produces a browser-viewable HTML page listing every table's properties, triggers, fields, and relations.
- **Predictable markup patterns:** Each table section starts with a `"[ - ]"` toggle label; values live inside `<td>` cells; booleans are represented by the presence/absence of an `<img>` tag; each subsection starts with an `<h2>` tag.
- **HTML over XML:** HTML requires no XPath, lists properties more consistently across value types, and has less noise to parse than the XML export.
- **JSON object construction:** A `parseStructDefHTML` method walks the HTML text and builds a JSON object with a "tables" collection (each holding table info, triggers, fields, and many-to-one/one-to-many relations) plus a flattened "all fields" collection.
- **StructDef class:** The constructor stores the parsed JSON in an instance property (`This.struct`); class functions like `findFields($prop; $val)` iterate the relevant collection and collect matches into an output collection.
- **Additional query functions:** `findTables` and `findRelations` mirror `findFields`, with parameter/type checking and partial-value matching support in the full sample implementation.
- **Sample UI application:** A form (`openStructDefFinder`) lets users search by property/value for tables, fields, and relations, and double-click a table row to drill into its fields.
- **Component-ready design:** The sample app can be built as a 4D component and installed into any existing application to instantly gain a structure-inspection tool.

## Featured Technology
- **EXPORT STRUCTURE (HTML mode):** New in 4D 20 R4, source of the parseable structure text.
- **Text/HTML parsing:** Custom method traversing tags/patterns without external XML libraries.
- **JSON object model:** Native 4D object/collection literals used to represent structure metadata.
- **4D Classes:** `StructDef` class encapsulating parsed data and query functions.
- **Collections:** `.push()` and iteration (`For each`) used to build and filter results.
- **4D Component packaging:** Sample app designed to be compiled/installed as a reusable component.

## Best Practices Highlighted
1. Prefer HTML over XML export when parsing structure definitions programmatically, due to consistency and simpler parsing.
2. Encapsulate parsed structure data behind a class with dedicated query functions rather than ad hoc traversal in calling code.
3. Package structure-inspection tooling as a component so it can be dropped into any target application.

## Context / Positioning
This note reflects 4D's continued investment in developer tooling and introspection capabilities around 4D 20 R4, encouraging developers to treat structure metadata as queryable data rather than a static export. It complements 4D's broader push toward object/collection-based programming (ORDA-era idioms) by modeling structure information as JSON rather than XML DOM trees.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
