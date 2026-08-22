# Tech Note 19-16: Creating a Custom File Explorer

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** September 25, 2019 | **Product/Version:** 4D v17 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78326
**Download:** https://kb.4d.com/DLTN/TN/2019/19-16_CustomFileExplorer.zip

## Proposition
With the introduction of object-notation File and Folder commands, 4D developers can build a fully custom in-app file explorer — complete with sorting, navigation history, and folder management — without relying on the OS's native file picker.

## Key Points
- **Listing contents:** `folder.folders(fk ignore invisible).concat(folder.files(fk ignore invisible)).orderBy(...)` builds the display collection.
- **Collection-based list box:** columns bind directly to object expressions like `This.getIcon(pxSize)`, `This.fullName`, `This.modificationDate`, `This.size`.
- **Custom formatting methods:** `displayDateModified` merges date+time into one readable string; `displaySize` scales bytes into KB/MB/GB with a simple loop.
- **Manual column sorting:** `LISTBOX GET ARRAYS` + `Find in array` identify the clicked header so `.orderBy()` can be re-applied ascending/descending.
- **Folder navigation:** two collections (`prev_stack`, `next_stack`) act as history stacks, pushed/popped on Previous/Forward clicks — a compact undo/redo-style pattern.
- **Folder creation/deletion:** `folder.create()` and `folder.delete()` are the primary commands; deletion is guarded with `ON ERR CALL` to catch non-empty-folder errors.
- **Error surfacing:** `GET LAST ERROR STACK` retrieves and displays a readable error message when a delete fails.

## Featured Technology
- Object-notation File/Folder commands (`folder.folders()`, `folder.files()`, `folder.create()`, `folder.delete()`)
- Collection-based list boxes, `.orderBy()`, `.concat()`
- `LISTBOX GET ARRAYS`, `OBJECT GET/SET COORDINATES`, `LISTBOX Get rows height`

## Best Practices Highlighted
1. Use collection-based list boxes with object-expression columns rather than parallel arrays for file/folder display.
2. Wrap risky operations like folder deletion in `ON ERR CALL` and surface the full error stack to the user.
3. Model navigation history as simple push/pop stacks rather than more complex state tracking.

## Context / Positioning
Published alongside a cluster of 2019 UI-recipe Tech Notes (drag-and-drop, search bars), this note showcases the practical payoff of the object-notation File/Folder command family introduced in the v17 R-release series, reinforcing 4D's move toward object/collection-based UI programming over legacy array-based techniques.

## Historical Commentary
**Status:** Still relevant

The File/Folder object command family (`folder.folders()`, `folder.files()`, `.create()`, `.delete()`) has remained 4D's standard file-system API ever since its introduction and is unchanged in current 4D versions — this note's core technique is fully usable today without modification. Collection-based list boxes are likewise still the recommended, actively-supported list box paradigm. This is one of the more durable "how-to" notes in the catalog: nothing here has been deprecated or replaced.
