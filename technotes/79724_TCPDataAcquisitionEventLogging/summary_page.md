# Tech Note 25-05: TCP Data Acquisition and Event Logging

**Author:** Anouar Moustarih, Technical Services Engineer, 4D Morocco
**Published:** May 30, 2025 | **Product/Version:** 4D v20 R8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79724
**Download:** https://kb.4d.com/DLTN/TN/2025/25-05_SendTCPData.zip

## Proposition
Networked applications increasingly need to talk directly to external TCP/IP servers and devices, but building reliable, non-blocking connection handling in 4D historically required low-level plugin work. This note shows how the new TCPConnection and TCPEvent classes make asynchronous TCP client communication and event logging straightforward and thread-safe.

## Key Points
- **4D.TCPConnection manages the socket lifecycle:** Instantiated with a URL, port, and a handler object, it supports both synchronous and asynchronous data exchange with a remote server.
- **4D.TCPEvent encapsulates event context:** Each event carries a type (connection, data, error), the remote IP/port, and any received payload data.
- **Five async callbacks drive the design:** onConnection, onShutdown, onData, onError, and onTerminate let the app react to lifecycle events without polling or blocking.
- **Class-based wrapper pattern:** The example wraps connection/url/port as class properties with connect(), disconnect(), sendPacket(), and getInfo() methods for a clean, reusable API.
- **Fragmented data handling is required:** TCP delivers data in order but not necessarily in single packets, so onData must be written to reassemble fragmented messages.
- **Demo relies on 4D Internet Commands:** The accompanying application uses TCP_Listen to create the listening socket side for the demonstration, requiring 20R8 build 100353+.
- **Forward-looking roadmap note:** 4D.TCPListener (from 20 R9) is called out as the coming server-side counterpart for accepting incoming TCP client connections.

## Featured Technology
- **4D.TCPConnection** — new async/sync TCP client connection class.
- **4D.TCPEvent** — event object describing connection/data/error occurrences.
- **4D.TCPListener** — upcoming (20 R9) class for TCP server-side connection acceptance.
- **4D Internet Commands (TCP_Listen)** — plugin commands used for the demo's listening socket.
- **BLOB to text** — conversion of received binary payloads into readable text.

## Best Practices Highlighted
1. Always design onData handlers to tolerate fragmented/partial packet delivery.
2. Use the async event-driven pattern rather than blocking calls to keep the application responsive.
3. Keep connection state (url, port, connection object) encapsulated in a dedicated class for reuse.

## Context / Positioning
This note reflects 4D's ongoing modernization of its networking stack, moving core TCP/IP capability from third-party plugins into first-class, object-oriented 4D language classes — part of a broader trend (seen alongside ORDA and class-based language features) of giving developers thread-safe, asynchronous building blocks natively in 4D.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
