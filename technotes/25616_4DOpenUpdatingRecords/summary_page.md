# Tech Note: 4D Open: Updating records

- **Asset ID:** 25616
- **Tech Note #:** 02-60
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=25616
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-60_4D_Open-UpdateRecords.hqx

## Overview

Christian Cypert's third installment in a 4D Open mini-series (following notes on adding and deleting records) walks through updating an existing record on a remote 4D Server from a client application using the 4D Open plug-in, assuming — as in the earlier notes — that the local and remote databases share an identical table/field structure so table numbers can simply be reused. The example maintains scrollable arrays of records fetched from the server, with a parallel al_RecordNums array (built when adding records, per the earlier Tech Note) mapping the row a user clicks (via an al_CompID index) back to the correct remote record number. Updating begins by confirming the selected record index is still within range using OP Records in selection, then calling OP Goto record with the previously established bind ID to position on that record and simultaneously check its lock status; if the record is locked by another user, the code alerts and aborts, otherwise it calls OP Update record to push the current values of the bound local variables (already edited on-screen by the user) up to the server, and finally OP Unload record to release the record so it doesn't remain locked. The note stresses that this update flow is structurally almost identical to the deletion flow from the previous Tech Note, differing only in the final command called once the lock check passes.

## Key Points

- The example assumes identical local and remote table/field structures, so a local `Table(->[Employee])` call can be reused directly as the remote table number in all 4D Open calls.
- Before updating, the code calls `OP Records in selection(vl_ConnectID;$TableNum;$RecInSelection)` to confirm the target record number is still valid for the current remote selection.
- `OP Goto record(vl_ConnectID;$TableNum;$RecNumber;vl_BindID;$LockStatus)` both positions on the target record and reports whether it is currently locked by another user via the returned `$LockStatus`; a locked record triggers an alert and aborts the update.
- If unlocked, `OP Update record(vl_ConnectID;vl_BindID)` pushes the current values of the previously bound local variables (already edited on-screen by the user) up to the record on the server, followed by `OP Unload record(vl_ConnectID;$TableNum)` to release the record so it doesn't remain locked.
- The note explicitly maps a client-side row selection back to a server record number via the `al_RecordNums`/`al_CompID` array pattern introduced in the earlier "Adding records" Tech Note, and notes that this update flow is nearly identical in structure to the deletion flow from the previous note, differing only in the final command called.

## Featured Technology

- 4D Open plug-in remote connection API
- OP Records in selection / OP Goto record for locking and positioning
- OP Update record via a previously established 4D Open bind
- OP Unload record to release a locked remote record
- Record-number array pattern (al_RecordNums / al_CompID) for mapping UI selections to remote records

## Historical Commentary

**Status:** Obsolete

As the third part of a tightly scoped, code-first mini-series on 4D Open, this note clearly documents the lock-check-then-update pattern (OP Goto record for locking, OP Update record to push changes, OP Unload record to release) that was the standard way to modify remote records from a 4D Open client in the early 2000s. The 4D Open plug-in itself has long been discontinued, and its bind/table-number-based client-server model has been superseded by 4D's ORDA remote datastores and REST-based APIs, which expose entity-level CRUD operations and handle locking and structural differences between client and server far more gracefully than this note's identical-structure assumption required. This technique is not usable with current 4D versions.

References to newer/updated information:
- The 4D Open plug-in has been discontinued and its bind/OP-command API is not available in current 4D versions
- ORDA remote datastores and REST APIs have superseded 4D Open for remote record read/update operations, offering entity-based access instead of table-number binds and manual lock checks
