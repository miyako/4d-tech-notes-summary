# Tech Note: Avoiding Semaphore Gotchas

- **Asset ID:** 25594
- **Tech Note #:** 02-53
- **Published:** November 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=25594
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_51-55_(NOV)/02-53_SemaphoreGotchas.hqx

## Overview

David Adams reviews the fundamentals of 4D semaphores for locking shared arrays/variables across processes (since 4D only auto-manages contention for records and Design-environment objects, not variables), using a hypothetical log-manager system with shared arrays and variables as the running example. He demonstrates the standard set/clear pattern (`Repeat / IDLE / Until (Not(Semaphore(...)))` then `CLEAR SEMAPHORE(...)`), then identifies the titular 'gotcha': when a routine that sets and clears a semaphore is called both as a subroutine of a lock-holding caller and directly on its own, the semaphore can be released prematurely mid-chain, letting two processes believe they each own the lock. His solution is a pair of wrapper methods (`LogManager_Lock`/`LogManager_Unlock`) that track a call-depth counter so the semaphore is only actually cleared when the outermost lock request unwinds, and he notes that consistently routing all locking through such wrappers also makes unbalanced calls easy to spot using 4D Insider.

## Key Points

- Establishes that 4D/4D Server auto-manage contention for records and Design-environment objects, but locking of shared arrays/variables must be implemented manually with semaphores.
- Shows the standard lock-acquire idiom: `Repeat / IDLE / Until (Not(Semaphore("$LogManagerLockSemaphore")))`, with `IDLE` included specifically to avoid monopolizing a compiled application while waiting.
- Diagnoses the 'gotcha': if a subroutine (`LogManager_AddColumnName`) sets and clears the same semaphore both when called standalone and when called from within an already-locked routine (`LogManager_Initialize`), the semaphore gets released prematurely mid-chain, letting a second process acquire it while the first still believes it holds the lock -- a bug that is intermittent, calling-chain-dependent, and invisible to SanityCheck, 4D Insider, or the 4D Compiler.
- Presents the fix: wrapper methods `LogManager_Lock`/`LogManager_Unlock` that maintain a `LogManagerLockCalls_count` variable (initialized via `Undefined()` checks), incrementing on every lock request and only calling `CLEAR SEMAPHORE` when the counter unwinds back to 1 -- a reentrant-lock counting pattern.
- Notes the wrapper methods don't prevent a separate common mistake (unbalanced Semaphore/CLEAR SEMAPHORE calls) but make it far easier to detect, since routing all access to a given semaphore through one dedicated pair of methods lets 4D Insider visually reveal mismatched call counts.

## Featured Technology

- Semaphore() / CLEAR SEMAPHORE() commands
- Object/variable locking across processes
- Wrapper lock/unlock methods with a reference counter
- IDLE command in polling loops
- 4D Insider for detecting unbalanced semaphore calls

## Historical Commentary

**Status:** still_relevant

David Adams reviews how 4D and 4D Server automatically manage record- and design-object-level contention, but leave variable/array locking to developer-managed semaphores, and identifies a specific, hard-to-detect bug: a nested-call chain that releases a shared semaphore prematurely because a subroutine sets and clears it independently of its caller. His fix -- wrapping Semaphore/CLEAR SEMAPHORE calls in a matched pair of methods that track a call-depth counter so the semaphore is only released when the outermost caller finishes -- is a reentrant-lock pattern that remains directly applicable in current 4D. Semaphores are still a supported concurrency primitive today, though modern 4D has since added additional concurrency tools (such as worker processes) that offer alternative ways to manage shared state across processes.

References to newer/updated information:
- Semaphores (Semaphore/CLEAR SEMAPHORE) remain a supported concurrency primitive in current 4D
- Modern 4D also offers worker processes and other concurrency tools introduced in later versions as alternatives for managing shared state across processes
