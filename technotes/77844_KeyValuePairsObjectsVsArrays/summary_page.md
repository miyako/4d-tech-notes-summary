# Tech Note 17-16: Key Value Pairs Using Objects vs. Arrays

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** August 31, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77844
**Download:** https://kb.4d.com/DLTN/TN/2017/17-16_KVPairUsingObject.pdf

## Proposition
This Tech Note compares the traditional two-parallel-array approach to key/value pair storage against using a single 4D object, arguing that objects are easier to update, faster to access, easier to serialize, and support multiple value types.

## Key Points
- **Array-based KV pairs:** two synchronized arrays (keys, values) require manual index management and extra existence checks.
- **Object-based KV pairs:** a single `C_OBJECT` with `OB SET` collapses key/value storage into simple property assignment.
- **Easier updates:** setting a property value overwrites in place without array index bookkeeping.
- **Faster access:** property-based lookup outperforms scanning parallel arrays for matches.
- **Serialization:** objects export/import as JSON text easily, unlike array pairs.
- **Multiple data types:** a single object can hold text, numeric, boolean, arrays, and nested objects as values.

## Featured Technology
- 4D Object type (C_OBJECT)
- OB SET / OB Get commands
- ARRAY TEXT / APPEND TO ARRAY (for comparison)
- JSON serialization of 4D objects

## Best Practices Highlighted
1. Prefer 4D objects over parallel arrays for key/value pair storage.
2. Use object serialization (JSON) for persisting key/value data to disk.
3. Take advantage of objects' mixed-type value support instead of maintaining separate arrays per type.

## Context / Positioning
Published in 2017 for 4D v16, this note reflects the classic Design Mode era where the 4D object type was already available but many developers still defaulted to older array-pair idioms from earlier 4D versions.

## Historical Commentary
**Status:** Still relevant

This note's central recommendation to prefer objects over parallel arrays for key/value storage has aged well and remains best practice in current 4D. The specific command syntax (`C_OBJECT`, `OB SET`) is classic-era 4D that has since been joined by newer object literal syntax, dot notation, and typed `var` declarations (from v19+), but the underlying architectural advice needs no correction.
