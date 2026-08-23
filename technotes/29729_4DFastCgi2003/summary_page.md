# Tech Note: 4D FastCGI 2003

- **Asset ID:** 29729
- **Tech Note #:** 03-27
- **Published:** June 26, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=29729
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_26-30_(JUN)/03-27_4D_FastCGI_2003.hqx

## Overview

David Adams documents the 4D FastCGI 2003 component, which allows 4D, 4D Client, or 4D Server to act as a persistent, high-performance FastCGI application server -- avoiding the per-request process-spawn cost of classic CGI and the server lock-in of proprietary APIs like ISAPI, NSAPI, or WSAPI.

## Key Points

- Frames FastCGI's benefits as language independence, server independence (works with any major web server on any platform), machine independence (the 4D process can run remotely from the web server), and increased performance via persistent processes that avoid per-request startup cost.
- Explains that FastCGI messages, though conceptually similar to HTTP, use a distinct binary-safe message format capped at roughly 65,000 bytes per message, with the component transparently chunking larger responses (documents, images) across multiple messages.
- Core API demonstrated: `FCGI_Accept` blocks for and receives an incoming FastCGI request; `FCGIRequest_ValueGetByName("REQUEST_URI")` reads request parameters; `FCGIResponse_SetContentType`, `FCGIResponse_AddBLOB`, and `FCGI_Reply` construct and send the response.
- Sample code returns a binary image response by converting a stored PICT resource with `PICTURE TO GIF` into a BLOB and streaming it back via `FCGIResponse_AddBLOB`/`FCGI_Reply`.
- Installed as a 4D Insider component requiring a compatible 4D Internet Commands plug-in; compatible with 4D, 4D Client, and 4D Server.
- Requires the 4D Extension License (WEL) for unrestricted use -- without it, the component stops handling FastCGI requests after roughly one hour until the database is restarted.
- Notes FastCGI as a complementary integration path to WebSTAR alongside 4D's existing 4DLINK and 4DCONNECT WebSTAR integrations, particularly relevant given WebSTAR's own added FastCGI support.

## Featured Technology

- FastCGI protocol
- 4D FastCGI 2003 component
- FCGI_Accept / FCGI_Reply
- FCGIRequest_ValueGetByName
- FCGIResponse_SetContentType / FCGIResponse_AddBLOB
- 4D Extension License (WEL)

## Historical Commentary

**Status:** Obsolete

FastCGI integration was a smart way in 2003 to let 4D scale behind serious Unix web servers like Apache without the overhead of spawning a process per request, and the component's design (persistent process, binary-safe messages, WEL licensing gate) reflects real production concerns of the era. Today this specific integration path is essentially obsolete: 4D's own mature built-in web server (and, more recently, ORDA/REST-based application delivery via Qodly) has long superseded the need for external CGI/FastCGI bridging in the vast majority of 4D deployments. The underlying lesson -- avoid per-request process spawning for performance -- remains valid systems-design wisdom even though the specific FastCGI component described here is no longer part of typical 4D architecture.

**References to newer/updated information:**
- 4D's own built-in web server has long superseded the need for external CGI/FastCGI-based web integration in typical 4D deployments
- Modern 4D applications more commonly expose REST/ORDA endpoints (including via Qodly) rather than bridging through FastCGI to a separate web server process
