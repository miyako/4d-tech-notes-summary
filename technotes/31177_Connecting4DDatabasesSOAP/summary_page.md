# Tech Note: Connecting 4D Databases through SOAP

- **Asset ID:** 31177
- **Tech Note #:** 04-02
- **Published:** January 31, 2004
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon, QA Manager, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=31177
- **Download:** https://kb.4d.com/ftp://@ftp.4d.com/ACI_TECHNICAL_NOTES/2004/MacOS/TN_2004_01-04_(JAN)/04-02_Connecting_4D_w_SOAP.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D, Inc.) shows how to use 4th Dimension 2003's brand-new native SOAP support to build a generic Web-services bridge that lets one 4D database (the "Client") remotely drive records, sets, and named selections on another 4D database (the "Server"), positioned as an alternative to the 4D Open for 4D plug-in that avoids its permanent, timeout-sensitive TCP connection.

## Key Points

- Each client session opens a persistent server-side process via the `s44D_NewConnection` Web service, which returns a session/connection ID that must be included on every subsequent SOAP call.
- The server process (`s44D_NewProcess`) is structured as a large `Case of` statement inside a loop; it pauses to avoid consuming CPU, and is woken by `SET VARIABLE PROCESS`/`VARIABLE TO VARIABLE` commands that poke a `CodeAction` variable telling it which action to perform before it pauses again.
- Roughly 30 `s44D_*` Web services are documented, each mapping directly to a native 4D command: record navigation (`s44D_FirstRecord`, `s44D_LastRecord`, `s44D_GotoSelectedRecord`), CRUD (`s44D_CreateRecord`... via `SAVE RECORD`/`DELETE RECORD`/`DELETE SELECTION`), set operations (`s44D_CreateSet`, `s44D_CopySet`, `s44D_Difference`, `s44D_Intersection`, `s44D_IsInSet`), named selections (`s44D_UsenamedSelection`, `s44D_CutNamedselection`, `s44D_CopyNamedselection`, `s44D_ClearNamedSelection`), and structural introspection (`s44D_GetAllTableNames`, `s44D_GetTableProperties`, `s44D_CountTables`, `s44D_FlushBuffers`) — the last group bypasses the process entirely since they don't need session state.
- `s44D_ArrayToSelection` demonstrates transferring bulk data by packing multiple 4D arrays into a single blob parameter and reconstructing them server-side with `ARRAY TO SELECTION`, noting the technique doesn't support every array type.
- On the client side, 4D auto-generates proxy project methods (e.g. `proxy_s44D_NewConnection`, `proxy_s44D_AllRecords`) by analyzing the server's WSDL, so calling a remote operation looks just like calling a local method.
- The author explicitly warns that these server-side processes never time out by themselves — developers must implement their own idle-session cleanup using a timestamp per session and a background process that periodically checks and force-closes stale connections.
- Explicitly framed as "another possible alternative," not a replacement, to the existing 4D Open for 4D plug-in-based approach to inter-database connectivity.

## Featured Technology

- 4D 2003 native SOAP support
- WSDL-generated proxy methods
- SET VARIABLE PROCESS / VARIABLE TO VARIABLE inter-process messaging
- Session-based connection IDs (s44D_NewConnection / s44D_CloseConnection)
- ADD TO SET, USE NAMED SELECTION, and other 4D Open-style server commands wrapped as Web services
- ARRAY TO SELECTION over a blob-encoded array payload

## Historical Commentary

**Status:** Superseded

This note presents a full generic "s44D_*" library of SOAP Web services (New/CloseConnection, AllRecords, sets, named selections, record CRUD, etc.) that recreates the behavior of the 4D Open for 4D plug-in using only 4D 2003's brand-new native SOAP support, keeping a live server-side process alive per session via a paused-loop/CodeAction dispatch pattern. It is an ambitious, well-engineered example of stateful client/server database access over Web services for its time, but the entire architecture (per-session paused processes, SOAP proxies generated from WSDL, manual set/named-selection plumbing) has been superseded by 4D's modern remote-datastore and ORDA client/server architecture, which provides equivalent multi-database record access natively and far more simply. The concept of one 4D database calling into another over a standard protocol remains current, just through REST/ORDA rather than hand-rolled SOAP session management.

**References to newer/updated information:**
- 4D's ORDA and remote datastore architecture (introduced from v16/v17, 2018+) now provides built-in client/server data access between 4D applications, replacing the need for a hand-built SOAP session/process framework like this one
- 4D's Web Services capabilities have broadly moved toward REST/JSON, with SOAP now a legacy, less-emphasized integration path
- The 4D Open for 4D plug-in referenced as the inspiration for this technique has itself been long discontinued
