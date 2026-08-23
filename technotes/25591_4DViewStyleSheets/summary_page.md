# Tech Note: 4D View Style sheets

- **Asset ID:** 25591
- **Tech Note #:** 02-50
- **Published:** October 31, 2002
- **Product / Version:** 4D View 6.8
- **Platform:** Mac & Win
- **Author:** Cha Yang
- **Page URL:** https://kb.4d.com/assetid=25591
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_46-50_(OCT)/02-50_4D_View_Style_Sheets.hqx

## Overview

Cha Yang explains 4D View style sheets -- reusable font/color/alignment formatting definitions applied to cells within a 4D View area -- covering both the interactive Style Sheets menu workflow and the procedural equivalent using `PV Add style` (which returns a style-sheet reference number) and `PV SET STYLE PROPERTY(area; style; property; value)` to set individual properties like bold, size, italic, underline, font, alignment, and background/text colors. A dedicated `PV_GetFont` helper method is shown resolving a font name to a font ID: it checks the local system's installed fonts via `FONT LIST`, checks whether the font already exists in the 4D View area via `PV GET FONT LIST`, and calls `PV Add font` to register it in the area if needed. The note then covers the two ways a style sheet can be persisted -- saved with an external document (loadable at any time, replacing the current 4D View area) or saved as part of the 4D data itself in a BLOB field -- and walks through a sample database that stores a library of style-sheet property/value pairs in `[StyleSheets]`/`[StyleSheets_User]` tables so users can create and apply named style sheets to any 4D View area globally.

## Key Points

- Distinguishes 4D View's three built-in permanent style-sheet types (Row/Column headers, Cells, Headers and footers) from user-created style sheets, and shows creating/applying one interactively via the Style Sheets menu under the Style drop-down.
- Shows procedural style-sheet creation: `Ref_ID:=PV Add style(PV_Area1; "My_Style")` followed by a series of `PV SET STYLE PROPERTY(PV_Area1;Ref_ID; property; value)` calls to reproduce a manually-created style (bold, size 12, italic, underline, centered alignment, yellow background color 65535, blue text color 16711680).
- Provides a `PV_GetFont` method that resolves a font name to a usable font ID for the area: verifies the font exists on the local system via `FONT LIST`, checks if it's already registered in the 4D View area via `PV GET FONT LIST`, and calls `PV Add font` to register it if not found -- warning that `FONT LIST` results vary machine to machine so fonts should be validated before loading/saving a style sheet.
- Explains 4D View Templates -- a single document per 4D View area used as a starting point for new records (e.g., standard report/invoice formats) that also carries any style sheets defined within it.
- Contrasts the two persistence models for style sheets: saved with an external document (loadable/reusable across records, replacing the current area on load) versus saved inline with the 4D View area's BLOB field (available only to that specific record).
- Describes the sample database's global style-sheet library: `[StyleSheets]` stores named style sheets by ID, `[StyleSheets_User]` stores each style's property/value pairs, and a method reads these via `SELECTION TO ARRAY`, checks whether the named style already exists in the target area via `PV GET STYLE LIST`, and creates/updates it with `PV Add style`/`PV SET STYLE PROPERTY` only for properties whose value differs from the target.

## Featured Technology

- 4D View style sheets (Row/Column headers, Cells, Headers/footers)
- PV Add style / PV SET STYLE PROPERTY
- PV Get style property / PV GET STYLE LIST
- PV Add font / PV GET FONT LIST / FONT LIST
- 4D View external documents and templates
- Storing style-sheet preferences in 4D tables

## Historical Commentary

**Status:** obsolete

Cha Yang (4D, Inc. Technical Support) shows both the interactive and procedural ways to create and apply 4D View style sheets -- font, color, alignment, bold/underline properties -- via `PV Add style` and `PV SET STYLE PROPERTY`, including a helper method that resolves or registers fonts by name with `PV GET FONT LIST`/`PV Add font`, and a sample database that stores reusable style-sheet preferences in two 4D tables so they can be applied to any 4D View area at a global level. 4D View was discontinued as a standalone product, making every PV-prefixed command in this note obsolete for current development; the underlying UX idea of saving and reapplying user formatting preferences is still sound design, but it is now realized through entirely different mechanisms in modern 4D forms or web-based UI.

References to newer/updated information:
- 4D View has been discontinued as a standalone product, so the PV Add style / PV SET STYLE PROPERTY / PV GET FONT LIST commands described in this note no longer apply to current 4D development
- The underlying idea of saving and reapplying reusable formatting preferences is now handled through current 4D form objects or web-based UI components rather than 4D View style sheets
