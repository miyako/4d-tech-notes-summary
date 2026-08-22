# Tech Note 09-19: Automatic Drop of External Files into 4D

**Author:** Joe Resuello, Tech Marketing Engineer, 4D Inc.
**Published:** May 14, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75757
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_18-21_(MAY)/09-19_DragDrop4D.zip

## Proposition
This note demonstrates 4D v11 SQL's new Automatic Drag/Automatic Drop object properties, which let external files (pictures, PDFs, HTML, QuickTime, rich/plain text) be dropped directly onto Picture Variables, Web Areas, and Text Variables with zero custom code required.

## Key Points
- **Automatic Drag/Drop vs. classic Draggable/Droppable:** the older properties require code in On Begin Drag Over/On Drag Over/On Drop; the new properties handle insertion automatically, only triggering On Data Change/On After Edit.
- **Picture Variable:** accepts dropped image files directly; a dropped multi-page PDF is imported but only its first page is captured.
- **Web Area** (new object type in v11 SQL): supports dropping pictures, PDFs (fully, unlike Picture Variable), rich text, plain text, text selections, HTML files, and QuickTime movies.
- **Text Variable:** accepts dropped text selections.
- Demo database includes a three-tab form (Picture Variable, Web Area, Text Variable) exercising each supported drop scenario.

## Featured Technology
- Automatic Drag / Automatic Drop properties (4D v11 SQL)
- 4D Web Area (drag-and-drop target for pictures, PDFs, HTML, QuickTime, rich/plain text)
- Picture Variable and Text Variable drag-and-drop targets
- On Data Change / On After Edit form events

## Best Practices Highlighted
1. Prefer a Web Area over a Picture Variable when full-fidelity multi-page PDF drops are required.
2. Enable Automatic Drag/Drop for zero-code file ingestion, reserving the classic Draggable/Droppable events for cases needing custom drop logic.
3. Test drop behavior per target object type and file format, since results (e.g., PDF page handling) vary meaningfully between object types.

## Context / Positioning
Published to showcase a then-new, low-code convenience feature in 4D v11 SQL, this note gave developers a practical reference for which file types drop cleanly into which form objects, saving trial-and-error during interface design.

## Historical Commentary
**Status:** Partially Superseded

This note explored 4D v11 SQL's then-new Automatic Drag/Automatic Drop properties, which let external files be dropped directly onto Picture Variables, Web Areas, and Text Variables with no custom code. The core drag-and-drop properties and events described are still present and functional in current 4D versions.

However, the classic Web Area showcased here has since been complemented by newer, Chromium-based web area implementations with materially different rendering/drop behavior, and QuickTime itself was discontinued by Apple years ago, making the QuickTime-specific drop behavior described obsolete.
