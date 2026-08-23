# Tech Note: Quick Reports: Output Types

- **Asset ID:** 29725
- **Tech Note #:** 03-31
- **Published:** July 29, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Hugo Fournier
- **Page URL:** https://kb.4d.com/assetid=29725
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_31-35_(JUL)/03-31_QuickReptOutputTypes.hqx

## Overview

Hugo Fournier (4D Inc. Technical Support Engineer) builds a small cross-platform utility that lists and previews Quick Report files in a folder, using it as a springboard to document all five output formats available from the Quick Report Editor: disk file, 4D View, 2D/3D graph, and HTML (including an XML export variant).

## Key Points

- The `M_Update_List` method populates a report file list via `DOCUMENT LIST`, filtering by the `.4qr` extension on Windows but falling back to `Document type` checks for the `4DQR`/`4DSE` Mac file types when the extension check fails, branching on the `<>Platform` interprocess variable.
- `M_Update_QR_Data` previews a selected report by loading it into an offscreen Quick Report area with `DOCUMENT TO BLOB` + `QR BLOB TO REPORT`, then displays its kind via `QR Get report kind` (List vs. Cross-tab) and its configured output type via `QR GET DESTINATION` (Printer, Text file, 4D View, 4D Chart, or HTML File).
- Handles relative vs. absolute folder paths carefully, prefixing with the `<>MacOS` separator variable on Mac OS for relative paths and tracking an `<>vAbsPath` flag once the user selects a new folder via `Select folder`.
- Disk file (text) output uses a simple tab-tab-return format with a tab between cells and a carriage return ending each row.
- 4D View output places each report cell into its own 4D View spreadsheet cell, applicable to both List and Cross-tab reports; 2D graphs require a List report with category/value columns, while 3D graphs require a Cross-tab report with two categories and one value.
- HTML File output is a tag-driven export mechanism controlled by `QR SET HTML TEMPLATE`; the note demonstrates that substituting an XML-flavored template and renaming the output file's extension to `.xml` produces a file compatible with 4D's own XML import/export format.

## Featured Technology

- Quick Report Editor
- QR BLOB TO REPORT / QR Get report kind / QR GET DESTINATION
- DOCUMENT LIST / Document type
- QR SET HTML TEMPLATE (HTML and XML export)
- 4D View / 4D Chart report output

## Historical Commentary

**Status:** Superseded

This note is a solid, practical survey of the Quick Report Editor's output pipeline circa 2003, including the clever cross-platform file-type-detection trick and the demonstration that the HTML template mechanism could double as an ad hoc XML exporter. 4D's reporting story has moved on considerably since then -- 4D Write Pro and modern list-box/ORDA-based reporting now cover most of what Quick Report addressed, and JSON has replaced ad hoc XML templating as the standard structured export format. The specific output-format survey here is dated, though the general goal of browsing and previewing report files programmatically remains a straightforward, still-usable utility pattern.

**References to newer/updated information:**
- 4D Write Pro and later Quick Report/list-box-based reporting have expanded well beyond the output options available in 2003
- JSON-based data export (JSON Stringify / entity selections) has largely replaced the QR SET HTML TEMPLATE XML-templating trick shown here for producing structured export files
