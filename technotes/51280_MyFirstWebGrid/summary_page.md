# Tech Note 08-36: My First Web Grid

**Author:** Add Komoncharoensiri  
**Published:** October 16, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51280  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_35-39_(OCT)/08-36_My_First_WebGrid.pdf

## Overview

This Tech Note serves as an introductory guide to the 4D Ajax Framework's Data Grid 2.0, a sophisticated AJAX-based component for building dynamic, interactive web applications that display and manipulate tabular data. It bridges the gap between 4D's desktop UI paradigms (like List Boxes and 4D View areas) and modern web-based interfaces, enabling developers to create web 2.0 applications with inline editing, sorting, searching, and data navigation capabilities.

## Key Points

- **Data Grid in 4D Ajax Framework Client:** Tables automatically appear in the client with built-in features including a toolbar (Add/Delete buttons, search), preset query tabs or sidebar navigation, column headers (clickable for sorting), inline editing, full-screen record editor access via double-click, field visibility controls, and field search toggles managed through an Admin Control Panel.

- **Integration into Custom HTML Pages:** Developers can bring the same Data Grid functionality into their own HTML pages using a structured HTML shell that includes XML parsing instructions, CSS references (theme files like leopard.css), JavaScript library imports, and placeholder DIV elements for grid placement.

- **HTML Shell Components:** Four critical parts: (1) XML parsing instructions and DOCTYPE declaration, (2) CSS stylesheet reference for visual consistency, (3) JavaScript library references (resources localization file + compile.js) and space for developer-written JS code, (4) a placeholder area (DIV) where the grid renders.

- **Localization Support:** Multiple language packs available (English resources_en.js, French resources_fr.js, German resources_de.js, Spanish resources_es.js, Japanese resources_ja.js) for presenting notifications and UI text to end users.

- **Data Binding:** Data Grid columns automatically bind to database fields (for table-based selections) or to arrays (for Developer Created Selections / DCS), allowing flexible data presentation.

- **JavaScript Constructor & API:** Developers instantiate Data Grids using JavaScript constructor syntax (new dax_dataGrid(selection, location, headerRows, ...)) and call JavaScript functions to load the grid into a specified location on the HTML page; the API allows programmatic manipulation of layout and feature enablement.

- **Field Visibility & Search Control:** Admin Control Panel checkboxes under the "O" (Output) column toggle which fields are returned in query responses, and "S" (Search) column checkboxes determine which fields appear in search functionality.

- **CSS Customization:** The framework's CSS files enforce a standard look-and-feel; developers can override or adapt CSS to match their branding.

## Featured Technology

- 4D Ajax Framework (4DAF/A4D)
- Data Grid 2.0 component
- Web 2.0 AJAX/JavaScript technologies
- JavaScript API for grid control
- HTML/CSS-based UI integration
- Multi-language localization
- Developer Created Selections (DCS)

## Historical Context

Published in October 2008 during the 4D Web 2.0 era, this note represents a pivotal moment in 4D's web strategy when AJAX-based interfaces were cutting-edge for delivering dynamic web UIs from a server-side database. The framework provided 4D developers with a familiar, object-oriented abstraction layer over raw JavaScript and web technologies, allowing them to build rich data-manipulation UIs in a browser without abandoning the 4D ecosystem.

## Historical Commentary

**Status:** Obsolete

The 4D Ajax Framework and its supporting tooling (4DAF, A4D) have been fully retired by 4D in favor of a modern REST/web-components architecture. Today's 4D web development relies on REST APIs, Qodly (4D's low-code web platform introduced in 2023), and standard JavaScript frameworks (Vue, React) for client-side UI, rather than the framework-specific JavaScript API described here. The CSS themes, localization mechanisms, and grid constructor patterns documented in this note are no longer applicable to any current 4D product release.
