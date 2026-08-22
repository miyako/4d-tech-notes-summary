# Tech Note 06-33: 4D Advanced Debugging Techniques – Part 2

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** August 18, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43939
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_31-34_(AUG)/06-33_Advanced_Debugging_2.zip

## Overview
Part 2 of a two-part Tech Note series on debugging in 4D 2004. Part 1 covered 4D's native debugging tools (debug/trace window, Runtime Explorer, debug log file, error messages); Part 2 presents a complementary custom text-file logging technique — plus an open-source "4D Logger 2004-1" component — for cases where native tools fall short, especially for compiled databases and timing/concurrency bugs.

## Key Points
- Custom logging offers three distinct advantages over interactive debugging tools: pattern recognition (filterable, comparable, archivable logs), detecting timing/synchronization bugs without the distortion a live debugger's breakpoints introduce, and working equally well in compiled databases, where most native 4D debugging tools are unavailable or limited.
- Worked example: a memory-leak pattern in a 4D-for-OCI plug-in integration, spotted by noticing "Handle Creation" log lines with no matching "Handle Free" line.
- Worked example: a factorial-calculation race condition, where a second process mutates a shared interprocess variable mid-calculation — made visible in the log via distinct process ID (PID) tags on each line.
- The "4D Logger 2004-1" ("Logger") component is provided open-source, giving developers a ready-made, reusable logging framework rather than requiring hand-rolled log calls.
- Introduces a per-process "stack level" concept: purely a logging/display construct (unrelated to 4D's actual call stack) that increases indentation as method/function calls are logged as starting and decreases as they end, making nested execution easy to read in the log text.
- Documents six logging command categories: before/after logging for functions (with parameters and return value) and procedures (without return value); start/end logging for methods (does not adjust stack level, since these simply bracket a method body); and general messages, with or without an associated stack level.
- Each logging category includes concrete sample log output demonstrating process ID tags, stack-level numbers, and consistent message formatting.

## Featured Technology
- 4D Logger 2004-1 (open-source text-file logging component)
- Custom stack-level/process-ID-tagged debug logging
- Debugging strategies specific to compiled 4D databases

## Historical Context
Written for 4D 2004, in an era when compiled 4D databases had substantially reduced access to native debugging tools compared to interpreted mode. This predates 4D's own SQL engine (v11, 2007), Project Mode (v17, 2018), and ORDA, but its subject — debugging technique, not language architecture — is largely independent of those later platform shifts.

## Historical Commentary
**Status:** Still relevant

The core debugging philosophy this note teaches — structured, stack-level, process-tagged logging to reveal patterns invisible to a live debugger, especially for timing/concurrency issues and in compiled/production builds — remains a widely used and durable technique across all of software development today, 4D or otherwise. The specific "4D Logger 2004-1" component and the framing around 4D 2004's particular compiled-vs-interpreted debugging tool gaps are dated, since 4D has since improved its native debugging and logging facilities, but the underlying lesson about log-based debugging for concurrency and production bugs remains directly applicable in 2026.
