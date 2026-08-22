# Tech Note 07-46: Developer Hooks for 4D Ajax Framework

**Author:** Add Komoncharoensiri, Manager of Internal Systems, 4D Inc.
**Published:** December 12, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=48355
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_46-47_(DEC)/07-46_4DAF_Dev_Hooks.pdf

## Overview
This note documents the Developer Hooks extension architecture of the 4D Ajax Framework (4DAF), which allowed 4D developers to override and extend the framework's default behavior when building Web 2.0-style, browser-based interfaces on top of a 4D database.

## Key Points
- 4DAF is composed of a database framework component (project methods) and front-end framework files (JavaScript library, CSS themes, HTML client).
- Component methods are grouped into Public (`DAX_DevHook_*`, developer-editable), Protected (`DAX_Dev_*`, callable utility methods), and Private (internal, hidden) categories.
- The note focuses on four Developer Hook areas: Developer Created Selections (DCS), Developer Defined Windows (DDW), Callbacks, and Choice Lists.
- **DCS (Developer Created Selections):** lets developers expose a custom, non-table "View" to the web front-end by composing 6 parallel arrays (field names, types, unique/mandatory/non-enterable/non-modifiable flags) via `DAX_DevHook_DCS_ViewAdd`, then populating data via `DAX_DevHook_DCS_SetSelection`.
- Record save/delete for a DCS view is handled via `DAX_DevHook_DCS_RecordSave` / `DAX_DevHook_DCS_RecordDelete`, keyed on the developer-chosen DCS view name.
- Other documented hooks include Callback install/event response, DDW install, Choice List install/override, Users/Groups override, Login/Session override, Query control (`OnQuery`, `QueryAdd`, `QueryFilter`), Record control (save/delete), and global Preferences override.
- Example code demonstrates building a "myContacts" DCS view backed by FirstName/LastName/DOB data pulled from a `[Contacts]` table via `SELECTION TO ARRAY`.

## Featured Technology
- 4D Ajax Framework (4DAF) database + front-end components
- Developer Created Selections (DCS)
- Developer Defined Windows (DDW)
- Callback and Choice List hook methods

## Historical Context
Published in December 2007 as part of the 4D Web 2.0 Pack line (v1.2), this note reflects 4D's late-2000s strategy of layering AJAX-driven web interactivity onto classic Design-Mode 4D databases, well before ORDA, REST APIs, or Project Mode existed. The 4DAF's method-prefix-based hook system (`DAX_DevHook_*`) was a bespoke extensibility mechanism specific to that framework.

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework has been discontinued and none of the DAX_DevHook_* methods, DCS/DDW mechanisms, or accompanying front-end JavaScript library exist in or are supported by current 4D products. Developers today would instead expose custom, non-table data to a web or mobile client using 4D's REST server and ORDA data model, or build the UI in a modern JS framework consuming that REST API — an approach conceptually similar in spirit (custom data views, custom UI controls) but implemented with entirely different, much more standards-based tooling.
