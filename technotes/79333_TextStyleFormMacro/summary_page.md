# Tech Note 23-20: Text Style Form Macro

**Author:** Shayanna Gatchalian, Technical Services Engineer, 4D Inc.
**Published:** November 28, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79333
**Download:** https://kb.4d.com/DLTN/TN/2023/23-20_TextStyleFormMacro.zip

## Proposition
4D's Form Editor Properties List shows fonts only as plain text names in a dropdown, forcing developers to click through each option one by one to see how it actually looks — a slow, awkward workflow when styling text-heavy forms. This note provides a self-contained form macro component that adds a proper live font preview and one-click style application/export directly inside the form editor.

## Key Points
- **Root problem:** The native Font property dropdown lists only font names; the actual typeface isn't visible until applied to a form element, and arrow-key navigation doesn't preview selections either.
- **Live-preview fonts list box:** The macro's modal dialog renders every available font in its own actual typeface inside a list box, updating a sample-text preview immediately as the developer scrolls with arrow keys.
- **Context-aware behavior by selection:** With 0 elements selected only JSON export is available; with 1 element selected its current style loads and Apply is enabled; with multiple elements selected, defaults are applied and the resulting style is pushed to all selected elements at once.
- **Project-mode requirement:** Because form macros rely on 4D classes, the target database must be exported to project mode (File > Export > Structure to project) before the component can be installed — binary databases have no workaround.
- **Simple installation:** Drop the `TextStyleFormMacro.4dbase` component into the database's Components folder; the macro then appears under the form canvas's right-click Macros menu.
- **Four-part dialog UI:** Sample text preview (with dark-background toggle), fonts list box, font style options (size, color, bold/italic/underline), and application options (Apply / Copy as JSON).
- **JSON export for reuse:** "Copy as JSON" places a style object (fontFamily, fontSize, stroke, fontWeight, fontStyle, textDecoration) on the clipboard for use in `.4DForm` files, CSS stylesheets, or 4D code via `Get text from pasteboard`.
- **Undo-friendly:** Because it's a standard form macro, applied changes can be reverted with the form editor's normal undo function.

## Featured Technology
- **4D Form Editor Macros:** The extensibility mechanism used to inject the custom dialog into the design-time environment.
- **4D Classes:** Power the macro's logic (e.g., `openTextStyleDialog`) and require project-mode databases.
- **Project mode / Export Structure to project:** Prerequisite conversion step for databases still in binary/classic structure format.
- **JSON serialization:** Encodes the generated text style for portability into form definitions, CSS, or code.
- **Get text from pasteboard:** Native command for retrieving the exported JSON style string from the clipboard in 4D code.

## Best Practices Highlighted
1. Verify cross-platform font availability (Mac vs. Windows font sets differ) before finalizing a text style meant for production deployment.
2. Convert legacy binary databases to project mode deliberately, since class-based tooling like form macros has no binary-mode equivalent.
3. Prefer exporting reusable style definitions as JSON (for `.4DForm`/CSS reuse) over hard-coding repeated style values across multiple forms.

## Context / Positioning
This note exemplifies 4D's continued investment in the Form Editor macro extensibility framework and the class-based, project-mode tooling ecosystem, offering developers a practical example of building design-time productivity tools rather than only runtime application features — consistent with 4D's broader push toward project mode as the modern development format.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
