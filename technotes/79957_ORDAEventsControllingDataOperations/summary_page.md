# Tech Note 26-03: ORDA Events in 4D: Controlling Data Operations with Event-Driven Logic

**Author:** Abir HSAINI, Technical Services Engineer, 4D Inc.
**Published:** March 23, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79957
**Download:** https://kb.4d.com/TN/2026/26-03_ORDAEvents.zip

## Proposition
Classic 4D triggers operate at the table level, locking the entire table during execution and
forcing all validation/business logic into a single per-table method with one big `Case of`
structure — a poor fit for multi-user performance and maintainability. ORDA events, new in 4D 21,
move this logic into Entity classes at the record level, enabling parallel execution and much
finer-grained, object-oriented control over the full data lifecycle.

## Key Points
- **Seven lifecycle events.** `touched` (in-memory change), `validateSave`/`saving`/`afterSave`
  (around save), and `validateDrop`/`dropping`/`afterDrop` (around delete) cover the complete
  entity lifecycle, each with a defined execution point, location (client/server), and whether it
  can abort the action.
- **Entity- vs. attribute-level scoping.** Events can be defined at the entity level (all
  attributes) or on a specific attribute, including computed attributes; when both exist, the
  attribute-level version runs first.
- **`touched` is unique to ORDA.** It fires on any in-memory modification — user typing in a form,
  `:=` assignment (even self-assignment), entity received from client, or a REST API update — and
  has no classic-trigger equivalent; it cannot stop the action, only reformat/derive data.
- **`validateSave`/`saving`/`validateDrop`/`dropping` can block the operation.** Returning an error
  object (e.g. `{errCode: 1001; message: "Margin below minimum 50%"; seriousError: False}`) halts
  the save or delete with rich, structured error detail — unlike classic triggers' bare integer
  codes.
- **`afterSave`/`afterDrop` are entity-level only and cannot re-trigger the action.** Calling
  `save()` on `This` inside `afterSave` raises an error specifically to prevent infinite loops.
- **Record-level locking enables concurrency.** Multiple ORDA events can execute simultaneously on
  different entities, unlike classic triggers, which serialize on a single table lock.
- **Classic triggers and ORDA events are not interchangeable.** `SAVE RECORD`/`DELETE RECORD` fire
  only classic triggers, never ORDA events; conversely `entity.save()`/`entity.drop()` fire ORDA
  events *and* any existing classic triggers.
- **Guided migration path.** The note walks through converting a real order-management system's
  `Client_Trigger`, `Product_Trigger`, and `Order_Trigger` methods into ORDA events, including
  automatic stock management and price calculation, validated with four test cases (valid order,
  insufficient stock, low-stock warning, empty order rejection).

## Featured Technology
- **ORDA Entity classes** — home for all seven event function definitions.
- **`Function event <name>` syntax** — entity- and attribute-level event declarations
  (`Function event touched`, `Function event validateSave <attribute>`, etc.).
- **`local` keyword** — controls whether `touched` executes client-side or server-side.
- **Error objects** (`errCode`, `message`, `seriousError`) — structured validation failures
  returned from `validateSave`/`validateDrop`/`saving`/`dropping`.
- **Classic 4D triggers** — the legacy table-level mechanism ORDA events are positioned to replace.

## Best Practices Highlighted
1. *Move business logic into Entity classes* — centralizing validation/business rules there makes
   them easier to find, test, and maintain than a single per-table trigger method.
2. *Use attribute-level events for targeted logic* — scope validation/formatting to the specific
   attribute it concerns rather than re-checking the whole entity.
3. *Return rich error objects, not bare codes* — give callers actionable detail (code, message,
   severity) when blocking a save or delete.
4. *Don't rely on classic-command paths to fire ORDA events* — remember `SAVE RECORD`/`DELETE
   RECORD` bypass ORDA events entirely; use `entity.save()`/`entity.drop()` for full lifecycle
   coverage.

## Context / Positioning
Published under 4D v21 (2026), this note continues 4D's multi-year push to modernize its data
layer around ORDA's object-oriented model, extending it from data access into data *behavior* —
replacing one of the last major classic-mode-only mechanisms (triggers) with a concurrency-friendly,
class-based equivalent, consistent with the same release cycle's broader emphasis on ORDA-native
tooling (sort interfaces, AI Kit integration) over classic-mode workarounds.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
