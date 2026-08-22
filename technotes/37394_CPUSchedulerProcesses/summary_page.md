# Tech Note 05-20: CPU, Scheduler and Processes

**Author:** Jean-Yves Fock-Hoon, QA Manager
**Published:** May 27, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37394
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_17-20_(MAY)/05-20_CPU_Sched_Processes.pdf

## Overview
This Tech Note explains how 4D's internal architecture allocates CPU time to its cooperatively-scheduled processes, and how developers can use SET DATABASE PARAMETER, IDLE, DELAY PROCESS, and sound process-management practices to improve database and Client/Server performance.

## Key Points
- The Database Properties CPU setting (Low/Normal/High) and the underlying SET DATABASE PARAMETER selectors 10/11/12 let developers tune CPU tick allocation for 4D stand-alone, 4D Server, and 4D Client independently.
- vMinTicks/vMaxTicks/vNbTicks parameters control how much CPU 4D claims per OS call, trading off 4D's own speed against OS/other-application responsiveness.
- 4D processes must periodically yield ("call back") to the internal scheduler; this happens automatically after most commands in interpreted mode but requires explicit IDLE (or DELAY PROCESS (0)) calls in compiled mode, especially inside tight loops.
- Over-using IDLE wastes CPU via rapid, low-value scheduler handoffs.
- Creating/deleting processes is CPU- and memory-expensive, especially with large variable tables in Client/Server; pooling (pausing and reusing idle processes) is recommended instead.
- Scheduler starvation on either the Client or Server side manifests as -10001/-10002 timeout errors.
- Over-indexing fields and overly complex triggers multiply CPU cost across many processes and should be minimized.

## Featured Technology
- 4D's internal cooperative process scheduler
- SET DATABASE PARAMETER / Get database parameter (scheduler selectors 10, 11, 12)
- IDLE and DELAY PROCESS commands
- 4D Server / 4D Client Client-Server process architecture
- Process pooling as a performance pattern

## Historical Context
**Status:** Still relevant

The fundamental execution model this note describes — a 4D-managed scheduler cooperatively allocating CPU ticks among classic 4D processes, requiring explicit yielding via IDLE/DELAY PROCESS in compiled code — remains how classic-language 4D processes behave today, both in Design Mode and Project Mode databases. While later 4D versions have introduced additional scheduling and performance refinements, the core guidance here (tuning scheduler parameters, using process pooling, avoiding over-indexing and complex triggers, understanding -10001/-10002 timeout causes) is still standard, directly applicable advice for anyone performance-tuning a 4D or 4D Server application, making this one of the more durable Tech Notes in this batch.
