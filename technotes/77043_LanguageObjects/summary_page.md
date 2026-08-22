# Tech Note 14-08: Getting Started with Language Objects in 4D

**Published:** May 16, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77043
**Download:** https://kb.4d.com/DLTN/TN/2014/14-08_C_OBJECTbasics.zip

## Proposition
4D v14 introduces `C_OBJECT`, a new JSON-inspired language data type for storing self-documenting key/value structured data in memory, along with a full command set to create, read, modify, and inspect objects — a foundational building block for all later 4D object-based development.

## Key Points
- Objects store data as named property/value pairs, are random-access, fully modifiable, and can be nested inside each other or stored in/hold arrays.
- Contrasted with BLOBs: an object's content is self-describing and inspectable, unlike an opaque byte blob whose layout only the creator understands.
- Core command family: `OB SET`, `OB Get`, `OB SET ARRAY`, `OB GET ARRAY`, `OB Copy`, `OB Remove`, `OB GET PROPERTY NAMES`, `OB Is defined`, `OB Get type`.
- `C_OBJECT` is a *language* type only — it cannot be stored directly as a table field; persisting requires converting to/from BLOB or Text.
- Related commands were extended to support objects/MIME types: `BLOB TO VARIABLE`/`VARIABLE TO BLOB`, `VARIABLE TO VARIABLE`, `SET/GET PROCESS VARIABLE`, `WEB SEND BLOB`, `HTTP Get`/`HTTP request`, `WEB SEND TEXT`, `WA EXECUTE JAVASCRIPT FUNCTION`, `WA Evaluate JavaScript`.
- Objects can be imported from or exported to JSON strings, enabling interchange with other languages/platforms.
- A nine-page bundled sample database walks through each command group (creation, get/set, arrays, copy/remove, property inspection, type/definedness checks, JSON null/empty handling).

## Featured Technology
- `C_OBJECT` language data type (4D v14)
- `OB_` command family for object manipulation
- JSON import/export of 4D objects
- Web/JavaScript command updates to support object and MIME-typed payloads

## Best Practices Highlighted
1. Use objects instead of BLOBs when structured, self-describing data needs to be passed around or debugged.
2. Remember objects cannot be stored as table fields directly — convert to Text/BLOB for persistence.
3. Leverage JSON import/export for exchanging structured data with external systems and languages.

## Context/Positioning
Published as 4D v14 shipped, this note introduced developers to what was, at the time, one of the most significant new language capabilities 4D had added in years, positioning objects as the future vehicle for JSON/web interoperability.

## Historical Commentary
**Status:** Partially superseded

This note captures the very first appearance of native objects in the 4D language — a foundational moment that ultimately enabled everything from modern JSON handling to ORDA. The verbose `OB_` command-based API documented here has since been almost entirely superseded by concise object literal syntax and dot notation (`$obj.property`, `$obj:={}`), which became the idiomatic way to work with 4D objects. Conceptually, however, the note's core message — that objects are a first-class, JSON-shaped structure at the heart of 4D — proved remarkably prescient, since this exact object model underpins ORDA entities and entity selections (4D v16 R5/R6, 2017) and, later, 4D classes.
