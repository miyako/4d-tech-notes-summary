# Tech Note 96-22: Changing File and Field Orders Using 4D Insider

**Author:** Forrest Swilling
**Published:** May 1, 1996 | **Product/Version:** 4D Insider v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11702
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_22-26_(MAY)/96-22_File-Field_Order.exe

## Overview
This Tech Note describes how to safely reorder fields or files within a 4D database structure during the development phase, using 4D Insider to avoid breaking the logical meaning of existing layouts and procedures. It explicitly does not cover reordering on a deployed database, which instead requires exporting and re-importing data into a new datafile.

## Key Points
- **Why order matters:** fields and files are referenced by tokenized position (not name) in layouts and procedures, so simply reordering them in the Structure window can silently corrupt existing code's logical meaning.
- **The 4D Insider trick:** moving objects between two structure copies via 4D Insider retokenizes references by name, sidestepping the positional-reference problem.
- **Changing field order (steps):** copy the database → edit fields in the copy → quit 4D → open both copies in 4D Insider → Control-drag affected procedures/layouts to the working copy, choosing "Replace" so Insider retokenizes based on field names.
- **Changing file order (steps):** create a new database and set up its first file → Control-drag files one at a time (without associated objects) into the desired order → then drag all remaining non-file objects across in one step.
- **Caveats:** always back up first; existing data must be migrated separately via 4D's Import/Export editors.

## Featured Technology
- 4D Insider (structure documentation/editing companion tool)
- 4D's classic tokenized, position-based binary structure file format
- 4D Import/Export editors

## Historical Context
This note is deeply tied to the mechanics of 4D's classic binary .4DB structure format of the v3.x/v4.x era, where layouts and procedures held positional (tokenized) references to fields and files rather than name-based ones — a fragile design by modern standards. 4D Insider, the standalone tool used to work around this limitation by retokenizing objects during cross-structure moves, is not part of the modern 4D toolset. The introduction of Project Mode in 4D v17 (2018) and the general evolution of the structure file format have fundamentally changed how structure objects are represented and referenced, largely eliminating the specific fragility this note was written to address.
