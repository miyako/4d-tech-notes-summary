# Tech Note 15-16: Introduction to Object field in v15

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** September 3, 2015 | **Product/Version:** 4D v15 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77362
**Download:** https://kb.4d.com/DLTN/TN/2015/15-16_ObjectField.zip

## Proposition
4D v15 extends the in-memory object type introduced in v14 into a persistent, indexable table field type. This note introduces the Object field, explains how schema-less or schema-based JSON-like data can be stored in it, and demonstrates fast indexed querying via the new `QUERY BY ATTRIBUTE` command.

## Key Points
- **New Object field data type:** persists property/value (JSON-like) data directly in a table field, with or without a predefined schema.
- **Builds on v14's C_OBJECT:** takes the in-memory object type introduced a version earlier and makes it a first-class, storable, indexable field.
- **Indexed for performance:** the note emphasizes that Object field queries remain fast even against schema-less data, thanks to indexing support.
- **Language integration:** populate via `OB SET` or `JSON PARSE`; interacts with array commands, formulas, and can be entered directly through 4D Forms.
- **`QUERY BY ATTRIBUTE` deep dive:** the core new query command, with its query-string syntax built from attribute path, operator, and value.
- **Special operators:** `#` tests for property presence/absence; `@` wildcard matches within array values; `*` combines multiple query conditions.
- **Extensive worked examples:** roughly a dozen labeled cases covering first/second-level nesting, array vs. scalar properties, numeric ranges, and date queries.

## Featured Technology
- Object field (new v15 data type)
- `QUERY BY ATTRIBUTE`
- `OB SET` / `JSON PARSE`

## Best Practices Highlighted
1. Use Object fields for genuinely variable/evolving data shapes rather than redesigning table structure for every new attribute.
2. Index Object fields when query performance on nested attributes matters.
3. Use the `#` presence operator to defensively check whether a property exists before querying its value.

## Context / Positioning
This note documents one of 4D v15's most forward-looking features, arriving in the classic Design Mode era, well before ORDA (v16 R5/R6, 2017) and Project Mode (v17, 2018). It represents 4D's earliest serious step toward native JSON-like, schema-less data storage — a concept that ORDA would later generalize much further.

## Historical Commentary
**Status:** Still relevant

The v15 Object field was ahead of its time and remains a supported, useful 4D data type today for schema-less or semi-structured data. That said, ORDA's later arrival added a richer, dot-notation query language and entity-based access model that covers much of the same ground as `QUERY BY ATTRIBUTE` with more modern ergonomics, so while this note's techniques still work, a current 4D project would often reach for ORDA entity selections/queries first and fall back to `QUERY BY ATTRIBUTE` mainly for legacy or Object-field-specific needs.
