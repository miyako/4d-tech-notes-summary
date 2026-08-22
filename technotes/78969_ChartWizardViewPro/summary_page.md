# Tech Note 22-13: Chart Wizard with 4D View Pro (R2)

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** July 19, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78969
**Download:** https://kb.4d.com/DLTN/TN/2022/22-13_ChartWizard_R2.zip

## Proposition
Beyond 4D View Pro's native commands, its underlying SpreadJS engine's JavaScript Charts API can be driven directly via WA Evaluate JavaScript. This note builds a full chart-creation wizard on top of that approach, exporting the finished chart as a picture usable elsewhere in a 4D application.

## Key Points
- **A 3-page wizard collects chart type, table/field mapping, and styling options** as Form variables before generating any chart.
- **SpreadJS's JS Charts API (sheet.charts.add, chart.title/.axes/.legend/.dataLabels)** is driven by assembling raw JavaScript strings in Form.data.js and executing them via WA Evaluate JavaScript.
- **activeSheet.suspendPaint()/resumePaint() bracket the chart-building JS** to optimize rendering performance during batch updates.
- **VP Export to object / VP IMPORT FROM OBJECT toggles low-level spreadJS UI properties** (scroll bars, headers) to produce a clean chart-only display before export.
- **VP EXPORT DOCUMENT natively produces PDF**, which is macOS-only for direct PDF handling; Windows requires converting to PNG via the third-party Xpdf tool through LAUNCH EXTERNAL PROCESS.
- **The finished chart returns as a picture variable**, letting it be embedded elsewhere in the 4D application UI rather than staying tied to the View Pro area.

## Featured Technology
- 4D View Pro (SpreadJS-based)
- WA Evaluate JavaScript
- SpreadJS Charts API (sheet.charts.add)
- VP Export to object / VP IMPORT FROM OBJECT
- VP EXPORT DOCUMENT
- LAUNCH EXTERNAL PROCESS (Xpdf)

## Best Practices Highlighted
1. Suspend and resume paint around programmatic chart-building JS to avoid unnecessary re-render overhead.
2. Strip UI chrome (scrollbars, headers, frozen panes) from a View Pro area before exporting it as a picture, so the exported image contains only the intended content.

## Context / Positioning
Published under 4D v19 (July 2022, revised as R2), this note shows how 4D View Pro's SpreadJS foundation lets developers go beyond native VP commands into SpreadJS's own richer JavaScript APIs (here, its Charts API) when 4D's own command set doesn't yet expose an equivalent feature directly.

## Historical Commentary
**Status:** partially superseded

4D View Pro/SpreadJS remains the current spreadsheet engine, and driving its JS API via WA Evaluate JavaScript is still a valid, supported escape hatch for advanced features. However, the specific cross-platform export workaround here — relying on the third-party Xpdf executable to convert PDF to PNG on Windows because 4D's PDF handling was macOS-only — is the kind of gap that later 4D releases have targeted for improvement; developers today should check whether current 4D versions offer native PDF/picture export parity across platforms before adopting this specific workaround, as it may no longer be necessary.
