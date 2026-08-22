# Tech Note 06-11: 4D System Tool

**Author:** Jeremy Sullivan, Developer, 4D Inc.
**Published:** March 17, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42238
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_09-13_(MAR)/06-11_4D_System_Tool.zip

## Overview
This note demonstrates the LAUNCH EXTERNAL PROCESS command, added to the 4D language in 4D 2004, via a small demo application ("4D System Tool") that exposes native OS utilities from within a 4D database on both Mac OS X 10.4 and Windows XP.

## Key Points
- On Mac OS X, the demo is similar to utilities like Cocktail/Onyx/TinkerTool: it offers Appearance, Maintenance, Man (Unix man page viewer/exporter), and Info tools, plus a raw "Execute Command" dialog.
- On Windows XP, it offers Maintenance (defrag/chkdsk scheduling), Tasks (process list/kill, like Task Manager), Quick Launcher (editable list of Control Panel/Run utilities stored as XML), and Info.
- All commands route through one project method, ST_comm_executeCommand, which handles optional Mac authorization prompts and, on Windows, suppresses the console window before calling LAUNCH EXTERNAL PROCESS.
- Code examples show calling "whoami" for convenience at startup, and chaining "/bin/sh -c" calls to man, groff, and open to convert and display Unix man pages as HTML.
- Notes the trick of wrapping complex shell commands in "/bin/sh -c \"...\"" to avoid parsing issues with LAUNCH EXTERNAL PROCESS.

## Featured Technology
- LAUNCH EXTERNAL PROCESS (4D language command, new in 4D 2004)
- Mac OS X Unix shell tools (bash, groff, osascript, man)
- Windows DOS/console commands
- 4D 2004 procedural language

## Historical Context
Written for 4D 2004 targeting Mac OS X 10.4 (Tiger) and Windows XP, this note predates 4D's SQL engine (v11, 2007), Project Mode (v17, 2018), and ORDA (2018+) by a wide margin. The LAUNCH EXTERNAL PROCESS command itself has persisted into current 4D versions and the general technique of shelling out to OS utilities remains valid, but the specific target operating systems, utilities (chkdsk, periodic, groff-based man page conversion), and UI conventions shown are long superseded, making the note interesting mainly as a historical reference for how 4D developers first exploited OS-level scripting.

## Status
**Historical interest only** — the featured language command persists, but the OS targets and demonstrated utilities are obsolete.
