# Tech Note 02-25: Printing Graphs from 4D Chart, Part II

- **Asset ID:** 23242
- **Tech Note #:** 02-25
- **Published:** June 30, 2002
- **Product / Version:** 4D Chart 6.8
- **Platform:** Mac & Win
- **Author:** Tim Tonooka
- **Page URL:** https://kb.4d.com/assetid=23242
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_25-27_(JUN)/02-25_Printing_Graphs_Part_II.hqx

## Overview

Tim Tonooka (4D Solution Partner) delivers Part II of a two-part series on printing 4D Chart graphs, providing concrete code for four different graph-resizing/printing strategies via the "ChartPrint" example database, plus techniques for intercepting 4D Chart's own Print menu command.

## Key Points

- "Print As Is" prints via `CT DO COMMAND (areaID; 1009)` at the exact on-screen pixel dimensions (1 pixel = 1 point when printed), which can split a large graph across pages or leave a small graph wasting page space.
- "Print Resized Graph" copies the document with `CT AREA TO AREA` into an offscreen area, locates the graph object via `CT Get ID`, and uses `CT MOVE`/`CT SIZE` to resize the actual graph object to a target 520x700-point area before printing — noting the graph is redrawn with different gridline density as it resizes.
- "Print Picture" converts the whole document into a picture variable with `CT Area to picture` for placement on a form and printing via `PRINT FORM`, preserving the same level of graph detail as on screen when stretched (since it's draw-type, not bitmap).
- "Print Resized Picture" (the `CHT_Print` project method) computes width/height ratios against a 540x720-point max page area, uses `CT Place picture` to paste the picture into an offscreen area, and `CT SIZE` to proportionally resize it before printing — avoiding the "stretched" look from non-proportional resizing.
- 4D Chart's own Print command is intercepted via `CT ON MENU` installing `CHT_MenuHandler`, which checks for menu command code 1009 (Print) and offers a `CONFIRM` dialog for Custom (`CHT_Print`) vs. Standard (`CT DO COMMAND`) printing.
- Additional patterns cover building an entire graph in an offscreen area and printing it directly (`DEM_PrintOffscreen`), printing via a picture variable with `PRINT FORM` (`DEM_PrintFormReport`), and per-record graph printing with `PRINT SELECTION`/`PRINT RECORD` — including printing from a temporary unsaved "dummy" record via `CREATE RECORD` when there's no real current record.
- Notes that `PRINT FORM` cannot print 4D Chart plug-in areas directly (they print as blank space), so any 4D Chart content used with `PRINT FORM` must first be converted to a picture variable.

## Featured Technology

- CT AREA TO AREA / CT Area to picture (copying a 4D Chart document for print resizing)
- CT New offscreen area / CT DELETE OFFSCREEN AREA
- CT SIZE / CT MOVE / CT GET BOUNDARY (resizing graphs or pictures to fit a page)
- CT ON MENU custom Print interception (CHT_MenuHandler / CHT_Print)
- PRINT FORM, PRINT RECORD, PRINT SELECTION with 4D Chart documents
- CT Place picture (pasting a picture back into an offscreen chart area)

## Historical Commentary

**Status:** Obsolete

Part II of Tim Tonooka's two-part series delivers the concrete code for the trickiest 4D Chart printing problem: making a graph print at the right size on a page instead of being split across pages or wasting space. It shows three concrete resizing strategies (resize the actual graph object in an offscreen area, convert to a picture and stretch it, or convert to a proportionally-resized picture) plus how to drive printing from PRINT FORM/PRINT RECORD/PRINT SELECTION and how to intercept 4D Chart's own Print menu command via CT ON MENU. This is detailed, still largely accurate 4D Chart mechanics for anyone maintaining a legacy 4D Chart-based reporting system, but 4D Chart itself has been superseded by more modern charting/reporting technology in current 4D, so the specific CT_ command techniques here are now mostly of value only for legacy-database maintenance rather than new development.

References to newer/updated information:
- 4D Chart (and its CT_ command family used throughout this note) has been superseded by modern chart/graphics components in current 4D versions
- Current 4D reporting more commonly relies on 4D Write Pro or newer chart area technology rather than resizing offscreen 4D Chart pictures for print
