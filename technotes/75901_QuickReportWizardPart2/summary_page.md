# Tech Note 09-35: Quick Report Wizard - Part II

**Author:** Luis Pineiros, Technical Services Team Member, 4D Inc.
**Published:** September 3, 2009 | **Product/Version:** 4D 11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75901
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_31-35_(AUG)/09-35_QuickReportWizardPart2.zip

## Proposition
This Tech Note is the implementation/programming half of a two-part series (following Part I, asset #75840) showing how to build a custom multi-step Quick Report Wizard for 4D v11 SQL using the built-in Report Plug-in and its Quick Report (QR) command set, covering both List Reports and Cross-Tab Reports.

## Key Points
- Two report types are addressed: List Reports (records with break levels for sub-calculations) and Cross-Tab Reports (two-dimensional tables categorized by two data sources).
- The Report Plug-in is built into 4D v11 SQL (like Web Area or 4D Chart), requires no separate install, and cannot be removed; it is displayed via a `DIALOG`-based custom interface using a form object (e.g. `QRBuilder_Obj` / variable `QRBuilder`).
- Over 40 QR commands (e.g. `QR REPORT TO BLOB`) control report generation programmatically, referencing the 4D v11 SQL Language Reference Manual for full command details.
- List Report steps documented: select fields/sort order, define break-level values and actions, set cell formats/styles/borders/column widths, define page header/footer, then generate.
- Cross-Tab Report steps documented: define cell formats, choose computations for data-source cells, total column, and grand-total line, set sort order, format data, style/border/width, header/footer, then generate.
- A "Navigation" section shows a `Wizard_SetFloattingwindows` helper that toggles visibility of floating windows (menu bar, toolbar, font, computation, background, move/hide, contextual menu) based on the current wizard page number via a `Case of` statement.

## Featured Technology
- 4D v11 SQL Quick Report Plug-in / Report Plug-in Area
- Quick Report (QR) commands (40+ commands, e.g. QR REPORT TO BLOB)
- List Reports and Cross-Tab Reports
- Custom multi-page Wizard interface (DIALOG-based)

## Best Practices Highlighted
1. Centralize per-page UI state (which floating windows/toolbars are visible) in a single dispatch method keyed on page number, rather than scattering visibility logic across each page's forms.
2. Reference the built-in Report Plug-in rather than an external plug-in for Quick Report functionality, simplifying deployment (no separate Plugins-folder install).
3. Separate List and Cross-Tab report logic clearly since their computation and formatting steps diverge (e.g. total/grand-total computations only apply to Cross-Tab).

## Context / Positioning
Published as the second half of a two-part series in the v11.4 "SQL" era, this note gave developers the concrete code needed to implement a "Print Center" — letting end users choose from a mix of built-in and self-customized reports — building directly on Part I's interface/UX walkthrough.

## Historical Commentary
**Status:** Partially Superseded

The classic Quick Report Plug-in and its QR command set were 4D's state-of-the-art reporting engine in the v11 SQL era, and the wizard pattern shown here (multi-step dialog driving report generation) was a reasonable way to expose ad hoc reporting to end users at the time.

4D has since layered much more capable reporting tools on top of this foundation — 4D Write Pro and 4D View Pro (roughly v16-v18) offer richer, more maintainable document and spreadsheet-style report generation, and 4D's own Quick Report/Quick Form concept has evolved well beyond the v11 SQL Release 4 baseline this note explicitly aimed to replace. A developer building self-service reporting today would likely reach for 4D Write Pro/View Pro rather than reconstruct this QR-command-based wizard from scratch.
