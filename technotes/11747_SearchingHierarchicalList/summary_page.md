# Tech Note: Searching a Hierarchical List

**Author:** Not specified
**Published:** June 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11747

## Overview
This Tech Note explains how to programmatically search items within a hierarchical list in 4D, accounting for the unique parent/child tree structure that distinguishes hierarchical lists from other data objects.

## Key Points
- **Unique data structure:** Hierarchical lists store "items" with parent/child relationships, not flat data.
- **Tree traversal:** Searching requires navigating the parent/child hierarchy rather than a simple linear scan.
- **Any item can be a parent:** Each item can have multiple children and one parent.
- **Easy to implement:** The note states the functionality is straightforward using 4D's commands.
- **Common use cases:** Category browsers, file system views, organizational hierarchies, navigation trees.

## Featured Technology
- Hierarchical lists (4D form object and data structure)
- Parent/child item relationships
- Tree search/traversal algorithms in 4D
- 4D hierarchical list commands

## Historical Context
**Status:** Superseded

Hierarchical lists remain available in modern 4D, and their fundamental parent/child data model is unchanged. However, the specific API has been updated over the years, and modern 4D also provides list boxes with hierarchical display modes as an alternative approach for tree-view interfaces. The algorithmic concepts — recursive tree traversal for searching hierarchical data — are timeless, even though the specific 4D commands used may have evolved. Developers working with hierarchical lists in current 4D versions should consult updated documentation.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
