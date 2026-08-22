# Tech Note 96-47: 4D V6: Events Replace Phases, Methods Replace Procedures

**Author:** Thomas D’Urso
**Published:** November 1, 1996 | **Product/Version:** 4D v6.0 (pre-release preview) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11686
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_45-50_(NOV)/96-47_Events-Triggers.exe

## Overview
Part of a monthly series previewing the unreleased 4D Version 6 for developers, this Tech Note introduces V6's foundational terminology shift: procedures and scripts become **Methods**, and execution-cycle **Phases** become **Events**. It explains the five method types, the event categories that trigger them, and how to view/create/edit them in the design environment, alongside the new **Constants** feature.

## Key Points
- **Five Method types:** Database Methods (environment-level, e.g. On Startup/On Exit/On Server Startup/On Web Connection), Project Methods (formerly global procedures), Table Methods/Triggers (formerly file procedures), Form Methods (formerly layout procedures), and Object Methods (formerly scripts).
- **Three Event categories:** Database Events (per-table record save/delete/load, handled in Triggers), Form Events (display/print/import-export, handled in Form/Object Methods), and user-generated events (keyboard/mouse), handleable via the forms architecture or `ON EVENT CALL`.
- Database Methods execute automatically on defined lifecycle events and cannot be manually invoked or deleted; a compatibility setting lets a V3-style Startup procedure keep running if desired.
- Triggers can be individually enabled/disabled per table in the Table Properties dialog; `Database event` and `TRIGGER PROPERTIES` determine which event fired.
- Form/Object Methods respond to a documented list of Form Events (On Before, On Click, On Double Click, On Data Change, On Keystroke, On Menu Selected, printing events, etc.), each individually enable/disable-able.
- **Constants** are introduced as built-in, compiler-optimized named values (e.g. `Carriage Return`) replacing ad hoc developer-defined variables, improving readability and compiled performance.
- All of Version 3's file/layout/procedure/script-based databases continue to work unchanged in V6; only the terminology and organizational model changes.

## Featured Technology
- 4D V6 Methods (Database, Project, Table/Trigger, Form, Object)
- 4D V6 Events (Database Events, Form Events, user-generated events)
- 4D V6 Constants
- Explorer and Browser design-environment dialogs

## Historical Context
Published November 1996 ahead of 4D Version 6's mid/late-1997 release, this note is a direct preview of one of the most consequential terminology and architectural changes in 4D's history: the shift from "Files/Layouts/Procedures/Scripts/Phases" (Version 3 vocabulary) to "Tables/Forms/Methods/Events/Triggers/Constants" (V6 vocabulary and beyond). This shift was explicitly framed as making 4D's terminology friendlier to developers coming from the Windows/mainstream programming world.

## Historical Commentary
**Status:** Still Relevant

Remarkably, the core terminology this note introduces — Project Methods, Table Methods/Triggers, Form Methods, Object Methods, Database Methods, and Constants — remains 4D's standard vocabulary essentially unchanged decades later, making this note conceptually still relevant as a historical explanation of *why* modern 4D uses this vocabulary. What has changed are the specific design-environment tools: the V6-era Explorer/Browser dialogs shown here have since been superseded by the modern 4D Design environment's Explorer, Method Editor, and property panels, and Project Mode (a text-based project structure, introduced in 4D v17, 2018) now exists alongside the binary-structure Design Mode this note assumes.

