# Tech Note 09-10: 4D Gantt Chart Component

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** March 11, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75207
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_09-12_(MAR)/09-10_4D_Gantt_Chart.zip

## Proposition
Demonstrates building an interactive, mouse-editable Gantt chart for project management using the newly introduced 4D SVG Component's low-level drawing commands, packaged as a reusable component with a setup Wizard.

## Key Points
- **Grid construction:** draws a day-scaled grid with vertical lines and month labels computed from a project date range.
- **Sub-project rendering:** for each sub-project, draws a labeled row with diamond "polygon" markers for planned/actual start and end dates, connected by gradient-filled duration bars.
- **Mouse-driven editing:** clicking a start/end marker then a grid line deletes and redraws that segment at the new date, updating both in-memory arrays and the on-screen SVG.
- **XML-based chart persistence:** table/field bindings and date boundaries for each saved chart are stored in an XML file keyed by chart ID, enabling later reload.
- **Six-step Wizard:** guides users through naming a chart, selecting a table, and binding main-project/sub-project name and date fields.
- **Load dialog:** lets users load, delete, or create Gantt charts from previously saved definitions.
- Explicitly scoped as an illustration of 4D SVG Component capability, not a full commercial project-management tool.

## Featured Technology
- 4D SVG Component (120 commands) introduced in 4D v11 SQL Release 3
- Interactive SVG Gantt chart built from SVG_New_rect/line/polygon/text and gradients
- SVG_Export_to_picture and DOM XML manipulation of the SVG structure
- Gantt Chart Wizard driven by field mapping to a 4D table

## Best Practices Highlighted
1. Keep the number of sub-projects around 12–15 so a printed Gantt chart fits legibly on one page.
2. Store the object ID of each SVG element so click events can be parsed back into type/number/position for interactive editing.
3. Persist chart configuration (table/field bindings, date boundaries) in an external XML file rather than hardcoding it, to support multiple saved charts.

## Context / Positioning
Written to showcase the newly bundled 4D SVG Component (v11 SQL R3) by applying it to a concrete, recognizable business use case — Gantt-style project tracking — without requiring developers to know SVG or XML themselves.

## Historical Commentary
**Status:** Partially Superseded

This note's approach — hand-driving dozens of individual SVG drawing commands and parsing element IDs to implement interactivity — reflects an era before 4D had richer built-in charting/reporting tools.

Today, 4D View Pro (introduced ~v17-18) provides native spreadsheet and charting capability, including timeline-style visualizations, without manual SVG coding, and 4D's picture/vector handling has otherwise modernized. The specific 4D SVG Component and its binary-component packaging are also tied to the pre-Project-Mode component architecture (superseded by Project mode, 4D v17+, 2018). The conceptual approach to Gantt charts remains instructive, but a developer building this today would very likely reach for 4D View Pro instead.
