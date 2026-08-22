# Tech Note 09-39: 4D Debug Log Analyzer

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** October 22, 2009 | **Product/Version:** 4D 11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75926
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_38-40_(OCT)/09-39_debugLogAnalyzer.zip

## Proposition
This Tech Note provides a sample 4D database that imports 4D Debug Log (4DDL) files and turns them into statistical reports of method call counts and execution times, repurposing the debug log — normally used for post-crash troubleshooting — as a performance analysis tool.

## Key Points
- The 4DDL (enabled via SET DATABASE PARAMETER) logs every Project, Form, and Object method call, plug-in method call, and 4D command call, including begin/end timestamps for execution-time measurement.
- Only interpreted-mode logs are supported; compiled-mode logs are not correctly parsed.
- Imported log lines are stored raw and de-normalized into a [Log_Lines] table (ID, DL_ID, MS_Stamp, PID, UPID, Stack_Level, Command, Execution_Time, IsStart, Cmd_Type) related to a [Debug_Logs] session table.
- Import can take minutes for large logs (the sample is 80 MB / 1.6 million lines) since spreadsheets like Excel 2003 (~67,000 rows/sheet) can't handle this volume.
- "Generate Summary" produces Top-20 rankings (by call count, average execution time, and longest execution time) for Project, Form, Object, Plug-in methods, and 4D Commands, exported as tab-delimited text.
- A documented "DBL_" prefixed method API (DBL_M_Import, DBL_M_LogSummary, DBL_DATA_DenormalizeData, DBL_DATA_CalcExecTimes, DBL_RPT_GetAverageExecutions, etc.) allows scripting custom reports.
- Execution times are millisecond-accurate; a value of -1 distinguishes "no timing data" from a genuine 0 ms execution.

## Featured Technology
- 4D Debug Log (4DDL) file / SET DATABASE PARAMETER
- Sample 4D database (Design Mode) with import/reporting engine
- DBL_ prefixed API (DBL_M_Import, DBL_M_LogSummary, DBL_DATA_DenormalizeData, DBL_DATA_CalcExecTimes, DBL_RPT_ commands)
- Tab-delimited text export for spreadsheet analysis

## Best Practices Highlighted
1. Pre-calculate expensive derived values (execution times) once at import time rather than on every report run.
2. Store session notes/labels alongside imported data since the only other identifiers are numeric IDs and timestamps.
3. Use raw + de-normalized storage together so original data is preserved while enabling fast querying.

## Context / Positioning
Published as one of a run of developer-tooling Tech Notes in late 2009 (v11.4 era), this note complements earlier documentation on the 4DDL feature (referencing TN 06-01) by shifting its use case from crash diagnostics to proactive performance profiling — a need before 4D shipped more integrated profiling tools.

## Historical Commentary
**Status:** Partially Superseded

The core idea — mining 4D's own debug log for statistical method-performance data — is clever and the underlying 4DDL format itself is still part of 4D today, so the analytical technique remains conceptually valid. However, the delivered tool is a binary Design Mode database rather than a modern, version-controllable Project mode component, and it only supports interpreted-mode logs.

A developer working today would more likely rely on 4D's expanded built-in debugging/profiling tooling (Project mode's text-based structure, and improved runtime diagnostics added since v17) rather than importing raw log text into a bespoke database, though the described approach would still function as documented for interpreted-mode applications.
