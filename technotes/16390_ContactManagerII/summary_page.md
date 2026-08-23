# Tech Note: Contact Manager II

- **Asset ID:** 16390
- **Tech Note #:** 01-35
- **Published:** July 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Hugo Fournier
- **Page URL:** https://kb.4d.com/assetid=16390
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_31-35_(JUL)/01-35_Contact_Manager_II.hqx

## Overview

Hugo Fournier (4D, Inc. Technical Support Engineer) presents Part II of the Contact Manager calendar code walkthrough, focused on interface behavior: selecting calendar events, dragging/dropping/duplicating them, and creating or editing them via a modal detail dialog. Part I (a separate Tech Note) covered how the calendar's objects were placed and displayed; this note picks up with user interaction.

## Key Points

- Single click selects an event; double-click opens the Detail event dialog (pre-filled for existing events, defaulted for a new date box); drag-and-drop moves an event to a new date, or duplicates it if the Shift/Option key is held during the drop.
- Selection highlighting uses up to six overlay rectangles (`SelectRect1`–`SelectRect6`) since a "banner" event (e.g., spanning several days like a conference) can be drawn across up to six form objects; `Calendar_SelectObject` and `Calendar_DeselectObject` manage moving these rectangles on/offscreen.
- Two parallel arrays, `<>Cal_aVariableNames` and `<>Cal_aRecIDs`, map each displayed form object to its `[Calendar]` record ID, letting `Calendar_LoadAssociatedRecord` find and load the correct record by searching for the object's variable name.
- The `On Drag Over` form event calls `DRAG AND DROP PROPERTIES` and blocks drops onto the event's current date; `On Drop` either calls `DUPLICATE RECORD` + `Sequence number` (Shift/Option-drag) or `READ WRITE`/`LOAD RECORD` (plain drag), updates `[Calendar]Event Date`, and calls `SAVE RECORD` then `Calendar_PlaceEvents` to redraw.
- `Calendar_DisplayRecord` opens the Input form as a modal dialog with `Open form window`/`INPUT FORM`, then dispatches to `ADD RECORD` (new event) or `READ WRITE` + `GOTO RECORD` + `MODIFY RECORD` (existing event), closing with `CLOSE WINDOW` and refreshing the calendar if `OK=1`.
- Banner resizing uses 30 pairs of invisible buttons (`DragBttnL1`–`DragBttnL30`, `DragBttnR1`–`DragBttnR30`) handled by `Calendar_DragObjectMethod`, one pair per potential concurrent banner.

## Featured Technology

- Calendar_TextObjectMethod click/double-click dispatch
- GET OBJECT RECT / MOVE OBJECT for selection-rectangle highlighting
- DRAG AND DROP PROPERTIES / On Drag Over / On Drop form events
- DUPLICATE RECORD for Shift-drag event copies
- Parallel-array record mapping (<>Cal_aVariableNames / <>Cal_aRecIDs)
- Open form window / INPUT FORM / MODIFY RECORD dialog pattern

## Historical Commentary

**Status:** Historical interest only

This note is a detailed code walkthrough of one specific sample application's hand-built calendar interaction model — parallel arrays mapping objects to records, manually drawn selection rectangles, and drag-and-drop event moving via classic Design Mode form events. The general goal (an interactive calendar with click/drag event management) remains common, but the specific implementation technique — dozens of individually named form objects and drag-detection buttons — has been superseded in practice by List Box-based calendars, dedicated calendar plug-ins, or web/JS calendar widgets, making this note now primarily a historical illustration of early-2000s 4D form programming style rather than a current best practice.

**References to newer/updated information:**
- Modern 4D calendar UIs are more commonly built with List Box objects, calendar plug-ins, or web/JS calendar components rather than dozens of individually named form objects
- The classic Design Mode form-object and drag-and-drop event techniques shown still function in current 4D versions
- The Contact Manager sample database referenced is no longer part of 4D's current example/download library
