# Tech Note 15-06: An Alternate Technique to Display Records

**Author:** Tai BUI, Technical Services Engineer, 4D Inc.
**Published:** March 18, 2015 | **Product/Version:** 4D v14 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77262
**Download:** https://kb.4d.com/DLTN/TN/2015/15-06_AlternativeRecDisplay.zip

## Proposition
This Tech Note proposes an alternative to 4D's standard Output/Input form pairing: a single two-page form where a list box replaces the Output form and a Tab Control plus hand-managed 4D Object containers replace the Input form, letting users open several records at once in tabs without the record, table, or process becoming locked.

## Key Points
- **Problem addressed:** standard Input forms lock the current record/process for as long as a record is open, preventing a user from viewing/editing multiple records concurrently in one process.
- **Core mechanism:** a Tab Control bound to a text array drives tabs; tab 1 is the list (Output-like) page, and each additional tab represents one open record.
- **Record container pattern:** each open record is represented by a 4D Object with metadata properties plus a nested object array holding one entry per field (name/type/value), built with `OB Get`/`OB SET ARRAY`.
- **Read-only browsing:** records are loaded with `READ ONLY`, so simply opening/viewing a record in a tab never places a lock; a lock is only acquired transiently around an explicit save (`READ WRITE` ... `SAVE RECORD` ... `READ ONLY`).
- **Helper methods:** `OB_REC_CONTAINER`, `OB_REC_SAVE`, `OB_WRITE`, `OB_SET_VARIABLE`, and `OpenInput` orchestrate building the container, populating form variables, and writing values back to the record.
- **New/unsaved records:** the technique also supports multiple new/unsaved record tabs simultaneously (tracked via "New", "New1", "New2"... placeholders in the tab array).
- **Sample database included** demonstrating the full tabbed, non-locking interface end to end.

## Featured Technology
- List Box
- Tab Control
- 4D Objects (C_OBJECT/ARRAY OBJECT)
- OB Get/OB SET
- Object arrays

## Best Practices Highlighted
1. Keep tables in `READ ONLY` mode except during the brief window needed to save, to minimize lock contention.
2. Represent in-memory record state as a generic object container rather than binding directly to fields, so multiple records can coexist per process.
3. Reuse one form with pages/tabs instead of opening one window per record to avoid workspace clutter.

## Context / Positioning
Published in early 2015 for 4D v14 R4, this note reflects classic Design-Mode 4D: binary structure files, table Input/Output forms, and pointer-based commands (`GOTO RECORD`, `SAVE RECORD`, `Locked`). List boxes and 4D Objects (introduced around v13/v14) were the cutting-edge tools of the day for building richer, non-modal UIs before ORDA or Project Mode existed.

## Historical Commentary
**Status:** Partially Superseded

The specific workaround — manually simulating a lock-free multi-record UI with object arrays — solved a real pain point (pessimistic record locking) that 4D later addressed architecturally.

With ORDA (v16 R5+, 2017) and its entity/entity selection model, records are naturally read without locking a process, and optimistic locking is opt-in per save, making this kind of hand-rolled object-container workaround largely unnecessary in modern (Project Mode/ORDA) 4D applications. The UI pattern (tabbed multi-record editing) remains valid, but the underlying plumbing would now be built with classes and entities rather than raw object arrays and `OB Get`.
