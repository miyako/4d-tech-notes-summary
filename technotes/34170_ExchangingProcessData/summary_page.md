# Tech Note: Exchanging Data Between Processes

- **Asset ID:** 34170
- **Tech Note #:** 04-39
- **Published:** September 30, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=34170
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_36-40_(AUG)/04-39_Exchanging_Data.hqx

## Overview

Jean-Yves Fock-Hoon addresses how to make multiple 4D processes reliably exchange data, using SET PROCESS VARIABLE, GET PROCESS VARIABLE, and VARIABLE TO VARIABLE as the core mechanism and five worked examples to illustrate the synchronization techniques (semaphores, buffered arrays, timer-driven polling) needed to avoid lost or desynchronized communication.

## Key Points

- Introduces the three core commands: `SET PROCESS VARIABLE` (sets a value in a destination process's variable), `GET PROCESS VARIABLE` (reads a value from a source process's variable), and `VARIABLE TO VARIABLE` (like SET PROCESS VARIABLE but the only one of the three that supports arrays) -- all requiring the variable to be declared in both processes.
- Example 1 shows a simple fully-synchronous two-process handshake: Process One waits on a shared `<>Ready` flag, then both processes alternately set and wait on a `vReceivedMessage` variable to pass messages back and forth in lockstep.
- Example 2 demonstrates three input processes feeding a single, deliberately slower output process through a semaphore-protected inter-process array buffer, driven from a dialog window using `On Timer` on the input side (to avoid blocking the UI) and `SET TIMER(30)` plus periodic re-checks on the output side.
- Example 3 applies the same input/output buffering pattern without any dialogs to implement a simple multi-process log-file writer (methods `M_ProcessOutput3`/`M_ProcessInput3`).
- Examples 4 and 5 invert the topology -- multiple output processes retrieving data from one input process -- using a semaphore plus a boolean `GetNextItem`-style handshake so each output process retrieves exactly one item at a time without duplicate consumption.
- Warns that `CALL PROCESS`/`On Outside Call` events are not queued and can be silently lost if a process is busy handling a prior event, using the classic "clicking Next too fast on a floating record-navigation window" bug as a cautionary real-world example, and stresses that semaphores and buffering are essential whenever more than one process touches a shared variable or array.

## Featured Technology

- SET PROCESS VARIABLE / GET PROCESS VARIABLE commands
- VARIABLE TO VARIABLE command (supports arrays)
- Semaphores for synchronizing shared inter-process buffers/arrays
- CALL PROCESS combined with On Timer / On Outside call / SET TIMER for UI-safe polling
- Inter-process variables and arrays as producer/consumer buffers

## Historical Commentary

**Status:** Still relevant

Jean-Yves Fock-Hoon walks through five progressively more complex multi-process communication scenarios in 4D -- from a simple synchronous two-process handshake using SET PROCESS VARIABLE/GET PROCESS VARIABLE, to buffered many-to-one and one-to-many producer/consumer patterns guarded by semaphores and drained via On Timer/CALL PROCESS polling loops, to a basic log-file writer fed by multiple worker processes. These low-level primitives (SET/GET PROCESS VARIABLE, VARIABLE TO VARIABLE, semaphores, CALL PROCESS) are foundational 4D language features that remain unchanged and fully supported today, so the synchronization patterns and cautions described are still directly applicable to any 4D multi-process application, even though many modern 4D apps now also have access to newer constructs (e.g. worker processes via 4D's newer process management commands) for some of these same use cases.

**References to newer/updated information:**
- SET PROCESS VARIABLE, GET PROCESS VARIABLE, VARIABLE TO VARIABLE, semaphores, and CALL PROCESS remain core, unchanged 4D language commands today
- 4D has since added additional process/worker management commands (e.g. CALL WORKER family) that offer alternative higher-level patterns for some inter-process communication scenarios
- The synchronization cautions in this note (semaphore-guarded buffers, avoiding lost On Outside Call events) remain valid guidance for multi-process 4D applications
