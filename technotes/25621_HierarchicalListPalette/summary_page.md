# Tech Note 03-4: Hierarchical List Palette

**Author:** Cha Yang, 4D Inc. Technical Support
**Published:** January 31, 2003 | **Product/Version:** 4D v6.8.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25621
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_01-05_(JAN)/03-04_list_palette.exe

## Overview
TN 03-4 is a reference-style Tech Note that goes beyond hierarchical list basics to show correct, edge-case-aware code for inserting, appending, replacing, and deleting items (including child items) in 4D's classic hierarchical list object, using the sample "Hierarchical List Palette" database.

## Key Points
- Clarifies that Count list items / Selected list item positions are always relative to the main list's top item, even inside a sublist.
- Shows how to emulate "insert after" (only INSERT LIST ITEM "before" exists natively) by locating the next sibling item.
- Covers edge cases: empty list, selected item is the list's last item, selected item is a sublist's last item, and an expanded child sitting between siblings.
- Explains adding a child item to a leaf node by creating a new list and attaching it via SET LIST ITEM with the same item text.
- Shows appending to a sublist by resolving the sublist reference through the item's parent.
- References an earlier tech note by Thomas D'Urso on basic hierarchical list construction as a prerequisite.

## Featured Technology
- Hierarchical lists
- APPEND TO LIST / INSERT LIST ITEM / SET LIST ITEM / DELETE LIST ITEM
- List item parent/position commands

## Historical Context
Hierarchical lists were (and remain) a core 4D form object used for tree-style displays; this note documents the classic list-reference-number-based API used before any of 4D's later object/collection language additions existed.

## Historical Commentary
**Status:** Still Relevant

The specific list commands discussed (APPEND TO LIST, INSERT LIST ITEM, SET LIST ITEM, List item parent, List item position) are still part of the current 4D language and remain the standard way to manipulate hierarchical lists, making this note's core technical content largely still relevant. What has changed since 2003 is mainly the surrounding tooling — Design Mode's binary structure file has since been supplemented by Project Mode, and modern 4D code would likely favor object/collection-based data structures for anything not directly tied to a list form object.
