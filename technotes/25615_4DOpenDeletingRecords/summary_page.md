# Tech Note: 4D Open: Deleting records

- **Asset ID:** 25615
- **Tech Note #:** 02-59
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=25615
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-59_4D_Open-Del_Records.hqx

## Overview

In this second entry of his 4D Open mini-series, Christian Cypert explains how to delete a record on a remote 4D Server from a client application using the 4D Open plug-in, again assuming identical local and remote table/field structures so a local Table() lookup can be reused as the remote table number. Building on the previous Tech Note's al_RecordNums array (populated when records were added), a user's click on a row in a scrollable display area is translated via an al_CompID index into the correct remote record number. The deletion code first calls OP Records in selection to confirm the record number is still valid for the current selection, then OP Goto record — passing the connection ID, table number, record number, and bind ID — to both position on that record and determine whether it is currently locked by another user; if $LockStatus comes back 1, the code alerts the user that the record is locked, and otherwise proceeds to call the two-parameter OP Delete record (connection ID and table number) to remove it from the server. The note closes by noting how closely this mirrors record updates, which follow the identical lock-check pattern but call OP Update record instead of OP Delete record.

## Key Points

- The example assumes identical local and remote table/field structures, so a local `Table(->[Employee])` call can be reused directly as the remote table number for the `OP` commands.
- A client-side row selection is mapped to the correct remote record number via the `al_RecordNums`/`al_CompID` array pattern established in the earlier "Adding records" Tech Note in the same series.
- `OP Records in selection` first confirms the record number is still valid for the current remote selection before any deletion is attempted.
- `OP Goto record(vl_ConnectID;$TableNum;$RecNumber;vl_BindID;$LockStatus)` positions on the target record and reports its lock status; if `$LockStatus=1` the code alerts the user rather than attempting the delete.
- If the record is unlocked, the two-parameter `OP Delete record(vl_ConnectID;$TableNum)` removes it from the server, and the note explicitly notes that this lock-check-then-act structure is nearly identical to the record-update flow covered in the next Tech Note in the series.

## Featured Technology

- 4D Open plug-in remote connection API
- OP Records in selection / OP Goto record for locking and positioning
- OP Delete record for removing a remote record
- Record-number array pattern (al_RecordNums / al_CompID) for mapping UI selections to remote records

## Historical Commentary

**Status:** Obsolete

This note documents the standard lock-check-then-delete pattern for the 4D Open plug-in in a clear, minimal example, forming a natural pair with the companion Adding and Updating records notes in the same series. The 4D Open plug-in has been discontinued for many years, so the specific OP Goto record / OP Delete record API shown here cannot be used with any current 4D version; 4D's ORDA remote datastores and REST APIs now provide equivalent (and considerably more capable) remote record-deletion functionality without requiring identical client/server table structures or manual bind/lock bookkeeping.

References to newer/updated information:
- The 4D Open plug-in has been discontinued and its OP Delete record / OP Goto record API is not available in current 4D versions
- ORDA remote datastores and REST APIs have superseded 4D Open for remote record deletion, without requiring identical client/server table structures
