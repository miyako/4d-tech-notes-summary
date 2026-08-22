# Tech Note 18-22: 4D Record Locking and ORDA Entity Locking

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** December 28, 2018 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78176
**Download:** https://kb.4d.com/DLTN/TN/2018/18-22_4DLockingTypes.zip

## Proposition
Multi-user 4D databases need a way to prevent record conflicts. This note contrasts 4D's traditional pessimistic record locking with the pessimistic *and* optimistic locking options newly introduced with ORDA entities in v17, so developers can choose the right mechanism for their app's conflict profile.

## Key Points
- **Classic locking is table-state driven:** each table per process is read-only or read/write (`READ ONLY`/`READ WRITE`); loading a record via `QUERY`, `NEXT RECORD`, etc. locks it until `UNLOAD RECORD`.
- **Checking lock state:** `Locked` returns whether the current record is locked; `LOCKED BY` and `Get locked records info` provide details on who/what holds the lock.
- **Standard pattern:** `READ WRITE([Table])` → `MODIFY RECORD` → `UNLOAD RECORD` → `READ ONLY([Table])` to safely load, edit, and release a record.
- **ORDA introduces entity stamps:** each entity carries a version stamp used to detect concurrent modification, underpinning ORDA's optimistic locking model.
- **Pessimistic ORDA locking:** `entity.lock()`/`entity.unlock()` explicitly reserve an entity for exclusive modification, similar in spirit to classic locking.
- **Optimistic ORDA locking (default):** a plain `entity.save()` fails if the entity's stamp changed since it was loaded, signaling a conflicting concurrent edit.
- **Optimistic locking with auto-merge:** `entity.save(dk auto merge)` merges non-conflicting attribute changes automatically instead of failing outright.
- **Choosing a strategy:** pessimistic locking suits high-conflict/high-contention records; optimistic (stamp-based) locking suits low-conflict, high-concurrency scenarios.

## Featured Technology
- Classic 4D locking commands (`READ ONLY`, `READ WRITE`, `Locked`, `LOCKED BY`, `Get locked records info`, `MODIFY RECORD`, `UNLOAD RECORD`)
- ORDA entities and entity stamps
- `entity.lock()` / `entity.unlock()`
- `entity.save()` and `entity.save(dk auto merge)`

## Best Practices Highlighted
1. Always pair `READ WRITE`/lock acquisition with a corresponding `UNLOAD RECORD`/`entity.unlock()` to avoid leaving records locked indefinitely.
2. Use `Locked`/stamp checks proactively in conditional logic rather than only handling failures after the fact.
3. Prefer optimistic (stamp-based) locking for scenarios with many concurrent users and low chance of simultaneous edits to the same record; reserve pessimistic locking for high-contention data.

## Context / Positioning
Published just as ORDA was maturing in 4D v17, this note helped developers reconcile two coexisting data-access paradigms — classic table/record-based 4D commands and the new object/entity-based ORDA layer — by clarifying that ORDA didn't replace classic locking outright but added a modern, stamp-based alternative suited to REST/entity-selection-driven apps.

## Historical Commentary
**Status:** Still relevant

Both locking mechanisms described remain fully current in 4D today. Classic pessimistic record locking (`READ ONLY`/`READ WRITE`, `Locked`, `LOCKED BY`, `Get locked records info`) is unchanged and still used in non-ORDA or hybrid 4D code. ORDA entity locking — `entity.lock()`/`entity.unlock()`, stamp-based optimistic `entity.save()`, and `entity.save(dk auto merge)` — is the standard, still-current approach for ORDA-based data access, and 4D has continued to build on this locking model in subsequent releases with additional save options and conflict-handling refinements.

Developers today can still rely on this note's core guidance largely as written; it remains a good conceptual introduction to the tradeoffs between pessimistic and optimistic locking in 4D, though newer 4D documentation should be checked for any additional `save()` flags added since v17.
