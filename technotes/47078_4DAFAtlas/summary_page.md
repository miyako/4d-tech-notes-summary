# Tech Note 07-29: An Atlas with the 4D Ajax Framework

**Author:** Jean-Yves Fock-Hoon
**Published:** July 25, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47078
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_26-29_(JUL)/07-29_4DAF_Atlas.zip

## Overview
This note builds an interactive country atlas "mash-up" that combines two features new in 4D Ajax Framework (4DAF) 1.1 — the Data Matrix/Image Browser and Data Driven Tabs — with the Google Maps API, all shown in a Developer Defined Window (DDW).

## Key Points
- **Data Matrix (Image Browser):** a new 4DAF 1.1 object displaying records, including Picture fields, as a visual grid — used here to show country flags.
- Setting a table's View style to "DataMatrix" (instead of "Grid") in the Control Panel's Access Control tab switches its display.
- **Data Driven Tabs:** navigation tabs auto-generated from a field's distinct values via a "dynamic" preset query (configured in the Query Manager tab), refreshing periodically as data changes; an "All records" tab can be shown first.
- A "Map It" DDW opens a separate window embedding the Google Maps API, showing the map for the selected country.
- The Data Matrix can also be embedded directly in custom HTML via the 4DAF `dataMatrix` JavaScript constructor and its `customize()` method, with detailed parameter documentation (target node, selection, header/content templates, image field, layout, margin, zoom, scroll mode, forced rows/columns, toolbar visibility).
- Known limitation: Data Matrix objects lacked auto-resize support in 4DAF 1.1, requiring a manual `onresize`-triggered JavaScript workaround.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- Data Matrix / Image Browser, Data Driven Tabs
- Developer Defined Windows (DDW)
- Google Maps API

## Historical Context
Published July 2007 during active 4D Web 2.0 Pack development, a few months before 4D v11 shipped native SQL support. The Control Panel-driven View/Query configuration model described predates Project Mode and ORDA by roughly a decade.

## Historical Commentary
**Status:** Obsolete

The 4DAF, its Control Panel, Query Manager, and the `dataMatrix` JavaScript object are all tied to the discontinued 4D Web 2.0 Pack and no longer exist in any current 4D product, making the concrete configuration steps obsolete. That said, the underlying idea — mashing up local structured data with a third-party mapping API, and generating dynamic navigation tabs from data values — remains a standard and still-relevant UI/integration pattern, just implemented today with modern JS mapping libraries and 4D's REST/ORDA APIs rather than 4DAF-specific objects.
