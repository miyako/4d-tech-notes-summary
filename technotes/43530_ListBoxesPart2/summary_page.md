# Tech Note 06-26: List Boxes (Part II)

**Author:** Jean-Yves Fock-Hoon, Quality Assurance Manager, 4D Inc.
**Published:** June 29, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43530
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_22-26_(JUN)/06-26_Listboxes_Part_II.zip

## Overview
Part II of a two-part introduction to the List Box object in 4D 2004, this note is dedicated exclusively to manipulating list boxes through the 4D language, using a demo dialog with buttons that each exercise a different set of programmatic list box commands.

## Key Points
- Clear All: uses `Get number of listbox columns` and `DELETE LISTBOX COLUMN` to remove all columns.
- Insert Default / More Columns: uses a generic `M_InsertColumn` method built on `INSERT LISTBOX COLUMN` and `BUTTON TEXT` to add columns and their headers.
- Important constraint: all columns must be inserted before any attributes are set within the same method call — you cannot insert-then-configure one column at a time.
- Attributes button: uses `M_SetupColumn`, built on `SET RGB COLORS`, `FONT`, `FONT SIZE`, and `FONT STYLE` to style individual columns.
- Grid button: cycles through five grid display settings via `SET LISTBOX GRID COLOR` and `SHOW LISTBOX GRID`.
- Re-Order button: reorders columns despite there being no direct "move column" command, via a workaround — retrieve widths/metadata with `Get listbox column width` and `GET LISTBOX ARRAYS`, compute a new order with a custom `M_Setorder` method, delete all columns, then reinsert them in the new order.

## Featured Technology
- 4D List Box object (language-level manipulation)
- INSERT/DELETE LISTBOX COLUMN commands
- GET LISTBOX ARRAYS / Get listbox column width
- Column-reorder workaround pattern

## Historical Context
Published in 2006 for 4D 2004, this note documents the List Box object in its first year of existence in 4D — introduced as a major new form control replacing older grouped scrollable areas. It predates 4D v11's 2007 SQL engine, Project Mode (2018), and ORDA by a decade or more.

## Historical Commentary
**Status:** Still relevant

The specific List Box commands referenced here remain part of 4D's language today, and the column-reorder workaround pattern (delete-and-reinsert in computed order) is still a conceptually valid technique for cases without a direct native "move column" command. That said, the List Box object's API has been considerably extended since 2004, so some of the constraints and workarounds described (like the insert-before-configure requirement) may have been relaxed in more recent 4D versions.
