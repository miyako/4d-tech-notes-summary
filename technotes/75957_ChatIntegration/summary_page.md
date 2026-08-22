# Tech Note 09-44: Chat Integration in 4D v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** November 25, 2009 | **Product/Version:** 4D v11.5 SQL | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75957
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_41-45_(NOV)/09-44_ChatIntegration.zip

## Proposition
Shows 4D v11 SQL developers how to build a client-to-client chat feature (distinct from 4D Server's admin-only "send message" tool) using a Web Area for the UI and server-hosted shared arrays plus timer polling for message delivery.

## Key Points
- **Chat UI is a 4D Web Area** rendering an HTML page (`Chat.html`) with custom CSS classes (`.send`/`.received`/`.messageSend`/`.messageReceived`) to visually distinguish sent vs. received messages.
- **JavaScript `addChat` function**, invoked via `WA EXECUTE JAVASCRIPT FUNCTION`, dynamically appends new message `div`/`p` elements to the page and auto-scrolls the Web Area.
- **Client naming**: each connected client registers with a unique name (machine name + user name), listed in a List box for selecting a chat partner; each chat session runs in its own process.
- **Server-side storage**: `Ch_sendText` (Execute on Server) stores each message plus a read/unread boolean into two-dimensional shared arrays (`<>message_at_at`, `<>message_read_ab_ab`) keyed by a `Caller-Called` chat identifier tracked in `<>chatClients_at`.
- **Delivery mechanism**: `EXECUTE ON CLIENT` immediately notifies the target client's process to open a chat window if needed; an `On Timer` event on each client periodically calls `Ch_getText` (Execute on Server) to retrieve unread messages, serialized through a `BLOB`/array round trip.
- **Cleanup**: `Ch_DeleteChat` removes a conversation's messages from the server arrays when the chat window is closed.
- A sample database, `Chat.4dbase`, demonstrates the full two-client conversation flow.

## Featured Technology
- 4D Web Area (HTML/CSS/JavaScript rendering)
- WA EXECUTE JAVASCRIPT FUNCTION
- EXECUTE ON CLIENT / Execute on Server method property
- Blob-based array serialization (VARIABLE TO BLOB / BLOB TO VARIABLE)
- On Timer form event polling

## Best Practices Highlighted
1. Use `Execute on Server` methods to centralize shared mutable state (message arrays) rather than trying to synchronize per-client copies.
2. Track only unread messages per client via a boolean flag to minimize redundant delivery.
3. Separate presentation (Web Area + CSS/JS) from data transport (blob-serialized arrays) so the chat's look and feel can be customized independently.

## Context / Positioning
Published as 4D v11 SQL was maturing, this note showcased how far a developer could get building near-real-time collaborative features using only the client/server language primitives available at the time (Web Areas, Execute on Server/Client, timers) — without any dedicated messaging or push infrastructure.

## Historical Commentary
**Status:** Partially Superseded

This note builds a real-time-feeling chat feature entirely from 4D v11 SQL primitives: a Web Area for rendering, client/server round-trips through `EXECUTE ON CLIENT` and Execute-on-Server methods, and `On Timer` polling to simulate push updates, since 4D had no publisher/subscriber or WebSocket mechanism at the time. The polling-and-shared-array architecture is a clever workaround but is inherently laggy and non-scalable compared to what's available now.

Modern 4D includes native WebSocket client/server commands and worker-process messaging (`CALL WORKER`), introduced in later v16-v18 releases, which would replace this timer-polling approach entirely for real-time delivery; the Web Area's rendering engine has also since moved to a modern Chromium-based component (4D v15+), making the CSS/JS techniques shown still valid but the underlying engine quite different from 2009.
