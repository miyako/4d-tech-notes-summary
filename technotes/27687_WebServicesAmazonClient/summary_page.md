# Tech Note: Web Services and 4D Internet Commands, the Amazon.com client

- **Asset ID:** 27687
- **Tech Note #:** 03-14
- **Published:** March 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=27687
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_11-15_(MAR)/03-14_Web_Services_and_4DIC.hqx

## Overview

Written by Frank Chang of 4D Inc. Technical Support, this Tech Note builds an Amazon.com Web Services client in 4D 2003 that searches Amazon's catalog for books by author, CDs by artist, and movies by actor using the Amazon Web Services SOAP SDK, and also displays the raw request/result XML for inspection. The note explains SOAP fundamentals — RPC versus DOC communication modes and simple versus complex data types — and shows that the Amazon service uses DOC mode, requiring the 4D developer to hand-build the XML request as a BLOB, send it via 4D 2003's new Web Services client, and manually parse the returned result BLOB. The core methods, parse_AmazonSearchResult_XML and Amz_Parse_Picture, use Parse XML variable together with Get First/Next XML element to walk the SOAP response, pulling out fields like ProductName, Manufacturer, and ImageUrlMedium into 4D arrays via a Case of dispatch on element name. For product images, rather than relying on the Web Services layer, the example switches to the separate 4D Internet Commands plug-in: it opens a raw TCP connection to the image host with TCP_Open, hand-crafts an HTTP/1.0 GET request as a BLOB, sends it with TCP_SendBLOB, loops on TCP_ReceiveBLOB to assemble the full response, strips the HTTP header text, and converts the remaining BLOB to a picture with Blob to Picture (falling back to a default picture if the download failed or returned too little data). The note's conclusion frames this as a demonstration of combining 4D's new Web Services commands with the older Internet Commands plug-in to pull data from two different kinds of network sources into one application.

## Key Points

- The Amazon SOAP client is built from Amazon's own Web Services SDK/WSDL, requiring a developer token, and demonstrates 4D 2003's new Web Services client operating in SOAP DOC mode (as opposed to RPC mode) against Amazon's book/CD/movie search functions.
- Because the Amazon service uses complex (non-simple) SOAP types, the request and response are exchanged as BLOBs; the response BLOB is parsed element-by-element with `Parse XML variable`, `Get First XML element`, and `Get Next XML element`, dispatching on element name (e.g. `ProductName`, `Manufacturer`, `ImageUrlMedium`) via a `Case of` block into the `Amz_InsertElement` helper.
- Product images are fetched not through Web Services but through the separate 4D Internet Commands plug-in: `TCP_Open` establishes a raw connection to the image host, a hand-built HTTP/1.0 GET request (with headers like `Accept`, `User-Agent`, `Host`) is sent as a BLOB via `TCP_SendBLOB`.
- `TCP_ReceiveBLOB` is called in a loop (concatenating each partial BLOB with `COPY BLOB`) until the connection state signals completion, after which the HTTP header is stripped from the response text and the remaining BLOB is converted with `BLOB TO PICTURE` — or a default library picture is used if fewer than 1KB were received.
- The note frames this as the value of combining 4D's newer Web Services commands with the older Internet Commands plug-in in a single application to pull data from two different kinds of network sources.

## Featured Technology

- 4D 2003 Web Services client (SOAP, DOC mode)
- Amazon.com SOAP SDK / WSDL discovery
- BLOB-to-text and XML parsing of SOAP responses (Parse XML variable, Get First/Next XML element)
- 4D Internet Commands plug-in (TCP_Open, TCP_SendBLOB, TCP_ReceiveBLOB)
- Manual HTTP GET request construction for image downloads
- Blob to Picture conversion

## Historical Commentary

**Status:** Obsolete

This note is a well-explained, hands-on introduction to SOAP/DOC-mode Web Services in 4D 2003, including the less-common technique of manually building raw HTTP requests over a plain TCP socket to fetch binary images when a higher-level command isn't convenient. Amazon retired its original SOAP-based Web Services API long ago in favor of a REST/JSON Product Advertising API with a completely different request signing scheme, so the specific Amazon integration code no longer functions. The underlying 4D techniques are also outdated: 4D's SOAP-based Web Services client has been superseded by native HTTP client commands and REST/JSON support, and raw TCP_Open/TCP_SendBLOB HTTP construction is no longer necessary given 4D's built-in HTTP Client commands.

References to newer/updated information:
- Amazon's original SOAP Web Services API has been retired in favor of the REST/JSON-based Amazon Product Advertising API, which uses a different signed-request authentication scheme
- 4D introduced native HTTP Client commands (HTTP Request and related APIs) that make manual TCP_Open/TCP_SendBLOB HTTP construction unnecessary for tasks like downloading an image over HTTP
- 4D's SOAP-based Web Services client shown here has been succeeded by REST/JSON-oriented web service support in modern 4D
