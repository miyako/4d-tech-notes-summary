# Tech Note: 4D Open: Adding records

- **Asset ID:** 25599
- **Tech Note #:** 02-58
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=25599
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-58_4D_Open-Add_Records.hqx

## Overview

This first Tech Note in Christian Cypert's 4D Open series introduces the basics of adding a new record to a remote 4D Server from a client application using the 4D Open plug-in, working from the simplifying assumption that the client and server databases share an identical table/field structure, so a local Table(->[Employee]) call yields the same table number as the equivalent remote table. With a bind already established (via OP Create bind, described as producing vl_BindID) to a small set of local variables — in the example, vs20_EmpLName, vs20_EmpFName, and vl_EmpSalary — the developer simply sets those variables to the desired new values and calls OP New record(vl_ConnectID; vl_BindID), which transfers their current contents to a brand-new record automatically saved on the server. Immediately afterward, OP Get record numbers(vl_ConnectID; $TableNum; al_RecordNums) retrieves an up-to-date array of record numbers for the table, which the note flags as essential groundwork for the deletion and update operations covered in the two follow-up Tech Notes, since later operations need to map a row selected in a client-side array back to its correct remote record number.

## Key Points

- The example assumes identical local and remote table/field structures, so `Table(->[Employee])` on the local database yields the same table number needed for the remote 4D Open calls.
- A bind is presumed already established (via `OP Create bind`, yielding `vl_BindID`) linking a small set of local variables — `vs20_EmpLName`, `vs20_EmpFName`, `vl_EmpSalary` — to the fields of the target remote table.
- Setting those bound variables to the desired values and calling `OP New record(vl_ConnectID;vl_BindID)` transfers their current contents into a brand-new record that 4D Server automatically saves.
- Immediately after creation, `OP Get record numbers(vl_ConnectID;$TableNum;al_RecordNums)` retrieves an up-to-date array of the table's record numbers on the server, needed for later delete/update operations to correctly map a client-side selection back to a specific remote record.
- The note explicitly positions this as groundwork for the following two Tech Notes in the series (deleting and updating records), which reuse the same table-number and record-number-array conventions introduced here.

## Featured Technology

- 4D Open plug-in remote connection API (OP Open connection, OP Create bind)
- OP New record for creating a remote record from bound local variables
- OP Get record numbers for retrieving the resulting server record numbers
- Bound-variable pattern for pushing form field values to a new remote record

## Historical Commentary

**Status:** Obsolete

As the opening note in a three-part 4D Open series, this is a concise, code-focused introduction to remote record creation via bound variables and the OP New record / OP Get record numbers commands — a foundational pattern the next two notes (Deleting and Updating records) build directly on. The 4D Open plug-in has been discontinued for many years, so this exact API is unavailable in current 4D versions; 4D's ORDA remote datastores and REST APIs have long since superseded 4D Open as the standard way to create records on a remote 4D Server, generally with simpler entity-based syntax and without the identical-structure/table-number assumptions this note relies on.

References to newer/updated information:
- The 4D Open plug-in has been discontinued and the OP New record / OP Create bind API described here is unavailable in current 4D versions
- ORDA remote datastores and REST APIs have superseded 4D Open as the standard way to create records on a remote 4D Server
