# Tech Note 96-07: A Module for Managing Recursive Relationships

**Author:** Forrest Swilling
**Published:** February 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11690
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_06-10_(FEB)/96-07_Recursive_Package.exe

## Overview
Building on the classic two-file recursive relationship pattern introduced in a 1990 Tech Note ("Two-File Hierarchical Filing System" by Ron Dell'Aquila, TN 90-205), this note provides a reusable module of five procedures for navigating an [Objects]/[Links]-based hierarchical tree structure of unlimited depth — useful for file systems, genealogies, help systems, bills of materials, and multi-level marketing hierarchies.

## Key Points
- **FindBranch(RecordID):** finds all records subordinate to a given node by repeatedly using `PROJECT SELECTION` and `JOIN` to walk down the tree, accumulating each level into a "Children" set via `UNION` until no more descendants are found.
- **FindNonBranch(RecordID):** the complement of FindBranch — every record *not* subordinate to (or equal to) the given node, computed via `DIFFERENCE` against the branch, orphans, and the start node.
- **FindNextLevel(RecordID):** returns only the immediate next level of children (a simpler one-step subset of FindBranch's logic).
- **FindOrphans:** finds records disconnected from the tree entirely, useful for a data-maintenance UI presented when adding new records.
- **FindTop:** finds the single root/topmost record by comparing arrays of child and parent record IDs; the note notes how to adapt this for structures needing multiple root/entry points.
- A key `JOIN` gotcha is explained: since `JOIN` takes no explicit field parameter, when multiple relations exist between two files, 4D resolves ambiguity using the **first relation in field order** — so the [Links] file's field order directly affects the module's correctness.
- An example genealogy of 1960s B-movie actors (illustrating parent/child, male/female groupings) demonstrates each procedure concretely.

## Featured Technology
- 4D's classic two-file recursive relationship pattern ([Objects]/[Links])
- `PROJECT SELECTION` and `JOIN` commands
- 4D Sets (`CREATE SET`, `UNION`, `DIFFERENCE`)
- Arrays (`SELECTION TO ARRAY`, `Find in array`)

## Historical Context
Published February 1996, this note is an explicit follow-up/extension to a 1990 Tech Note, showing the multi-year lineage of hierarchical data modeling techniques within the 4D developer community well before any built-in recursive-query language features existed in 4D — everything here is implemented from first principles using JOIN, PROJECT SELECTION, and Sets.

## Historical Commentary
**Status:** Still Relevant

The specific classic-4D-language commands used here (`PROJECT SELECTION`, `CREATE SET`/`UNION`/`DIFFERENCE`, `SELECTION TO ARRAY`) reflect 4D's pre-V6, pre-ORDA procedural/set-based language, and modern 4D offers alternative, more current ways to express similar queries. However, the underlying conceptual pattern — a self-referencing parent/child relationship table for representing arbitrarily deep hierarchical data — remains a completely standard and still-used relational data modeling technique today, independent of the specific 4D commands shown.

