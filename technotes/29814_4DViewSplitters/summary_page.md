# Tech Note: 4D View Splitters

- **Asset ID:** 29814
- **Tech Note #:** 03-40
- **Published:** September 30, 2003
- **Product / Version:** 4D View 2003
- **Platform:** Mac & Win
- **Author:** Gou Yang
- **Page URL:** https://kb.4d.com/assetid=29814
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_40-43_(SEP)/03-40_4D_View_Splitters.hqx

## Overview

Gou Yang, a 4D Technical Support Engineer, introduces the concept of panes and splitters in the 4D View plug-in — the mechanism that lets part of a spreadsheet-like area (e.g., a 'Last Name' and 'Average' column) stay fixed while the rest scrolls — and documents the commands to add, remove, and configure them programmatically instead of relying only on manual mouse dragging.

## Key Points

- Explains that a 4D View area starts as one scrollable pane, and adding a horizontal or vertical splitter divides it into two independently scrolling panes — the mechanism behind 'freeze pane' style layouts
- Documents manual splitter add/remove via drag handles at the top of the horizontal/vertical scrollbar (drag down/right to add, drag back to the edge to remove)
- PV ADD HOR SPLITTER(Area;Splitter;Position;Locked) / PV ADD VERT SPLITTER(...) add a new splitter at a pixel offset from the last one, with an optional locked flag
- Shows querying current pane count and row/column size with PV Get area property(...;pv hor pane count), PV Get row height, and PV Get column width before computing where a new splitter should go
- PV REMOVE HOR SPLITTER / PV REMOVE VERT SPLITTER remove the last splitter of that orientation, guarded by a pane-count > 1 check since removing the sole remaining pane raises an alert
- PV SET HOR PANE PROPERTY / PV SET VERT PANE PROPERTY configure an individual pane after creation — demonstrated locking a pane's scrollbar and splitter, and scrolling a pane to a specific column via a relative-scroll pixel offset
- Notes that 4D View numbers the first column as index zero when computing relative-scroll offsets from column width

## Featured Technology

- 4D View plug-in panes and splitters
- PV ADD HOR SPLITTER / PV ADD VERT SPLITTER
- PV REMOVE HOR SPLITTER / PV REMOVE VERT SPLITTER
- PV SET HOR PANE PROPERTY / PV SET VERT PANE PROPERTY
- PV Get area property / PV Get row height / PV Get column width
- Locked scrollbars/splitters for frozen header-like panes

## Historical Commentary

**Status:** Obsolete

This note documents 4D View plug-in commands for a spreadsheet-style pane/splitter UI that has since been retired from 4D's supported toolset — the 4D View plug-in was deprecated and removed as native List Box form objects (with their own built-in frozen-column and frozen-row support) matured and became the standard way to build grid/spreadsheet-like interfaces in 4D. The PV_ADD/REMOVE/SET SPLITTER commands themselves are not applicable to current 4D form objects, making this note of historical interest only for developers maintaining very old 4D View-based databases.

**References to newer/updated information:**
- The 4D View plug-in has been discontinued; current 4D form development uses native List Box objects, which have their own built-in frozen-row/frozen-column support
- Developers still maintaining legacy 4D View-based databases would need the discontinued plug-in to use the PV_ splitter commands documented in this note
