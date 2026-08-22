# Tech Note 16-21: Access Files in 4D using 4D Mobile

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** November 22, 2016 | **Product/Version:** 4D Mobile v15.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77685
**Download:** https://kb.4d.com/DLTN/TN/2016/16-21_AccessFilesThru4DMobile.zip

## Proposition
4D BLOB fields and disk-based documents can be exposed to 4D Mobile web clients, but JavaScript's BLOB representation differs from 4D's, requiring conversion into a proper File object before a browser can meaningfully use the data. This note explains the Wakanda File API and demonstrates the full round-trip for both database-stored and disk-stored files.

## Key Points
- **BLOB vs File distinction:** JavaScript's Blob is an immutable raw-data object; Wakanda's File class inherits from Blob but adds file-system semantics (path, save, move, rename, remove).
- **W3C File API compliance:** the Wakanda File class follows the W3C File API spec for HTML5, giving it standard, browser-familiar semantics.
- **BLOB methods:** `copyTo()`, `slice()`, `toBuffer()`, and `toString()` are available for manipulating Blob content.
- **Server-side conversion:** BLOBs retrieved from a 4D data field are converted into File objects using `copyTo()` in Wakanda server-side JavaScript.
- **Disk file access:** files stored on the 4D server's disk (outside the database) are read and Base64-encoded in 4D methods so they can cross the HTTP/text-based protocol boundary.
- **Client-side decode/download:** the client-side JavaScript decodes the Base64 payload and reconstructs a downloadable file for the end user.

## Featured Technology
- 4D Mobile / Wakanda Application Framework
- Wakanda File and Blob JavaScript classes
- W3C File API (HTML5)
- Base64 encoding for BLOB transport over HTTP

## Best Practices Highlighted
1. Always convert a Blob to a File object (via `copyTo()`) before attempting file-system operations like save, move, or rename.
2. Base64-encode binary data before transmitting it through text-based HTTP/REST channels between 4D and the web client.

## Context / Positioning
Published in November 2016 for 4D Mobile v15.3, this note documents 4D's native mobile/web app framework of that era — built on the bundled Wakanda server — which existed as a separate stack from classic 4D desktop development, well before ORDA matured (~2017+) as the unified data-access layer for both desktop and web/mobile 4D development.

## Historical Commentary
**Status:** Obsolete

4D Mobile and the underlying Wakanda engine were discontinued as 4D consolidated its web/mobile strategy around ORDA and REST APIs, and later the Qodly low-code platform. The specific Wakanda File/Blob JavaScript classes, and the entire client/server split described in this note, no longer exist in current 4D.

File access for modern 4D web/mobile clients today would be implemented through standard REST endpoints (serving files as HTTP responses) or ORDA-based methods returning Base64 or binary payloads directly, without any dependency on the Wakanda-specific APIs this note relies on. It stands as a useful historical record of 4D's mid-2010s mobile strategy rather than an actionable current-day integration guide.
