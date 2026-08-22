# Tech Note 23-05: Create Documentation for 4D Methods, Forms, and Classes

**Author:** Ricki Barragan, Technical Services Engineer, 4D Inc.
**Published:** March 27, 2023 | **Product/Version:** 4D v19 R7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79154
**Download:** https://kb.4d.com/DLTN/TN/2023/23-05_DocumentWithMarkdown.zip

## Proposition
Documentation is often skipped in software projects, but it materially improves maintainability, collaboration, and — critically for compiled components whose internals are hidden — usability. 4D v19 introduces built-in, Markdown-based documentation creation directly from the Explorer window, extended to classes in v19R7.

## Key Points
- **Documentable elements:** project/database/trigger methods, project and table form methods, forms, and (since v19R7) classes.
- **One-click creation:** the Explorer window's Documentation tab shows a "Create" button that generates and opens a `.md` file in the developer's default Markdown editor, pre-filled with an HTML-comment summary placeholder and a ```4d fenced code-block template.
- **File naming and lifecycle sync:** each `.md` file is named after its element and stored in the project's root-level "Documentation" folder; renaming/deleting the element renames/deletes its documentation file automatically.
- **Shared docs for forms:** a project form and its form method (and likewise a table form and its method) share a single documentation file.
- **Editing:** right-click an element and choose "Edit Documentation" to open (or create, if missing) its Markdown file.
- **Supported Markdown syntax:** headings, bold/italic/strikethrough, fenced ```4d code blocks, tables, and links render officially in the Explorer preview.
- **Unofficial-but-working syntax:** underline (`<ins>`), indentation (`&nbsp;`), centered/colored text via inline HTML/CSS, and special Unicode symbols also display despite not being formally documented.
- **Code-editor tooltip:** the first line's HTML-comment summary also appears as a hover tooltip directly in the method code editor.
- **Component documentation:** the Documentation folder is automatically included when building an application, giving developers integrating a compiled component their only window into its intended usage since the method internals are inaccessible.

## Featured Technology
- **4D Explorer documentation panel** — the UI surface for creating, previewing, and editing element documentation.
- **Markdown (.md) files** — plain-text documentation format stored per element, fully version-control friendly.
- **Documentation folder** — root-level project folder holding all generated `.md` files, auto-copied into built applications.
- **Class documentation** — v19R7 extension of the feature to cover class-level documentation in the Explorer.

## Best Practices Highlighted
1. Document components thoroughly since their compiled internals are inaccessible — Markdown docs become the only reference for consumers.
2. Use the HTML-comment summary line deliberately, since it doubles as the code-editor hover tooltip.
3. Rely on officially supported Markdown syntax (headings, code blocks, tables, links) for consistent rendering across environments, treating unofficial HTML/CSS tricks as best-effort only.

## Context / Positioning
Landing alongside 4D v19's continued expansion of project-mode tooling (following classes, Git-friendliness, and component support), this note reflects 4D's push to bring modern software-engineering hygiene — inline, version-controllable documentation — natively into the IDE, reducing reliance on external wikis or documentation generators.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
