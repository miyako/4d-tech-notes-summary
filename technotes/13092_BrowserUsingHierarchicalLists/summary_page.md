# Tech Note: Implementing a Browser using Hierarchical Lists

- **Asset ID:** 13092
- **Tech Note #:** 01-11
- **Published:** March 30, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Jean-Luc Pellerin
- **Page URL:** https://kb.4d.com/assetid=13092
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_11-15_(MAR)/01-11_Browser_using_HLists.hqx

## Overview

Jean-Luc Pellerin (Training Manager, 4D SA) shows how to build a two-level drill-down browser interface using 4D's classic hierarchical list commands, using a `[Customers]` database organized by Region and County as the working example. Clicking a region reveals its counties, and clicking either updates the current selection displayed elsewhere in the interface.

## Key Points

- An interprocess variable `◊LH` holds the hierarchical list reference so the list is shared across all processes rather than duplicated per process; it's cleared with `CLEAR LIST(◊LH;*)` if it already exists before rebuilding.
- The top level is populated by getting all distinct region names via `DISTINCT VALUES([Customers]Region;$T_Region)`, then looping through the array and calling `APPEND TO LIST(◊LH;$T_Region{$i};Random)` for each one, assigning random item IDs.
- On click, the code determines whether the selected item is a region (level 1) or county (level 2) by walking up the hierarchy with a `While` loop calling `List item parent(◊LH;$Element_Ref)` and counting iterations.
- For a region click, a sublist of counties is built lazily — only if it doesn't already exist — via `DISTINCT VALUES([Customers]County;$T_Dpt)`, then attached to the parent region item with `SET LIST ITEM(◊LH;$Element_Ref;$Tx;$Element_Ref;$Sous_Liste;True)`, followed by `REDRAW LIST`.
- A county click instead performs a direct `QUERY([Customers];[Customers]County=$Tx)` to filter records to that specific county.
- On form exit, `DELETE LIST(◊LH;*)` must be called (with the `*` parameter to also remove attached sublists), since simply nulling out the reference variable would leak the list itself in memory.

## Featured Technology

- Hierarchical lists (New list, APPEND TO LIST, SET LIST ITEM)
- DISTINCT VALUES for building list source arrays
- List item parent / Selected list item / GET LIST ITEM
- REDRAW LIST / DELETE LIST
- Interprocess variables for shared list references
- Two-level drill-down region/county browser

## Historical Commentary

**Status:** Partially superseded

Jean-Luc Pellerin's note builds a two-level drill-down browser (region then county) entirely from 4D's classic hierarchical list commands, dynamically populating parent items from DISTINCT VALUES on a Region field and lazily building each region's county sublist only when first clicked, tracking list depth by walking List item parent. Hierarchical lists remain part of 4D's classic language and this technique still works, but modern list box objects (especially hierarchical list boxes bound to ORDA entity selections) provide a considerably more capable, easier-to-maintain way to build drill-down browsers than manually managing list references, sublists, and interprocess variables by hand.

**References to newer/updated information:**
- 4D's list box form objects, including hierarchical list box support bound to ORDA entity selections, now offer a more modern and maintainable way to build multi-level drill-down browsers
- The classic hierarchical list commands (New list, APPEND TO LIST, SET LIST ITEM, etc.) remain available and functional in current 4D versions for cases still using classic hierarchical lists
