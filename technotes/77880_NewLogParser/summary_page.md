# Tech Note 17-20: New Log Parser

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** November 2, 2017 | **Product/Version:** 4D v16 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77880
**Download:** https://kb.4d.com/DLTN/TN/2017/17-20_NewLogParser.zip

## Proposition
This Tech Note documents the format of 4D's Request Log and Debug Log files and introduces a Log Parser tool that correlates them together by process, using a new field added to the Request Log in v16 R5, for easier performance profiling and troubleshooting.

## Key Points
- **Request Log:** enabled/disabled via `SET DATABASE PARAMETER(4D Server log recording;...)`, producing `4DRequestLog.txt` and `4DRequestLog_ProcessInfo.txt`.
- **Debug Log:** documented in both standard and tabular formats (`4DDebugLog.txt`).
- **New v16 R5 field:** a process-correlating field added to the Request Log enables joining it with Debug Log data.
- **Log Parser tool:** provides a job list to select logs, then parses and merges them into a unified, process-organized view.
- **Log Viewer:** lets the developer browse correlated Request/Debug log data interactively.
- **Web-based ID updates:** supports updating Request IDs via the web for further correlation workflows.
- **Use case:** performance profiling and troubleshooting on 4D Server deployments.

## Featured Technology
- 4DRequestLog.txt / 4DRequestLog_ProcessInfo.txt
- 4DDebugLog.txt (standard and tabular)
- SET DATABASE PARAMETER command
- Custom Log Parser / Log Viewer tool

## Context / Positioning
Published in late 2017 for 4D v16 R5, this note sits squarely in the classic Design Mode era, before Project Mode and ORDA. Log-based diagnostics were the primary way to profile 4D Server performance at the time, well before more modern observability tooling existed for 4D.

## Historical Commentary
**Status:** Partially superseded

The Request Log and Debug Log file formats described are largely still part of 4D today, and the general technique of correlating them by process ID remains valid, so the conceptual content holds up. However, the specific Log Parser/Log Viewer tool shipped with this note is a point-in-time utility built for the v16 R5 log schema; 4D's own log tooling and log formats have continued to evolve in subsequent releases, so a modern developer would likely need updated or newer tooling rather than this exact parser.
