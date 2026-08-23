# Tech Note: 4D Write, Programming Styles, and Entry Control (part II)

- **Asset ID:** 25588
- **Tech Note #:** 02-47
- **Published:** October 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel
- **Page URL:** https://kb.4d.com/assetid=25588
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_46-50_(OCT)/02-47_4D_Write_Styles_Etc.hqx

## Overview

Roland Lannuzel builds on the entry-control technique from Tech Note 02-02 to solve two related problems in classic 4D Write: controlling the Paste command so pasted text takes on the cursor's style rather than its original formatting, and converting a piece of styled, paragraph-structured text typed into a controlled 4D Write area into a native 4D hierarchical list (for use in list boxes, outlines, etc., persistable via BLOB to list/LIST TO BLOB for databases without 4D Write). Paste interception uses `WR ON COMMAND` to hook the hidden 4D Write menu, memorizing the cursor's location and style before executing the paste and reapplying that style to the newly pasted text. The list-building method (`WR_BuildList`) walks the document paragraph by paragraph, comparing each paragraph's style level to the previous one to decide whether to append a sibling list element or descend into a new sublist, attaching green/red icons from the picture library to indicate element type, plus a companion `WR CheckText` validator that flags any paragraph whose style jumps by more than one level as invalid (coloring it red).

## Key Points

- Intercepts the Paste command via `WR ON COMMAND(zWR;"WR_OnCommand")` registered on form load, then in the handler memorizes the selection/cursor style with `WR GET SELECTION`/`WR_GetStyleSheetIndice`, executes `WR EXECUTE COMMAND($WR;wr cmd paste)`, and reapplies the pre-paste cursor style to the newly inserted text via `WR APPLY STYLESHEET`.
- Validates paragraph style consistency before list-building with a `WR CheckText` method that walks every paragraph via `WR_SelectParagraph("NEXT")`, comparing each paragraph's style index to the previous one; if a jump greater than one level is detected, the whole area's text is set to red (`WR SET TEXT PROPERTY(...;wr text color;wr red)`) and an error is returned.
- Builds a 4D hierarchical list from the styled paragraphs in `WR_BuildList`: creates a new list via `New list`, then for each paragraph compares its style level to the previous paragraph's level -- an equal-or-lower level becomes a sibling element (`APPEND TO LIST`) in the current list, while a higher level starts a nested sublist (a fresh `New list` attached as the previous element's sublist), tracking nesting via parallel arrays `◊tRefList`/`◊tLvlList`.
- Attaches distinct picture-library icons (green for elements-with-sublists, red variants for a toggled/alternate state) to list items via `SET LIST ITEM PROPERTIES(...;Use PicRef+$GreenIcon)`, and provides a companion method that lets users toggle an item's icon color and expand/collapse its sublist by holding Command (Mac) or Ctrl (Windows) while clicking.
- Shows how to color a bullet character in a 4D Write area (matching the following text's color) by inserting a leading space and setting its color via `WR SET TEXT PROPERTY`/`WR Get text property`.
- References `BLOB to list`/`LIST TO BLOB` for persisting the resulting hierarchical list in databases that don't use 4D Write.

## Featured Technology

- 4D Write commands (WR EXECUTE COMMAND, WR GET/SET SELECTION, WR APPLY STYLESHEET)
- WR ON COMMAND for intercepting Paste
- New list / hierarchical lists built from paragraph styles
- GET LIST ITEM / SET LIST ITEM / SET LIST ITEM PROPERTIES
- BLOB to list / LIST TO BLOB
- Style-based paragraph-to-outline conversion

## Historical Commentary

**Status:** obsolete

Roland Lannuzel (4D S.A.) extends the entry-control technique from Tech Note 02-02 to intercept and control the Paste command in a 4D Write area (preserving cursor style rather than pasted formatting), and demonstrates converting styled paragraphs typed into a controlled 4D Write area directly into a 4D hierarchical list, where each paragraph's relative style level determines whether it becomes a list element or the start of a new nested sublist. The classic 4D Write plug-in referenced throughout this note has since been succeeded by 4D Write Pro, which uses a substantially different, more modern document/object model, so the specific WR-prefixed commands, style-sheet indices, and BLOB-based list persistence shown here no longer apply to current 4D document development, even though the general concept of deriving structured data from styled text remains a reasonable technique.

References to newer/updated information:
- The classic 4D Write plug-in has been succeeded by 4D Write Pro, which uses a different, more modern document and formatting model than the WR-prefixed commands (WR EXECUTE COMMAND, WR GET/SET SELECTION, WR APPLY STYLESHEET) described in this note
- BLOB to list / LIST TO BLOB and the style-index-based hierarchical list construction shown here are tied to classic 4D Write and are not directly applicable to 4D Write Pro documents
