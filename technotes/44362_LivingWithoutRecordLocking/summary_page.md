# Tech Note 06-38: Living Without Record Locking

**Author:** David Adams
**Published:** October 6, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44362
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_38-39_(OCT)/06-38_Record_Locking.pdf

## Overview
4D and 4D Client/Server automatically manage record locking at the database engine level, but this note explains that the protection silently disappears in Web-, SOAP-, and array/variable-based record editing scenarios, because 4D's automatic locking depends on a record being held open within a live 4D process — something stateless request-response protocols like Web and SOAP don't have. It then presents a simple, robust alternative: optimistic concurrency via a per-record version/update counter.

## Key Points
- 4D's record locking is fully automatic *only* when standard 4D commands/processes (e.g., forms, `MODIFY SELECTION`) are used; it doesn't extend to array-based, file-based, Web-based, or SOAP-based record editing.
- Root cause: 4D never actually "shows" a record directly — it always hands out a copy for display/editing, and the original stays locked only as long as a specific 4D process holds it open. Stateless Web/SOAP requests have no persistent process to hold that lock.
- Attempting to build a custom artificial-locking system is discouraged: there's no principled answer to how long a record should stay "locked" (a minute? a day?), and it isn't necessary.
- Worked example: a warehouse worker (Web) and a traveling sales rep (SOAP) both pull the same address record; the note walks through exactly how their copies diverge and how a version-counter check resolves the conflict correctly regardless of order or timing.
- Recommended solution: maintain an integer "update/version number" field per table row, incremented on each save, most reliably enforced in a trigger using `On Saving New Record Event` / `On Saving Existing Record Event`, comparing the incoming record's version against `Old([Table]Update_Number)` and rejecting stale saves with a custom trigger error code (range -32,000 to -15,000).
- Alternatives to a simple integer counter (e.g., date-time stamps) are mentioned.
- A sidebar offers tips for developers who still want to experiment with custom process-based record locking (e.g., using `PUSH RECORD` or holding locks via transactions).

## Featured Technology
- 4D / 4D Client-Server automatic record locking
- Database triggers (`Database event`, `On Saving New/Existing Record Event`)
- Optimistic concurrency control via a version/update counter field
- Web, SOAP, and array-based record editing patterns

## Historical Context
Published for 4D 2004, well before 4D's native SQL engine (v11, 2007), Project Mode (v17, 2018), or ORDA (2018+). SOAP was still 4D's primary Web-service integration mechanism at this point, and array/list-box-based UI (4D View, AreaList) was a common way to display bulk data outside of standard forms.

## Historical Commentary
**Status:** Still relevant

The optimistic concurrency pattern this note teaches — a per-record version/update counter validated (and incremented) in a trigger, rejecting saves based on stale data — is a timeless, still-standard technique used broadly across modern databases, ORMs, and APIs today (often called "optimistic locking" or handled via ETag/If-Match headers in REST APIs). While the specific 4D commands referenced (SOAP, `PUSH RECORD`, `Old(...)` in triggers) are era-specific, and the framing around 4D's classic process model predates ORDA's REST-based entity locking mechanisms, the underlying concurrency-control lesson remains directly applicable to 4D and non-4D development alike in 2026.
