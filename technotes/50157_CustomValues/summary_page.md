# Tech Note 08-23: Custom Values in the 4D Ajax Framework

**Author:** Tim Penner, Technical Services Team Member, 4D Inc.
**Published:** June 19, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_21-24_(JUN)/08-23_4DAF_Custom_Values.zip

## Overview
The 4D Ajax Framework's Data Grids, Charts, and Queries are powerful out-of-the-box objects, but they address specific data patterns. Custom Values extend this power by allowing developers to pass arbitrary name/value pairs from JavaScript to the 4D backend, enabling business logic (lookups, calculations, validations) to run server-side and return computed results back to the frontend—all without requiring a full grid/chart object. Custom Values work hand-in-hand with the beta-stage Data Bridge 2.0 object, which replaces the earlier Bridge 1.0 with improved flexibility.

## Key Points
- **Three-step interaction model:** Frontend sends custom values → backend processes them → frontend receives computed results.
- **Frontend: Sending custom values (charts, grids, queries):** All three object types support custom values through similar APIs:
  - `object.clearCustomValues()` — resets the custom value collection.
  - `object.addCustomValue(name, value)` — adds a name/value pair.
  - `object.runQuery()` or `object.refresh()` — transmits the values to 4D (for grids/charts).
- **Backend: DAX_DevHook_OnQuery and Data Bridge 2.0:** The `DAX_DevHook_OnQuery` project method is invoked when the frontend requests data. Within this hook, developers call `DAX_Dev_GetWebVar(customValueName)` to retrieve custom value data, execute business logic (database lookups, price calculations, etc.), and assemble results into two matching text arrays: `customVarName_at` (names) and `customVarValue_at` (values). The values are then returned to the frontend via `DAX_Dev_SetCustomVariables()`.
- **Frontend: Receiving results:** After the query completes, JavaScript retrieves returned custom values via `object.getCustomValuesFrom4D()`, which returns an array of objects with `.name` and `.value` properties. Arrays are 0-indexed.
- **Array synchronization requirement:** Critical constraint: the order of `customVarName_at[i]` must exactly match the order of `customVarValue_at[i]`. Misalignment silently corrupts returned data.
- **Data Bridge 2.0 status:** Marked as Beta at the time this Technical Note was released, requiring a beta version of the 4DAF to use with interpreted source databases.
- **Example: Car dealership quoting system:** The included sample demonstrates a realistic use case: a web form displays car models in a grid; selecting a model fires a custom value `modelID` to the backend. The backend looks up available colors and options for that model, computes their prices, and returns two custom values (`colors_cv` and `options_cv`) to dynamically update the frontend UI. Without Custom Values, this would require either a full grid refresh or complex JavaScript/REST manipulation.
- **Installation requirement:** Custom values require a one-line modification to the installed `DAX_DevHook_OnQuery` method to call a developer-defined hook function at the correct insertion point (line 53).

## Featured Technology
- 4D Ajax Framework (v11.2 Release 2, beta Data Bridge 2.0)
- Custom Values mechanism (name/value pairs)
- Chart, Grid, and Query objects
- JavaScript frontend (DOM manipulation, variable scoping)
- 4D backend project methods (DAX_DevHook_OnQuery)
- DAX_Dev_GetWebVar() and DAX_Dev_SetCustomVariables() commands
- 4D Web 2.0 Pack subscription model

## Historical Context
Published in June 2008, Custom Values represented a pragmatic solution to the limitations of declarative framework objects. The 4D Ajax Framework's Data Grids and Charts handled standard data fetching and display well, but developers often needed to pass contextual parameters (selected model ID, date range, user preference) to influence what data was returned. Custom Values bridged this gap without requiring developers to implement full-blown REST endpoints or write backend methods outside the framework. Data Bridge 2.0, replacing Bridge 1.0, offered improved flexibility and was positioned as the foundation for deeper framework integration.

However, this design pattern—passing name/value pairs through a hook method to compute and return results—was always somewhat ad-hoc. By the time 4D v12 (2012) introduced REST APIs, this pattern was already beginning to feel obsolete. REST provided a cleaner, more standards-aligned way to pass parameters and receive results. ORDA (v18, 2018) further standardized data access with JSON-based serialization and type safety. Modern 4D developers would never use Custom Values; they would build REST endpoints or ORDA data models.

## Historical Commentary
**Status:** Obsolete

The entire 4D Ajax Framework, including Data Bridge 2.0 and Custom Values, has been discontinued. The specific DAX_Dev_GetWebVar() and DAX_Dev_SetCustomVariables() commands no longer exist in modern 4D. Developers seeking equivalent functionality today would:
- **Use 4D REST APIs (v12+):** Define REST resource functions to accept query parameters and return JSON responses—a standards-based approach vastly simpler and more familiar to modern web developers.
- **Use ADORA (v18+):** Build data models with ORDA entities and class functions that return computed results. Call these functions via REST or directly in web components.
- **Use Qodly (GA 2021):** The modern low-code web platform abstracts data access entirely, providing reactive data binding and formula-based computed fields without requiring manual parameter passing.
- **Use 4D Web Components:** Modern web components in 4D provide built-in data binding and event handling, eliminating the need for manual custom variable marshaling.

The concept of passing client-side parameters to server-side logic for computation remains foundational to modern web development (every REST API endpoint does this). However, the 4DAF's Custom Values approach, with its manual name/value array handling and hook-method interception, is now a historical artifact—a snapshot of how 4D web development worked before REST APIs and JSON became the standard lingua franca of the web.
