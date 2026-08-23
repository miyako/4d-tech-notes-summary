# Tech Note: Creating Referer Logs with 4D Web Server

- **Asset ID:** 11981
- **Tech Note #:** 00-57
- **Published:** December 1, 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Eric Saltzen
- **Page URL:** https://kb.4d.com/assetid=11981
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_56-60_(DEC)/00-57_Referer_Logs.hqx

## Overview

Eric Saltzen (4D Inc. Technical Support) shows how to capture the HTTP "Referer" header with 4th Dimension's web server using the new v6.7 GET HTTP HEADER command, storing referring-page data in a table and optionally writing it to a standard-format log file for analysis with tools like Analog.

## Key Points

- Referer information (`Referer: http://...`) is sent by browsers inside HTTP request headers and identifies the page a visitor clicked a link from; it cannot be seen via "View Source" since it's part of the HTTP header, not the HTML payload.
- The sample pair — 67RefererGrab (published on port 8080, "Start without Context") and 67LinkerSample (port 80, with linker.html/sublinker.html hard-linking to 127.0.0.1) — lets the Referer mechanism be tested entirely on one machine without an external referring site.
- index.shtml embeds a `<!--4DSCRIPT/RefererGrabber-->` tag; any page wanting Referer tracking must include this tag and use the `.shtml` extension so 4D processes its server-side include.
- The On Startup method sets two preference flags: `<>refererDiagnosticMode` (store the entire HTTP header text per hit) and `<>refererLogFile` (also append entries to a "RefererLog" file in the standard web-log format).
- The RefererGrabber project method calls `GET HTTP HEADER(nameArray; valueArray)` to retrieve all header name/value pairs, then uses `Find in array` to locate "Referer" and "X-URL" entries — noting that $1/$2 aren't available here since this runs as a 4DSCRIPT preprocessing call, not a direct 4DACTION URL call.
- Matched Referer/date/time/URL data is stored in an `[HTTP_Requests]` table via `CREATE RECORD`/`SAVE RECORD`, and if `<>refererLogFile` is set, a "referer -> url" line is appended to the RefererLog file using `Append document` and `SEND PACKET`, matching the format standard web server logs use so any log analysis tool can process it.

## Featured Technology

- GET HTTP HEADER command (4D v6.7)
- 4DSCRIPT HTML tags for server-side page preprocessing
- .shtml server-side-include pages
- Find in array for parsing HTTP header name/value arrays
- Append document / SEND PACKET for writing a standard web server log file
- HTTP Referer header capture and analysis

## Historical Commentary

**Status:** Partially superseded

This note shows how to use 4D v6.7's new GET HTTP HEADER command inside a 4DSCRIPT-triggered project method to capture the HTTP Referer header from incoming requests, store it in a table, and optionally append it to a standard-format RefererLog file analyzable by tools like Analog. GET HTTP HEADER remains a valid, still-supported 4D web server command for low-level HTTP header inspection, so the core technique still works, but this kind of traffic-source analytics is now overwhelmingly handled by external, much more capable analytics platforms (server access logs, Google Analytics-style JS trackers, etc.) rather than hand-rolled in-database Referer logging, making the specific use case here a historical curiosity even though the underlying command is not obsolete.

**References to newer/updated information:**
- GET HTTP HEADER remains part of the current 4D language for inspecting HTTP request headers from the 4D web server
- Modern web traffic and referrer analysis is typically handled by dedicated web analytics tools rather than hand-built 4D log parsing as shown in this note
