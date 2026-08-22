# Tech Note 15-15: Extended Functionality with Object Get Coordinates and Listbox Sub Objects

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** September 3, 2015 | **Product/Version:** 4D v15 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77361
**Download:** https://kb.4d.com/DLTN/TN/2015/15-15_ExtendedFnWithOGC.zip

## Proposition
In 4D v15, `OBJECT GET COORDINATES` gained the ability to return accurate coordinates for listbox sub objects (columns, headers, footers) rather than just the parent listbox. This note explains the new behavior and shows two practical UI techniques enabled by it.

## Key Points
- **Prior limitation:** before v15, calling `OBJECT GET COORDINATES` on a listbox column/header/footer returned the parent listbox's coordinates instead of the sub object's own.
- **Coordinate plane convention:** origin (0,0) at the form's top-left corner; X increases rightward, Y increases downward; every object has left/top/right/bottom coordinates.
- **Command parameter forms:** objects can be referenced by variable name or by object name, each with slightly different call syntax.
- **Listbox sub-object hierarchy:** columns, headers, and footers each have their own coordinate space relative to the parent listbox, illustrated with diagrams.
- **Example 1 — moving objects with listbox columns:** demonstrates repositioning other form objects to track a specific column's location, useful for overlays.
- **Example 2 — hover detection:** determines which listbox column the mouse is currently over by comparing cursor position against each column's coordinates.

## Featured Technology
- `OBJECT GET COORDINATES`
- Listbox sub objects: columns, headers, footers

## Best Practices Highlighted
1. Reference listbox sub objects by their explicit sub-object names when precise coordinate data is needed, rather than assuming parent-listbox coordinates suffice.
2. Recompute overlay object positions whenever the listbox is resized or scrolled, since sub-object coordinates change dynamically.

## Context / Positioning
This is a small, focused classic Design Mode-era enhancement note (v15, 2015) about a specific form-object command used in traditional pixel-coordinate-based 4D form scripting — years before Project Mode and any move toward more declarative UI approaches.

## Historical Commentary
**Status:** Still relevant

`OBJECT GET COORDINATES` and the listbox sub-object coordinate model documented here remain functionally unchanged and fully supported in current 4D, so the technique still works as described. That said, this kind of manual pixel-coordinate UI scripting is characteristic of classic 4D form development; while it's not deprecated, more recent 4D form/listbox capabilities have expanded around it, and developers today have more built-in options for some UI customization needs that once required this level of manual coordinate math.
