# Tech Note 19-02: A Look at The Features of 4D View Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 30, 2019 | **Product/Version:** 4D View Pro v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78199
**Download:** https://kb.4d.com/DLTN/TN/2019/19-02_4DVPFeatures.zip

## Proposition
As 4D moved fully to 64-bit and phased out the legacy 32-bit 4D View plugin, 4D View Pro emerged as its object-based, SpreadJS-powered successor. This Tech Note (as of v17R4) surveys 4D View Pro's list box integrations, dedicated form area, document structure, and range/formula APIs to orient developers migrating off legacy 4D View.

## Key Points
- **Legacy 4D View deprecated:** 4D View was a 32-bit plugin; 4D View Pro is a native 64-bit component built from scratch around the Object data type, mirroring the 4D Write → 4D Write Pro transition.
- **Variable/Automatic Row Height:** list boxes gain a `Longint` Row Height Array for manual per-row control, or an Automatic Row Height mode with min/max bounds — both require array-based list boxes and a 4D View/View Pro license.
- **Object Type Arrays for list box columns:** assigning an object array lets each cell define its own `valueType` (text, real, integer, Boolean, color, event) plus properties like `requiredList`, `choiceList`, and `alternateButton` for widgets (dropdowns, buttons, combo boxes).
- **4D View Pro Area:** a dedicated form object with a modern ribbon toolbar, contextual menu, and multi-sheet tab navigation, distinct from the classic 4D View plugin area.
- **VP command family:** document manipulation (create/open/save) is handled by commands prefixed `VP`, replacing legacy 4D View commands.
- **Document conversion:** legacy 4D View documents can be converted to the 4D View Pro format for continued use.
- **Ranges, named ranges, and formulas:** 4D View Pro Ranges provide structured objects for reading/writing cell data and defining named ranges/formulas programmatically.
- **Built on SpreadJS:** 4D View Pro is explicitly built atop the third-party SpreadJS spreadsheet engine.

## Featured Technology
- 4D View Pro (64-bit component, Object-based document model)
- `VP` command family
- List box Row Height Array / Automatic Row Height / Object Type Arrays
- 4D View Pro Ranges, Named Ranges, Formulas
- SpreadJS (underlying third-party engine)

## Best Practices Highlighted
1. Read this Tech Note before the bundled sample database, since the sample's inline comments assume this background.
2. Plan migration off legacy 4D View before upgrading to 4D v17R5/v18, where 32-bit plugin support is dropped entirely.
3. Use Object Type Arrays rather than single-typed arrays when a list box column needs mixed data types or widget-like cells.

## Context / Positioning
This note captures 4D View Pro at an early, actively-evolving stage (v17R4), positioning it as functionally comparable to but architecturally distinct from legacy 4D View — part of 4D's broader multi-year effort (alongside 4D Write Pro) to modernize document/spreadsheet handling for a 64-bit-only future.

## Historical Commentary
**Status:** Partially superseded

4D View Pro itself is very much alive and remains 4D's current spreadsheet/grid technology in 2026 — but it has evolved substantially since v17R4, gaining many new APIs, formatting options, and SpreadJS engine upgrades over subsequent 4D versions. Developers should treat this note as historically useful context (why 4D View Pro exists, its architecture) rather than an up-to-date API reference; check current 4D documentation for the full, modern `VP` command set.

The legacy 4D View plugin discussed here as "deprecated" is now fully gone from current 4D releases (32-bit support was dropped as anticipated around v17R5/v18), so the side-by-side comparisons to classic 4D View are purely historical. The list box features described (Row Height Array, Automatic Row Height, Object Type Arrays) remain valid and commonly used today, largely unchanged in concept.
