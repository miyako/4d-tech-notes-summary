# Tech Note 17-10: Object Columns in Listboxes

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** May 25, 2017 | **Product/Version:** 4D View Pro v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77787
**Download:** https://kb.4d.com/DLTN/TN/2017/17-10_ObjectColumnsInListbox.zip

## Proposition
This Tech Note explains 4D v15's list box object-column feature, which lets a single column display mixed data types per row by backing the column array with 4D objects, and documents the object properties that control rendering and behavior (requires a 4D View Pro license).

## Key Points
- **4D Object structure:** property/value pairs similar to JSON, supporting text, numeric, boolean, array, and nested object values.
- **Object-backed columns:** a single list box column array of objects can display different data types per row.
- **Color value type:** documents a color-specific value option for object columns.
- **Events:** covers events specific to object column interaction.
- **Key properties:** Value, Min/Max, Behavior, Dropdowns, Unit Lists, and Alternate Button configuration.
- **Use case walkthrough:** parses an object structure and builds the corresponding list box arrays.
- **License requirement:** this feature requires a 4D View Pro license.

## Featured Technology
- List Box object columns
- 4D Object type
- 4D View Pro
- List box events and properties

## Context / Positioning
Published in 2017 for 4D v16 (documenting a v15-introduced feature), this note is a focused feature reference from the classic Design Mode era, predating Project Mode and ORDA, though the specific List Box/View Pro capability it documents is unrelated to those later architectural shifts.

## Historical Commentary
**Status:** Still relevant

Object-type list box columns remain a supported 4D View Pro feature today, so this note's technical explanation of the property model (Value, Min/Max, Behavior, Dropdowns, Unit Lists, Alternate Button) is still directly usable. The main change since 2017 is that 4D View Pro has grown substantially with additional spreadsheet-grade features, and object columns are now often paired with ORDA entity selections rather than classic arrays/selections, but the core mechanism this note teaches has not been superseded.
