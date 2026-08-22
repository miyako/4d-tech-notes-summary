# Tech Note 15-07: Managing Server Files from the Client

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** April 22, 2015 | **Product/Version:** 4D v14 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77275
**Download:** https://kb.4d.com/DLTN/TN/2015/15-07_FileManager.zip

## Proposition
In a 4D client/server deployment, users often need to view, transfer, or manage files that live on the server. This note builds a self-contained, sandboxed file-browser UI that lets client machines create, upload, download, rename, and delete files/folders on the server, all confined to an administrator-controlled root directory.

## Key Points
- **"Execute on server" is the enabling mechanism:** any 4D method flagged with this property runs on the server when invoked from a client, powering every remote file operation.
- **Custom listbox-based browser:** an array-based listbox with headers/footers/gridlines turned off, showing icon, filename, modified date, and an invisible full-path column.
- **`BROWSER_GET_DIR_ITEMS` server method:** enumerates directory contents via `FOLDER LIST` and `DOCUMENT LIST`, and fetches metadata/icons via `GET DOCUMENT PROPERTIES`/`GET DOCUMENT ICON`, returning results to the client through array pointers.
- **Breadcrumb navigation:** tracks folder depth, letting users drill into subfolders (double-click) and jump back up via breadcrumb clicks.
- **Full file-op coverage:** creating folders, downloading files/folders (including drag-and-drop), uploading files/folders (including drag-and-drop), deleting, and renaming — each documented with its underlying commands.
- **Sandboxed root folder:** the server administrator defines the exposed root directory, controlling exactly what clients can see and manipulate.
- **Appendix with full source:** provides the complete `BROWSER_GET_DIR_ITEMS` method code for reuse.

## Featured Technology
- `Execute on server` method property
- `FOLDER LIST` / `DOCUMENT LIST`
- `GET DOCUMENT PROPERTIES` / `GET DOCUMENT ICON`
- Classic array-based listbox (custom "browser" UI)
- Drag-and-drop file transfer

## Best Practices Highlighted
1. Restrict client-exposed file operations to a single, explicitly controlled root folder rather than the full server filesystem.
2. Run all filesystem-manipulating logic via `Execute on server` methods so clients never touch server files directly.
3. Fetch and cache file metadata (icons, modified dates) server-side in one batch call rather than per-file round trips.

## Context / Positioning
A classic Design Mode-era client/server utility note (v14 R4, 2015), built entirely on 4D's traditional two-tier client/server architecture and classic array-based listbox UI — well before Project Mode, ORDA, or 4D's later web/REST-first deployment patterns.

## Historical Commentary
**Status:** Still relevant

Every command and mechanism referenced — `Execute on server`, `FOLDER LIST`, `DOCUMENT LIST`, `GET DOCUMENT PROPERTIES`/`GET DOCUMENT ICON` — remains fully supported in current 4D, so this pattern still works unchanged for traditional client/server deployments today. That said, as more 4D applications shift toward web/REST-based architectures (via ORDA and 4D's web server), file-management needs are increasingly handled through REST endpoints or cloud storage integrations rather than classic client/server file browsers, making this pattern somewhat less central to modern 4D development even though it remains technically sound.
