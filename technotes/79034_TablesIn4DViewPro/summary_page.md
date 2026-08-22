# Tech Note 22-20: Working with Tables in 4D View Pro (R2: November 11th, 2022)

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** October 25, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79034
**Download:** https://kb.4d.com/DLTN/TN/2022/22-20_TablesIn4DVP_2.zip

## Proposition
4D View Pro's spreadsheet component can turn 4D data into organized tables and aggregating pivot tables, usable interactively through its Toolbar/Ribbon UI or built entirely by code. This note documents both paths, including the newer VP CREATE TABLE command and the pivot-table configuration object model.

## Key Points
- **4D View Pro is powered by SpreadJS (GrapeCity)** embedded in a Web Area-derived component; developers can mix native VP commands with SpreadJS JS calls for advanced behavior.
- **On VP Ready signals when the area has finished loading** — code executed before this event fires on a newly opened area will error out.
- **VP Run offscreen area enables headless spreadsheet processing** without a visible form, useful for server-side report generation.
- **VP CREATE TABLE (new in 4D v19 R6)** creates a spreadsheet table procedurally at a given range, complementing the Toolbar/Ribbon interactive table creation.
- **Pivot tables are built from a configuration object** (name, sourceData, row, column, layout, theme, options) plus per-field objects (sourceName, displayName, area, subtotal, index).
- **Both tables and pivot tables can be created interactively or procedurally**, letting developers choose end-user self-service reporting vs. fully automated report generation.
- **A bundled sample database** demonstrates table creation and a working pivot table built from the same source data.

## Featured Technology
- 4D View Pro (SpreadJS-based spreadsheet component)
- VP CREATE TABLE
- VP Run offscreen area
- On VP Ready event
- Pivot tables (SpreadJS pivot API)
- Ribbon / Toolbar UI modes
- VP SET DATA CONTEXT

## Best Practices Highlighted
1. Always gate code that manipulates a View Pro area behind the On VP Ready event to avoid errors from acting on a not-yet-initialized spreadsheet engine.
2. Use VP Run offscreen area for batch/report-generation scenarios where a visible form isn't needed.

## Context / Positioning
Published under 4D v19 R (October 2022, revised R2 in November 2022), this note documents 4D View Pro's maturing table and pivot-table capabilities as the SpreadJS-based component has progressively replaced the classic 4D View area as 4D's primary spreadsheet/reporting surface.

## Historical Commentary
**Status:** current

4D View Pro (built on SpreadJS) remains 4D's current spreadsheet component and classic 4D View is legacy technology; the table and pivot-table APIs documented here (VP CREATE TABLE, pivot configuration objects, VP Run offscreen area) are still part of the supported 4D language today. 4D View Pro has continued to receive new VP commands and SpreadJS version upgrades in subsequent releases, so while the fundamentals in this note remain valid, developers should check the current 4D documentation for any newer, more direct pivot-table commands added since 19 R.
