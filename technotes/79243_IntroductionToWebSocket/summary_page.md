# Tech Note 23-12: Introduction to WebSocket

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** July 24, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79243
**Download:** https://kb.4d.com/DLTN/TN/2023/23-12_WebSocket_r2.zip

## Proposition
Modern web applications increasingly need instant, two-way updates between server and client, but traditional HTTP is stateless and requires inefficient polling to approximate real time. 4D v20 introduces native WebSocket support so 4D Web Server can push and receive updates instantaneously without third-party messaging infrastructure.

## Key Points
- **HTTP vs. WebSocket:** HTTP is stateless (server can only reply to requests); WebSocket keeps a stateful, full-duplex TCP connection open so either side can send at any time.
- **Polling trade-offs:** short polling wastes requests and still has latency; long polling reduces waste but requires the server to track pending requests and handle timeouts — WebSocket avoids both problems.
- **WebSocketServer creation:** `4D.WebSocketServer.new()` must run inside a worker (via `CALL WORKER`) as a persistent process variable, paired with a "ServerHandler" class instance.
- **ServerHandler callbacks:** `onOpen` (server start), `onConnection` (mandatory — must return a ClientHandler instance or Null to reject), `onTerminate`, and `onError`.
- **WebSocketConnection object:** created automatically per accepted client; exposes `.send()`, `.terminate()`, `.handler`, and `.wss` (back-reference to the server).
- **ClientHandler callbacks:** `onOpen` (connection established), `onMessage` (mandatory — receives `.data`), `onTerminate`, `onError`.
- **Example application:** a shared sales "prospect list" where team members flag contacts as busy/available; a `WSServerHandler`/`WSClientHandler` pair broadcasts JSON state to all connected clients on every change.
- **Client-side integration:** plain JavaScript `WebSocket` object (`ws://` URL) combined with the third-party Tabulator.js library to render and interact with the live table in a web area/browser.

## Featured Technology
- **4D.WebSocketServer** — creates and manages a WebSocket server instance and its client connections.
- **4D.WebSocketConnection** — represents and controls an individual client connection (send/terminate).
- **CALL WORKER** — hosts the persistent WebSocketServer process variable.
- **WebSocket protocol** — full-duplex, HTTP-upgrade-based real-time transport.
- **Tabulator.js** — third-party JS table library used to render and edit live data in the demo's web client.

## Best Practices Highlighted
1. Always verify the 4D Web Server is running before creating a WebSocketServer.
2. Instantiate the WebSocketServer inside a worker so the object persists as a process variable across the server's lifetime.
3. Use the `onConnection` handler to validate/authenticate incoming clients via the request's headers/IP before accepting them.

## Context / Positioning
Released with 4D v20, this note reflects 4D's push to modernize its web stack with real-time capabilities that rival Node.js/Socket.IO-style architectures, reducing the need for external messaging middleware and reinforcing 4D Web Server as a full-stack option for live web and mobile applications.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
