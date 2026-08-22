# Tech Note 15-21: Conversion between XML and JSON

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** November 17, 2015 (revised May 22, 2019) | **Product/Version:** 4D v17 (originally v15) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77416
**Download:** https://kb.4d.com/DLTN/TN/2015/15-21_XMLandJSONConversion_R2.zip

## Proposition
XML and JSON both store/transport structured data but differ in verbosity and syntax. This note explains their structural differences and demonstrates a purely 4D-language, recursive method to convert data from one format to the other in both directions, complete with a sample database.

## Key Points
- **Structural mapping:** XML's nested `<Element>` tags map conceptually to JSON's property/value objects; repeated child elements become JSON arrays.
- **XML → 4D object:** Parses XML using `DOM PARSE XML SOURCE`/`DOM PARSE XML VARIABLE`, then recursively walks element names, attributes, and values into a native 4D object via `OB SET`.
- **4D object → JSON:** Once XML is captured as an object, `JSON STRINGIFY` produces the JSON text directly.
- **JSON → XML:** `JSON PARSE` reconstructs a 4D object from JSON text, then the DOM XML creation commands (`DOM CREATE XML REF`, `DOM SET XML ATTRIBUTE`, `DOM SET XML ELEMENT VALUE`) rebuild an XML tree recursively.
- **Repeated elements handled manually:** Because the algorithm processes one element at a time, repeated XML elements must be accumulated into JSON arrays using `OB GET ARRAY`/`OB SET ARRAY` rather than overwritten.
- **Known lossy limitations:** colons in property names, 2D arrays, and mixed value/child XML nodes (folded into a `#text` pseudo-property) are called out explicitly as imperfect conversions.
- **Sample database:** ships with a simple two-variable UI (XML pane, JSON pane) and conversion buttons in each direction, plus a pretty-print toggle.

## Featured Technology
- `JSON STRINGIFY` / `JSON PARSE`
- DOM XML theme (`DOM PARSE XML SOURCE/VARIABLE`, `DOM GET XML ELEMENT NAME/VALUE`, `DOM COUNT XML ATTRIBUTES`, `DOM GET ATTRIBUTE BY INDEX`, `DOM CREATE XML REF`, `DOM SET XML ATTRIBUTE/ELEMENT VALUE`, `DOM EXPORT TO FILE/VAR`)
- `OB SET` / `OB SET ARRAY` / `OB GET ARRAY`

## Best Practices Highlighted
1. Use recursion to handle arbitrarily deep XML/object nesting rather than fixed-depth code.
2. Accumulate repeated sibling elements into arrays rather than overwriting a single property.
3. Be aware of and document lossy conversion edge cases before relying on round-tripping data.

## Context / Positioning
Published in the classic Design Mode era (v15, later revised for v17), this note predates ORDA and 4D's more modern object/collection APIs, but JSON STRINGIFY/PARSE were already fairly mature 4D commands at this point, showing 4D's early pivot toward JSON as the primary interchange format even while XML tooling (DOM commands) remained in heavy use for legacy integrations.

## Historical Commentary
**Status:** Partially superseded

The core JSON commands (JSON STRINGIFY/PARSE) used here remain valid in modern 4D, but the manual recursive DOM-XML-to-object conversion approach has become less necessary as 4D's object and collection classes matured and as JSON-first APIs (particularly with ORDA, introduced ~v16 R5/R6 in 2017) became the default way to move data around. XML integration work has generally declined industry-wide in favor of JSON/REST, so while the DOM XML commands still function for backward compatibility, most new 4D projects would reach for JSON natively rather than needing this XML bridge at all.
