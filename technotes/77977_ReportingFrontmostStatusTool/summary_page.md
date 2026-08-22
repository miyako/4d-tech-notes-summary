# Tech Note 18-05: Reporting Frontmost Status Tool with 4D

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** March 27, 2018 | **Product/Version:** 4D v16R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77977
**Download:** https://kb.4d.com/DLTN/TN/2018/18-05_ReportingFrontMostStatusTool.zip

## Proposition
Implements a client/server component (RFST) that tracks and reports whether the 4D application is the frontmost, actively-used window on each connected client, using v16R6-era Storage, Workers, and preemptive processing to build a real-time productivity/usage dashboard on 4D Server.

## Key Points
- **Motivating question:** whether a user actually has 4D as the frontmost window matters more than just having the app open, since a minimized/backgrounded 4D isn't truly "in use."
- **Client registration lifecycle:** clients register with the server on connect and unregister on disconnect.
- **Platform-specific frontmost checks:** separate Mac and Windows logic determines whether the 4D client process is currently the frontmost application.
- **CALL Worker for status reporting:** clients send frontmost status updates to the server asynchronously via CALL Worker.
- **Storage object as shared state:** the server maintains registered-client and status data in a Storage object accessible across processes.
- **CALL FORM for live updates:** used to push updates into the RFST monitoring form as new status reports arrive.
- **RFST form UI:** shows In Front, Users, and Time Elapsed columns, opened on 4D Server via a Shift-key shortcut.
- **Full lifecycle wiring:** At Startup/At Exit (client) and On Server startup/On Server shutdown (server) hooks integrate the tool automatically.

## Featured Technology
- Storage object
- Workers (`CALL Worker`)
- Preemptive processing
- `CALL FORM`
- Mac/Windows platform-specific frontmost-window detection

## Best Practices Highlighted
1. Use Storage rather than global variables to hold cross-process/cross-client shared state on 4D Server.
2. Use Workers for asynchronous client-to-server status reporting to avoid blocking client processes.
3. Wire monitoring tools into standard startup/shutdown database methods so they activate automatically without manual intervention.

## Context / Positioning
Published in early 2018, this note showcases 4D's then-recent v16R6 feature set (Storage, Workers, preemptive processes) applied to a real operational concern — usage/productivity monitoring — rather than to core data access. It is representative of the classic, component-based 4D development style of that era, predating Project Mode and ORDA, and focused on server administration tooling rather than end-user application features.

## Historical Commentary
**Status:** Still relevant

Storage, Workers, and preemptive processing are all durable, still-current 4D concepts, and the overall architecture — clients reporting status asynchronously to a server-side Storage object, displayed via CALL FORM — remains a valid pattern for building custom server monitoring tools today. This note has aged well relative to many others from the same era because it deals with infrastructure/process concepts rather than data-access APIs that were later overhauled by ORDA.

The one part that may require periodic revisiting is the low-level, platform-specific code used to detect whether 4D is the frontmost application on Mac vs. Windows, since OS-level APIs and behaviors can shift across macOS/Windows releases — this is a normal maintenance concern for any OS-integration code rather than a sign the underlying 4D technique is obsolete.
