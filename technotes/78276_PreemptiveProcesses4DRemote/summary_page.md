# Tech Note 19-10: Preemptive Processes on 4D Remote

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** June 21, 2019 | **Product/Version:** 4D v17 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78276
**Download:** https://kb.4d.com/DLTN/TN/2019/19-10_PreemptiveProcessOn4DRemote.pdf

## Proposition
Starting in v17R4, 4D Remote clients — not just Server and standalone — can run truly parallel, multi-core preemptive processes. This note covers the requirements, thread-safety verification, and refactoring techniques needed to take advantage of it.

## Key Points
- **Cooperative vs. preemptive:** cooperative processes share one CPU by yielding control (via `IDLE` or implicitly); preemptive processes are OS-scheduled across multiple cores for true parallelism.
- **Requirements:** 64-bit 4D/4D Server, Compiled execution context, and every command/method in the call chain marked thread-safe ("can be run in preemptive processes").
- **Thread-safety verification:** check the green preemptive icon in command documentation, or rely on compiler errors that name the first offending non-thread-safe command.
- **4D Remote specifics:** requires v17R4+ and the **New Network Layer** — the legacy network layer disables client-side preemptive execution.
- **Refactoring non-thread-safe calls:** spin off an async cooperative task via `New process` when no result is needed, or use the **Signal** object (`New signal`, `signal.wait()`, `signal.trigger()`) to synchronously wait for a cooperative task from a preemptive one.
- **Checking process mode at runtime:** `PROCESS PROPERTIES` reports whether a process is preemptive or cooperative; the Runtime Explorer and 4D Server admin window also show dedicated icons per process type.

## Featured Technology
- Preemptive/cooperative multitasking model, New Network Layer
- `New process`, `CALL WORKER`, `New signal`/`signal.wait()`/`signal.trigger()`
- `PROCESS PROPERTIES`, compiler thread-safety checking

## Best Practices Highlighted
1. Mark methods "can be run in preemptive processes" explicitly and rely on the compiler to surface non-thread-safe dependencies.
2. Use asynchronous `New process` calls when a preemptive task doesn't need to wait for a cooperative result.
3. Use the Signal object rather than polling loops when a preemptive process must synchronously wait on a cooperative task.

## Context / Positioning
This note documents a significant multi-core performance milestone in the v17 R-release cycle — extending preemptive execution from server-side to client-side (4D Remote) processes — part of 4D's ongoing multi-year effort to modernize its historically single-threaded runtime for better use of modern multi-core hardware.

## Historical Commentary
**Status:** Still relevant

The preemptive/cooperative concurrency model, thread-safety requirements, and the Signal object pattern described here remain 4D's current concurrency architecture and are still accurate today. The conditional framing ("must use 64-bit", "must enable New Network Layer") is now moot in practice since 32-bit 4D and the legacy network layer have both been fully phased out in subsequent 4D versions — those requirements are simply the only option now rather than a choice developers need to actively make. The refactoring techniques (async `New process`, synchronous `Signal`) are still the standard approaches for bridging preemptive and cooperative code today.
