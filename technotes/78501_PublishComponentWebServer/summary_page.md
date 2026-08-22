# Tech Note 20-11: Publishing a 4D Component on its dedicated Web Server

**Author:** Karim Meghraoui, Technical Support Engineer, 4D Inc.
**Published:** June 29, 2020 | **Product/Version:** 4D v18 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78501
**Download:** https://kb.4d.com/DLTN/TN/2020/20-11_PublishWebFromComponent.zip

## Proposition
Starting with 4D v18R3, each 4D component can run its own independent Web/HTTP Server separate from the host database's. This note demonstrates the pattern by publishing the "ServerAdmin" monitoring component on its dedicated web server, letting administrators check 4D Server status from a browser without competing with the host app's own web publishing.

## Key Points
- **`WEB Server` command**: instantiates and returns a read-only object describing a specific web server (host database, current database, or the server that received the request).
- **`On Host Database Event`**: the required lifecycle hook (must be explicitly authorized by the host database) where a component creates its web server object on startup/shutdown.
- **`.start(options)` / `.stop()`**: member methods that start/stop a server, optionally overriding `HTTPPort`, `HTTPSPort`, `HTTPEnabled`, `HTTPSEnabled`, and `rootFolder` without altering host database web preferences.
- **`WEB Server list`**: returns a collection of every instantiated web server object (host + components), useful for administration/discovery.
- **Port separation requirement**: component web server ports must differ from the host database's web server ports.
- **Component packaging**: the ServerAdmin component ships as an interpreted `.4dbase` plus a `Web` folder placed alongside it in the `Components` folder.

## Featured Technology
- 4D Web Server / HTTP Server object API (`WEB Server`, `WEB Server list`)
- 4D component architecture (`.4dbase`, Components folder)
- `On Host Database Event` component lifecycle method

## Best Practices Highlighted
1. Use distinct HTTP/HTTPS ports per component web server to avoid conflicts with the host database.
2. Explicitly authorize `On Host Database Event` execution in the host database for security.
3. Stop a web server before changing its settings, then restart it — settings cannot be changed on a running server.

## Context / Positioning
This note arrived as 4D was expanding ORDA-era, object-based control over infrastructure (web servers, sessions) rather than relying solely on global database preferences. It reflects 4D's push toward modular, component-based application architecture where reusable admin/utility tools (like a server monitor) can be dropped into any project as a self-contained, independently network-addressable component.

## Historical Commentary
**Status:** Still relevant

The object-based `WEB Server` command family (and `WEB Server list`) introduced around v18R3 remains part of 4D's current language reference with no deprecation notice — this is still the standard way to manipulate per-database and per-component web servers today. The technique of publishing a utility component (like a monitoring dashboard) on its own web server is a durable architectural pattern that predates and survives the Design Mode → Project Mode transition, since it operates purely at the language/component level. One caveat: distribution of components evolved somewhat over later 4D versions (with the introduction of 4D packages/compiled components in some contexts), but the core web-server-per-component mechanism described here is unaffected and still works as documented.
