# Tech Note 24-10: Structure Info Class

**Author:** Thomas Maul, VP 4D Product Strategy, 4D Germany.
**Published:** August 27, 2024 | **Product/Version:** 4D v20 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79506
**Download:** https://kb.4d.com/DLTN/TN/2024/24-10_StructureInfoClass.pdf

## Proposition
While 4D offers many commands to introspect a database's structure, the project mode catalog.xml file is the richest source of structural information — but it isn't directly queryable. This note introduces a class that converts the catalog into an object, making it trivial to query relations, indexes, tables, and fields.

## Key Points
- **Shared singleton eliminates setup boilerplate:** Built with 4D 20 R5's singleton pattern, the class auto-initializes on first use — no manual instance creation or explicit loading step required.
- **Reads catalog.4DCatalog via Filesystem pathnames:** Using `File("/PROJECT/Sources/catalog.4DCatalog").getText()`, the class transparently reads the catalog even from inside a compiled/zipped .4DZ package.
- **.get() exposes the full structure object:** Developers can browse the entire parsed structure (tables, fields, indexes, relations, journal info) using standard object notation and collection.query().
- **getTableInfo()/getFieldInfo() support flexible lookups:** Both accept name, uuid, or pointer identifiers, e.g. `{name: "Customer"}` or `{ptr: ->[Table_1]}`.
- **getRelationInfo()/getRelationInfos() find relations directionally or bidirectionally:** Supports fromTable_name/toTable_name for directed lookups, Table_name1/Table_name2 for either direction, and wildcards like "Cust@".
- **getIndexInfo()/getIndexInfos() cover multi-index fields:** A single field can be indexed individually and as part of a combined index simultaneously; getIndexInfos() returns all of them for a table or field.
- **Published as open source:** Available on GitHub (ThomasMaul/Classes) for direct copy-in, allowing ongoing updates and bug fixes from the community.

## Featured Technology
- **Shared singleton class** — 4D 20 R5 pattern enabling zero-setup, cross-process cached class instances.
- **catalog.4DCatalog (catalog.xml)** — the project mode structure definition file parsed by the class.
- **4D Filesystem pathnames (File() command)** — used to transparently read files from interpreted or compiled/.4DZ packages.
- **collection.query()** — used for ad hoc filtering of the raw structure object's tables/fields/relations/indexes.

## Best Practices Highlighted
1. Use the class's dedicated helper functions (getTableInfo, getRelationInfos, etc.) rather than manually parsing .get()'s raw output for common lookups.
2. Leverage wildcard identifiers (e.g., "I@") when searching for relations or tables matching a naming pattern.

## Context / Positioning
Published shortly after 4D 20 R5 introduced singleton classes, this note showcases a practical, real-world application of that new language feature — reinforcing 4D's pattern of pairing new core language capabilities (like singletons) with example utility classes that solve everyday introspection and tooling needs for developers working in project mode.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
