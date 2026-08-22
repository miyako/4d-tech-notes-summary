# Tech Note 19-18: Custom File Drag and Drop Area

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** October 28, 2019 | **Product/Version:** 4D v17 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78344
**Download:** https://kb.4d.com/DLTN/TN/2019/19-18_CustomFileDragAndDropArea.zip

## Proposition
Modern applications benefit from drag-and-drop file collection instead of relying solely on OS file browsers. This note shows how to build such an interface natively in a 4D form using a drop zone, a file displayer list box, and deletion controls.

## Key Points
- **Drop Zone construction:** a transparent variable placed over an invisible highlight rectangle, toggled with `OBJECT SET VISIBLE` on drag-over/mouse-leave/drop events.
- **`Get file from pasteboard`** is looped to pull each dropped file's absolute path into a `Form.filePath` collection.
- **File Displayer** is a collection-based list box placed directly over the drop zone, swapped in once files exist.
- **Current Item Position** tracks which file is selected in the list for follow-on actions.
- **Deletion** uses `.remove()` on the collection; a `SET TIMER`/`On Timer` combo is used to call `LISTBOX SELECT ROW` outside the button method so the highlight updates correctly.
- **Reverting to drop zone:** when the file collection empties, the file displayer and buttons are hidden again to reveal the original drop zone.
- **Extensibility:** the sample exposes collected paths via `$formData_o`, letting developers insert custom file actions (upload, zip, print, convert) into a single handler.

## Featured Technology
- `OBJECT SET VISIBLE`, `Get file from pasteboard`
- Collection-based list boxes and `.push()`/`.remove()`
- `LISTBOX SELECT ROW`, `SET TIMER`/`On Timer`, `OBJECT SET ENABLED`

## Best Practices Highlighted
1. Overlay UI elements (drop zone vs. file displayer) rather than swapping forms, to keep interactions smooth.
2. Use a timer-triggered listbox selection update to avoid update-ordering issues after a button-triggered collection mutation.
3. Centralize custom file-handling logic in one place fed by the collected file paths object.

## Context / Positioning
Released alongside several other 2019 "custom UI component" Tech Notes (custom file explorer, search bar with dropdown), this note reflects 4D's ongoing series of practical UI recipes built on the newer collection/object-notation-based listbox features introduced through the v17 R-releases, giving developers native alternatives to OS-level file pickers without needing plugins.

## Historical Commentary
**Status:** Still relevant

This is a UI recipe note whose techniques — form events, collection-based list boxes, `OBJECT SET VISIBLE`/`OBJECT SET ENABLED`, and collection `.push()`/`.remove()` — remain fully valid in current 4D versions; none of the core commands used have been deprecated. The main thing that has evolved since 2019 is the broader ecosystem (e.g., 4D now also supports similar drag-and-drop patterns in web-based/Qodly interfaces), but for classic native 4D forms this technique is still the standard approach a developer would use today.
