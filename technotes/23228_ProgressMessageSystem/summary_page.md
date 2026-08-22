# Tech Note 02-09: Progress Message System

**Author:** Not specified in source document
**Published:** February 28, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=23228
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2002/windows/tn_2002_05-09_(feb)/02-09_progress_message.exe

## Overview
A Tech Note presenting a versatile, text-based, multi-line progress display system for 4D, useful both for user-facing status reporting and for troubleshooting complex code sequences.

## Key Points
- Provides a text-based, multi-line progress display that can update each line independently.
- Well suited for monitoring complex sequences of events and troubleshooting complicated code.
- Final activity results can be redisplayed even after the monitored process has finished.
- Demonstrates practical use of a two-dimensional array and streamlined interprocess communication.

## Featured Technology
- Text-based progress display
- Two-dimensional arrays
- Interprocess communication

## Historical Context
Reflects classic 4D's cooperative multiprocess model, where careful interprocess communication design was needed to stream live status updates from a worker process to a display window.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Still Relevant

The core techniques this note relies on — two-dimensional arrays and interprocess communication for status reporting — remain valid concepts in current 4D, though modern 4D applications now also have access to object/collection-based data structures and, in later versions, true multithreaded worker processes that could implement similar progress-reporting systems somewhat differently.
