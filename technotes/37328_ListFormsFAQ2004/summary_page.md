# Tech Note 05-19: FAQ - List Forms in Version 2004

**Author:** 4D Technical Support
**Published:** May 20, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37328
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_17-20_(MAY)/05-19_List_Forms_in_2004.pdf

## Overview
This FAQ Tech Note explains 4D 2004's harmonization of the three previously different ways of displaying record lists (Output form in User Mode, MODIFY/DISPLAY SELECTION-driven output forms, and subforms) into a single, consistent underlying behavior, and documents all of the resulting new commands, properties, and events.

## Key Points
- Introduces precise terminology (included form, form "displayed as a list", highlighted line) for discussing the unified list-form model.
- Documents how upgraded-database subform properties (Enterable, Selectable, Non-modifiable, etc.) map to 2004's new Focusable / Enterable-in-list / Selection Mode / Double-click properties.
- The current record is no longer auto-loaded on window redraw in Single selection mode — developers must call the new LOAD RECORD command, typically on the On Load event.
- Three new selection modes (Single, Multiple, None) are settable via MODIFY SELECTION/DISPLAY SELECTION or subform properties.
- Blank clickable area below the last list record is removed (to match OS GUI conventions); workarounds use buttons/menus/shortcuts tied to Add Subrecord, CREATE RECORD, or ADD RECORD.
- The old blinking-focus triangle is gone, replaced by native OS focus indication (or simulated via On getting focus/On losing focus).
- New form events: On Load Record (detects entry-mode record loads) and On Selection Change (detects user highlighting); On Display Detail now fires even for empty lines.
- New commands: EDIT ITEM, GET HIGHLIGHTED RECORDS, HIGHLIGHT RECORDS for programmatic record highlight management under Multiple selection mode.

## Featured Technology
- 4D 2004 unified list/output form architecture (Output forms, Subforms, User mode)
- MODIFY SELECTION / DISPLAY SELECTION commands
- LOAD RECORD command
- Selection modes: Single / Multiple / None
- On Load Record / On Selection Change / On Display Detail form events
- GET HIGHLIGHTED RECORDS / HIGHLIGHT RECORDS commands

## Historical Context
**Status:** Still relevant

The commands, properties, and events this FAQ documents (MODIFY SELECTION, DISPLAY SELECTION, LOAD RECORD, the three selection modes, On Load Record, On Selection Change, GET HIGHLIGHTED RECORDS/HIGHLIGHT RECORDS) remain part of the current 4D classic language and continue to function the same way in both Design Mode and Project Mode databases today, making this a still directly usable reference for anyone maintaining classic subform/list-form code. That said, for new development 4D's List Box object — introduced around this same era and dramatically expanded since (object/entity selection/collection data sources, richer column types) — has become the dominant tool for tabular UI, so developers today reach for these classic list-form/subform mechanisms less often than in 2005, even though the underlying behavior this FAQ explains has not been removed.
