# Tech Note 22-09: The Power of System Workers

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** May 19, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78930
**Download:** https://kb.4d.com/DLTN/TN/2022/22-09_SystemWorker.zip

## Proposition
System Worker solves the specific pain of needing a response from a command-line/OS-level task without blocking 4D's UI thread, something LEP could not do reliably in asynchronous mode.

## Key Points
- **LEP limitations**: LAUNCH EXTERNAL PROCESS can only retrieve a response/error when run synchronously, which freezes the interface for the duration.
- **System Worker class**: available via 4D's class store (not a traditional 4D command), requires project mode and 4D v19R4+.
- **Asynchronous callbacks**: the key advantage — a callback method processes the command-line result while the calling process keeps running, keeping forms responsive.
- **Demo 1** compares synchronous/asynchronous LEP vs. System Worker retrieving OS details.
- **Demo 2** shows an inventory list form staying interactive while System Worker runs `find`/`lpstat`/`open` (Mac) or `dir`/`wmic` (Windows) commands in the background.
- **Demo 3** builds a Git GUI (init/add/commit/push, SSH key generation, remote config) entirely by shelling out to `git` via System Worker.
- **Environment PATH**: notes that commands must be discoverable via the system PATH, with a Windows walkthrough for editing it.

## Featured Technology
- System Worker class
- LAUNCH EXTERNAL PROCESS (LEP)
- asynchronous callbacks
- class store
- Git command-line integration

## Best Practices Highlighted
1. Prefer System Worker over LEP whenever a response is needed without blocking the UI.
2. Set up callback methods to process command-line output rather than polling synchronously.
3. Verify required CLI tools (e.g., git) are installed and on PATH before invoking System Worker.

## Context / Positioning
Published as 4D was deep into its ORDA/class-based modernization (project mode, class store), this note exemplifies 4D's broader push to let developers use 4D's own object/class system for systems-level tasks that previously required clunky external-process commands, reflecting the platform's shift toward more expressive, asynchronous, JavaScript/Node-like idioms within 4D code.

## Historical Commentary
**Status:** Still Relevant

System Worker is still the current, documented mechanism in 4D for asynchronous external process execution; it has not been superseded. LEP still exists for simple synchronous cases but System Worker is now the recommended approach for anything requiring non-blocking behavior — this guidance holds true in 4D's current documentation (developer.4d.com). The Git integration demo is a good illustration of a pattern (driving external CLIs from 4D) that remains fully viable today, including for CI/build tooling embedded in 4D apps. No API in this note has been deprecated; it's a solid, durable reference.
