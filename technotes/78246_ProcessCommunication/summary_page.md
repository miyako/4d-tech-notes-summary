# Tech Note 19-07: Communication Between Processes in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 24, 2019 | **Product/Version:** 4D v17 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78246
**Download:** https://kb.4d.com/DLTN/TN/2019/19-07_CommunicationBtwProcesses.zip

## Proposition
4D applications are inherently multi-process, and processes often need to share data or coordinate timing. This note surveys the full toolkit — from classic interprocess variables to modern shared objects, Storage, semaphores, workers, and signals — and explains when to use each.

## Key Points
- **Process-local state:** current selection/record per table, process variables, `ON ERR CALL` handler, and Debugger window are all scoped per process, not shared automatically.
- **Interprocess variables** (`<>name`): simplest sharing mechanism, but not thread-safe — disqualifies a method from running in a preemptive process.
- **`SET/GET PROCESS VARIABLE`** and `VARIABLE TO VARIABLE`: direct cross-process variable access by process number, with the latter also supporting arrays.
- **Shared objects/collections** (`New shared object`/`New shared collection`, introduced v16R6): thread-safe, usable in preemptive processes, but require `Use…End use` blocks for modification and must be passed as parameters to reach other processes.
- **`Storage`:** a globally accessible system object holding shared objects/collections without parameter-passing, at the cost of persisting in memory for the app instance's lifetime.
- **`Semaphore`/`CLEAR SEMAPHORE`:** named locks for coordinating timing between processes; `$`-prefixed names are local, others are database/server-wide global.
- **`CALL WORKER`/`KILL WORKER`:** message-passing between persistent worker processes, each maintaining its own state across calls.
- **`New signal`/`.wait()`/`.trigger()`:** finer-grained mid-method synchronization between workers, with optional timeout grace periods.

## Featured Technology
- Interprocess variables, `SET/GET PROCESS VARIABLE`
- Shared objects/collections, `Storage`
- `Semaphore`, `CALL WORKER`, `New signal`

## Best Practices Highlighted
1. Use interprocess variables only for simple, non-preemptive scenarios; prefer shared objects/collections when preemptive execution matters.
2. Avoid over-relying on `Storage` for transient data, since it persists in memory for the entire application instance's lifetime.
3. Use local (`$`-prefixed) semaphores when coordination is scoped to a single machine instance, and global semaphores for database/server-wide coordination.
4. Prefer `Signal` objects over polling/flag loops for precise synchronous hand-off between preemptive and cooperative tasks.

## Context / Positioning
Published as a consolidated reference note during 4D's v17 R-release push to modernize concurrency (workers, shared objects, signals joining older interprocess variables and semaphores), this tech note reflects 4D's effort to give developers clear guidance on choosing the right inter-process communication tool as multi-core and preemptive execution became more central to the platform.

## Historical Commentary
**Status:** Still relevant

Every mechanism described in this note — interprocess variables, `SET/GET PROCESS VARIABLE`, shared objects/collections, `Storage`, semaphores, `CALL WORKER`/`KILL WORKER`, and the `Signal` object — remains part of 4D's current, unchanged concurrency toolkit. None of it has been deprecated or replaced; if anything, workers and shared objects/collections have become more central to 4D application architecture as preemptive, multi-core execution has matured since 2019. This is one of the more durable, still fully applicable reference notes in the catalog.
