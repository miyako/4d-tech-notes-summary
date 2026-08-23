# Tech Note: Reading a Full SOAP Response

- **Asset ID:** 32705
- **Tech Note #:** 04-20
- **Published:** May 20, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=32705
- **Download:** https://kb.4d.com/ftp://@ftp.4D.com/ACI_TECHNICAL_NOTES/2004/MacOS/TN_2004_16-20_(APR)/04-20_Full_SOAP_Response.hqx

## Overview

David Adams explains how to retrieve the complete, raw SOAP response body from a 4th Dimension Web Service call using CALL WEB SERVICE's "Web Service Manual Out" argument, instead of relying on 4D's automatic SOAP-to-native-type binding, for debugging, learning, and handling values not automatically exposed.

## Key Points

- By default, `CALL WEB SERVICE` with the `Web Service Dynamic` argument automatically parses the SOAP response, and results are read individually via `GET WEB SERVICE RESULT` calls keyed to named output elements (e.g. `outSecondsSinceMidnight`, `outPi`, `outServerVersion`).
- Passing `Web Service Manual Out` instead returns the entire SOAP response message body as a single BLOB via `GET WEB SERVICE RESULT(proxy_fullResponse_blob;*)`, which can be parsed with `Parse XML variable` or copied to text if small.
- The note shows extracting individual values from the manual BLOB using the companion XML_Utilities component's `xutil_GetValue` function, converting text results with `Num()` where numeric values are needed.
- Advantages of manual mode include easier debugging when a SOAP server renames/adds/removes elements, avoiding the errors `GET WEB SERVICE RESULT` throws for missing elements, and reusing existing XML-processing code for both SOAP and non-SOAP XML.
- Limitations: the manual BLOB captures only the SOAP message body, not the full SOAP message (headers aren't retrievable), HTTP-level cookies/status codes aren't accessible either, and a SOAP fault response returns no results under either technique.
- The note cross-references TN 04-19 ("Reading a Full SOAP Request") and TN 04-21 ("The XML_Utilities Component") as companion pieces covering the request side and the value-extraction tooling, respectively.

## Featured Technology

- CALL WEB SERVICE command with Web Service Manual Out argument
- GET WEB SERVICE RESULT (dynamic vs. manual/full BLOB modes)
- Web Service Dynamic vs. Web Service Manual Out constants
- Parse XML variable on a raw SOAP response BLOB
- XML_Utilities component (xutil_GetValue) for manual value extraction
- SOAP debugging and fault handling

## Historical Commentary

**Status:** Superseded

This note explains how to bypass 4th Dimension's automatic SOAP response binding and instead retrieve the complete raw SOAP message body as a BLOB, by calling `CALL WEB SERVICE` with the `Web Service Manual Out` argument instead of `Web Service Dynamic`, then parsing it manually with `Parse XML variable` or the companion XML_Utilities component. This was a genuinely useful debugging and flexibility technique in the SOAP era, letting developers see server-added/renamed elements and read values not bound to declared parameters. SOAP itself has since been broadly superseded by REST and JSON as the default web-service integration approach industry-wide, and 4D's own strategy shifted decisively to REST/ORDA (2017+), though the `CALL WEB SERVICE` command and this manual-parsing technique likely still function in current 4D for legacy SOAP integrations.

**References to newer/updated information:**
- REST and JSON have broadly replaced SOAP as the dominant web-service integration standard industry-wide
- 4D's own web-services strategy has shifted to REST APIs built on ORDA (introduced 2017+), alongside continued support for legacy SOAP-based commands like CALL WEB SERVICE
