# Tech Note 19-06: Engaging Database Tests in your 4D Database

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** April 24, 2019 | **Product/Version:** 4D v17 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78245
**Download:** https://kb.4d.com/DLTN/TN/2019/19-06_EngagingDatabaseTests.pdf

## Proposition
Automating unit/functional testing of a 4D database across launch modes previously required ad hoc marker files. This note explains v17R3's new "User parameter" (`SET/GET DATABASE PARAMETER`), a persistent, settable value usable from code, the command line, or a `.4DLink` file to drive automated test scenarios at startup.

## Key Points
- **`SET DATABASE PARAMETER(User param value; ...)`** accepts either plain text or a JSON-stringified 4D object.
- **Persists across restarts:** the value survives `OPEN DATABASE`, `OPEN DATA FILE`, and `RESTART 4D` calls (but not a full application shutdown).
- **Command-line entry:** `--user-param <text or JSON-like text>`, usable when launching 4D directly (with platform-specific quoting differences).
- **`.4DLink` file entry:** a `user_param="..."` XML attribute lets client connections carry the same parameter, openable directly via command line.
- **Retrieval:** `GET DATABASE PARAMETER(User param value; $userParam)` reads it back as text.
- **Malformed-JSON detection helper:** a `CHECK_MALFORMED_JSON` method wraps `JSON Parse` in `ON ERR CALL` to distinguish a serialized object from plain text safely.
- **Three testing strategies:** simple standalone test-mode selection on `On Startup`; a repeating standalone test chain driven by `RESTART 4D` and a `Case` statement; and client-side testing via a customized `.4DLink` file.

## Featured Technology
- `SET DATABASE PARAMETER`/`GET DATABASE PARAMETER` (User param value)
- 4D command-line `--user-param`, `.4DLink` file `user_param` attribute
- `JSON Parse`/`JSON Stringify`, `ON ERR CALL`

## Best Practices Highlighted
1. Use the User parameter rather than marker files or other ad hoc mechanisms to signal test mode at startup.
2. Guard `JSON Parse` calls with `ON ERR CALL`/a malformed-JSON check before assuming a parameter is a serialized object.
3. Chain multiple automated tests using `RESTART 4D` plus a `Case` statement keyed on the User parameter value.

## Context / Positioning
This note documents a small but practical v17R3 addition aimed at supporting QA and CI-style automation for 4D databases — useful for teams managing server farms or needing repeatable, scriptable test launches — reflecting 4D's broader efforts during the R-release cycle to improve tooling for professional development and deployment workflows.

## Historical Commentary
**Status:** Still relevant

The User parameter mechanism (`SET/GET DATABASE PARAMETER` with the `User param value` selector, the `--user-param` command-line flag, and the `.4DLink` file's `user_param` attribute) introduced in v17R3 remains unchanged and fully functional in current 4D versions. This is a narrowly scoped but durable feature note — nothing described here has been deprecated, though it remains just one building block a developer would combine with their own test framework/harness rather than a complete testing solution on its own.

Note: the PDF's own header lists "Technical Note 17-16", which appears to be a typo in the original document — the KB URL/filename and publication sequence place this note at TN 19-06.
