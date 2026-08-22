# Tech Note 21-09: The Possibilities of Form Macros

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** May 25, 2021 | **Product/Version:** 4D v18 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78712
**Download:** https://kb.4d.com/DLTN/TN/2021/21-09_FormMacro.zip

## Proposition
Form macros, introduced in v18 R5 for Project mode, let developers run custom code straight from a contextual right-click menu in the form editor, with full read/write access to the form's objects, pages, and properties — turning repetitive form-development tasks into one-click actions.

## Key Points
- **Two required artifacts:** a `formMacros.json` file (in the project's Sources folder) declaring macro names, their backing class, and optional custom parameters, plus a **4D Class** implementing `onInvoke`.
- **`onInvoke($editor)` is mandatory:** receives an object with the form's current page, objects, selection, pages/views, and properties; returns a `$result` object with any modifications to apply.
- **Optional Class constructor** retrieves custom parameters passed from the macro's `formMacros.json` definition; optional `onErr` handles execution errors.
- **Duplicate-name resolution:** macros with the same name collapse to one entry, favoring names with uppercase letters, or the later-declared macro otherwise.
- **Host + component coexistence:** a host database can access both its own and its components' form macros simultaneously, labeled by source.
- **Visibility gate:** a macro won't appear in the menu unless its class exists and defines `onInvoke`.
- **Rich demo set:** adding a button object, changing/removing object properties (font color, icon) via generic reusable classes, opening `formMacros.json`/CSS files, checking 4D version, validating image paths, and scanning for obsolete commands during Project mode conversion.

## Featured Technology
- Form Macros (`formMacros.json`)
- 4D Classes (`onInvoke`, `onErr`, Class constructor)
- Project mode form editor object model (`$editor.editor.currentPage`, `.currentSelection`)
- `OB Copy`

## Best Practices Highlighted
1. Build generic, parameterized macro classes (e.g. a single `ChangeObjectProperty` class taking property name/value) rather than one class per specific edit.
2. Use form macros to automate conversion-checking tasks (obsolete commands, unsupported plugin areas, broken image paths) when migrating older forms.
3. Always define `onInvoke` before expecting a macro to appear in the editor's macro list.

## Context / Positioning
Form macros are explicitly a Project-mode-only capability, reflecting 4D's strategy of making the newer text-based project format (introduced around v17-18) more attractive by giving it developer-productivity tools unavailable in classic/binary Design mode — reinforcing the broader industry-wide push toward Project mode adoption happening at the same time.

## Historical Commentary
**Status:** Still relevant

Form macros remain a current 4D feature with no successor or deprecation — they continue to exist in later versions exactly as described here, since Project mode (their prerequisite) has itself become the default, dominant project format rather than being replaced. The technique of building reusable macro classes for form/object automation and conversion checking remains directly applicable today; a developer adopting form macros now would follow essentially the same `formMacros.json` + class + `onInvoke` pattern shown in this 2021 note.
