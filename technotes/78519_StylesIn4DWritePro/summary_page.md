# Tech Note 20-14: Applying and Managing Styles in 4D Write Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 27, 2020 | **Product/Version:** 4D Write Pro v18 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78519
**Download:** https://kb.4d.com/DLTN/TN/2020/20-14_4D WriteProStyles.zip

## Proposition
4D Write Pro documents can be styled interactively through its toolbar/contextual menu, but they can also be built and styled entirely in code. This Tech Note explains 4D Write Pro's element/range object model and demonstrates both ways of applying styles — attribute commands and object notation — as well as how to create and reuse named style sheets.

## Key Points
- **Document object model**: headers, footers, bodies, tables, rows, paragraphs, pictures, sections, and subsections are all obtainable/creatable elements (`WP Get header`/`WP New header`, etc.).
- **Ranges**: a more generic target — with `owner`/`start`/`end`/`type` — that can address arbitrary spans of text, even across multiple paragraphs.
- **WP SET/GET ATTRIBUTES**: the primary command pair for applying/reading styles, supporting multiple attribute-value pairs per call and `wk`-prefixed constants (e.g. `wk font bold`) for safer, autocomplete-friendly attribute names.
- **Error handling**: incompatible attribute/target combinations throw a 205 error; invalid attribute values throw a 204 error.
- **Object notation alternative**: attributes can be read/set as direct properties of a range object; bracket notation with `wk` constants is recommended over hardcoded dot-notation names.
- **Style sheets**: document-scoped, uniquely named style bundles created with `WP New style sheet`, in "character" (exact range only) or "paragraph" (whole paragraph) variants.
- **Style sheet application**: styled like a range via `WP SET ATTRIBUTES`, then applied to text using the `wk style sheet` attribute; duplicate names throw a 208 error.
- **Toolbar integration**: created style sheets automatically appear in the 4D Write Pro toolbar's style dropdowns, alongside the default "Normal" paragraph style.

## Featured Technology
- WP SET ATTRIBUTES / WP GET ATTRIBUTES
- 4D Write Pro object-notation range attributes
- WP New style sheet (character vs. paragraph types)
- wk-prefixed style constants (e.g., wk font bold, wk style sheet)
- 4D Write Pro elements and ranges (headers, footers, tables, paragraphs)

## Best Practices Highlighted
1. Use `wk`-prefixed constants rather than raw attribute name strings, for autocomplete support and resilience against future API renames.
2. Batch multiple attribute-value pairs into a single `WP SET/GET ATTRIBUTES` call rather than issuing them one at a time.
3. Choose character vs. paragraph style sheet type deliberately based on whether the intended scope is an exact selection or entire paragraphs.
4. Prefer bracket notation with constants over dot notation with literal property names when using object-notation style access.

## Context / Positioning
Published as 4D Write Pro continued to mature as 4D's flagship, code-first word-processing engine, this note is a core reference for developers building document-generation features (templates, reports, contracts) that require both interactive editing and precise, reusable, procedurally-applied styling — reinforcing 4D Write Pro's positioning as a modern, structured alternative to legacy 4D Write.

## Historical Commentary
**Status:** Current

4D Write Pro's document/element/range/style-sheet model, and the dual attribute-command/object-notation API described here, remain the current and unchanged way to style documents programmatically in 4D — there has been no architectural replacement of this system since publication. This is one of the more durable, evergreen Tech Notes in the batch: it documents core, actively-maintained 4D Write Pro functionality rather than a workaround or transitional technique, so a developer today can follow this note's guidance directly.
