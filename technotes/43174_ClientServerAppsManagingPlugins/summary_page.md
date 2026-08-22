# Tech Note 06-21: Creating Client/Server Applications: Managing clients, plug-ins, tips and tricks

**Author:** Chiheb NASR, QA Engineer, 4D S.A.
**Published:** May 26, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43174
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_18-21_(MAY)/06-21_Creating_CS_Apps.pdf

## Overview
4D 2004 introduced a custom client/server multiplatform application generator, accessible via the Build Application dialog or, for finer control, via an XML project file passed to the BUILD APPLICATION command. This Tech Note walks through the mechanics: building platform-specific clients, auto-connecting clients to servers, automatic client upgrades, and how plug-ins get bundled into the final build.

## Key Points
- **Building clients:** you select 4D Client folders/packages for Mac and Windows in the Build dialog; you can only build a double-clickable client for the platform you're currently on, and each target platform requires its own Developer Edition license.
- **Auto-connect via EnginedServer.xml:** placed in the "4D Extensions" folder, this file lets a client find its server's IP/port automatically; if absent, the client displays a manual connection dialog and, once it finds the server, generates the file itself.
- **XML project keys:** the BuildApp.XML file supports keys for server/client IP and port, custom icons, version-range management (minimum/maximum/current version), and plug-in exclusion by name or ID. The note flags that some tag names (e.g., FolderIsValid → IncludeIt) changed between 4D 2004 and 2004.1.
- **Automatic client upgrade:** enabled via `<BuildCSUpgradeable>True</BuildCSUpgradeable>`, this feature has an old client detect a version mismatch, download a new archive, run a platform script (upgclnt.bat/upgclnt.sh) to swap in the new client and remove the old one, then reconnect — a 12-step documented process. This only works with compiled, not interpreted, databases.
- **Plug-in bundling and priority:** plug-ins can come from three folders (4D's own Plugins folder, the source database's plugins/Mac4dx/Win4dx folders, or 4D Server's plugins folder), with 4D Server's folder always winning conflicts; a worked example shows the resulting merged plugin set after excluding 4D View.
- **Conflict detection:** if the same plug-in ID appears twice under different names, 4D Server detects the conflict at launch and quits with an alert.

## Featured Technology
- 4D 2004 compiled Client/Server application generator (Build Application dialog / BUILD APPLICATION command)
- XML build project files (BuildApp.XML)
- EnginedServer.xml client auto-connect mechanism
- Automatic client upgrade scripts (upgclnt.bat / upgclnt.sh)
- 4D Server / 4D Client plug-in folder precedence

## Historical Context
Written for 4D 2004, this note predates 4D's SQL engine (introduced in v11, 2007), Project Mode (v17, 2018), and ORDA — it describes deployment tooling for the classic binary Design Mode structure file and compiled client/server generator of that era. The XML schema, file names, and upgrade-script mechanism documented are specific to that generation of 4D and have been substantially reworked in subsequent 4D Server/Client releases.

## Historical Commentary
**Status:** Superseded

The general need this note addresses — versioned client/server deployment with automatic client updates — remains a real concern for 4D developers today, but the specific mechanisms described (this exact BuildApp.XML schema, the EnginedServer.xml format, and the upgclnt shell/batch script pipeline) are tied to 4D 2004-era tooling and have since been reworked in later 4D Server/Client releases. Anyone building a modern 4D client/server deployment would need to consult current 4D documentation rather than rely on these specific XML tag names and file paths.
