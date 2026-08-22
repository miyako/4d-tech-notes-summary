# Tech Note 07-21: Customization of the Data Grid

**Author:** Tim Penner, Technical Support Engineer, 4D Inc.
**Published:** May 31, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46602
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_17-21_(MAY)/07-21_Custom_Data_Grid.zip

## Overview
This note is a practical, video-supported walkthrough of customizing the Data Grid object of the 4D Ajax Framework (4DAF), using the 4D Web 2.0 Pack "Contacts" demo database as the working example.

## Key Points
- Basic setup: a custom HTML file loads 4DAF's localization/compile scripts and a stylesheet, wires login/logout to `<body>` onload/onunload, and instantiates a `DataWindow` JS object bound to a `<div>` inside an `onAfterInit` callback.
- Control visibility: `.customize(toolbar, tabbar, statusbar, editor)` toggles the four Data Grid controls on/off.
- Column visibility: `.hideColumns([colNumbers])` hides specific zero-indexed columns.
- Column widths: set via a `.grid.onafterload` callback calling `.grid.column(colNum).setWidth(pixels)` per column.
- Tab-driven layouts configured through the 4DAF Admin Control Panel's Query Manager: "Dynamic Queries" auto-generate tabs from a column's distinct values; "Template Queries" apply prebuilt templates (e.g., "A-Z Steps") to a chosen field.
- Setting a database's default "Home Page" is done via 4D's Preferences window, accessible in User Mode, Design Mode, and optionally Custom Menus Mode.
- Six companion videos cover: basic grid setup, hiding controls, hiding columns, column widths, tab-driven layout, and default home page.

## Featured Technology
- 4D Ajax Framework (4DAF) Data Grid / DataWindow JavaScript API
- 4DAF Admin Control Panel Query Manager (Dynamic and Template Queries)
- 4D Web 2.0 Pack Contacts demo database
- 4D Preferences / Custom Menus Mode

## Historical Context
Published May 2007, this note is a granular, code-level example of the "rich internet application" techniques of the 4D Web 2.0 Pack era — a proprietary JavaScript client library (4DAF) driving grid/tab UI over an HTML page — predating 4D v11's native SQL engine (2007), Project Mode (2018), and ORDA (2018), and reflecting the general 2007-era web-UI toolkit landscape of custom grid rendering and framework-specific client libraries (comparable to contemporaneous use of libraries like YUI elsewhere in the industry).

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework and 4D Web 2.0 Pack, including the Data Grid/DataWindow JavaScript API this note documents in detail, have been discontinued by 4D. None of the specific API calls (`.customize()`, `.hideColumns()`, `.grid.column().setWidth()`) or Control Panel workflow described here apply to current 4D products, which now offer built-in Web Server and Qodly-based component tooling for building rich web interfaces instead of a bespoke JS client framework.
