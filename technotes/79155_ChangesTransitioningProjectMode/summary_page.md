# Tech Note 23-06: 7 Changes to Check When Transitioning to Project Mode

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** March 27, 2023 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79155
**Download:** https://kb.4d.com/DLTN/TN/2023/23-06_ChangesInProjectMode.zip

## Proposition
Converting a binary 4D database to project mode is mostly automatic, but several UI and code-logic behaviors change silently and can introduce bugs if not manually reviewed. This note walks through seven such changes with a side-by-side demo comparing binary vs. project mode.

## Key Points
- **Forced Designer user:** in project mode standalone/single-user mode, the current user is always "Designer" and `CHANGE CURRENT USER` has no effect (client-server mode behaves as before).
- **USERS TO BLOB is inert:** returns an empty blob in project mode; custom login systems should instead read the new `directory.json` (Settings folder) via `Document to text` + `JSON Parse`.
- **No more Picture Library:** all pictures move to disk in the Resources folder, so `READ PICTURE FROM LIBRARY` must be replaced with `READ PICTURE FILE`.
- **Transparent picture property removed:** superseded by native PNG alpha-channel support; `TRANSFORM PICTURE(pic; Transparency; 0x00FFFFFF)` is offered as a workaround technique.
- **Radio Group property replaces legacy compatibility setting:** the old "Radio buttons grouped by name" prefix-based grouping is replaced by an explicit "Radio Group" property.
- **Highlight buttons become regular buttons:** losing their enabled/disabled/clicked states; the note ships a full utility method that parses the project conversion log JSON, builds a 2-state SVG via the SVG toolbox, and rewrites affected `.4DForm` files to restore equivalent visual behavior with a custom background picture.
- **List access varies by version/mode:** 19.x/19R5 4D Remote clients only get read-only source access (including lists) since 4D Remote uses a snapshot `.4DZ`; 19R6+ adds development mode for write access, with moving lists into a table as a fallback for older versions.

## Featured Technology
- **CHANGE CURRENT USER** — legacy user-switching command, inert in project mode standalone.
- **USERS TO BLOB / BLOB TO USERS** — legacy user-management commands superseded by `directory.json`.
- **directory.json** — project mode's JSON-based user directory, parsed with `Document to text` + `JSON Parse`.
- **READ PICTURE FILE** — project mode's disk-based picture-loading replacement for `READ PICTURE FROM LIBRARY`.
- **SVG custom buttons** — 2-state SVG images generated via the SVG_ toolbox to emulate removed highlight-button behavior.
- **Radio Group property** — modern explicit replacement for legacy name-based radio button grouping.

## Best Practices Highlighted
1. Always test-run the converted project database against real use cases before assuming a clean conversion.
2. Use the project conversion log (JSON) programmatically to locate and batch-fix affected forms (e.g., highlight buttons) rather than manually hunting through the UI.
3. Plan list-data storage strategy around the 4D version and remote client mode in use, since read/write access to lists differs materially across 19.x/19R5 vs. 19R6+.

## Context / Positioning
Published as project mode adoption accelerated (features like classes, Git-friendliness, and M1 support drove migration), this note reflects 4D's effort to smooth binary-to-project transitions by documenting the residual manual-fix surface area that automated conversion doesn't fully cover.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
