# Tech Note 25-09: Error Management and Logging in 4D Applications

**Author:** Karim Meghraoui Technical Support Engineer, 4D Morocco.
**Published:** September 29, 2025 | **Product/Version:** 4D v20 R9 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79831
**Download:** https://kb.4d.com/TN/2025/25-09_ErrorManagement.zip

## Proposition
By default, 4D errors trigger a blocking system dialog exposing technical details and forcing
manual intervention (Abort/Continue/Trace/Edit) — interrupting the user, with no automatic
recovery or logging. This note explains how to replace that experience with both the traditional
`ON ERR CALL` mechanism and 4D's newer `throw`/`Try`/`Try...Catch` primitives, to build stable,
diagnosable applications.

## Key Points
- **Three `ON ERR CALL` scopes with a strict hierarchy.** Local (`ek local`, highest priority,
  scoped to one code block) → component (`ek errors from components`, catches only
  component-unhandled errors) → global (`ek global`, typically installed in `On Startup`) → the
  default system dialog if nothing else is installed.
- **Always save and restore the previous handler.** `Method called on error` captures the
  currently active handler name before installing a temporary local one (e.g. around file I/O),
  so `ON ERR CALL($previousErrorHandler)` can cleanly restore it afterward.
- **Enrich and persist captured errors.** A handler method reads `Last errors`, adds context
  (`Error method`, `Error line`, `Error formula`, timestamp, app/OS version) to the most recent
  error, and appends the record to a JSON log file (`errors.json`) for later analysis.
- **`throw(code; message)` for simple immediate errors.** Raises an error that either an active
  `ON ERR CALL` handler intercepts, or the standard error dialog displays with the custom code and
  message.
- **`throw(errorObj)` for rich, localizable errors.** Supports `componentSignature`, `errCode`,
  `message` (with automatic XLIFF fallback lookup as `ERR_{componentSignature}_{errCode}`), and a
  `deferred` flag that postpones delivery to the end of the method/Try block — useful for
  components to batch multiple errors for the host application.
- **`Try(expression)` for non-blocking single operations (4D 20 R4).** Returns `Null` on failure
  and records the failure in `Last errors`, without stopping execution or requiring a handler.
- **`Try...Catch...End try` for structured multi-statement recovery (4D 20 R5).** Wraps code in a
  Try block; any thrown error jumps directly to the paired Catch block, where `Last errors`
  retrieves the specific error — nested Try/Catch blocks are supported for handling multiple
  distinct errors in sequence.
- **`Last errors` is the shared foundation.** Both the classic `ON ERR CALL` handler and the
  modern `Try`/`Try...Catch` constructs rely on the same `Last errors` collection to expose
  `errCode`, `message`, and `componentSignature` for each captured error.

## Featured Technology
- **`ON ERR CALL`** — classic scoped error-handler installation (local/global/component).
- **`throw(code; message)` / `throw(errorObj)`** — immediate and rich structured error raising.
- **`Try(expression)`** — single-expression non-blocking error trapping (4D 20 R4).
- **`Try / Catch / End try`** — structured, block-based exception handling (4D 20 R5).
- **`Last errors`** — canonical error-stack retrieval used by both classic and modern approaches.
- **`Method called on error` / `LOG EVENT`** — handler introspection and diagnostic logging.

## Best Practices Highlighted
1. *Always restore the previous error handler* — save it via `Method called on error` before
   installing a temporary local one, to avoid disrupting the rest of the application.
2. *Install a global handler at `On Startup`* — ensures error handling is active from the very
   start of the application's execution.
3. *Log enriched error context, not just the raw message* — capture method, line, formula,
   timestamp, and version alongside the error for effective post-mortem diagnosis.
4. *Prefer `Try`/`Try...Catch` for new code* — the block-based structure is clearer and more
   robust than manually saving/restoring `ON ERR CALL` handlers around sensitive operations.

## Context / Positioning
Published under 4D v20 R9 (2025), this note bridges 4D's long-standing `ON ERR CALL` error model
with the more modern, block-structured `Try`/`Try...Catch` additions introduced in 20 R4/R5,
reflecting the platform's ongoing effort to bring its exception-handling ergonomics closer to
contemporary language conventions while remaining backward compatible with existing handler-based
code.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
