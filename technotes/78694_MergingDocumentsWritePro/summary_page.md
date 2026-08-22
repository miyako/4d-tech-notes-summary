# Tech Note 21-06: Merging Documents In 4D Write Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 29, 2021 | **Product/Version:** 4D Write Pro v18 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78694
**Download:** https://kb.4d.com/DLTN/TN/2021/21-06_4DWPMerge.zip

## Proposition
4D Write Pro documents are complex, styled objects, not plain text. This note explains the `WP INSERT DOCUMENT` command and the underlying Write Pro range/target model for reliably merging two documents — or template pieces — while preserving styling.

## Key Points
- **`WP INSERT DOCUMENT(target; source; mode)`** inserts the entire body of the source document into a target document or Write Pro range.
- **Three insertion modes:** `wk append`, `wk prepend`, `wk replace`, mirroring standard insert behaviors.
- **Write Pro ranges** (obtained via `WP Selection range`) let the target be any position — a paragraph, header, table cell, or selected text — not just the whole document.
- **Style-conflict handling is automatic:** matching styles are reused, new styles are created, and conflicting same-named styles are copied in with an incrementing suffix (e.g. "Custom1") rather than overwritten.
- **Headers, footers, and backgrounds are never merged** — only the body and its supporting style/tab properties — so these must be handled via separate templates inserted individually.
- **Partial merges** (inserting just a selection) require creating a temporary document scoped to a range via `WP New`, then using that as the source document.
- **Five progressive demos** cover simple append, controllable insertion mode, style-conflict resolution, omitted elements, and partial-selection merging.

## Featured Technology
- `WP INSERT DOCUMENT`
- `WP Selection range` (Write Pro ranges)
- `WP New` (creating scoped temporary documents)

## Best Practices Highlighted
1. Design reusable templates with headers/footers/backgrounds already present, since these elements are never copied by `WP INSERT DOCUMENT`.
2. Use `WP New` with a range to extract just a portion of a document when a full-body merge isn't desired.
3. Be aware of the auto-renaming behavior for conflicting styles to avoid unexpected "Custom1"-style duplicates in generated documents.

## Context / Positioning
This note extends core 4D Write Pro documentation with a specific, advanced use case — procedural document generation from templates — reinforcing 4D Write Pro's role as the modern replacement for classic 4D Write in scenarios like contract/report generation that benefit from reusable, mergeable building blocks.

## Historical Commentary
**Status:** Current

`WP INSERT DOCUMENT` and the Write Pro range/target model remain 4D's current, fully supported mechanism for merging documents — this is core, still-accurate API documentation rather than a technique that has been superseded. 4D Write Pro has continued to add capabilities since 2021, but nothing here has been deprecated; a developer building template-based document generation today would use this exact command and range model.
