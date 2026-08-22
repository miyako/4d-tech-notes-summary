# Tech Note 19-21: Error Handling with Call Chains

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** December 3, 2019 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78368
**Download:** https://kb.4d.com/DLTN/TN/2019/19-21_ErrorHandlingWithCallChains.zip

## Proposition
Diagnosing production errors is hard without full context on how execution reached the failing code. This note introduces `Get call chain` (new in v18/v17R6) and shows building a JSON-based error handler and companion log parser that captures the full call stack, error stack, and environment details for every runtime error.

## Key Points
- **`Get call chain`**: returns a collection describing every call-stack frame — `database`, `line`, `name`, and `type` (`projectMethod`, `formObjectMethod`, `databaseMethod`, `triggerMethod`, `executeOnServer`, `executeFormula`) — usable from any 4D environment, including compiled mode with Range Checking enabled.
- **Bottom-up ordering**: the returned collection lists the oldest call at the bottom and the most recent at the top, matching the Debugger's Call Chain area.
- **`GET LAST ERROR STACK`**: captures cascading underlying errors (e.g., a full-disk error causing a subsequent write failure) alongside the call chain.
- **JSON error logging**: a sample error handler combines call chain, error stack, timestamp, 4D/OS usernames, machine name, and standard `Error`/`Error method`/`Error line`/`Error formula` variables into one JSON object saved to `LOGS/errors`.
- **Minimal end-user disclosure**: the alert shown to users only references the log file path, keeping full diagnostic detail server/file-side.
- **Error Log Parser UI**: a companion sample interface browses saved JSON logs, displaying call chain and error stack in dedicated list boxes per selected file.

## Featured Technology
- `Get call chain` (4D v18/v17R6+)
- `GET LAST ERROR STACK`
- JSON Stringify-based structured logging

## Best Practices Highlighted
1. Log full diagnostic detail (call chain, error stack, environment) to disk while showing only a minimal, non-technical message to end users.
2. Avoid attempting to transmit logs to a central server at the exact moment of failure, since the failure itself (e.g., disconnection) may prevent delivery.
3. Periodically ship accumulated error logs off-device (SMTP/FTP/HTTP) rather than relying solely on local storage.

## Context / Positioning
This note showcases one of 4D v18's more developer-facing diagnostic improvements, reflecting a broader trend of 4D strengthening its error-handling and observability tooling as applications grew more complex and multi-component (with components, triggers, formulas, and server-executed code all potentially involved in a single call chain).

## Historical Commentary
**Status:** Still relevant

`Get call chain` remains a current, fully supported 4D command with unchanged core behavior, and the pattern of combining it with `GET LAST ERROR STACK` and structured JSON logging is still standard, recommended practice for building robust error handlers in 4D today. 4D has continued to add error/exception-handling capabilities in more recent versions, but these are additive refinements rather than replacements — this note's technique remains directly applicable to current 4D development.
