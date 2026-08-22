# Tech Note 22-22: A First Preview of the Updated Web Monitoring Component

**Author:** Cédric Gareau, Technical Services Engineer, 4D SAS & Marouane AIT SALAH, Technical Services Engineer, 4D Morocco
**Published:** November 30, 2022 | **Product/Version:** 4D v19 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79059
**Download:** https://kb.4d.com/DLTN/TN/2022/22-22_WebMonitoring.zip

## Proposition
For headless 4D Server deployments without a visible admin window, this component exposes a web-based dashboard (users, processes, memory, settings) built as a 4D component with its own dedicated web server, refreshed to use newer 4D v19 R6 server APIs and worker-based actions.

## Key Points
- **Requires "Execute on host database event method of the components"** enabled in host database settings, plus a server restart, before the component becomes active.
- **Runs on its own dedicated web server** via the WEB Server command/object, made possible by 4D's multi-web-server support since 18 R3 — it doesn't share the host app's main web server.
- **On Host Database Event registers route definitions** as shared objects under Storage.obWebAPI (e.g. /admin/ini, /admin/users, /admin/processes, /admin/settings), each mapped to a static file or a method.
- **GET MEMORY STATISTICS and Get process activity** power the Dashboard and Processes pages, returning structured data later serialized with JSON Stringify.
- **Administrative actions (drop user, send message, abort process) run via CALL WORKER**, executing cooperatively rather than blocking the requesting web process.
- **Shared objects require Use()/End use()** when modifying Storage-scoped data from within the component's event handler.
- **Explicitly described as a customizable starting point**, intended to be extended by developers as new 4D Server releases add capabilities.

## Featured Technology
- Web Monitoring component
- WEB Server (multiple web servers, 18 R3+)
- On Host Database Event
- GET MEMORY STATISTICS
- Get process activity
- CALL WORKER
- Shared objects (Storage)

## Best Practices Highlighted
1. Enable a dedicated component web server rather than reusing the host application's main web server, to avoid routing conflicts and let the monitoring UI run independently.
2. Use CALL WORKER for administrative actions like dropping sessions so the web request thread isn't blocked while the action completes.

## Context / Positioning
Published under 4D v19 R6 (late 2022), this note shows 4D's technical support team maintaining and modernizing a long-lived community/blog-sourced tool rather than shipping a fully native, first-party monitoring UI — reflecting how 4D Server administration tooling has historically evolved through sample components and technical notes rather than as a core product feature.

## Historical Commentary
**Status:** still relevant

As a sample/community component (not a core 4D product feature), this specific web-monitoring implementation is not guaranteed to be maintained long-term, and organizations should check whether a newer revision exists before adopting the 2022 version verbatim. That said, the underlying APIs it relies on — WEB Server, Get process activity, GET MEMORY STATISTICS, CALL WORKER, On Host Database Event — are all still current, actively used 4D Server administration and worker APIs, so the architectural approach remains valid even if this exact component build has since been superseded by further "previews" or by customers' own extensions.
