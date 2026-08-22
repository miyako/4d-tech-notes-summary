# Tech Note 02-26: Multi-level Clipboard in 4D

**Author:** Not specified in source document
**Published:** June 14, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=23243
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/Windows/TN_2002_25-29_(JUN)/02-26_Multi-Level_Clipboard.exe

## Overview
A Tech Note describing a custom, multi-item "4D Clipboard" system that simulates a private clipboard within a 4D application, supporting the storage and retrieval of multiple cut/copied items.

## Key Points
- Builds a custom 4D Clipboard that supports multiple stored items, unlike the OS's native single-item clipboard.
- Lets users retrieve/paste any individually stored item on demand.
- Demo handles text and pictures, but the approach is extensible to any data type.

## Featured Technology
- Custom multi-item clipboard
- Interprocess communication

## Historical Context
Written when native OS clipboards on both Mac and Windows only supported a single stored item, motivating this kind of application-level multi-item clipboard workaround.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

Modern operating systems now commonly offer native multi-item clipboard history features (e.g., Windows Clipboard History, various macOS clipboard manager utilities), somewhat reducing the novelty of this technique, but the underlying pattern of building an application-specific multi-item data store using interprocess communication remains a useful, still-applicable software design approach.
