# Tech Note: Server Processes

- **Asset ID:** 39582
- **Tech Note #:** 05-32
- **Published:** October 3, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Larry Sharpe
- **Page URL:** https://kb.4d.com/assetid=39582
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_30-33_(SEP)/05-32_Server_Process.hqx

## Overview

Larry Sharpe's third Tech Note in his example-database series demonstrates how to build a background process — used here for periodically importing files — that is configured and monitored from a 4D Client but is actually executed on the 4D Server, with the same code also working unmodified on a single-user or 4D Client installation.

## Key Points

- The People_ImportProcess project method is the core of the note: called with no parameters it starts a new process via `Execute on server` (or `New process` on a client/single-user machine), and called with a `$command` parameter it performs the actual work (`RunProcess`, `UpdateWindow`, `ShowAlert`, `UserInterface`, `OnStartup`).
- The RunProcess loop delays in 1-second increments inside a `Repeat` loop (rather than one long `DELAY PROCESS`) so the user can request a stop mid-wait, then checks the Import Needed folder, imports files, sends email/alert notifications, and moves the file to Import Finished.
- Because the server cannot show dialogs or alerts, `EXECUTE ON CLIENT` is used to run UI-related code (`UpdateWindow`, `ShowAlert`) on connected clients, which in turn use `CALL PROCESS` to trigger an `On Outside Call` form event that refreshes the open preferences window.
- Process preferences (run at startup, run on server vs. client, polling delay in minutes, email/alert settings) are stored in the [xPreferences] table under the fixed name "Processes" rather than per-user, separating server process configuration from user preferences introduced in the prior Tech Note.
- The note clarifies naming/behavior differences among several related commands: `New process` (same machine, client or single-user), `Execute on server` (always the server on client/server, same as `New process` in single-user), `EXECUTE ON CLIENT` (runs a method, not a process, only on registered clients), and `REGISTER CLIENT`/`UNREGISTER CLIENT`.
- Also documents `GET PROCESS VARIABLE` / `SET PROCESS VARIABLE` (cannot pass local variables, arrays, or pointers) versus `VARIABLE TO VARIABLE` (the true opposite of `GET PROCESS VARIABLE`), and uses `PLATFORM PROPERTIES` to determine the correct application/structure path depending on whether the code runs on a client or the server.
- Builds directly on the two prior notes in the series: "User Changeable Output Form" (July 2005) and "User Preferences" (August 2005).

## Featured Technology

- Execute on server / New process commands
- EXECUTE ON CLIENT and On Outside Call form event
- REGISTER CLIENT / UNREGISTER CLIENT
- GET PROCESS VARIABLE / SET PROCESS VARIABLE / VARIABLE TO VARIABLE
- DELAY PROCESS-based polling loop
- xPreferences table (BLOB-based preference storage)
- PLATFORM PROPERTIES for client/server path resolution

## Historical Commentary

**Status:** Partially superseded

This note demonstrates a manual but genuinely clever pattern for running the same background-process code on a 4D Server, a 4D Client, or a single-user application, complete with careful handling of the fact that server code cannot display UI. That client/server process-delegation approach remained the standard technique for years, but 4D has since added dedicated worker-process language commands (CALL WORKER and related APIs) that handle inter-process messaging and background execution more directly, reducing the need for this much manual EXECUTE ON CLIENT / On Outside Call plumbing. The core ideas — server-only processes, careful command selection for client vs. server execution — remain conceptually valid and are still explained in current 4D documentation.

**References to newer/updated information:**
- CALL WORKER and the worker-process command family, added in later 4D versions, provide a more direct built-in mechanism for background/server process communication than manual EXECUTE ON CLIENT plus On Outside Call polling
- 4D's process/worker model has continued to evolve; the fundamental client-vs-server execution distinction described here (New process vs. Execute on server) still applies in current 4D
