# Tech Note 02-27: Taming The Splitter For Printout

- **Asset ID:** 23244
- **Tech Note #:** 02-27
- **Published:** June 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Steve Hartman
- **Page URL:** https://kb.4d.com/assetid=23244
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_25-27_(JUN)/02-27_Taming_The_Splitter.hqx

## Overview

Steve Hartman (4D, Inc. Information Systems, with Kent Wilbur co-authoring the sample database) solves the problem of splitters on an output form snapping back to their default position at print time, by duplicating the form for printing and saving/reapplying splitter positions with GET OBJECT RECT and MOVE OBJECT.

## Key Points

- Standard 4D output-form splitters are implemented as invisible buttons; moving one on screen to widen a field so its full contents are visible has no effect on the printed page, because splitters reset to their designed position for printing.
- The fix: duplicate the output form into a print-only form, visually identical minus the Print button, with each invisible-button splitter replaced by a line object, and label/field objects renamed generically (label1, label2..., field1, field2...) to enable generic loop-based repositioning.
- The Print button's `On Clicked` object method loops `For ($i;1;Size of array(apSplitter))` over pointers to each Splitter object (`Get pointer("Splitter"+String($i))`) and calls `Save_Splitter_Position` for each before invoking `Shell_Print`.
- `Save_Splitter_Position` uses `RESOLVE POINTER` to identify which splitter number was passed, then `GET OBJECT RECT` to capture its left/top/right/bottom into parallel arrays (`aLSplitterLeft`, `aLSplitterRight`, `aLSplitterTop`, `aLSplitterBottom`); this same method is also attached to each splitter's own `On Clicked` event so the arrays update live as the user drags splitters.
- The print form's form method calls `Object_Move` on the `On Header` and `On Printing Detail` events; it loops over the saved splitter array and uses `MOVE OBJECT` to reposition each corresponding `vLine`, `label`, and `field` object relative to the remembered splitter coordinates.
- The label/field naming convention (label1/field1, label2/field2, etc.) is what allows `Object_Move` to reposition all affected objects generically in a single `For` loop, instead of requiring hardcoded per-object move calls.

## Featured Technology

- Splitter (invisible button) objects on output forms
- GET OBJECT RECT / MOVE OBJECT
- On Clicked splitter event capturing
- On Header / On Printing Detail print form events
- Generic label/field naming convention (label1, field1, Splitter1...) for loop-driven repositioning
- Duplicate print-only form replacing splitters with lines

## Historical Commentary

**Status:** Superseded

This note solves a specific, well-known 4D quirk of its era: standard splitters (implemented as invisible buttons) reset to their design-time position when a form is printed, even if the user had dragged them to reveal more of a field's contents on screen. The fix — a duplicate print form with lines instead of splitters, a generic label/field naming scheme, and code that captures splitter positions via On Clicked and reapplies them via MOVE OBJECT during On Header/On Printing Detail — is a clever, still-conceptually-valid workaround, but it targets classic 4D output forms and PRINT SELECTION/PRINT RECORD-based reporting. Modern 4D report generation (list forms, form objects with saved user layouts, and 4D Write Pro-based reporting) has largely eliminated the need for this splitter-position workaround, making the specific technique here superseded by more capable built-in printing/report tools, though the general idea of preserving user-adjusted column widths for printed output remains a relevant UX concern.

References to newer/updated information:
- Modern 4D form/report tooling (list forms with persisted column widths, 4D Write Pro-based reports) largely avoids the splitter-reset-on-print problem this note works around
- Classic output-form-based PRINT SELECTION/PRINT RECORD printing with manual splitter objects is a legacy pattern; current 4D projects more commonly use 4D Write Pro or richer report generation for user-adjustable printed layouts
