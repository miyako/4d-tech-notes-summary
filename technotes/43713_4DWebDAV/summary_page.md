# Tech Note 06-29: 4D WebDAV

**Author:** Jeremy Sullivan, 4D Evangelist, 4D Inc.
**Published:** July 21, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43713
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_27-30_(JUL)/06-29_4D_WebDAV.zip

## Overview
This note introduces the 4D DAV plug-in, which provides 4D developers with routines to connect to WebDAV servers (including Apple's iDisk service), and presents a fully functional example WebDAV client database built on top of it.

## Key Points
- The 4D DAV plug-in supports all standard WebDAV commands, SSL communication, and connections to Apple's iDisk (.Mac) service.
- Built on the cURL library (libcurl) to handle TCP communication, and works with files directly on disk rather than requiring BLOBs, avoiding memory overhead for large files.
- Positioned as an improvement over manually implementing WebDAV using the low-level Internet Commands plug-in's TCP commands.
- The example database is a complete WebDAV client with connect/browse/download, folder creation, lock/unlock, and delete functionality.
- Includes progress-bar transfer feedback and the ability to cancel uploads/downloads mid-transfer using the plug-in's progress commands.
- Notes that Apple's iDisk does not support file locking, so lock/unlock controls are disabled when connected to iDisk.
- Deleting a folder recursively deletes all of its child files and folders.

## Featured Technology
- 4D DAV plug-in (WebDAV client commands)
- WebDAV protocol
- libcurl / cURL library
- Apple iDisk / .Mac service (client integration)

## Historical Context
Published in 2006 for 4D 2004, this note reflects the era's approach to file-collaboration integration via plug-ins built on C libraries like cURL, well before 4D v11's 2007 SQL engine, Project Mode, or ORDA existed. WebDAV was a relevant protocol for collaborative file editing at the time, and Apple's iDisk was a widely-used consumer cloud storage service.

## Historical Commentary
**Status:** Obsolete

Apple's iDisk/.Mac service was discontinued long ago, so the example client's iDisk integration no longer functions, and the specific 4D DAV plug-in binary described here is tied to a 4D 2004-era plug-in architecture no longer used. WebDAV as a protocol persists in some contexts, but current 4D applications needing similar file-transfer/collaboration features would rely on 4D's expanded native HTTP/network commands or other modern integrations rather than this specific plug-in.
