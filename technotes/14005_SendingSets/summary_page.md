# Tech Note: Sending Sets

- **Asset ID:** 14005
- **Tech Note #:** 01-22
- **Published:** June 4, 2001
- **Product / Version:** 4D Client 6.7
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=14005
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_21-25_(MAY)/01-22_Sending_Sets.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D, Inc.) shows how sending a Set from one 4D Client to other connected 4D Clients became significantly simpler in 4D 6.7.x thanks to two new commands that eliminate the need for a temporary document, comparing the technique against the more cumbersome approaches required in 4D 6.0.x and 6.5.x.

## Key Points

- Prior to 6.7.x, sending a set required saving it as a document, loading that document into a Blob, transmitting the Blob (via `GET/SET PROCESS VARIABLE` or `Execute on Server` in 6.0.x, or `REGISTER CLIENT`/`EXECUTE ON CLIENT` in 6.5.x), and having the receiving client re-save the Blob as a document before reloading it as a set.
- 4D 6.7.x's `BOOLEAN ARRAY FROM SET` converts a set directly into a Boolean array (one bit per record, with unused trailing bits set False), and `CREATE SET FROM ARRAY` does the reverse — recreating a set from a Boolean array — with no document round-trip required.
- The example uses `VARIABLE TO BLOB` to pack each Boolean array into a Blob, then broadcasts all three (`BlobF`, `BlobG`, `BlobH`) via `EXECUTE ON CLIENT("@";"SERVER_Update_Client_Requested";BlobF;BlobG;BlobH)`, where `"@"` targets every connected client (or a loop over `GET REGISTERED CLIENTS(AClientList;AMethods)` targets specific ones).
- Each 4D Client polls the server for pending method calls (every 2 seconds by default, configurable via the `REGISTER CLIENT` command) and, on receiving `SERVER_Update_Client_Requested`, reconstructs the arrays with `BLOB TO VARIABLE` and recreates interprocess sets, e.g., `CREATE SET FROM ARRAY([People];A_SetF;"<>SetF")`.
- After recreating the sets, `CALL PROCESS(<>CurProcNum)` notifies the client's main process, which checks `On Outside Call` events to recompute dependent selections and redraw its window.
- A toggle ("Disallow updates from others" in the "4D Server" menu) flips a Boolean flag that gates whether incoming set updates are accepted at all.

## Featured Technology

- CREATE SET FROM ARRAY command (4D 6.7.x)
- BOOLEAN ARRAY FROM SET command (4D 6.7.x)
- VARIABLE TO BLOB / BLOB TO VARIABLE serialization
- EXECUTE ON CLIENT for broadcasting to registered 4D Clients
- GET REGISTERED CLIENTS / REGISTER CLIENT
- Interprocess Sets and CALL PROCESS-based UI refresh

## Historical Commentary

**Status:** Partially superseded

The core commands this note demonstrates — `CREATE SET FROM ARRAY`, `BOOLEAN ARRAY FROM SET`, and `EXECUTE ON CLIENT` — remain part of 4D's classic language today, and the document-free set-broadcasting technique described is still fully functional in current 4D client/server deployments. However, most modern multi-client 4D architectures increasingly favor ORDA/REST-based data access and newer synchronization patterns over classic client/server set broadcasting, so while the technique is not obsolete, it has become a less common approach for new development compared to 2001.

**References to newer/updated information:**
- 4D's classic client/server architecture has been supplemented by ORDA and REST-based access, offering different patterns for sharing selections/state across clients
- CREATE SET FROM ARRAY, BOOLEAN ARRAY FROM SET, and EXECUTE ON CLIENT remain part of the current 4D language, unchanged in core behavior since this note
- 4D Server has gained additional built-in interprocess/network communication commands since 2001 that reduce the need for this specific workaround
