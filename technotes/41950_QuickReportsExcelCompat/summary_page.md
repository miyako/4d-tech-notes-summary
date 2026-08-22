# Tech Note 06-08: Making Quick Reports Compatible with Excel

**Author:** Yvan Ayaay, Technical Support Engineer, 4D Inc.
**Published:** February 24, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41950
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_05-08_(FEB)/06-08_Quick_Reports_Excel.zip

## Overview
This note shows how to repurpose 4D's Quick Report HTML-file output and its templating tags to generate XML output that Microsoft Excel 2003 can open directly, either as a custom XML file or as Excel's own native XML Spreadsheet (SpreadsheetML) format.

## Key Points
- Quick Report can target several destinations (printer, text file, HTML file, 4D View, 4D Chart); when set to HTML file, a tag-based template constructs the output.
- Documents the four core template tags: `#4DQRheader`, `#4DQRrow`, `#4DQRcol` (optionally with a column index), and `#4DQRdata`.
- Since these tags can emit any markup, they can be redirected via `QR SET HTML TEMPLATE` to build XML instead of HTML.
- Shows a "basic" custom XML output (one element per table/row) importable into Excel 2003 as generic XML.
- Shows a full XML Spreadsheet (SpreadsheetML) output that Excel opens natively without any import dialog.
- The SpreadsheetML-generating method dynamically detects each Quick Report column's field type to emit correct `ss:Type` (Number/String) attributes, and concatenates a static metadata header (from a template file) with a dynamically built body.
- A companion sample database demonstrates both output modes via "Generate XML file" and "Generate XML SpreadSheet" buttons.

## Featured Technology
- 4D Quick Report (`QR SET DESTINATION`, `QR SET HTML TEMPLATE`, `QR GET INFO COLUMN`, etc.)
- HTML/XML templating tags (`#4DQRheader`, `#4DQRrow`, `#4DQRcol`, `#4DQRdata`)
- Custom XML and Excel's XML Spreadsheet (SpreadsheetML) formats
- Microsoft Excel 2003 XML import/open behavior

## Historical Context
Published in February 2006 for 4D 2004, this note predates any native Excel export commands in 4D and targets Excel 2003's XML capabilities specifically, a full year before Excel 2007 introduced the now-ubiquitous .xlsx (Office Open XML) format that superseded SpreadsheetML for native Excel files. It also predates 4D's own SQL engine (v11, 2007). The Quick Report tool and its tag-based HTML/XML templating still exist conceptually in 4D's reporting story, but the specific XML Spreadsheet schema and Excel-2003-era workaround are now a historical curiosity rather than a practical technique, since both 4D and Excel have since gained more direct spreadsheet interchange options.

## Status
**Obsolete** — targets a superseded Excel XML format and predates modern spreadsheet export approaches in 4D.
