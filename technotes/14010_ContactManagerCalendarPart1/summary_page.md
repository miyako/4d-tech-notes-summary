# Tech Note: Contact Manager, Behind the code, Part I

- **Asset ID:** 14010
- **Tech Note #:** 01-25
- **Published:** June 4, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Hugo Fournier
- **Page URL:** https://kb.4d.com/assetid=14010
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_21-25_(MAY)/01-25_Contact_Manager_EDB_1.hqx

## Overview

Hugo Fournier (4D, Inc. Technical Support) reviews the forms and code behind the Contact Manager example database's Calendar interface, covering how the calendar's date-box grid is initialized, laid out, and displayed. This is Part I of a two-part series; Part II (a separate Tech Note) covers how user actions (selecting, dragging, editing events) are handled.

## Key Points

- User-level feature overview: a button bar (Add/Delete Event, Go to Today, Go to Date, Previous/Next Month/Year, Print Calendar) sits above a grid of up to 42 date boxes; double-clicking a box or event opens one of four Event Detail dialog variants — Special Day, Appointment, Banner, or Picture — all backed by a single `[Calendar]` table distinguished by an Event Type field, so retyping an event requires no data conversion.
- Startup sequence: the `On Startup` database method calls `Calendar_Startup`, which calls `Calendar_Setup` (detects mm/dd/yy vs. dd/mm/yy format, loads the month-name array, sets interprocess date variables and `<>Cal_SelectedObjectPtr` to Nil) and `Menu_Calendar`/`Shell_DoProcess` (launches the calendar in a new process via the standard 4D sample-database shell).
- `Calendar_Dialog` opens the modal window: `Open form window([Calendar];"Calendar";Plain window;Modal dialog box;Horizontally Centered)` followed by `DIALOG([Calendar];"Calendar")`, after which execution becomes fully event-driven.
- On the `On Load` event: `Calendar_GetCoordinates` captures reference-object positions (margins, banner height, etc.) so the form adapts automatically to layout edits without hard-coded values; `Calendar_SetupMonth` computes `<>Cal_FirstBox`/`<>Cal_LastBox` (accounting for months needing 5 vs. 6 rows of boxes) and the dates for the first/last displayed box; `Calendar_SetNumbers` then loops through three ranges — tail of previous month, current month, head of next month — assigning day numbers into `<>Cal_Num1`–`<>Cal_Num42` via `Get pointer`.
- `Calendar_DeselectObject` (also run on load) clears any prior selection by moving `SelectRect@`/`DragRect@` objects offscreen via `MOVE OBJECT`, and disables the delete-event button since nothing is selected yet.
- The final layout step — positioning date boxes (`Calendar_PlaceBoxes`, using nested `For` loops based on current window size) and redrawing existing events — is deliberately tied to the form's `On Resize` event rather than only `On Load`, ensuring the grid recalculates whenever the user resizes the calendar window.

## Featured Technology

- Calendar_Startup / Calendar_Setup / Calendar_Dialog method chain
- Open form window / DIALOG for a modal calendar window
- On Load / On Resize form event-driven layout
- Calendar_SetupMonth / Calendar_SetNumbers date-box calculation
- Calendar_PlaceBoxes nested-loop object positioning
- [Calendar] table event types (Special Day, Appointment, Banner, Picture)

## Historical Commentary

**Status:** Historical interest only

This note is a detailed code walkthrough of one specific sample application's hand-built calendar layout engine — computing date-box ranges, placing 42 named objects via nested loops, and tying layout recalculation to the On Resize event. The general goal (a resizable calendar grid) remains common, but the specific implementation technique — dozens of individually named date-box and label objects manipulated via pointers — has been superseded in practice by List Box-based calendars, dedicated calendar plug-ins, or web/JS calendar widgets, making this note now primarily a historical illustration of early-2000s 4D form programming style.

**References to newer/updated information:**
- 4D has since introduced richer native list box and form object capabilities that make hand-built calendar-grid interfaces like this one largely unnecessary
- The specific Contact Manager sample database referenced is no longer part of 4D's current example/download library
- The classic Design Mode form-object placement and On Load/On Resize event techniques shown still function in current 4D versions
