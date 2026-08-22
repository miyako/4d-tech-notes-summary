# Tech Note 02-28: Progress Indicator

**Author:** Not specified in source document
**Published:** June 14, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=23245
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2002/windows/tn_2002_25-29_(jun)/02-28_progress_indicator.exe

## Overview
A Tech Note describing how to design a custom progress indicator in 4D, including a discussion of the performance overhead trade-offs involved.

## Key Points
- Explains the value of progress indicators for reporting long-running operation status to users.
- Describes a simple design model for building a custom progress indicator.
- Discusses the performance overhead trade-off of updating a progress indicator during an operation.

## Featured Technology
- Custom progress indicator
- Operation status feedback

## Historical Context
Reflects classic 4D's need for hand-built UI feedback widgets before richer native progress controls existed; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Still Relevant

The general design principle — balancing user feedback against the performance cost of updating a progress display — remains a timeless UI/performance engineering trade-off, though later 4D versions have added native progress-related form objects that reduce the need for the fully custom implementation this note likely demonstrated.
