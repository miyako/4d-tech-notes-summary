# Tech Note: Simple Applications for Choice Lists

- **Asset ID:** 11994
- **Tech Note #:** 00-55
- **Published:** November 2000
- **Product / Version:** 4D not specified
- **Platform:** Mac & Win
- **Author:** Steve Hussey
- **Page URL:** https://kb.4d.com/assetid=11994
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_51-55_(NOV)/00-55_Choice_Lists.hqx

## Overview

Steve Hussey, CEO of Alto Stratus LLC, surveys practical uses of 4D's non-hierarchical choice lists for field entry, drop-down menus, and tab-object labels, then presents a data-file-backed technique (Util_List/Util_List_Item tables plus a LIST_Updt rebuilding method) that lets end users edit list contents without losing their changes when the developer ships a new structure.

## Key Points

- Choice Lists speed and standardize field data entry; Required Lists restrict entries to only the listed values; Excluded Lists block specific values from being entered — all three assignable at the table level (Field Properties) or overridden per-form (Object Properties' Data Control tab).
- Drop-down menus are populated by copying a list's contents into an array with LIST TO ARRAY("clst_Platform";drop_Platform); the resulting variable holds the selected element's index (e.g., drop_Platform{drop_Platform}) which is then assigned into the target field.
- Tab object labels can be driven by a choice list, with each list element corresponding to one tab in order; SET LIST ITEM PROPERTIES(SomeTabName;1;False;Plain;0) programmatically disables (grays out) an individual tab, and Selected List Item reads which tab the user chose.
- Because lists are stored in the structure file, any values an end user adds are lost the moment the developer ships an updated structure — a core motivating problem the note sets out to solve.
- The fix duplicates list data into two data-file tables, Util_List (List_ID, List_Name) and the related-many Util_List_Item (keyed by List_ID), so user edits persist independently of the structure file.
- The custom LIST_Updt($ListName) function queries Util_List/Util_List_Item, sorts the items, and rebuilds the corresponding in-memory 4D list via SELECTION TO ARRAY and ARRAY TO LIST; a Modify Lists dialog lets end users create/delete lists and add/edit/delete/sort list items entirely from the data file.

## Featured Technology

- Non-hierarchical choice lists (List Editor)
- Required Lists and Excluded Lists
- LIST TO ARRAY / ARRAY TO LIST for drop-down menus
- SET LIST ITEM PROPERTIES for tab enable/disable
- Data-file-backed list storage (Util_List / Util_List_Item tables)

## Historical Commentary

**Status:** Partially Superseded

Written by Steve Hussey, CEO of Alto Stratus LLC, this note surveys the practical uses of 4D's non-hierarchical choice lists — field data-entry aids, drop-down menu sources, and tab-object labels — and then addresses a real structural limitation: choice lists live in the structure file, so any client customization to them is overwritten the next time a developer ships a structure update. The proposed fix, replicating list contents into data-file tables (Util_List/Util_List_Item) and rebuilding the in-memory list from that data via LIST_Updt, remains a workable pattern today, though many modern 4D applications solve the same underlying problem more directly using an ORDA/database-backed configuration table queried straight into an array or collection rather than round-tripping through the classic List object model.

**References to newer/updated information:**
- LIST TO ARRAY, ARRAY TO LIST, and SET LIST ITEM PROPERTIES remain part of the current 4D language with unchanged core behavior for choice lists and tab objects
- Modern 4D applications increasingly store user-editable choice values directly in ORDA entities/collections rather than layering a data-file-backed list-rebuilding system atop the classic List object model
