# Tech Note 09-33: Triggers in 4D v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** August 20, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75876
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_31-35_(AUG)/09-33_Triggers.zip

## Proposition
This Tech Note explains 4D's table-level trigger mechanism — methods that automatically fire on save/delete database events regardless of how the record change originated (form, web, ODBC, SQL, import) — and demonstrates common uses via a sample database.

## Key Points
- A trigger is a method attached to exactly one table, fired on three events: On Saving New Record, On Saving an Existing Record, and On Deleting Record (return codes 1/2/3 via the `Database event` system variable).
- Triggers fire consistently no matter the data-entry path: 4D forms, Plugins, Web connections, ODBC, SQL Pass-through, IMPORT DATA, or RECEIVE RECORD — `TRUNCATE TABLE` is the one exception that bypasses them.
- **Major v11 improvement:** triggers on different (non-cascading) tables now execute in parallel/concurrently, versus strictly serial execution in prior versions.
- Triggers always execute on the machine hosting the database engine (the single-user machine, or the 4D Server in client/server mode) — meaning alerts/dialogs from a trigger appear on the server, not the client, in remote mode.
- Triggers have their own private table of process variables and cannot see the invoking process's variables directly; `VARIABLE TO VARIABLE` (combined with an "Execute on server" method) is used to pass values like an SSN from client to server-side trigger.
- Cascading triggers (a trigger's action invoking another table's trigger) are tracked via trigger execution "levels," inspectable with `Trigger Level` and `TRIGGER PROPERTIES` to avoid infinite loops.
- Triggers return error codes like functions; custom error codes (recommended range -32000 to -15000) combined with an `ON ERR CALL` handler on the client let errors be surfaced gracefully instead of alerting on the server machine.

## Featured Technology
- 4D table triggers (On Saving New/Existing Record, On Deleting Record events)
- Parallel/concurrent trigger execution (new in 4D v11)
- Cascading triggers, `TRIGGER LEVEL` and `TRIGGER PROPERTIES` commands
- `VARIABLE TO VARIABLE` / `GET PROCESS VARIABLES` / `SET PROCESS VARIABLES`
- "Execute on server" method property

## Best Practices Highlighted
1. Use triggers, not form-level code, to guarantee data rules are enforced no matter how a record is modified (SQL, ODBC, web, etc.).
2. Install an `ON ERR CALL` handler on the client before calling `SAVE RECORD`/`DELETE RECORD`, since trigger-originated alerts would otherwise appear on the server machine in remote mode.
3. Limit cascading trigger depth and check `TRIGGER LEVEL`/`TRIGGER PROPERTIES` to prevent runaway or infinite trigger chains.
4. Keep trigger code short and fast, even though v11's concurrency reduces (but doesn't eliminate) the performance cost of frequent trigger execution.

## Context/Positioning
Published to explain a foundational (if pre-existing) 4D mechanism in the context of 4D v11 SQL's newly parallelized trigger execution model, emphasizing data-integrity enforcement across the many new client access paths (SQL, ODBC) that v11 SQL introduced.

## Historical Commentary
**Status:** Still Relevant

This note documents 4D's classic table-level trigger mechanism, which fires uniformly regardless of whether records are modified via the 4D language, forms, SQL, ODBC, or the web — a design that has proven durable. Triggers remain a core, actively supported part of 4D today and are still the recommended place to enforce table-level data integrity.

ORDA (4D v16 R5+, 2017) later added complementary entity-level datastore class events (e.g. onSaving, onDeleting) for object-oriented and REST-driven data access, but classic triggers were not replaced — they continue to work exactly as described here, including the parallel-execution behavior and process-variable isolation this note explains.
