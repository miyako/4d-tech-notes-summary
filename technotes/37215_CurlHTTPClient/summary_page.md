# Tech Note: cURL - HTTP Client, Get and Post, FTP and Much More, Using 4D 2004

- **Asset ID:** 37215
- **Tech Note #:** 05-18
- **Published:** May 10, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thomas Maul
- **Page URL:** https://kb.4d.com/assetid=37215
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_17-20_(MAY)/05-18_cURL_and_4D_2004.hqx

## Overview

Thomas Maul (General Manager, 4D Germany) demonstrates driving the free cURL command-line tool from 4D 2004's new LAUNCH EXTERNAL PROCESS command to perform HTTP(S) GET/POST, cookie/session handling, and FTP(S) operations — an alternative to building a dedicated plug-in — illustrated with progressively more advanced demos culminating in an automated Google Image search.

## Key Points

- cURL is invoked via 4D 2004's new `LAUNCH EXTERNAL PROCESS` command through `RunCurl` (text results) and `RunCurlBlob` (binary results such as PDFs/images, avoiding the 32 KB text limit) project methods, which handle platform differences between Mac OS X (preinstalled) and Windows (bundled via the "4D Extras" folder).
- Demo 1 performs a simple GET (`vResult:=RunCurl(vURL)`); Demo 2 performs an HTTP POST against a real EU VAT-number-validation service, manually building the POST body (`-d "Lang=EN&MS=..&ISO=..&VAT=.."`) and parsing the plain-text response for validity phrases — with a walkthrough of using Firefox's "View Page Info" to discover a target form's real field names.
- Demo 3 automates a Google Image search end-to-end: acquiring cookies with `-b cookies.txt -c cookies.txt`, spoofing a User-Agent and Referrer (`-A`, `-e`) to satisfy anti-bot checks, encoding the search term (Mac to ISO, `ConvertStringToURL`), scraping result image URLs by locating the `<a href=/imgres?imgurl=` marker in the returned HTML, and fetching thumbnails one at a time in an `On Timer` loop via `RunCurlBlob` to avoid freezing the UI — explicitly noted as an educational example only, given Google's terms of service.
- Positions LAUNCH EXTERNAL PROCESS as advantageous over building a compiled plug-in around the cURL library: upgrading cURL is just replacing the executable, with no recompilation needed and reduced exposure to 4D/OS/library version changes.
- Windows installation guidance: bundle curl.exe (v7.13.2 Non-SSL tested) in the 4D Extras folder, retrieved at runtime via `Get 4D folder(Extras Folder)`, with an optional separate OpenSSL-based build for HTTPS.
- Recommends packet-sniffing tools — Ethereal/MacSniffer (cross-platform, free) and HTTPLook (commercial, Windows) — for diagnosing cookie/referrer/User-Agent issues that are otherwise invisible when shelling out to curl.

## Featured Technology

- LAUNCH EXTERNAL PROCESS command (4D 2004)
- cURL command-line HTTP(S)/FTP(S) client
- Cookie-jar session persistence (-b/-c)
- User-Agent and Referrer spoofing (-A/-e)
- HTTP POST form automation
- MacRoman-to-URL character encoding
- On Timer-driven incremental binary downloads via RunCurlBlob

## Historical Commentary

**Status:** Superseded

This note shows an inventive way to gain full-featured HTTP(S)/FTP(S) client capability in 4D 2004 without writing a plug-in, by shelling out to cURL via the then-new LAUNCH EXTERNAL PROCESS command — impressively handling cookies, POST forms, and User-Agent spoofing entirely through command-line flags and text parsing. This shelling-out approach became largely unnecessary once 4D introduced native HTTP Client commands (4D v13, 2012) that provide the same GET/POST/cookie/auth capabilities directly in the language. LAUNCH EXTERNAL PROCESS itself, however, remains a valid and still-used 4D command for invoking other external command-line tools.

**References to newer/updated information:**
- 4D introduced native HTTP Client commands (HTTP Request and related APIs, added in 4D v13, 2012) providing built-in GET/POST/cookie/auth support without shelling out to cURL
- LAUNCH EXTERNAL PROCESS itself remains part of the current 4D language and is still commonly used to invoke external command-line tools for other integration needs
