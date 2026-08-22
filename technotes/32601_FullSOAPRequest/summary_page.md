# Tech Note 04-19: Reading a Full SOAP Request

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** May 13, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32601
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_16-20_(APR)/04-19_Full_SOAP_Request.exe

## Overview
This Tech Note covers 4th Dimension 2003 and later's ability to publish 4D methods as Web Services, letting any Web Services-enabled application, tool, or development environment integrate with 4D by sending SOAP (Simple Object Access Protocol) messages to the native 4D Web server. As with SOAP responses on the client side, 4D's Web Service publishing system by default automatically handles the complex parsing, navigation, and conversion between XML/SOAP formats and native 4D data types dictated by the SOAP/XML standards. The note explains that developers sometimes need or prefer to read the raw incoming SOAP request message directly, and demonstrates how to do this using an undocumented behavior of the GET WEB FORM VARIABLES command, alongside reading incoming HTTP headers via the GET HTTP HEADER command when needed. This reflects the early-2000s SOAP/XML-web-services era in which 4D positioned its native Web server as both a SOAP client and a SOAP service publisher, letting 4D methods act as backend services for external SOAP-based callers well ahead of REST becoming the dominant lightweight alternative. It targets 4D developers publishing Web Services from 4D who need lower-level access to incoming SOAP request data than the default automatic conversion exposes.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- A guide to reading raw incoming SOAP messages sent to 4th Dimension's native Web Service publishing system, using an undocumented behavior of GET WEB FORM VARIABLES, plus reading HTTP headers with GET HTTP HEADER.

## Featured Technology
- GET WEB FORM VARIABLES
- GET HTTP HEADER
- SOAP (Simple Object Access Protocol)
- 4D native Web Service publishing

## Historical Context
**Status:** superseded

This note documents a low-level, partly undocumented technique (via GET WEB FORM VARIABLES) for reading raw incoming SOAP requests in 4th Dimension's native Web Service publishing system, reflecting the SOAP-centric web-services standard dominant in the early-to-mid 2000s. SOAP-based service publishing has since been broadly superseded industry-wide, and within 4D specifically, by REST APIs (especially via ORDA, introduced 2017+) as the primary way to expose 4D data and logic to external callers, though 4D's classic SOAP publishing commands likely remain available for legacy compatibility.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
