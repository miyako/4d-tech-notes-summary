# Tech Note 09-28: Quick Report Wizard - Part I

**Author:** Luis Pineiros, Technical Services Team Member, 4D Inc.
**Published:** July 16, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75840
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_27-30_(JUL)/09-28_Quick_Report_Wizard.zip

## Proposition
This note (Part I of two) shows how to build a custom, guided Wizard dialog that recreates and controls 4D's built-in Quick Report environment, using the Report Plug-in Area and its QR command set, so developers can present users with a simplified, tailored report-building experience for List Reports.

## Key Points
- **Report Plug-in Area:** a built-in (not external) plug-in similar to Web Area or 4D Chart, used inside a custom `DIALOG` to host the Quick Report canvas.
- **40+ QR commands** let developers programmatically drive every aspect of a Quick Report — table/kind selection, column insertion, break-level totals, formatting, styling, borders, column widths, and headers/footers.
- **Step-by-step List Report wizard:** field selection via drag-and-drop (detected with `DRAG AND DROP PROPERTIES`/`QR Get drop column`), break-level calculation tags (`#S`, `#N`, `#X`, `#A`, `#C`), break actions (page breaks/spacing), cell formats/styles/borders, column widths, and page header/footer.
- **Two report types:** List Reports (detail rows with break levels) and Cross-Tab Reports (two-dimensional summaries) — Cross-Tab is previewed here and covered fully in Part II.
- Supports relating to "Many" tables, with 4D automatically detecting the deepest related table for the report.

## Featured Technology
- 4D Quick Report plug-in / Report Plug-in Area (List and Cross-Tab reports)
- QR SET REPORT KIND / QR SET TABLE / QR INSERT COLUMN / QR GET INFO COLUMN (Quick Report commands)
- Drag and drop (DRAG AND DROP PROPERTIES, QR Get drop column)
- Custom Quick Report Wizard dialog (interface/UX layer)

## Best Practices Highlighted
1. Build a virtual structure to hide tables/fields you don't want users choosing from in an ad hoc report.
2. Apply consistent cell formats (predefined or custom # 0 * ^ patterns) to improve legibility rather than leaving raw values unformatted.
3. Use a guided wizard to reduce the intimidation factor of a from-scratch report builder for less technical end users.

## Context / Positioning
Published as a two-part deep dive into a long-standing 4D feature (Quick Reports), this note targeted developers wanting to expose ad hoc reporting to end users without the complexity — or inconsistent branding — of 4D's stock Quick Report environment.

## Historical Commentary
**Status:** Partially Superseded

This note walked through recreating the built-in Quick Report interface as a guided Wizard using 4D v11 SQL's Report Plug-in Area and its 40+ QR commands. The classic Quick Report engine and QR command set are still present and functional in current 4D versions, so the described commands remain usable as documented.

However, 4D has since introduced 4D Write Pro and 4D View Pro as far more capable, modern reporting and document-generation engines, and most new report-building projects today would lean on those rather than the legacy Quick Report plug-in area described in this note.
