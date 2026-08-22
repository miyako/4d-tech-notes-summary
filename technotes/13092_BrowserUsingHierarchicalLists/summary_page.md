# Tech Note 01-11: Implementing a Browser using Hierarchical Lists

**Author:** Not specified in source document
**Published:** March 30, 2001 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13092
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_11-15_(MAR)/01-11_Browser_using_HLists.exe

## Overview
An example implementation of a tree-style browser interface built with 4D's hierarchical list form object. This technical note demonstrates how to implement a browser-style interface — a tree view allowing users to navigate nested, expandable categories of data — using 4D's hierarchical list form object.

## Key Points
- Rather than focusing purely on the theory of hierarchical lists, the note provides a good, concrete example of the object in active use, showing developers how the pieces fit together to create a working, navigable tree browser.
- As a compact, example-driven Tech Note, its featured technology is centered entirely on the hierarchical list control itself as the vehicle for building tree-style navigation interfaces, a common UI pattern needed for anything from category browsers to outline-style data displays in classic 4D applications.

## Featured Technology
- Hierarchical lists (form objects)
- Tree/browser-style data display

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Partially_superseded

This note demonstrates building a tree/browser-style interface using 4D's hierarchical list form object, a classic-language UI control for displaying nested, expandable data. Hierarchical lists remain part of 4D's current form object set and continue to function as documented, so the core technique is still usable today, though many modern 4D interfaces increasingly favor the hierarchical mode of list boxes (which offer richer formatting and data-binding options) over the older dedicated hierarchical list object for tree-style displays.

**Related updates since:**
- 4D's hierarchical list form object remains supported in current versions, but list boxes with hierarchical/tree display modes now offer a more modern, flexible alternative for similar tree-style interfaces
- ORDA entity selections provide a more contemporary way to back a tree/browser interface with underlying data than classic selection-driven hierarchical lists

