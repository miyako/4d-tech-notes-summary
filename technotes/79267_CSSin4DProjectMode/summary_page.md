# Tech Note 23-15: CSS Style Sheets in 4D Project Mode

**Author:** Shayanna Gatchalian, Technical Services Engineer, 4D Inc.
**Published:** August 24, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79267
**Download:** https://kb.4d.com/DLTN/TN/2023/23-15_CSSin4DProjectMode.zip

## Proposition
Manually configuring style properties across many form elements and forms is tedious with 4D's form editor alone, and binary mode's built-in style sheets only cover font/size/style for text. Project mode's external CSS style sheet feature lets developers style forms more comprehensively and consistently using familiar, rule-based CSS syntax.

## Key Points
- **Binary vs. project mode style sheets:** Binary mode style sheets configure only font/size/style per platform; project mode replaces this with external CSS2 files (`styleSheets.css`, `styleSheets_mac.css`, `styleSheets_windows.css`) in the Sources folder that can style most form-element properties.
- **Automatic conversion on export:** Converting a binary database to project mode auto-generates platform-specific CSS files with each prior style sheet turned into a CSS class, wired to each form element's new CSS Class property.
- **Five selector types:** Object type (JSON "type" value), object name ("#id"-style), class (".className", multiple classes per element allowed), the universal "*" selector, and four attribute selectors (`[attribute]`, `[attribute=value]`, `[attribute~=value]`, `[attribute|=value]`).
- **Selector precedence:** When rules clash, more specific selector types (e.g., class) take priority over more general ones (e.g., object type), following a defined priority order.
- **CSS color constants:** Named color strings (e.g., "orchid") can be used directly in place of hex codes or RGB values for any color-type property.
- **prefers-color-scheme media query:** The only media query 4D currently supports, letting a style sheet apply different rules for macOS light vs. dark appearance modes via `@media (prefers-color-scheme: light|dark)`.
- **@import modularization:** Large style sheets can be split into partial CSS files and combined via `@import "path.css";`, with "/" for child-folder paths and "../" for parent-folder paths relative to the Sources folder.
- **"Dynamic" per-form style sheets:** A community workaround (credited to Thomas Maul) attaches an individual CSS file to a specific form via a JSON pointer in the .4DForm file (`"css": {"$ref": "/RESOURCES/theme.json#/css1"}`), referencing a directory JSON file in Resources, with the CSS itself stored in the client/server-writable Logs folder — enabling per-user/per-client theming, at the cost of losing CSS Preview support.
- **Style sheet precedence hierarchy:** From highest to lowest priority: dynamic style sheets, form definition, `!important`-tagged rules, platform-specific default file, then the general styleSheets.css.

## Featured Technology
- **External CSS style sheets (CSS2):** Core mechanism for project-mode form styling.
- **4D Form Editor CSS Preview:** Live preview of style-sheet changes without running the application (for default style sheets only).
- **@media (prefers-color-scheme):** Native support for macOS light/dark mode theming.
- **JSON pointer ($ref) in .4DForm files:** Enables the dynamic per-form stylesheet workaround.
- **Directory JSON file (Resources folder):** Maps named style sheet references to actual CSS file paths for dynamic stylesheets.

## Best Practices Highlighted
1. Modularize large style sheets with `@import` to keep individual CSS files maintainable rather than one monolithic file.
2. Use the `!important` tag sparingly and deliberately when a CSS rule must override a form definition's explicit property value.
3. Reserve the "dynamic" per-form stylesheet technique for cases needing true per-form or per-client theming, understanding it forgoes live CSS Preview support.
4. Consult 4D's properties reference documentation before styling via CSS, since not all form elements or properties are CSS-styleable.

## Context / Positioning
This note reflects 4D's ongoing investment in project mode's file-based, web-standards-aligned architecture, bringing familiar CSS tooling and conventions (selectors, precedence, media queries, imports) into desktop form design. It aligns with the broader industry and 4D trend of improving UI/UX tooling and theming (light/dark mode, per-client branding) as a first-class concern alongside raw functionality.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
