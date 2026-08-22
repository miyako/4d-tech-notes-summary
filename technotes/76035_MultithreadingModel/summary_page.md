# Tech Note 10-06: The New Multithreading Model in 4D v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** February 26, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76035
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_04-07_(FEB)/10-06_NewMultithreadingModel.pdf

## Proposition
This note explains the multithreading model of 4D v11 SQL's rewritten data engine — including cooperative vs. preemptive threads and how the Application Server, Web Server, and SQL Server run in separate threads on distinct ports — so developers can understand and benefit from multi-core hardware.

## Key Points
- Defines **threads**, and the distinction between **cooperative** (voluntarily yielding) and **preemptive** (OS-interruptible) threads.
- 4D Server v11 SQL runs its **Application Server, Web Server, and SQL Server simultaneously in separate threads**, transparent to the user.
- Requests route through **different ports**: port 19813/Web requests use a cooperative thread, while ports 19812 and 19814 use preemptive threads.
- Explains threading behavior for **stored procedures** and the **"Execute on Server"** method property.
- Covers how **triggers, indexing, data cache, and backup procedures** are threaded under the new model.
- Discusses resulting **scalability** benefits on multi-core/multi-processor hardware.

## Featured Technology
- 4D v11 SQL multithreading architecture (cooperative and preemptive threads)
- Application Server / Web Server / SQL Server running as separate threads
- Stored procedures and Execute on Server method property
- Multi-core scalability

## Best Practices Highlighted
1. Understand whether a given 4D process is cooperative or preemptive before making assumptions about its execution timing or blocking behavior.
2. Use "Execute on Server" and stored procedures deliberately, understanding which threads they run on relative to client connections.
3. Design applications with the threading model in mind to avoid poor programming decisions that create the impression of a slow, unresponsive application.

## Context / Positioning
Published as 4D v11 SQL's ground-up rewritten multithreaded engine matured, this note gave developers the conceptual foundation to reason about and design for the new architecture underpinning 4D Server's combined Application/Web/SQL server model.

## Historical Commentary
**Status:** Still Relevant

This note explains 4D v11 SQL's then-new multithreaded engine, which let the Application Server, Web Server, and SQL Server run in separate preemptive/cooperative threads on distinct ports to exploit multi-core hardware, while 4D language code itself remained single-threaded/cooperative per process.

This foundational threading model is still substantially the architecture 4D uses today, and understanding cooperative vs. preemptive processes remains directly relevant for performance tuning. It is a still-valid conceptual reference, though later 4D versions have continued to refine scalability (e.g., more granular preemptive process support for compiled code) beyond what is described here.
