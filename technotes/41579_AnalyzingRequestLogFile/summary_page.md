# Tech Note 06-04: Analyzing the Request Log file

**Author:** Jean-Yves Fock-Hoon
**Published:** January 27, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41579
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_01-04_(JAN)/06-04_Analyzing_Request_Log.zip

## Overview
A follow-up to TN 06-03, this note uses 4D Server's request log file as a profiling tool to compare, request by request, the network cost (bytes in/out, duration) of several common 4D Client/Server programming patterns, since request volume and network latency are frequently the limiting factor on client performance.

## Key Points
- **Example 1 (browsing):** compares a While/End selection loop, a For loop with NEXT RECORD, and a For loop with GOTO SELECTED RECORD — the first two are request-equivalent, while GOTO SELECTED RECORD triggers two extra requests because ALL RECORDS already loads the first record.
- **Example 3 (batch modification):** shows the Rec_load/Rec_Save/Rec_Unload request cycle generated when modifying and saving 8 records in a loop.
- **Examples 4–6 (transactions, sorting, searching):** extend the same request-log analysis technique to transactional updates, selection sorting, and searching.
- **Example 7 (variable transfer):** compares GET PROCESS VARIABLE for string arrays vs. text arrays, showing string arrays transfer significantly more bytes — relevant when passing arrays to stored procedures via BLOB parameters.
- **Example 8 (semaphores):** analyzes a classic Execute on server + DELAY PROCESS + busy-wait IDLE/Test semaphore pattern, revealing thousands of granular polling requests in the log.
- Frames the request log as a black-box, data-driven performance profiling tool rather than relying on assumptions about internal 4D behavior.

## Featured Technology
- 4D Server request log file (enabled via `SET DATABASE PARAMETER` ID 28)
- Client/Server request pattern analysis (Rec_load, Rec_Save, Sel_AllRecords, Proc_GetProcessVar, Sem_Set, etc.)
- NEXT RECORD / GOTO SELECTED RECORD / GOTO RECORD / SELECTION TO ARRAY
- Stored procedures (Execute on server), semaphores, GET PROCESS VARIABLE

## Historical Context
Published in January 2006 for 4D 2004, this note reflects the architecture of a 4D Client/Server deployment where minimizing chatty network round-trips was a first-order performance concern, well before 4D's native SQL engine (v11, 2007), Project Mode, or ORDA existed. The specific request-log format and request names are tied to this generation of 4D Server, but the underlying discipline — profiling actual network requests to choose between functionally equivalent coding patterns — remains a valid and still-applicable performance methodology for any 4D Client/Server application today.

## Status
**Still relevant** — the request-log profiling methodology and client/server performance concerns remain applicable, though the exact log format and request names are specific to this generation of 4D Server.
