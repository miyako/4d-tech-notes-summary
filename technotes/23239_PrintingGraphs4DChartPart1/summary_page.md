# Tech Note 02-22: Printing Graphs from 4D Chart, Part I

- **Asset ID:** 23239
- **Tech Note #:** 02-22
- **Published:** May 31, 2002
- **Product / Version:** 4D Chart 6.8
- **Platform:** Mac & Win
- **Author:** Tim Tonooka
- **Page URL:** https://kb.4d.com/assetid=23239
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_20-24_(MAY)/02-22_Printing_Graphs_Part_I.hqx

## Overview

Tim Tonooka (4D Solution Partner) surveys all nine techniques available for printing 4D Chart graphs — the 4D Chart menu bar's Print/Print Merge, CT DO COMMAND codes 1009/1010, and PRINT FORM/RECORD/SELECTION/LABEL — and provides a decision framework for matching each real-world printing scenario to the best-suited technique, ahead of Part II's coding details.

## Key Points

- Recaps 4D Chart's history: originally a $295 add-on requiring per-4D-Client expansion packs, it became a free, built-in part of core 4D starting in v6, while the legacy GRAPH/GRAPH TABLE/GRAPH SETTINGS commands remain supported with 4D Chart now acting as the rendering engine behind them.
- Splits printing techniques along two axes: printing from a 4D Chart document itself (Print/Print Merge/CT DO COMMAND — only chart objects appear on the page, but a large multi-page document can print in full, by rows or columns) versus printing from a 4D form (PRINT FORM/RECORD/SELECTION/LABEL — can combine the chart area with other form objects, but is limited to the chart area's on-form dimensions).
- Also splits techniques by whether they require an actual current record: record-based (Print Merge, the User Environment's Print command, PRINT RECORD, PRINT SELECTION, PRINT LABEL) versus non-record-based (the 4D Chart Print command / CT DO COMMAND 1009, PRINT FORM) — the latter avoiding the need to set up a "dummy" table and temporary unsaved record.
- Print Merge (menu command or `CT DO COMMAND` code 1010) requires a 4D Chart field-reference placeholder object; it prints one identical document per record in the current selection, with only field-reference values (not the graph data) varying per copy.
- `PRINT FORM` cannot print 4D Chart plug-in areas or subforms — a blank space prints instead — so any chart must first be converted into a picture variable placed on the form; by contrast `PRINT RECORD`/`PRINT SELECTION` can directly print a 4D Chart plug-in area on a form.
- Form event firing order differs by command: `PRINT RECORD`/`PRINT SELECTION` runs `On Printing Header`, `On Load`, `On Printing Detail`, `On Printing Break`, `On Printing Footer` in the form method (with only `On Load` and `On Printing Detail` firing in object methods), while `PRINT LABEL` fires only `On Load`.
- Closes with scenario-specific recommendations: a graph only in memory (use the 4D Chart Print command, or copy to a picture and print via `PRINT FORM`), a graph in a plug-in window (print via its own File menu, or intercept Print with `CT ON MENU` as detailed in TN 02-10), and graphs stored in record picture fields (use `PRINT RECORD`/`PRINT SELECTION`).

## Featured Technology

- 4D Chart Print / Print Merge (CT DO COMMAND 1009/1010)
- PRINT FORM vs PRINT RECORD vs PRINT SELECTION vs PRINT LABEL
- Record-based vs non-record-based printing techniques
- 4D Chart field references for Print Merge
- 4D Chart document-oriented model (picture field / disk document storage)
- Form event ordering during PRINT RECORD/PRINT SELECTION/PRINT LABEL

## Historical Commentary

**Status:** Obsolete

This is Part I of Tim Tonooka's two-part series methodically cataloguing every technique available in 4D v6.x for printing a 4D Chart graph — distinguishing document-based printing (4D Chart's own Print/Print Merge commands) from form-based printing (PRINT FORM/RECORD/SELECTION/LABEL), and record-based printing from non-record-based printing — then matching each real-world scenario (graph only in memory, graph in a plug-in window, graph stored in a record, etc.) to its best-suited technique. It's a clear, well-organized decision framework for a genuinely confusing area of classic 4D printing with nine overlapping possible commands. Since 4D Chart itself has been superseded by newer charting technology in current 4D, and 4D's overall reporting/printing stack has evolved considerably (4D Write Pro, newer form technology), this note's specific command inventory and decision tree are now of historical interest for legacy database maintenance rather than current development guidance.

References to newer/updated information:
- 4D Chart (and the printing commands built around it, like CT DO COMMAND for Print/Print Merge) has been superseded by newer charting/graphics technology in current 4D
- 4D's modern reporting stack (4D Write Pro, newer report/list form technology) offers different and generally more capable printing workflows than the PRINT FORM/RECORD/SELECTION/LABEL decision tree described here
