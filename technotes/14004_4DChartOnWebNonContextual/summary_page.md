# Tech Note: 4D Chart on the Web in Non-Contextual Mode

- **Asset ID:** 14004
- **Tech Note #:** 01-21
- **Published:** June 4, 2001
- **Product / Version:** 4D Chart 6.7
- **Platform:** Mac & Win
- **Author:** Kent D. Wilbur
- **Page URL:** https://kb.4d.com/assetid=14004
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_21-25_(MAY)/01-21_4D_Chart_on_the_Web.hqx

## Overview

Kent D. Wilbur (Manager, Information Systems, 4D, Inc.) revisits Tim Tonooka's 1998 Tech Note (98-13) on serving 4D Chart graphs to the web, updating it for 4D v6.7's new non-contextual web server. The note walks through the 4DChartOnTheWeb example database, covering both display of pre-saved chart pictures and creation of fully interactive charts driven by HTML form input, with particular attention to how non-contextual mode's lack of process state changes the implementation.

## Key Points

- Displaying charts already saved in `[Charts]` records is the simplest case: an `On Web Connection` dispatch calls `Web_Fields`, which does `ALL RECORDS([Charts])` and `SEND HTML FILE("ListCharts.shtml")`; the `.shtml` page loops through records with a `4DLOOP` tag and links to `Web_ShowSavedChart` by record ID, and the picture field is displayed simply by referencing it with a `<!--4DVAR [Charts]MyArea_-->` tag.
- The `On Web Connection` database method manually parses everything after `/4DCGI/` in the URL, splitting on `/` to get a function name and parameters, then dispatches via a `Case of` to project methods (`Web_CreateChart`, `Web_AdvancedChart`, `Web_Fields`, `Web_ShowSavedChart`).
- Building an interactive chart uses 4D Chart's offscreen-area API: `CT New offscreen area`, `CT Chart arrays` to plot categories/series/values, `CT SET DISPLAY` to hide menu bars/tools/scrollbars/rulers, and `CT Area to picture` to capture the result into a picture variable, followed by `CT DELETE OFFSCREEN AREA`.
- Because non-contextual mode has no live process variables to hand off between the request that creates a chart and the request that must serve its image, the note's key trick is to `CREATE RECORD([Charts])` with a `"###Web_CreateChart:..."` marker as a temporary holder for the rendered picture, then have a second request (`HTML_SendChart`) query for that record by ID, convert the picture with `PICTURE TO GIF`, `DELETE RECORD` if the description starts with `"###"`, and `SEND HTML BLOB(...;"image/gif")`.
- Chart parameters (categories/values) are round-tripped through the stateless web tier as flat HTML form variables (`tCategory1`, `tValue1`, etc.) retrieved via `GET WEB FORM VARIABLES`, since HTML forms have no native array concept.
- The bundled "Advanced Interactive 4D Chart Web Demo" extends the same technique to render adjustable 3D charts, reusing Tonooka's original 1998 chart-creation code with only minor changes for non-contextual mode.

## Featured Technology

- 4D Chart plug-in commands (CT Chart arrays, CT Area to picture, CT SET DISPLAY)
- Non-Contextual Mode 4D Web Server
- SEND HTML FILE / .shtml 4DLOOP and 4DVAR tags
- On Web Connection database method routing (4DCGI)
- GET WEB FORM VARIABLES
- Temporary-record BLOB image serving (PICTURE TO GIF, SEND HTML BLOB)

## Historical Commentary

**Status:** Obsolete

Kent Wilbur's note updates Tim Tonooka's 1998 TN 98-13 to show how 4D v6.7's new non-contextual web server model can serve both saved and live-generated 4D Chart graphs, working around the statelessness of non-contextual mode by stashing rendered charts as temporary records and streaming them back out as GIF BLOBs. Both halves of the technique -- the 4D Chart plug-in itself and the manual On Web Connection/4DCGI routing style of web serving -- have been fully retired: 4D Chart was discontinued years ago, and 4D's web server has since moved to WebActions/REST and ORDA-based approaches that don't require hand-parsing the URL or stuffing images into temporary database records.

**References to newer/updated information:**
- The 4D Chart plug-in has been discontinued; current charting needs are met by 4D View Pro or web-based JavaScript charting libraries
- Manual On Web Connection/4DCGI URL routing and .shtml tag parsing have been superseded by 4D's WebActions and modern REST/ORDA-based web service techniques
