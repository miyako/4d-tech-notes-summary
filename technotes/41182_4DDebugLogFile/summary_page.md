# Tech Note 06-01: The 4DDebugLog.txt File

**Author:** Hugo Fournier, Technical Support Manager, 4D, Inc.
**Published:** January 3, 2006 | **Product/Version:** 4D 2004.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41182
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_01-04_(JAN)/06-01_4DDebugLog.zip

## Overview
This Tech Note introduces the 4DDebugLog.txt file, a debug logging mechanism added in 4D 2004.3 for 4D Server, 4D Client, and 4th Dimension (single-user), and shows a technique for safely archiving/rotating that log so it doesn't fill up the hard disk when left running for troubleshooting.

## Key Points
- Debug logging is toggled with `SET DATABASE PARAMETER(34;Option)`, where Option 0 = off (default), 1 = basic recording, 2 = detailed recording (adds plug-in event and externCall tracing).
- The log records, per event: elapsed milliseconds since file creation, process number, executed commands/plug-in calls (with stack level), and calls to project/object/form methods.
- Each event is written *before* execution, so the log remains useful even if the application crashes immediately after.
- The file is named `4DDebugLog.txt`, located next to the structure file (4D Server/4th Dimension) or in the 4D Preferences folder (4D Client), and is recreated fresh on each application launch.
- Logging significantly degrades performance and should never be left on in production — it's intended purely for hard-to-reproduce bugs like intermittent server crashes.
- The note's example solution uses a dedicated monitoring process (`M_Monitor_Process`) that polls the log's size every 60 seconds, archives it via `MOVE DOCUMENT` with a date/time-stamped filename once it exceeds ~500KB, restarts logging into a fresh file, and keeps at most 5 archived logs by deleting the oldest.
- Provides the exact `On Startup`/`On Server Startup`, `On Exit`/`On Server Shutdown`, and `M_Monitor_Process` method code needed to install this in a database.

## Featured Technology
- 4D 2004.3 (4D Server, 4D Client, 4th Dimension)
- `SET DATABASE PARAMETER` selector 34 (debug logging)
- Interprocess variables and `New process` / `DELAY PROCESS`
- `MOVE DOCUMENT` / `DELETE DOCUMENT` for log archiving and rotation

## Historical Context
Published in January 2006 for 4D 2004.3, this note predates 4D's native SQL engine (added in v11, 2007), Project Mode (2018), and ORDA — at the time, 4D databases were still built exclusively in binary Design Mode. The manual, polling-based log rotation scheme (a background process checking file size every 60 seconds) reflects programming idioms typical of mid-2000s 4D development, before more modern monitoring and logging infrastructure existed.

## Historical Commentary
**Status:** Superseded

The core diagnostic idea — a rolling, timestamped execution trace to diagnose crashes that resist normal debugging — remains conceptually valid and a similar debug-log capability persisted in later 4D versions, but the specific mechanics shown here (the `SET DATABASE PARAMETER` selector 34 syntax and the hand-rolled polling/archiving process) are very much artifacts of 2004-2006-era 4D. Later 4D releases and platform improvements (including 4D Server administration/activity logging and the eventual SQL engine and language modernizations from v11 onward) have provided more structured alternatives to this manual approach.
