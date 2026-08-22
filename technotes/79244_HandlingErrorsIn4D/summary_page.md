# Tech Note 23-13: Handling Errors in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 24, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79244
**Download:** https://kb.4d.com/DLTN/TN/2023/23-13_Handling4DErrors.zip

## Proposition
4D's default error handler shows a detailed but developer-oriented blocking dialog that end users may not know how to act on or report correctly. This note explains how to replace that default behavior with a custom error handler tailored to both troubleshooting needs and end-user experience, especially in deployed applications.

## Key Points
- **Default error dialog anatomy:** title/type, line number and summary, offending code snippet, Edit/Trace/Continue/Abort buttons, and an expandable details section with the error call stack (most recent at top) plus Save/Copy export.
- **ON ERR CALL installs a handler:** a project method name is passed as a string to become the process's error handler; passing an empty string uninstalls it and restores the default handler.
- **New scoping in v19R8/v20:** an optional second parameter accepts `ek local` (default, current process), `ek global` (entire database), or `ek errors from components` (catches component errors from the host), with local handlers taking precedence over global ones.
- **Method called on error** retrieves the name of the currently installed handler for a given scope, useful for temporarily swapping handlers and restoring the previous one.
- **System variables on trigger:** `Error`, `Error method`, `Error line`, and `Error formula` are automatically populated process variables available inside the handler.
- **Richer diagnostics via new commands:** `Last errors` returns a collection of objects (`errCode`, `message`, `componentSignature`) replacing the older array-based `GET LAST ERROR STACK`; `Get call chain` returns the ordered method call chain; `Get system info` returns OS/hardware details.
- **Expected vs. unexpected errors:** expected errors (e.g., DELETE FOLDER's -47 "not empty" or -120 "not found") should be handled inline with conditional logic; unexpected errors need generic information-gathering and safe recovery (often recommending a restart).
- **Information delivery strategies:** save a text file and instruct the user to send it, auto-generate and email details programmatically, or log errors to a dedicated database table — trading off user involvement vs. automation.

## Featured Technology
- **ON ERR CALL** — installs/uninstalls a process-, database-, or component-scoped custom error handler.
- **Method called on error** — inspects which handler is currently active for a scope.
- **Last errors** — modern object-collection based error stack accessor (v19R8/v20).
- **GET LAST ERROR STACK** — legacy three-array error stack accessor.
- **Get call chain** — returns the calling method chain leading to the error.
- **Get system info** — returns OS/hardware environmental details for diagnostics.

## Best Practices Highlighted
1. Prefer the global error-handler scope for a catch-all safety net, and use local handlers only where specific behavior is needed, since local takes precedence over global.
2. Avoid infinite recursion by ensuring the handler method itself cannot trigger the same error it is meant to catch.
3. For unexpected errors, err on the side of a safe recovery path (e.g., recommend restarting the app) rather than silently continuing and risking data loss.
4. Use object-based `Last errors` and `Get call chain` instead of the legacy array commands for simpler, more maintainable diagnostic code.

## Context / Positioning
Published alongside 4D v20, this note reflects 4D's ongoing move toward object/collection-based APIs (replacing array-heavy legacy commands) and toward giving developers finer-grained control (error handler scopes) as databases and component ecosystems grow more complex. It complements 4D's broader deployment-readiness guidance for production applications.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
