# Tech Note 07-26: Inside the XMLTreeList System

**Author:** David Adams
**Published:** July 6, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46886
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_26-29_(JUL)/07-26_XML_Tree_List.zip

## Overview
This note explains the XmlTreeList module of the XML Tools component (see companion Technical Note 07-25), which solves the problem of visually displaying a DOM XML tree in 4D by mapping it onto 4D's native hierarchical list interface object.

## Key Points
- 4D reads/writes XML via SAX (stream) or DOM (tree); DOM is described as the more commonly used approach and central to modern web applications.
- `XmlTreeList_CopyXmlToHList` translates an in-memory DOM tree (produced by `DOM Parse XML variable`) into a 4D hierarchical list, showing element names and/or values.
- 4D hierarchical list items are limited to 255 characters, while DOM nodes can hold arbitrary-length text, CDATA sections, and multiple attributes — so the system avoids copying all data into the list.
- Instead, the XmlTreeList system maintains internal two-dimensional arrays pairing each list item's unique ID with the corresponding DOM node reference string, keeping the list and the original DOM tree in sync.
- Developers can then read/write the underlying element names, values, CDATA, and attributes directly via standard 4D DOM commands or other XML Tools routines.
- The note references the "XML Tree List" and "Test Related Nodes" demos in the bundled XML Tools example database, plus an alternative XML Parser 2 example database for a different approach.

## Featured Technology
- XML Tools component (`XmlTreeList_*` routines)
- 4D hierarchical lists (native UI tree/list object)
- 4D native DOM XML commands

## Historical Context
Published July 2007, alongside the broader XML Tools component note (07-25) and the XmlTreeWalker note (07-27), this Technical Note reflects the classic 4D 2004-era procedural language, Design Mode-only development (no Project Mode until 2018), and predates 4D v11's native SQL engine. It documents a solution to a UI/data-mapping problem that was genuinely awkward at the time given 4D's limited native XML-display tooling.

## Historical Commentary
**Status:** Superseded

The core idea — pairing a lightweight display structure with an ID-based reference back to richer source data — remains a sound UI pattern, but 4D's classic hierarchical list widget and the standalone XML Tools component are legacy technology. Modern 4D applications benefit from improved native list/tree UI objects and generally favor JSON over XML for data interchange, making this specific implementation of historical interest rather than a current best practice.
