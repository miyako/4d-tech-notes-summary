# Tech Note: Drag and Drop Data between 4D and Excel

- **Asset ID:** 49867
- **Tech Note #:** 08-19
- **Published:** May 21, 2008
- **Product / Version:** 4D v11 SQL
- **Platform:** Mac & Win
- **Author:** Atanas Atanassov
- **Page:** https://kb.4d.com/assetid=49867
- **Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_17-20_(MAY)/08-19_Drag_Drop_Excel.zip

## Overview

This Tech Note showcases a significant 4D v11 SQL feature: native, built-in support for Drag and Drop and direct pasteboard (clipboard) access, which eliminated the previous reliance on third-party plug-ins to implement drag-and-drop interactions between a 4D Listbox and external Windows/Mac applications like Microsoft Excel.

## Key Points

- Two implementation styles are demonstrated:
  - **Automatic drag-and-drop**, enabled entirely by setting form object properties on a Listbox, requiring no code.
  - **Manual drag-and-drop**, implemented via 4D database methods that respond to the `On Drop` and `On Drag Over` form events, giving full programmatic control over what happens when data is dragged into or out of the Listbox.
- Data exchanged with Excel is parsed and generated as tab-delimited (column separator) and carriage-return-delimited (row separator) plain text, matching the clipboard format Excel itself uses for cell ranges.
- The sample supports bidirectional transfer: dragging data from a 4D Listbox into an open Excel sheet, and dragging Excel-selected cells into a 4D Listbox.
- Demonstrates direct interaction with the OS pasteboard/clipboard object from 4D database methods, rather than relying on plug-in wrappers.

## Featured Technology

- Drag and Drop mechanism in 4D v11 SQL
- Pasteboard (clipboard) management
- Automatic Drag and Drop form object properties
- Listbox control interactions
- `On Drop` and `On Drag Over` form events
- Tab and carriage-return text parsing
- Cross-application data exchange

## Historical Commentary

**Status:** Still relevant

This note demonstrates a major feature addition in 4D v11 SQL: native Drag and Drop support and pasteboard access, eliminating the need for plug-ins to implement drag-and-drop between 4D Listboxes and external applications like Microsoft Excel. The implementation shows both automatic drag-and-drop (via form object properties) and manual drag-and-drop (via database methods and the pasteboard), allowing bidirectional data transfer between 4D and Excel with tab-delimited and carriage-return-formatted text. This capability remains functional in modern 4D but is now considered foundational rather than noteworthy; however, the pattern of pasteboard-based cross-application data exchange is still relevant for desktop integration scenarios.

**References to newer/updated information:**
- Drag and Drop and pasteboard APIs remain in modern 4D with largely the same syntax and behavior.
- Excel integration patterns have evolved to include modern file I/O (native XLSX handling) and web APIs rather than clipboard-only approaches.
- The `On Drop` and `On Drag Over` event system is still the primary mechanism for implementing advanced drag-and-drop in 4D forms today.
