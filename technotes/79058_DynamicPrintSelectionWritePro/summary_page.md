# Tech Note 22-21: Dynamic Print Selection Using 4D Write Pro (Revised Jan 5th, 2023)

**Author:** Add Komoncharoensiri, Director of Technical Services Engineer, 4D Inc.
**Published:** November 30, 2022 | **Product/Version:** 4D v19 R7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79058
**Download:** https://kb.4d.com/DLTN/TN/2022/22-21_dynamicPrintSelection4DWP_3.zip

## Proposition
Classic list-form print selection reports are form-heavy and costly to modify. This note shows how to reproduce header/detail/break/footer report layouts using 4D Write Pro tables bound to ORDA entity selections, and ships a small declarative API (apiWPPrintSelection/apiWPSetHeader/apiWPSetFooter) that builds such reports from query and field-definition objects alone.

## Key Points
- **WP Insert table + WP SET ATTRIBUTES(wk datasource; Formula(...))** binds a table's data rows directly to an ORDA query, e.g. `Formula(ds.People.query("firstname = :1"; "a@"))`.
- **This.item is the repeat keyword**: formulas referencing This.item.<attribute> repeat the row once per entity in the bound selection when WP COMPUTE FORMULAS runs.
- **WP Table get cells + WP INSERT FORMULA** binds individual cells to ORDA attributes (including related attributes like worksFor.name), decoupling report layout from manual field placement.
- **Headers/footers use WP New header/WP New footer plus formula expressions**, e.g. This.pageNumber for page numbers, evaluated per page.
- **apiWPPrintSelection(WPPointer; QueryDefinition; FieldDefinition)** is a single declarative call that builds one or more tables, applies ORDA query/orderBy constraints, and supports up to 2 break levels with sum/count aggregation per group.
- **FieldDefinition objects control both data binding and appearance** — columnTitle, fieldTitle, columnWidth, break, sum, count, fontColor/fontSize, titleBGColor, etc.
- **WP PRINT sends to a physical printer; WP EXPORT DOCUMENT generates a PDF**, covering both interactive and headless/automated report generation.

## Featured Technology
- 4D Write Pro (WP commands)
- WP Insert table / WP Table get cells / WP SET ATTRIBUTES
- WP INSERT FORMULA / Formula() objects
- ORDA entity selections (This.item)
- WP New header / WP New footer
- WP PRINT / WP EXPORT DOCUMENT
- Custom apiWPPrintSelection / apiWPSetHeader / apiWPSetFooter API

## Best Practices Highlighted
1. Toggle wk visible references view property while building a document to visually confirm formula bindings before calling WP COMPUTE FORMULAS to materialize real data.
2. Prefer the declarative apiWPPrintSelection API over hand-building tables/cells for straightforward reports, reserving manual WP command sequences for custom layouts it doesn't cover.

## Context / Positioning
Published under 4D Write Pro v19 R7 (late 2022), this note continues 4D's push to have 4D Write Pro — the HTML/CSS-based successor to classic 4D Write — absorb use cases that used to require the older list-form print engine, reinforcing 4D Write Pro plus ORDA entity selections as the modern, data-driven reporting stack.

## Historical Commentary
**Status:** current

4D Write Pro has fully superseded classic 4D Write as 4D's document engine, and this note's approach — binding WP tables to ORDA entity selections via Formula()/This.item — remains the recommended, current pattern for data-driven reporting years later. The custom apiWPPrintSelection/apiWPSetHeader/apiWPSetFooter methods are a tech-note-provided convenience layer rather than official 4D commands, so they should be treated as a reusable sample rather than a guaranteed-to-be-maintained product API, but the underlying WP command set they wrap is stable and still fully supported.
