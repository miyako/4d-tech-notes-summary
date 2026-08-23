# Tech Note: Making the most of BEST OBJECT SIZE

- **Asset ID:** 23268
- **Tech Note #:** 03-11
- **Published:** March 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Kent D. Wilbur
- **Page URL:** https://kb.4d.com/assetid=23268
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_11-15_(MAR)/03-11_Best_Object_Size.hqx

## Overview

Kent D. Wilbur explores 4D 2003's newly introduced BEST OBJECT SIZE command, which returns the optimal pixel width and height a form object needs based on its current data, the active OS, and its font/size/style -- accounting for hyphenation and carriage returns for text objects -- while noting it reports the object's ideal content size only, not accounting for frame decorations like sunken/raised borders or scroll bars, and that the optional fixedWidth parameter is effectively required for usable results with text fields. Building on his earlier Tech Note #02-37, he demonstrates three practical applications: dynamically resizing an input-form window around a variable-length Synopsis text field (also repositioning labels and constraining to available screen space), and two print-report techniques -- a side-by-side layout that measures the tallest of several fields per record and shifts the print marker accordingly, and a full 'catalog' style report with proportionally-scaled pictures and individually-resized Actors/Synopsis fields -- both leveraging 4D 2003's new ability to get/set the print marker inside `On Printing Detail` and to `CANCEL` mid-print so a record can be pushed cleanly to the next page.

## Key Points

- Documents the command syntax `BEST OBJECT SIZE({*;} object; bestWidth; bestHeight {;fixedWidth})`, noting it works on Alpha, Numeric, Boolean, Date, Time, Static text, and button objects (returning current size like `GET OBJECT RECT` for non-text objects), but is most useful for text objects where hyphenation/line-wrapping affects the ideal height.
- Warns that BEST OBJECT SIZE returns only the object's own ideal size, not accounting for presentation-frame extras (sunken/raised appearance, scroll bars, button borders) which must be added on top manually, and that omitting the optional `fixedWidth` parameter for text typically yields unusably wide results.
- Input-form resizing example: computes the Synopsis field's ideal height via `BEST OBJECT SIZE([Products]Synopsis;$LWidth;$LSynopsisIdealHeight;$LSynopsisFixedWidth)`, adds padding, repositions the SynopsisLabel via `MOVE OBJECT`, clamps the result to the maximum available screen height, and resizes the field/window accordingly.
- Side-by-side print report: loops over an array of field pointers (Title, Actors, Synopsis) with `GET OBJECT RECT`/`BEST OBJECT SIZE` inside the `On Printing Detail` event, tracks the largest resize needed among them, calls `SET PRINT MARKER(Form Detail;...)` to shift where the next form section starts, and uses the new ability to `CANCEL` inside `On Printing Detail` (which cleanly aborts printing just that record without terminating the calling PRINT FORM loop) combined with `PAGE BREAK` in the calling method to push an oversized record to a fresh page.
- Catalog-style report: proportionally scales a picture object based on `PICTURE PROPERTIES` and its frame's aspect ratio, then independently resizes and repositions the Actors and Synopsis fields (and their labels) based on `BEST OBJECT SIZE`, again using `SET PRINT MARKER`/`CANCEL` to keep each product's block dimensions correct and to page-break records that don't fit.
- Notes the driving project method saves/restores the current selection and sort order via `COPY NAMED SELECTION`/`ORDER BY`/`USE NAMED SELECTION`, checks `OK=0` after each `Print form` call to detect a mid-print CANCEL, and reprints the header plus the cancelled record on the next page via an explicit `PAGE BREAK`.

## Featured Technology

- BEST OBJECT SIZE command (4D 2003)
- GET OBJECT RECT / MOVE OBJECT
- GET PRINTABLE AREA / Get printed height / SET PRINT MARKER / Get print marker
- On Printing Detail form event
- CANCEL during PRINT FORM (mid-print page-break control)
- Dynamic side-by-side and catalog-style report layout

## Historical Commentary

**Status:** still_relevant

Kent D. Wilbur (Manager of Information Systems, 4D, Inc.) demonstrates 4D 2003's then-new BEST OBJECT SIZE command, which computes the optimal pixel width/height a text (or other) object needs for its current content, font, and OS, and shows how to combine it with GET OBJECT RECT/MOVE OBJECT to dynamically resize input forms around a variable-length Synopsis field, and with the newly-CANCEL-able On Printing Detail event and SET/Get print marker to build side-by-side and full catalog-style reports whose row heights adapt per record. The BEST OBJECT SIZE command has remained part of 4D's language in all subsequent versions, so the technique for computing optimal object sizing is still directly usable; while 4D's print architecture and form engine have continued to evolve since 2003 (and 4D Write Pro / newer list box and form object models offer additional layout options), the core BEST OBJECT SIZE-driven resizing technique described here remains applicable to current 4D form and print development.

References to newer/updated information:
- BEST OBJECT SIZE has remained part of 4D's language in every version since its 2003 introduction and continues to work as described
- 4D's form and print architecture has evolved considerably since 2003 (e.g., 4D Write Pro and modern list box objects), offering additional layout mechanisms alongside the BEST OBJECT SIZE-based technique shown here
