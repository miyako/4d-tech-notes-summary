# Tech Note: Executing Functions Between Different Machines

## Overview
- **Technical Note (number unavailable)**
- **Author:** Unknown / not specified
- **Published:** June 1, 2000
- **Product/Version:** 4D Server v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This brief Tech Note demonstrates, via an example, how to execute a task on a different machine within a 4D client-server deployment — specifically, between two separate 4D Client machines, or between a 4D Client and the 4D Server itself — and then retrieve the result of that remote task back on the originating machine. This addresses a fundamental need in distributed 4D architectures of the era: coordinating work across multiple processes and machines, and getting data back from that coordinated work, at a time before 4D had introduced dedicated, purpose-built language commands for exactly this kind of remote execution and result retrieval. The featured technology is 4D's client-server process communication model circa v6.5, illustrating one of the more advanced architectural patterns developers had to construct largely by hand in this period. Because only the teaser abstract for this note survives — its kb.4d.com page had no working download link at all, so no downloadable archive was ever available to recover — the specific example code and exact mechanism used to trigger the remote task and retrieve its result could not be reconstructed here.

## Featured Technology
- EXECUTE ON CLIENT / EXECUTE ON SERVER (era-equivalent)
- 4D Client/4D Server process communication
- Inter-process variables

## Historical Context
This note demonstrates how to trigger a task on a remote machine (between two 4D Clients, or between 4D Client and 4D Server) and retrieve a result back from it — a foundational distributed-execution pattern for classic 4D client-server architecture. The general need (run code elsewhere, get a result back) remains completely valid today, but 4D has since introduced dedicated, more robust language commands for exactly this purpose (executing code on the server or on other client processes and passing results back), making the specific 2000-era mechanism this note likely relied on superseded by cleaner, purpose-built commands.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The old kb.4d.com page had no working download link at all, so no downloadable archive was ever available to recover; this summary is based only on the teaser abstract.

## What's Changed Since
- 4D's language has since added dedicated commands for executing code on the server or other client processes and retrieving results, replacing the more manual inter-process signaling techniques common in this era
- The general architectural need this note addresses — triggering remote execution and retrieving a result — remains a standard requirement in modern 4D client-server applications

