# Tech Note: Creating an HTML File with the Report Editor

- **Asset ID:** 33477
- **Tech Note #:** 04-31
- **Published:** August 5, 2004
- **Product / Version:** 4th Dimension 2003.4
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon (QA Manager, 4D, Inc.)
- **Page URL:** https://kb.4d.com/assetid=33477
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_31-35_(JUL)/04-31_HTML_in_Report_Editor.hqx

## Overview

Written by Jean-Yves Fock-Hoon, this note explains the HTML template mechanism behind 4th Dimension 2003's new Quick Report editor, which can export a report to HTML using either 4D's built-in default template or a custom one supplied by the developer. It shows building a basic report programmatically with QR New offscreen area, QR SET REPORT KIND, QR SET DESTINATION (targeting qr HTML file), QR SET REPORT TABLE, QR INSERT COLUMN, and QR RUN, and demonstrates overriding the default template with QR SET HTML TEMPLATE (noting it must be called after QR SET DESTINATION, and that QR GET HTML TEMPLATE should be used first if the default template -- stored as text resource ID 14900 in the 4DQR resource file -- may need to be restored later). The bulk of the note documents the template's special HTML comment-style tags, explaining how <!--#4DQRlHeader/cHeader/rHeader and their footer counterparts wrap the <!--#4DQRData tag to pull left/center/right header and footer text, how <!--#4DQRHeader plus a nested <!--#4DQRCol loop generates column titles generically without knowing the column count in advance, how the analogous <!--#4DQRRow/4DQRCol combination generates data rows, break-level rows, and the grand total row, and how a numbered <!--#4DQRCol;n> variant lets a fixed-column template (useful for generating well-formed XML) target a specific column instead of looping generically.

## Key Points

- QR SET DESTINATION($ID;qr HTML file;$path) targets an HTML file, using 4D's built-in default template unless overridden.
- QR SET HTML TEMPLATE($ID;$HTML_Template) must be called after QR SET DESTINATION or the custom template will not take effect; QR GET HTML TEMPLATE can capture the default template for later restoration since it cannot otherwise be retrieved once replaced.
- 4D's default HTML template is stored as text resource ID 14900 inside the 4DQR resource file in the 4D Extension folder.
- <!--#4DQRlHeader/cHeader/rHeader ... <!--#4DQRData ... <!--/#4DQRlHeader (and analogous footer tags) retrieve the report's left/center/right header and footer text.
- <!--#4DQRHeader wrapping a nested <!--#4DQRCol/<!--#4DQRData loop generically emits column titles regardless of how many columns the report has, without requiring the template author to know the column count in advance.
- <!--#4DQRRow wrapping the same <!--#4DQRCol/<!--#4DQRData pattern generates data rows, break-level rows, and the grand total row using the identical generic looping mechanism.
- A numbered variant, <!--#4DQRCol;n> ... <!--/#4DQRCol;n>, lets a template address one specific column by number instead of looping — useful for producing well-formed, fixed-schema XML output from a report.

## Featured Technology

- Quick Report editor (introduced in 4th Dimension 2003)
- QR SET DESTINATION / QR SET HTML TEMPLATE / QR GET HTML TEMPLATE commands
- Quick Report HTML template tags (4DQRData, 4DQRHeader, 4DQRCol, 4DQRRow, 4DQRlHeader/cHeader/rHeader, 4DQRlFooter/cFooter/rFooter)
- QR New offscreen area / QR SET REPORT KIND / QR INSERT COLUMN / QR RUN

## Historical Commentary

**Status:** Historical Interest Only

This note documents the tag-based HTML templating system behind 4D 2003's original Quick Report editor, which was a useful bridge at the time for generating styled HTML/XML reports and export files without hand-writing HTML from scratch. The Quick Report engine and its QR-prefixed command set and comment-tag templating language shown here are legacy features tied to that specific report editor generation; 4D's reporting and export capabilities have evolved substantially since 2003 (including newer reporting tools and more general JSON/REST-based data export paths), so this exact template-tag mechanism is now mostly of historical interest for anyone still maintaining databases built on the original Quick Report engine.

**References to newer/updated information:**
- 4D's report-generation and data-export tooling has evolved considerably since the 2003 Quick Report editor described here
- Modern 4D applications more commonly generate structured export/report output via JSON and REST-based approaches alongside or instead of the QR-prefixed Quick Report commands
- The QR SET HTML TEMPLATE tag language documented here is specific to the classic Quick Report engine and does not apply to newer 4D reporting mechanisms
