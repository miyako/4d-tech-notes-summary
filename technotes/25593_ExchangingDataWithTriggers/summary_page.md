# Tech Note: Exchanging Data with Triggers

- **Asset ID:** 25593
- **Tech Note #:** 02-52
- **Published:** November 30, 2002
- **Product / Version:** 4D 6.8.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=25593
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_51-55_(NOV)/02-52_Exchanging_Data.hqx

## Overview

David Adams explains why code that shares process variables between a triggering action and its trigger works fine under single-user 4D but breaks under 4D Client/Server -- because triggers execute on the server machine while the client action runs on the client machine, and process variables aren't shared across machines. Using a hypothetical library-lending system where a librarian's ID is stored in an interprocess variable during login, he shows how a `GetCurrentUser` function called from a trigger either errors or silently returns 0 under Client/Server. He argues that 4D's built-in cross-process variable commands (GET PROCESS VARIABLE, SET PROCESS VARIABLE, VARIABLE TO VARIABLE) are a fragile fix because they require semaphore-guarded access and behave differently under compiled vs. interpreted server code, and don't help for non-4D-variable clients like 4D Open or Web processes at all. His solution is a `[TriggerMessage]` utility table with a single Message_ field: the client loads/updates the record before triggering an action, and the trigger code reads the same record (since client and trigger share records even though they don't share variables), via a small set of reusable subroutines.

## Key Points

- Diagnoses the root cause: under 4D Server, trigger code executes in a process on the server machine, not the client machine, so the interprocess variable holding the current librarian's ID (set during a custom login) is invisible to the trigger's `GetCurrentUser` function, causing errors or wrong results that don't manifest in single-user testing.
- Rejects GET PROCESS VARIABLE/SET PROCESS VARIABLE/VARIABLE TO VARIABLE as the fix, citing three problems: they require semaphore-guarded access that's easy to get wrong, compiled server code shares one process-variable collection across all triggers while interpreted code gives each trigger a full separate collection, and non-4D clients (4D Open, Web processes, stored procedures) have no 4D variables to exchange at all.
- Proposes a `[TriggerMessage]` utility table with a `Message_` field and a `RecordInUse` flag: the client process loads/creates an available record via `TriggerMessage_Load` (querying `RecordInUse=False`, creating a fresh record if none is free or the found one is locked), updates it via `TriggerMessage_Update` (prepending the new value with a carriage return), and the trigger reads it back via `TriggerMessage_GetMessage`, with `TriggerMessage_Unload` releasing the record when done.
- Rewrites `GetCurrentUser` to read `Num(TriggerMessage_GetMessage)` instead of the process variable, working identically for compiled and interpreted 4D and 4D Server.
- Suggests extensions for more complex needs: multiple fields for different message types, avoiding type conversions with multiple field types, packing values into a BLOB field for arbitrary-type messages, or using an ObjectTools object in a BLOB field for custom data types.
- Lists common uses beyond the library example: sending pseudo-parameters or state values from the client, sending structured data, and returning detailed error descriptions back out of a trigger.

## Featured Technology

- 4D Server triggers (client/server execution model)
- GET PROCESS VARIABLE / SET PROCESS VARIABLE / VARIABLE TO VARIABLE (rejected approach)
- [TriggerMessage] utility record pattern
- QUERY / LOAD RECORD / SAVE RECORD / UNLOAD RECORD
- Cross-machine data sharing between client and trigger code

## Historical Commentary

**Status:** still_relevant

David Adams addresses a specific 4D Client/Server pitfall: because triggers execute on the server machine while the client action that provoked them runs on the client machine, they do not share process variables, so patterns that work fine in single-user 4D silently break under Client/Server. Rather than using GET PROCESS VARIABLE/SET PROCESS VARIABLE/VARIABLE TO VARIABLE (which he argues is needlessly fragile across compiled vs. interpreted server code and doesn't work for non-4D clients like 4D Open or Web processes), he proposes storing shared data in a dedicated [TriggerMessage] utility record that both the client process and the server-side trigger can read/write since they share the same records. 4D's trigger mechanism itself remains fully supported today, so this utility-record data-sharing pattern is still valid, though modern 4D also offers object/collection-based session variables that can provide a more structured alternative for some of these use cases.

References to newer/updated information:
- 4D triggers remain a fully supported feature in current 4D with the same client/server execution model described in this note
- Modern 4D also offers object/collection-based session and process variables that provide additional, more structured ways to pass context data beyond the utility-record technique shown here
