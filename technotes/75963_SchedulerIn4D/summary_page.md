# Tech Note 09-45: The 4D v11 SQL Scheduler

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** December 3, 2009 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75963
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_41-45_(NOV)/09-45_4Dv11SQL_Scheduler.pdf

## Proposition
This note explains how 4D's internal cooperative Scheduler works — an endless loop that checks system events and gives CPU time to active processes — and how developers can tune it via SET DATABASE PARAMETER and Preferences settings to better understand and, rarely, adjust 4D's CPU behavior.

## Key Points
- The 4D language remains a **single, non-thread-safe, cooperative execution model** even though the v11 SQL data engine itself is multithreaded.
- The Scheduler is conceptually a loop: **check for system events**, then **give CPU time to each active 4D process**.
- Three tunable values via **SET DATABASE PARAMETER**: `min_ticks` (yield time when busy), `max_ticks` (yield time when idle), `ticks_between` (how long 4D holds the CPU between system calls); 1 tick = 1/60th second.
- Equivalent **Preferences settings**: Average to 4D, Max to 4D, Max to Other Apps.
- Only **active** processes consume CPU time in the "give time" loop; delayed/paused/semaphore-waiting processes do not — relevant for polling-heavy designs.
- Discusses **processor spoofing** and multi-processing considerations tied to specific tick values.
- Explicit caution: **defaults are fine for most situations**; tweaking should be reserved for diagnosed, specific scenarios.

## Featured Technology
- 4D cooperative process Scheduler
- SET DATABASE PARAMETER (min_ticks, max_ticks, ticks_between)
- Preferences-based scheduler tuning (Average/Max to 4D, Max to Other Apps)
- Processor spoofing / multi-processing preferences

## Best Practices Highlighted
1. Leave Scheduler defaults untouched unless you have a specific, diagnosed performance problem.
2. Pause or delay "pooling" processes explicitly, since active processes always consume at least 1 tick even when idle-looking.
3. Understand busy vs. not-busy process states before tuning min_ticks/max_ticks to avoid unintended CPU consumption tradeoffs.

## Context / Positioning
Published shortly after the multithreaded v11 SQL engine's introduction, this note clarified that classic 4D process scheduling remains cooperative underneath the new multithreaded server architecture, complementing the companion note "The New Multithreading Model in 4D v11 SQL" (asset #76035).

## Historical Commentary
**Status:** Still Relevant

This note explains 4D's internal cooperative-process Scheduler loop and the tunable min_ticks/max_ticks/ticks_between parameters (set via SET DATABASE PARAMETER) plus related Preferences settings, giving developers a mental model for how 4D allocates CPU time to cooperative processes.

The 4D language remains cooperative per process today, and this Scheduler model, along with SET DATABASE PARAMETER, is still substantially accurate and the note's core guidance (rarely tweak the defaults; understand busy/idle yielding behavior) is still relevant for developers debugging performance or CPU usage issues in cooperative 4D processes.
