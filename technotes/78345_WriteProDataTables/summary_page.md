# Tech Note 19-19: Adding Data Tables in a Write Pro Document

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** October 28, 2019 | **Product/Version:** 4D Write Pro v17 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78345
**Download:** https://kb.4d.com/DLTN/TN/2019/19-19_AddDataTablesIn4DWP.zip

## Proposition
4D Write Pro can embed data tables generated from a database selection directly into a word-processing document, useful for invoices, reports, and technical documentation. This note demonstrates the object-range-based commands needed to insert, populate, and format such tables programmatically.

## Key Points
- **Object ranges are central:** all Write Pro manipulation works through range objects obtained via commands like `WP Selection range`.
- **`WP Insert Table`** creates a table at a target range with an insertion mode (`wk append`, `wk prepend`, `wk replace`) and optional column/row counts, returning a table range object.
- **`WP Table append row`** adds rows dynamically but requires a fixed number of parameters unless called via `EXECUTE STATEMENT` (which breaks compilation).
- **`WP Table get cells`** + **`WP SET TEXT`** is the recommended way to programmatically fill specific cells, more suited to automation than UI-based `ST INSERT`.
- **Data population pattern:** entity selections are looped (row = record, column = field) to populate an inserted table.
- **`WP SET ATTRIBUTES`** applies border, font/text, image, and table-level formatting; because Write Pro is HTML-based, cell-level styles override row/table styles, so column-wide styling must target cell/column ranges directly.
- **Known limitation (as of v17R6):** removing or restructuring table columns/rows isn't straightforward; adding rows/columns is easy, removal generally isn't.
- Five progressive demos show header toggling, insertion-mode choice, border customization, and a full filter/reorder dialog for exporting selected fields.

## Featured Technology
- 4D Write Pro object ranges and range commands (`WP Selection range`, `WP Cell`, `WP Table get cells`)
- `WP Insert Table`, `WP Table append row`, `WP SET ATTRIBUTES`, `WP SET TEXT`
- ORDA entity selections as the data source

## Best Practices Highlighted
1. Use `WP SET TEXT` rather than UI-driven text insertion for automated/batch cell population.
2. Plan the table's column/row structure up front since restructuring after creation is difficult.
3. Apply visual attributes at the cell (not column) level due to HTML child-element style precedence.

## Context / Positioning
Published shortly after 4D Write Pro's table commands were introduced in the R-release cycle, this note reflects 4D's mid-2019 push to round out 4D Write Pro as a full replacement for the deprecated 4D Write plugin, while also showcasing the broader shift toward object-notation-based development (ORDA entity selections feeding directly into UI/document generation) that characterized the v17 R-release series.

## Historical Commentary
**Status:** Partially superseded

The fundamental API described here — object ranges, `WP Insert Table`, `WP Table append row`, `WP SET ATTRIBUTES` — remains the current way to manipulate 4D Write Pro tables and is still valid in modern 4D versions. However, the specific limitation flagged in the note (inability to remove/insert table columns and rows without recreating the whole table) has been addressed in more recent 4D releases, which added dedicated table row/column manipulation commands, so a developer today has more flexibility than what's described here. 4D Write Pro itself remains 4D's actively maintained document-processing engine, having fully displaced the legacy 4D Write plugin referenced in the introduction.
