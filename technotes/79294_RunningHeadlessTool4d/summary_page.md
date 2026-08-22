# Tech Note 23-16: Running Headless using tool4d

**Author:** Erick, Technical Services Engineer, 4D Inc.
**Published:** September 29, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79294
**Download:** https://kb.4d.com/DLTN/TN/2023/23-16_Running_Headless_using_tool4d.zip

## Proposition
Some operations — exporting data, running a print job, fetching settings, verifying a data file — don't need a full 4D application, a license, or a UI. tool4d, introduced in 4D v20, addresses this by letting developers open a 4D structure and run code entirely from the command line, license-free, ideal for scripted, CI/CD, or unattended environments.

## Key Points
- **License-free CLI execution:** tool4d requires no 4D license, making it suitable for multiple unlicensed VMs or automated environments that just need to run quick 4D code.
- **Standard app lifecycle:** Execution follows On Startup → (assigned or `--startup-method`) Startup Method → On Exit → quit, mirroring normal 4D application behavior.
- **Reduced feature surface:** By default, the application/web/SQL servers, backup scheduler, ODBC, all components, spell checkers, WebAdmin, CEF, PHP, and the debugger are disabled — component method calls are silently ignored, so only native 4D commands should be used.
- **Simple invocation syntax:** `<path_to_tool4d> <path_to_.4dbase_or_.4DProject> [optional_arguments]`, with per-OS differences in locating the executable (e.g., inside `tool4d.app/Contents/MacOS/tool4d` on macOS).
- **Key CLI arguments:** `--data`, `--create-data`, `--user-param`, `--dataless`, `--skip-onstartup`, and `--startup-method`; `--headless` is a no-op since tool4d is always headless.
- **LOG EVENT for troubleshooting:** Since headless runs produce no console output, a cross-platform `logEvent` helper (writing via `LOG EVENT` to Event Viewer on Windows or `Into 4D debug message` for macOS Console) confirms code ran successfully.
- **`--user-param` for scripted branching:** Combined with `Get database parameter(User param value; $param)` inside a startup method, a single structure can perform different actions (export, settings, print, verify) selected entirely via the command line.
- **Demo use cases:** `exportDataToText` (via `EXPORT TEXT`), `getSettings` (JSON dump of app/system/log info), `printTest` (via `PRINT SELECTION` to a PDF driver), and `verifyDataFile` (via `VERIFY CURRENT DATA FILE`) illustrate practical lightweight, scriptable operations.

## Featured Technology
- **tool4d:** New v20 command-line executable for headless 4D structure execution.
- **LOG EVENT:** Native logging command bridging to OS-level Event Viewer (Windows) or Console (macOS) for headless diagnostics.
- **Get database parameter (User param value):** Reads the `--user-param` CLI value inside 4D code for conditional branching.
- **EXPORT TEXT / PRINT SELECTION / VERIFY CURRENT DATA FILE:** Native commands used for the demo's data export, printing, and integrity verification operations.
- **JSON Stringify:** Serializes application/system/log settings into a JSON log file.

## Best Practices Highlighted
1. Instrument On Startup/On Exit (and key methods) with `LOG EVENT` calls, since headless execution provides no other visible confirmation that code ran.
2. Rely only on native 4D commands in tool4d scripts, since component calls are silently ignored due to components being disabled by default.
3. Use `--user-param` with a `Case of` dispatch in a startup method to support multiple distinct scripted actions from one structure file rather than building separate structures per task.

## Context / Positioning
tool4d reflects 4D's growing emphasis on scriptable, license-free, CI/CD-friendly tooling around v20, complementing the platform's move toward project-mode source control and automation-friendly workflows. This note positions tool4d as a foundation for unit testing and continuous integration pipelines, an area 4D's blog expands on with further examples.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
