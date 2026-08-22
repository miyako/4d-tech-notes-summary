# Tech Note 96-46: 4D V6 Language Part 2: New Commands by Category

**Author:** Not specified
**Published:** November 1, 1996 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11719
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_45-50_(NOV)/96-46_Language_Pt2.exe

## Overview
Part 2 of a two-part series cataloging new and enhanced 4D V6 language commands by functional category, described as the most significant upgrade to 4D since the release of 4D Server, fulfilling many developer "wish list" requests submitted since Version 3.

## Key Points
- **4D/System Environment Commands:** query the running application (ACI folder, Application file/type/version, Compiled, Data/Structure file paths, DATA SEGMENT LIST) and the host system (Count Screens, Current Machine/Owner, FONTLIST, Gestalt, screen dimensions/depth, System/Temporary folder).
- **Language commands:** `RESOLVE POINTER` resolves a pointer to a variable name, table/field number, or array name + element index; supports building dynamic command names via constants.
- **Message commands:** `ALERT`, `CONFIRM`, `REQUEST` gain customizable OK/Cancel button text.
- **Resource commands:** a full new suite for cross-platform (Mac/Windows) resource file manipulation (create/open/close, get/set icon/picture/text/string resources, resource lists).
- **Set commands:** adds `COPY SET`.
- **ASCII conversion commands:** `ISO TO MAC`, `MAC TO ISO`, `WIN TO MAC`, `MAC TO WIN` for cross-charset text conversion.
- **Window commands:** Window-ID-based suite (`DRAG WINDOW`, `ERASE/REDRAW WINDOW`, `Find window`, `Get/SET WINDOW RECT`, `WINDOW LIST`, etc.) — some syntax noted as not yet finalized.
- **Password System (Users & Groups) commands:** built around unique User/Group IDs (`DELETE USER`, `GET/SET GROUP/USER PROPERTIES`, `GET GROUP/USER LIST`).
- Notes that a Menu command suite existed only in an external "Menuset" package pending finalization at time of writing.

## Featured Technology
- 4D V6 new language commands (Environment, Resource, Window, Password/Users&Groups, ASCII conversion)
- RESOLVE POINTER command
- Resource file manipulation commands
- Window ID-based window management commands

## Historical Context
**Status:** Superseded

Most of the specific command suites cataloged here are now legacy: modern 4D uses Unicode text natively (eliminating most need for the ISO/Mac/Windows ASCII conversion commands), relies much less on OS-level resource files for icons/pictures/strings, and has significantly extended its password/permission model well beyond the Users & Groups system described. The Window-ID and pointer-resolution introspection concepts, along with the Events/Methods terminology V6 introduced (replacing Phases/Procedures), remain recognizable in 4D's language today, even as the surrounding command set has grown substantially since 1996.
