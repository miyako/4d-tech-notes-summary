# Tech Note: Using MOVE OBJECT During Printing

- **Asset ID:** 11991
- **Tech Note #:** 00-51
- **Published:** November 1, 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=11991
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_51-55_(NOV)/00-51_MOVE_OBJECT_Printing.hqx

## Overview

Jean-Yves Fock-Hoon (4D, Inc. Quality Assurance Manager) documents a 4D v6.7 enhancement enabling MOVE OBJECT and GET OBJECT RECT to run during PRINT SELECTION, PRINT FORM, and PRINT RECORD, demonstrated through a family-tree database that dynamically rearranges printed fields per record.

## Key Points

- MOVE OBJECT and GET OBJECT RECT now work during printing when triggered by PRINT SELECTION, PRINT FORM, or PRINT RECORD (they do not work with PRINT LABEL); they accept the same relative/absolute coordinate parameters used in display mode and can also resize objects while printing.
- Absolute vs. relative coordinates are controlled with the `*` parameter; if coordinates are absolute, GET OBJECT RECT must be used to re-read an object's current position so the next move computes correctly relative to it.
- The example [People]/[Children] family-tree database's Print Selection report sorts by an internally computed `ID_Line` printing order and generation `Level_Family`, then uses MOVE OBJECT in the On Printing Detail event (relative coordinates) to indent each name by family level and to move a spouse-name variable into place only when the current person is a married male — otherwise pushing it out of the print body past the footer marker.
- The Print Record demo modifies field values (appending " (modified)") from an On Timer event on an Input form, then calls PRINT RECORD to print the current, unsaved in-memory values rather than the values on disk, with MOVE OBJECT using absolute coordinates in the On Detail event to reorder first/last name order based on gender.
- The Print Form demo builds a complete columnar report from scratch: a `Setup_Report` method computes column widths per field type, then a loop over PRINT FORM invokes per-section methods (`FF_PrintHeader1`, `FF_PrintBlankLine`, `FF_PrintHeader2`, `FF_Print_Body`, `FF_Print_Footer`) that use MOVE OBJECT with absolute coordinates to draw borders, column dividers, and text at precisely computed pixel positions.
- The note concludes that, combined with 4D structure-access commands like GET RELATION PROPERTIES, developers now have the tools needed to build their own dynamic "quick report" style layouts.

## Featured Technology

- MOVE OBJECT command during printing
- GET OBJECT RECT command during printing
- PRINT SELECTION command
- PRINT RECORD command
- PRINT FORM command with dynamic report layout
- On Printing Detail / On Header / On Printing Footer form events

## Historical Commentary

**Status:** Still relevant

This note documents a 4D v6.7 enhancement letting MOVE OBJECT and GET OBJECT RECT run during PRINT SELECTION, PRINT FORM, and PRINT RECORD, and demonstrates it with a family-tree database that dynamically repositions name, spouse, birth-date, and gender fields per record to build an indented genealogical report and a hand-built columnar report. Both commands remain part of the current 4D language and this general object-repositioning technique for print layouts is still valid today, though 4D Write Pro and other modern reporting tools now offer a considerably higher-level alternative for the kind of dynamic, per-record report layout this note builds by hand.

**References to newer/updated information:**
- MOVE OBJECT and GET OBJECT RECT remain part of the current 4D language for programmatic form/print layout control
- 4D Write Pro and other modern reporting tools now provide a higher-level way to build dynamic reports that once required manually computing and moving object coordinates as shown here
