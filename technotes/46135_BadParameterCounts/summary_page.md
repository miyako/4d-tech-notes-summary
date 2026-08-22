# Tech Note 07-14: Protecting Against Bad Parameter Counts

**Author:** David Adams
**Published:** April 11, 2007 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46135
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_13-16_(APR)/07-14_Bad_Parameter_Counts.zip

## Overview
Using a trivial `DisplaySum` example method, this note surveys the full range of behaviors 4th Dimension can exhibit when a custom method is called with fewer parameters than it expects, then presents a reusable defensive-coding pattern to eliminate the risk entirely.

## Key Points
- **Interpreted mode:** a missing parameter reliably produces a clear syntax error dialog — the "best case" outcome.
- **Compiled without range checking (Windows):** the same bug can trigger an outright application crash with an unhelpful, non-diagnostic error screen.
- **Compiled without range checking (OS X):** arguably worse — the routine can silently produce corrupted/incorrect results (e.g., an alert claiming "1 = 1584") with no visible error at all, which is especially dangerous if such a routine's output feeds further calculations.
- **Compiled with range checking:** produces a syntax-error-like dialog similar to interpreted mode; the note recommends always compiling with range checking on, citing negligible runtime cost.
- Explicitly warns that these behaviors are undocumented and not guaranteed to remain consistent across future 4D versions — a bad parameter list is a developer bug that should never be relied upon to "fail gracefully" by accident.
- **Solution 1:** wrap parameter use in `If (Count parameters=N)` with an `ALERT` on failure (noting ALERT is inappropriate for triggers, Web, or SOAP contexts, where errors should be logged/returned instead).
- **Solution 2 (recommended):** centralize the logic in a reusable `ParameterCountIsOkay(methodName; min; max; count)` validator function, called from any method needing protection, producing a consistent, identifying error message.
- Notes that `ON ERR CALL` does not meaningfully help trap bad-parameter-count errors in compiled code.

## Featured Technology
- `Count parameters`
- Compiler range-checking option
- `ALERT` command
- `ON ERR CALL`
- Centralized validator method pattern (`ParameterCountIsOkay`)

## Historical Context
This note documents classic 4D 2004 compiler and interpreter behavior — including now-historical crash and memory-corruption scenarios on period Windows/OS X builds — that predates 4D's more modern language features (e.g., typed/optional/named parameters) introduced in later versions. Despite the dated specifics of the demonstrated crash behaviors, the core defensive-programming discipline (validate parameter counts/types before use, centralize validation logic, avoid "magic" error codes) remains standard, directly applicable advice for 4D developers today.

## Historical Commentary
**Status:** Still relevant

While the specific compiled-crash behaviors described are tied to the classic 4D compiler of that era, the recommended defensive pattern of validating parameter counts before use — ideally via a centralized helper method — remains sound, current best practice in 4D development.
