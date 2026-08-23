# Tech Note: Understanding Processes in 4th Dimension

- **Asset ID:** 25598
- **Tech Note #:** 02-57
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=25598
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-57_Understand_Processes.hqx

## Overview

Jean-Yves Fock-Hoon, 4D Inc.'s Q.A. Manager, provides a broad conceptual explanation of how processes work in 4th Dimension, clarifying upfront that 4D processes are not true OS threads but are cooperatively scheduled within a single underlying thread of execution, alongside the built-in User/Custom menu process (or, on 4D Server, the User Interface, Client Manager, and Cache Manager processes). The note covers how processes are created (New process, Execute on Server, Execute on Client, or via the Custom menu's "Start a new process" option), the distinction between global processes (replicated to the server in Client/Server mode, with full access to tables/selections) and local $-prefixed processes (cheaper, but without record access in Client/Server mode), and the meaning of a process's method, stack size, and title — including the special * parameter to New process that prevents duplicate processes sharing a title. It then explains process lifecycle management: that a process can only end itself (aside from being killed via the Runtime Explorer or 4D Server's window), how to pause it with DELAY PROCESS / PAUSE PROCESS / RESUME PROCESS, and how to manage its windows with HIDE PROCESS / SHOW PROCESS / BRING TO FRONT / Frontmost process, plus how the current user propagates (or doesn't) across new stored procedures and client processes. Inter-process communication is covered via GET PROCESS VARIABLE, SET PROCESS VARIABLE, and VARIABLE TO VARIABLE, and the note ties everything together with a worked example database implementing a simplified runtime process explorer that lists local and server-side (stored procedure) processes, refreshes itself via a self-limiting *-named $RefreshList process, and coordinates a client/stored-procedure handshake using a tri-state ScanPerformed variable to safely retrieve arrays across the client/server boundary.

## Key Points

- 4D processes are cooperatively scheduled within a single underlying OS thread rather than being true preemptive OS threads, coexisting with the built-in User/Custom menu process (or, on 4D Server, the User Interface, Client Manager, and Cache Manager processes).
- Processes can be created via `New process`, `Execute on Server`, `Execute on Client`, or the Custom menu's "Start a new process" checkbox, and are distinguished as global (replicated to the server in Client/Server mode, with full table/selection access) versus local `$`-prefixed processes (cheaper, but without record access in Client/Server mode).
- The `*` parameter to `New process` prevents duplicate processes: if a process with the given title already exists, 4D returns its existing process number instead of creating a new one — used in the example database's self-refreshing `$RefreshList` process.
- A process can only end itself (barring being killed via the Runtime Explorer or 4D Server's window management); lifecycle and window management are handled with `DELAY PROCESS` / `PAUSE PROCESS` / `RESUME PROCESS` and `HIDE PROCESS` / `SHOW PROCESS` / `BRING TO FRONT` / `Frontmost process`.
- Cross-process communication uses `GET PROCESS VARIABLE`, `SET PROCESS VARIABLE`, and `VARIABLE TO VARIABLE` (with negative process numbers addressing stored procedures), demonstrated in a worked example where a 4D Client and a stored procedure coordinate array retrieval using a tri-state `ScanPerformed` handshake variable to avoid disrupting the user's current selection mid-refresh.

## Featured Technology

- 4D's cooperative (non-preemptive) process model, distinct from OS threads
- New process / Execute on Server / Execute on Client for process creation
- Global vs. local ($-prefixed) processes and Client/Server replication implications
- Process stack size, title, and the * unique-process-name convention
- DELAY PROCESS / PAUSE PROCESS / RESUME PROCESS and HIDE/SHOW PROCESS/BRING TO FRONT
- Inter-process communication via GET PROCESS VARIABLE / SET PROCESS VARIABLE / VARIABLE TO VARIABLE
- PROCESS PROPERTIES-based runtime explorer example

## Historical Commentary

**Status:** Superseded

This note remains a genuinely useful, clearly written explanation of 4D's classic cooperative process model — global vs. local processes, stack sizing, the * unique-process trick, and safe cross-process variable exchange via GET/SET PROCESS VARIABLE — concepts that still describe how 4D processes behave today and are essential for reading or maintaining legacy 4D code. However, 4D has since introduced true preemptive multithreading via worker processes (added in later 4D versions well after 2002), giving developers a genuinely concurrent execution model alongside the cooperative process system this note describes, so a developer working with current 4D needs to layer that newer worker/thread model on top of the concepts taught here rather than relying on this note alone.

References to newer/updated information:
- 4D introduced true preemptive multithreading with worker processes in later versions, extending beyond the purely cooperative process model this 2002 note describes
- The core process concepts here (global vs. local processes, GET/SET PROCESS VARIABLE, DELAY/PAUSE/RESUME PROCESS) remain accurate for 4D's classic process model and are still relevant for understanding legacy 4D code
