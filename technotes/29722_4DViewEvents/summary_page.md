# Tech Note: 4D View Events

- **Asset ID:** 29722
- **Tech Note #:** 03-34
- **Published:** July 29, 2003
- **Product / Version:** 4D View
- **Platform:** Mac & Win
- **Author:** Gou Yang
- **Page URL:** https://kb.4d.com/assetid=29722
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_31-35_(JUL)/03-34_4D_View_Events.hqx

## Overview

Gou Yang (4D Technical Support) explains how to hook into 4D View grid-area interactions and menu commands programmatically using `PV ON EVENT` and `PV ON COMMAND`, since 4D View areas -- unlike regular form objects -- do not expose events through property-list checkboxes.

## Key Points

- `PV ON EVENT(Area;Event;Method)` attaches a 4D method to one of eleven 4D View-specific events (On Active Cell Changed, On Cell Value Changed, On Clicked, On Double Clicked, On Drag, On Drop, On Getting Focus, On Keyboard, On Losing Focus, On Right Clicked, On Scrolled, On Selection Changed); passing an empty method name clears the handler.
- Clarifies the distinction between On Active Cell Changed (fires whenever the active cell moves, even within an unchanged multi-cell selection) and On Selection Changed (fires only when the selected range itself changes) -- a subtlety the note illustrates with concrete before/after selection diagrams.
- Compiled event methods must declare `$0` (Boolean, whether to suppress the event) and `$1`-`$6` (Longint: area reference, event code, key-modifier code, column, row, and ASCII key code respectively).
- `PV ON COMMAND(Area;Command;Method)` intercepts standard menu commands (demonstrated with `pv cmd file new`, `pv cmd file open`, `pv cmd file save`, and `pv cmd file save as`) and redirects them to custom 4D methods instead of 4D View's default file-based behavior.
- The example's custom New/Open/Save/Save As methods use `PV Area to blob` and `PV BLOB TO AREA` to persist the entire 4D View grid's contents as a BLOB inside a `[zDialogs]` table record, keeping saved documents fully inside the 4D database rather than as external files.
- The custom Save method demonstrates a full save/save-as flow: prompting for a document name with `Request`, querying `[zDialogs]` for an existing record with that name, confirming overwrite, and creating or updating the record accordingly.

## Featured Technology

- PV ON EVENT
- PV ON COMMAND
- 4D View grid area events
- PV Area to blob / PV BLOB TO AREA
- 4D View menu-command overriding

## Historical Commentary

**Status:** Obsolete

4D View was 4D's classic spreadsheet-grid component, and this note gives a clear, practical explanation of its distinctive event model (PV ON EVENT/PV ON COMMAND) at a time when few other resources covered the Active-Cell-vs-Selection-Changed distinction or in-database document storage via PV Area to blob. 4D View itself has since been discontinued, making the specific PV-prefixed API obsolete for current development, but the underlying concept -- an event-driven, interactive grid with programmatic event hooks -- lives on in modern 4D through list box form objects and their own on-event model, or through web-based grid/table components embedded in web areas.

**References to newer/updated information:**
- 4D View has been discontinued; list box form objects (with their own event/method model) are the modern 4D equivalent for interactive grid data
- Web area-embedded JS grid/table components are another modern alternative for spreadsheet-style interactive data display in current 4D applications
