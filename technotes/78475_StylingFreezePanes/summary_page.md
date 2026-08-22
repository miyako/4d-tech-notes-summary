# Tech Note 20-09: Styling Freeze Panes

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** May 26, 2020 | **Product/Version:** 4D View Pro v18 R2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78475
**Download:** https://kb.4d.com/DLTN/TN/2020/20-09_StylingFreezePanes.zip

## Proposition
4D v18R2 added the ability to set View Pro freeze panes programmatically. This note demonstrates layering a custom, persistent cell style on top of frozen panes — automatically applied and removed as panes are frozen/unfrozen — to visually distinguish frozen from scrollable spreadsheet regions.

## Key Points
- **`VP SET FROZEN PANES` / `VP Get frozen panes`**: set and read the number of leading/trailing frozen rows and columns via a simple object (`columnCount`, `rowCount`, `trailingColumnCount`, `trailingRowCount`).
- **Range computation**: `VP Column`/`VP Row` convert pane counts into concrete cell ranges for both newly frozen panes and panes being reverted from frozen to unfrozen.
- **`VP SET CELL STYLE`**: applies a style object to a range collection; passing `Null` as the style reverts cells to their original appearance.
- **Font manipulation**: `VP Get default style`, `VP Font to object`, and `VP Object to font` let a font string (e.g. "18pt Calibri") be decomposed/recomposed from user-selected attributes (size, family, weight/italic).
- **Conditional autofit**: `VP COLUMN AUTOFIT`/`VP ROW AUTOFIT` are called only when a font comparison detects an actual change, avoiding costly autofit operations on every freeze/unfreeze.
- **Persistence**: the chosen style is saved to a JSON file so it survives and reapplies automatically on subsequent pane freezes.

## Featured Technology
- 4D View Pro (v18 R2 command additions)
- JSON for style persistence
- Object-based range/style APIs (`VP SET CELL STYLE`, `VP Column`, `VP Row`)

## Best Practices Highlighted
1. Compare previous vs. new styles before calling autofit commands to avoid unnecessary performance cost on large documents.
2. Store user-customized styles as JSON so they persist across sessions and can be reapplied consistently.
3. Use `Null` as an explicit "revert to default style" value rather than tracking original styles manually where possible.

## Context / Positioning
This note is part of a wave of tech notes following the v18R2 release that showcased newly added View Pro commands, reflecting 4D's continued investment in View Pro (its modern, in-house spreadsheet component) as a first-class, scriptable building block for business applications, positioned as the forward-looking replacement for older spreadsheet plugin approaches.

## Historical Commentary
**Status:** Still relevant

The freeze-pane and cell-style commands shown here (`VP SET FROZEN PANES`, `VP SET CELL STYLE`, `VP Get/Set default style`, `VP Font to object`/`VP Object to font`) remain part of 4D View Pro's current command set with no deprecation — this pattern is directly usable in modern 4D versions. 4D View Pro itself has continued to receive new built-in capabilities in the years since (more style/format options, improved API ergonomics), so some manual scripting shown here may now have more direct built-in equivalents, but the underlying approach and commands are still valid and commonly used for custom View Pro styling logic.
