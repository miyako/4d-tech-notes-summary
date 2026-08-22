# Tech Note 98-27: Preventing Web Page Caching with ACI Pack

**Author:** Not specified in source document
**Published:** August 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11810
**Download:** Not available

## Proposition
This Tech Note describes how to use ACI Pack's AP SET WEB FILTERS command to inject EXPIRES meta-tags into 4D-served web pages, preventing browsers from showing cached versions.

## Key Points
- Uses ACI Pack's AP SET WEB FILTERS to filter outgoing HTML
- Inserts EXPIRES meta-tag into HTML headers
- Prevents browsers from displaying stale cached pages
- Browser must support the EXPIRES meta-tag for the technique to work
- Relevant for dynamic, database-driven web content served by 4D

## Featured Technology
- ACI Pack
- AP SET WEB FILTERS
- Web Caching
- EXPIRES Meta-tag
- 4D Web Server

## Context / Positioning
Web caching was a significant usability concern for dynamic database applications served via 4D's web server. ACI Pack provided extended web publishing capabilities that complemented 4D's built-in web server.

## Historical Commentary
**Status:** Obsolete

Web page caching control remains a relevant concern in web development, though the approach of using a plug-in command (ACI Pack) to inject meta-tags into HTML responses is very much a product of its time. Modern 4D handles HTTP headers directly through built-in web server commands, and cache control is now managed via standard HTTP headers rather than HTML meta-tags.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
