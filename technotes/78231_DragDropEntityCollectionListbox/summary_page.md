# Tech Note 19-05: Implementing Drag-and-Drop with Entity/Collection Listboxes

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** March 25, 2019 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78231
**Download:** https://kb.4d.com/DLTN/TN/2019/19-05_EntityCollectionDragDrop.zip

## Proposition
List boxes bound to entity selections or collections can support rich drag-and-drop interactions — reordering, moving, and multi-selecting rows between list boxes — but the right implementation technique depends heavily on which data source type is used.

## Key Points
- **Unordered entity selections** (`query()`, `newSelection()`, `or()`, `and()`, `minus()`): no duplicates, always primary-key ordered, fastest and smallest in memory.
- **Ordered entity selections** (`orderBy()`, `newSelection(dk keep ordered)`): freely reorderable, allow duplicate references, slower/larger.
- **Collections:** fully ordered, mixed-type, and offer the richest manipulation API (`insert`, `slice`, `filter`, `combine`).
- **Drag origin tracking:** `On Begin Drag Over` records the source list box (e.g., into a shared `LB` variable); `On Drop` performs the actual manipulation.
- **Single-entity move (unordered):** `entitySelection.add()` on the destination, `entitySelection.minus()` on the source.
- **Multi-selection move (unordered):** `entitySelection.or()` to union without duplicates, `entitySelection.minus()` to remove.
- **Ordered-entity insertion at a position:** custom `Entity_Insert`/`Entity_Splice`-style helpers combined with the `Drop position` command.
- **Collection same-listbox swap:** uses `Drop position` and current item position (both 0-based, so subtract 1) with a temp variable to avoid overwriting data.
- **Collection cross-listbox multi-move:** `collection.combine()` (optionally at a drop position) to insert, `collection.filter()` with an `indexOf()`-based callback to remove.

## Featured Technology
- ORDA entity selections (`query()`, `newSelection()`, `orderBy()`, `or()`, `and()`, `minus()`)
- Collections (`combine()`, `filter()`, `indexOf()`)
- `Drop position`, `On Begin Drag Over`, `On Drop` form events

## Best Practices Highlighted
1. Choose unordered entity selections when uniqueness and fast bulk removal matter most; choose collections when rich insertion/positioning logic is needed.
2. Use a shared variable set in `On Begin Drag Over` to track the drag's originating list box before `On Drop` fires.
3. Guard collection swaps against dropping on an empty row (check the drop position isn't -1) to avoid data loss.

## Context / Positioning
Published during 4D's v17 R-release wave of ORDA-focused UI recipe notes, this tech note gives developers a clear decision framework and concrete code for one of the more UI-intensive ORDA scenarios — letting end users rearrange or transfer records between list boxes interactively.

## Historical Commentary
**Status:** Still relevant

The entity-selection and collection manipulation methods used throughout (`or()`, `minus()`, `add()`, `combine()`, `filter()`, `orderBy()`) remain part of 4D's current, unchanged ORDA and collection API, and the drag-and-drop event pattern (`On Begin Drag Over`/`On Drop` plus `Drop position`) is still the standard way to implement this UI behavior in 4D forms today. This is a durable reference note with no significant obsolescence — a 4D developer implementing drag-and-drop list boxes today would follow essentially the same approach.
