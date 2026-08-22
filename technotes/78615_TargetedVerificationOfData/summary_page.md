# Tech Note 20-22: Targeted Verification of Data

**Author:** Tim Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** December 29, 2020 | **Product/Version:** 4D v18 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78615
**Download:** https://kb.4d.com/DLTN/TN/2020/20-22_TargetedDataVerification.zip

## Proposition
4D provides UI-based ways to check a data file's health (MSC, Server Admin Window), but developers sometimes need finer control — checking only certain tables, logging only errors, or building a repeatable maintenance script. This Tech Note demonstrates how to build custom, targeted data verification tooling on top of the `VERIFY CURRENT DATA FILE` command and its callback mechanism.

## Key Points
- **Built-in UI options**: MSC's Verify tab (works without the app running, on both 4D and 4D Server) and the 4D Server Admin Window's "Verify Records and Indexes" button for live checks.
- **Programmatic control**: `VERIFY DATA FILE`/`VERIFY CURRENT DATA FILE` accept specific table/field arrays and a callback method fired per verification event.
- **Callback event model**: the callback receives numeric event codes for message, verification-finished, error, end-of-execution, and warning.
- **`_checkTheseTables`**: lets a developer pass a collection of specific tables to verify, saving time versus a full scan.
- **`_checkAllTablesS2A`**: a cheap pre-check technique — running `SELECTION TO ARRAY` under an `ON ERR CALL` handler to flag tables likely to be problematic before running full verification on just those.
- **`_checkAllTables`**: a straightforward full verification of every table.
- **JSON error/warning reports**: results are serialized with `JSON Stringify` and written as timestamped log files, then revealed with `SHOW ON DISK`.

## Featured Technology
- Maintenance Security Center (MSC) Verify tab
- 4D Server Administration Window Maintenance tab
- VERIFY DATA FILE / VERIFY CURRENT DATA FILE commands and callbacks
- ON ERR CALL / GET LAST ERROR STACK
- JSON Stringify-based reporting

## Best Practices Highlighted
1. Use a lightweight pre-check (`SELECTION TO ARRAY` + error handler) to narrow down which tables need full verification before running an expensive full scan.
2. Filter callback events to only log errors/warnings, keeping verification reports concise and actionable.
3. Persist verification results as structured JSON logs (with timestamps) rather than ephemeral UI output, for later review or automation.

## Context / Positioning
This note extends 4D's long-standing data integrity tooling (MSC, Admin Window) by showing developers how to script and automate maintenance checks using the flexible callback-driven `VERIFY CURRENT DATA FILE` command — useful for administrators managing large production databases who want scheduled or targeted health checks rather than manual, full-database verification runs through the UI.

## Historical Commentary
**Status:** Still relevant

The verification commands and UI entry points described here (MSC Verify tab, Server Admin Window, `VERIFY DATA FILE`/`VERIFY CURRENT DATA FILE` with callbacks) remain 4D's current data-integrity toolset; there has been no replacement or deprecation of this mechanism in subsequent 4D versions. The component patterns shown — targeted table checks, a cheap pre-scan via forced runtime errors, and JSON-based error logging — are still directly reusable today. This is a good example of a 4D "utility/how-to" Tech Note whose value has not diminished with time, since it documents a stable, foundational part of the platform rather than a feature later superseded by a newer paradigm.
