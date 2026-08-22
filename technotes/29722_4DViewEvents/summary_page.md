# Tech Note 03-34: 4D View Events

**Author:** Not specified in source document
**Published:** July 29, 2003 | **Product/Version:** 4D View v | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=29722
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_31-35_(JUL)/03-34_4D_View_Events.exe

## Overview
A Tech Note demonstrating how 4D View's event model works, covering all supported area events and the PV ON EVENT / PV ON COMMAND commands used to hook into them for interactive spreadsheet-like behavior.

## Key Points
- Covers the full set of 4D View area events: cell changes, click/double-click, drag/drop, focus, keyboard, scroll, and selection change.
- Introduces PV ON EVENT for handling 4D View area events.
- Introduces PV ON COMMAND for handling command-style interactions with a 4D View area.

## Featured Technology
- 4D View
- PV ON EVENT
- PV ON COMMAND

## Historical Context
4D View was the standard spreadsheet-area component for classic 4D applications needing spreadsheet-like interactivity beyond plain list/output forms; only the short teaser text for this note goes beyond the command list shown here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Obsolete

4D View and its PV-prefixed event commands are tied to a discontinued companion product, making this note's specific API obsolete for current 4D development; the general concept of an event-driven, interactive grid area remains fully relevant and is now realized through list box form object events or web-based grid/table components in modern 4D applications.
