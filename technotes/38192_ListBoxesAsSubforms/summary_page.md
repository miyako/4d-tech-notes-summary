# Tech Note: Using ListBoxes as Subforms

- **Asset ID:** 38192
- **Tech Note #:** 05-26
- **Published:** July 25, 2005
- **Product / Version:** 4D 2004.7r3
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=38192
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_25-27_(JUL)/05-26_ListBoxes_as_Subforms.hqx

## Overview

Kent Wilbur (Manager of Information Systems, 4D, Inc.) explores when 4D 2004's newly introduced List Box object can substitute for a classic Subform, focusing on the performance and transaction benefits of arrays over per-record Client/Server communication, using an [Invoices]/[LineItems] input form as the working example.

## Key Points

- Subforms send each related record to the server individually as the user navigates rows, requiring transactions (with their temporary-storage overhead) to support Cancel; List Boxes transfer all data as arrays once, with no further network traffic until the final save.
- Because List Box data isn't committed until `ARRAY TO SELECTION` runs, the example eliminates the need for transactions entirely in the input form — a Cancel simply discards the in-memory arrays.
- The List Box object (`fLineItems`) is configured with 6 columns (5 displayed), column headers shown, single selection, both grid lines on, vertical-only growth, alternating background color, movable rows, sortable columns, and only the On After Sort and On Row Moved events enabled.
- Column arrays can each have distinct object methods; only `atProductCode` and `aiQty` are Enterable with an On Data Change object method, while `aLInvoiceNo` is the sole invisible column.
- The Input form's On Load event populates the arrays via `SELECTION TO ARRAY` sorted by a saved Position field; On Validate strips rows with empty product code or zero quantity, recomputes Position, and writes changes back with `ARRAY TO SELECTION`; On Unload frees the arrays and returns an unused invoice sequence number on cancel.
- Built-in List Box features requiring no code include alternating row colors, resizable rows without splitters, and drag-and-drop reordering of both rows and columns — capabilities not available on a traditional subform.
- The note cautions that per-cell formatting (colors, fonts) based on a cell's value is not supported by List Boxes of this era — only whole-row formatting via a parallel "Font Colors" array is possible.

## Featured Technology

- 4D 2004 List Box object (array-backed)
- ARRAY TO SELECTION / SELECTION TO ARRAY
- On After Sort / On Row Moved / On Data Change events
- Drag-and-drop row and column reordering
- Transaction-free record editing via arrays
- Classic Subform comparison

## Historical Commentary

**Status:** Still relevant

This note captures a genuinely important architectural tradeoff from the early List Box era: trading the Subform's ease of setup for the List Box's reduced Client/Server chatter and transaction-free editing. That comparison remains broadly valid today — List Box (now with object/entity-selection/collection data sources rather than only classic arrays) has become the default choice for most tabular editing in current 4D applications, and classic Subforms are used far less often. The specific array-based mechanics shown here (SELECTION TO ARRAY / ARRAY TO SELECTION) still work, though ORDA-based List Box data sources now offer an alternative that avoids manual array management altogether.

**References to newer/updated information:**
- 4D's List Box object has been substantially enhanced since 2005, including object/entity-selection/collection-backed data sources (rather than only arrays), which this note predates
- Modern 4D UI guidance generally favors List Box over classic Subforms/output forms for most tabular data display and editing needs, exactly as this note anticipated
