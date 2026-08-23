# Tech Note: Taking Advantage of Execute on Server

- **Asset ID:** 33643
- **Tech Note #:** 04-33
- **Published:** August 19, 2004
- **Product / Version:** 4D 2003.4
- **Platform:** Mac & Win
- **Author:** Bertrand Soubeyrand (4D Developer)
- **Page URL:** https://kb.4d.com/assetid=33643
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_31-35_(JUL)/04-33_Execute_on_Server.hqx

## Overview

Written by Bertrand Soubeyrand, this note addresses a common Client/Server performance problem: operations such as large queries or formulas applied across big selections that are not optimized for client/server mode generate heavy network traffic when run on the client. The note's core technique is Execute on server, which behaves like New process except that it launches the named procedure as a process on the server machine rather than the client (falling back to New process-like behavior in a standalone application). Rather than splitting logic into a launcher method and a separate worker method, the note advocates writing a single 'pseudo-recursive' method that branches on Count parameters: called with zero parameters it acts as branch A (the client, which calls Execute on server on itself with a parameter and then polls), and called with a parameter it acts as branch B (the server-side work). Synchronization between the two branches is handled with a DELAY PROCESS/IDLE polling loop reading a shared boolean via GET PROCESS VARIABLE, with a second boolean and further GET/SET PROCESS VARIABLE round-trip ensuring the server doesn't exit before the client has read its results; the note also shows converting an array to a BLOB via VARIABLE TO BLOB (since GET PROCESS VARIABLE cannot fetch arrays directly) to return a record selection from server to client, and cautions against locking the server.

## Key Points

- Execute on server(procedure;stack{;name{;param;...}{;*}}) launches the named procedure as a new process on the server machine (unlike New process, which runs on the client).
- The 'pseudo-recursive method' pattern uses Case of (Count parameters=0) to make one method serve as both the client-side launcher/waiter (branch A, called with no parameters) and the server-side worker (branch B, called with a parameter), keeping both branches visible in one method.
- Branch A polls with Repeat/DELAY PROCESS(Current process;60)/IDLE/GET PROCESS VARIABLE(...B_End;B_End) Until (B_End) to wait for the server process to finish.
- A second synchronization flag (B_Variable_Read) and a further GET/SET PROCESS VARIABLE round trip ensure the server-side process does not terminate (and destroy its variables) before the client has retrieved the results.
- GET PROCESS VARIABLE can retrieve simple variables directly but not arrays; the note demonstrates converting a selection array to a BLOB with VARIABLE TO BLOB on the server and reading it back with the client, then rebuilding the array/selection there.
- An alternative for large or shared results is writing them to a dedicated results table rather than passing BLOBs directly between processes.
- The note explicitly warns to follow 4D's server-locking guidelines when using Execute on server so the technique does not degrade performance for other connected clients.

## Featured Technology

- Execute on server command
- Pseudo-recursive method pattern (Count parameters branching)
- GET PROCESS VARIABLE / SET PROCESS VARIABLE for client-server synchronization
- DELAY PROCESS / IDLE polling loops
- VARIABLE TO BLOB for passing arrays between processes

## Historical Commentary

**Status:** Still Relevant

This note's core recommendation -- using Execute on server to move network-intensive query and formula work onto the server machine, synchronized via GET/SET PROCESS VARIABLE polling -- remains a valid and commonly used pattern in current 4D Client/Server applications, since Execute on server itself is unchanged in the modern language. The 'pseudo-recursive' single-method style shown here is a stylistic choice from that era; many developers today prefer separate named methods for clarity, and 4D has since added additional client/server-aware commands and worker-process patterns, but the fundamental technique of offloading heavy operations to the server process is still directly applicable.

**References to newer/updated information:**
- Execute on server remains part of the current 4D language and is still the standard way to run a procedure on the server machine in Client/Server
- GET PROCESS VARIABLE / SET PROCESS VARIABLE remain valid for inter-process synchronization, though 4D has since added further client/server and worker-process oriented commands
- The single 'pseudo-recursive' method style shown is a stylistic pattern from this era; many developers now prefer separate client and server methods for readability, without changing the underlying Execute on server mechanism
