# Tech Note: Connecting to a 4D Server

- **Asset ID:** 27787
- **Tech Note #:** 02-32
- **Published:** July 31, 2002
- **Product / Version:** 4D 6.8.3
- **Platform:** Mac & Win
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=27787
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_30-35_(JUL)/02-32_Connecting_to_Server.hqx

## Overview

Christian Cypert (4D & WebSTAR Plug-in Evangelist) documents the full connect/use/disconnect lifecycle for programmatically connecting a 4D Client or standalone 4th Dimension application to a specific 4D Server using the 4D Open plug-in.

## Key Points

- `OP Count network components` plus a loop over `OP Get network component info` enumerate the network protocols/components available on the local machine, building parallel arrays of component IDs and names for the user to pick from.
- `OP Set option(2;0)` suppresses 4D Open's built-in error dialogs so the application can handle errors itself.
- `OP Load network component` activates the chosen network component before a server can be located; `OP Select 4D Server` presents a server-selection UI and returns the server name/ID, while `OP Find 4D Server` is the alternative when the target database name is already known.
- `OP Open connection(ServerID; ConnectionID; "Display Name"; "UserName"; "Password"; "Process Name")` establishes the actual connection, authenticating against the target server's 4D Users and Groups and creating a named process on the 4D Server.
- Teardown must happen in a specific order: `OP Close connection` closes the 4D Open session, `OP Delete 4D Server` frees the memory holding server reference information, and `OP Unload network component` releases the network component that was loaded earlier.
- The note is built entirely around three demo buttons ("Network Component Info", "Connect to 4D Server", "Disconnect to 4D Server") that map directly onto these three lifecycle stages.

## Featured Technology

- 4D Open plug-in
- OP Count network components / OP Get network component info
- OP Select 4D Server / OP Find 4D Server
- OP Open connection
- OP Close connection / OP Delete 4D Server / OP Unload network component

## Historical Commentary

**Status:** Obsolete

The 4D Open plug-in and its OP-prefixed connection API were the standard, and at the time only, way to programmatically connect a client application to a specific 4D Server outside of 4D's normal interactive connection dialog. This entire mechanism is now obsolete: current 4D applications rely on the built-in remote/client-server architecture for interactive sessions, and on ORDA remote datastores (introduced in 4D v17+) for programmatic cross-database access, neither of which requires a separate connectivity plug-in or the manual network-component enumeration shown here.

**References to newer/updated information:**
- 4D's native client-server architecture and ORDA remote datastores have superseded the 4D Open plug-in for connecting to remote 4D Servers
- Programmatic cross-database access today is done via ORDA remote datastores rather than the OP Open connection-based API described in this note
