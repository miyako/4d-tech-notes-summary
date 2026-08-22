# Tech Note 07-23: Custom List Manager

**Author:** Larry Sharpe
**Published:** June 13, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46705
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_22-25_(JUN)/07-23_Custom_Lists.zip

## Overview
This note presents a technique for building customizable, user-editable lists in 4D, combining 4D's native list functionality with a custom data-file-backed system so list edits are not lost when the database structure is updated — a redesign of an approach from a 2000-era Technical Note by Steve Hussey, updated for 4D v6.0-and-later conventions.

## Key Points
- Adds a single [xLists] table (ListName, SortOrder, Element fields), storing list data in the data file instead of the structure, so edits survive structure updates.
- The master list-of-lists is itself maintained as a 4D hierarchical list named "ListNames".
- A single Project Method, "xLists", implemented as a `Case of` dispatcher, handles opening the editor dialog, saving changes (delete-all-and-recreate strategy rather than diffing), and building inter-process arrays at startup.
- The "ListEditor" form lets end users manage elements of developer-defined lists, but not create new lists themselves.
- Extends the pattern to a keywords feature: a "People_Keywords" Project Method and form let each [People] record have zero, one, or many keywords via a two-list interface (drag-and-drop or double-click), with cleanup on record deletion.
- Demonstrates single-selection use cases too: a City popup menu and State-field validation, both driven by [xLists]-backed inter-process arrays.
- Notes the pattern is easy to replicate for other tables (e.g. adding a [CompaniesKeywords] feature via copy-paste-and-rename).
- Limitation: no support for icons/images per list element (author suggests adding a field to support this).

## Featured Technology
- 4D hierarchical lists (native list UI object)
- Data-file-backed custom list table ([xLists])
- Single dispatching Project Method (Case of pattern)
- Inter-process arrays for shared in-memory list data

## Historical Context
Published June 2007, this note reflects classic 4D 2004-era Design Mode development: raw tables, hierarchical lists, Project Methods, and inter-process arrays, well before Project Mode (2018), ORDA (2018), or 4D's native SQL engine (later in 2007). It's also an interesting example of community-authored Technical Notes building on prior community work spanning several major 4D versions (v6.0 to 2004).

## Historical Commentary
**Status:** Still relevant

The underlying problem — keeping user-editable pick lists and tags independent of structure/schema changes so they survive updates — remains a real and common requirement in database application development today. While the specific implementation techniques (raw hierarchical lists, inter-process arrays, manual Case of dispatch methods) are classic 4D idioms that a modern developer would likely replace with newer list-box/collection-based UI objects and more current data-access patterns, the conceptual approach of separating editable reference data from the schema is still sound and applicable.
