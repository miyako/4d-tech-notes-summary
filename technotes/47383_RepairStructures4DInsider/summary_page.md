# Tech Note 07-34: Repairing Corrupted Structures with 4D Insider

**Author:** Achim Peschke, Manager of Support Department, 4D Germany
**Published:** August 29, 2007 | **Product/Version:** 4D Insider v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47383
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_30-34_(AUG)/07-34_Repair_with_4D_Insider.pdf

## Overview
This note explains how to use 4D Insider to recover a 4D database whose internal "data dictionary" (the arrays/pointers describing objects, their relations, and dependencies) has become corrupted, by moving all uncorrupted objects into a fresh destination structure in a carefully ordered sequence.

## Key Points
- 4D Insider does not literally repair the data dictionary — moving objects to a new empty database causes it to be fully rebuilt from scratch.
- **Step 1 – Empty the Trash:** clear the source Trash, including moving stray tables (which can't be truly deleted) back to the top level.
- **Step 2 – Remove tables from groups/folders:** only top-level (ungrouped) tables retain correct internal references.
- **Step 3 – Move Lists first:** preserves structure-level choice list assignments.
- **Step 4 – Move all Tables together, in one operation:** preserves table creation-order numbering, important for code referencing tables/fields by number.
- **Step 5 – Move everything else:** 4D Insider automatically skips objects already present in the destination.
- Users/Groups (the password system) are not moved automatically; Designer-created accounts are lost, while Administrator-created ones can be preserved via `USERS TO BLOB` / `BLOB TO USERS`.
- Table access assignments are restored by the *order* in which new groups are recreated, not by name.

## Featured Technology
- 4D Insider
- 4D Design Mode / Explorer (Trash, Groups/Folders)
- `USERS TO BLOB` / `BLOB TO USERS` commands

## Historical Context
Written for 4D 2004-era Design Mode, where the structure file is a binary .4DB/.4DC file and Explorer-based Trash/groups concepts govern object management — well before Project Mode (v17, 2018) replaced this with text-based project files, and before 4D v11 (2007) added native SQL support.

## Historical Commentary
**Status:** Superseded

The core diagnosis — that a "repair" is really a rebuild via object migration to a clean structure — remains conceptually informative for understanding how fragile binary structure files were, but the specific tool (4D Insider), UI (Design Mode Explorer, Trash, Groups), and commands described are tied to the 2004-era binary structure file format. Recovery/verification workflows in modern 4D versions, and the shift to Project Mode's text-based files, have superseded this specific process.
