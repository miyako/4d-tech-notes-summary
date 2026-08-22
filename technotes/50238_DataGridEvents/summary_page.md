# Tech Note 08-24: Data Grid Events

**Author:** Joe Resuello, Technical Marketing Engineer, 4D Inc.
**Published:** June 26, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_21-24_(JUN)/08-24_Grid_Events.zip

## Overview
The Data Grid is the marquee component of the 4D Ajax Framework's web toolkit, providing list-style data display with inline editing and built-in pop-up editing windows. However, to build truly interactive web applications, developers must capture and respond to user interactions—clicks on grid cells, rows, and column headers. This note documents the JavaScript event model for doing so, allowing client-side logic to be triggered by grid interactions and to extract rich metadata about the interaction (field types, record IDs, column indices, etc.).

## Key Points
- **Five primary events:** The Data Grid supports column header clicks, row clicks, cell clicks, and double-click variants for rows and cells—each with distinct parameter signatures and available metadata.
- **onDataColumnClick:** Fired when a user clicks a column header. Parameters: column (integer index, 0-based) and fieldReference (object with fieldid, fieldalias, fieldtype, fieldsearchable properties). Returns: column ID, field alias, field data type, searchability flag.
- **onDataRowClick:** Fired when a user clicks a row. Parameters: row (integer, 0-based) and recordId (in [x][y] format referencing the record). Returns: row number, record ID.
- **onDataCellClick:** Fired when a user clicks an individual cell. Parameters: row, column, recordId, fieldReference. Returns: row number, column number, record ID, field alias, field ID, field data type, field searchability, and the cell's value.
- **onDataRowDblClick / onDataCellDblClick:** Double-click equivalents of row and cell clicks, enabling distinct logic for single vs. double interactions.
- **Event binding via JavaScript:** Event handlers are assigned directly: `myGrid.onDataColumnClick = myFunction;`. The framework invokes the function with the appropriate parameters when the event fires.
- **Browser-side logic:** All event handling occurs client-side in JavaScript; no backend 4D method is involved (unless the event handler initiates an AJAX call to 4D).
- **Field metadata access:** Events provide rich field information via the fieldReference object, enabling dynamic validation, formatting, or UI behavior based on field type and properties.
- **Inline event feedback:** Developers can update the DOM or display alerts directly in response to events, providing immediate visual feedback to users.

## Featured Technology
- 4D Ajax Framework (v11.2 Release 2 / Beta version)
- Data Grid component
- JavaScript event listener binding
- Field metadata objects
- Browser DOM manipulation
- HTML/CSS/JavaScript development
- Sample 4D databases (2004 and v11 SQL flavors)

## Historical Context
Published in June 2008, this note captures the golden age of the 4D Ajax Framework, when the Data Grid was positioned as 4D's primary web UI component. The event model documented here was the standard way to build interactive web applications with 4D: developers wrote JavaScript to bind event handlers to framework objects, extracted metadata, and orchestrated complex UIs. However, by the mid-2010s, the web development landscape had shifted dramatically toward component-based frameworks (React, Angular, Vue), RESTful APIs, and single-page application (SPA) architectures. The 4DAF's hand-rolled, proprietary event system became a liability rather than an asset.

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework, including the Data Grid and its JavaScript event model, has been discontinued. The specific event handlers (onDataColumnClick, onDataRowClick, etc.) no longer exist in any current 4D product. Developers looking to replicate this functionality today would:
- **Use modern web frameworks:** React, Vue, or Angular provide their own event handling, state management, and reactive data binding—far more powerful and standardized than the 4DAF's event model.
- **Build REST APIs:** Instead of relying on framework objects to fetch data, developers now build 4D REST APIs (available since v12, 2012) and fetch data via fetch() or axios.
- **Use Qodly:** 4D's modern low-code web platform (GA 2021) provides a visual grid component with built-in event handling and data binding, eliminating the need for manual JavaScript coding.
- **Use 4D Web Components:** Modern 4D web development leverages 4D Web Components (2020s), which use reactive binding and standard JavaScript events rather than proprietary event handlers.

The conceptual goal—capturing user interactions on data grids and responding with business logic—remains as relevant as ever. The technical implementation has evolved entirely, and the 4DAF's approach is now primarily of historical interest to developers maintaining legacy 4D v11 systems or studying the history of web application frameworks.
