# Tech Note: Reading a Full SOAP Request

- **Asset ID:** 32601
- **Tech Note #:** 04-19
- **Published:** May 13, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=32601
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_16-20_(APR)/04-19_Full_SOAP_Request.hqx

## Overview

David Adams shows how to recover the complete, unmodified incoming SOAP request received by a 4th Dimension Web Service method, by exploiting an undocumented behavior of GET WEB FORM VARIABLES, and demonstrates applying it to build a custom SOAP request logging system.

## Key Points

- A SOAP request arrives as an HTTP request whose body is a well-formed SOAP-ENV:Envelope/Body XML message; HTTP headers (including the `SoapAction` header) sit outside the SOAP message and are readable separately via `GET HTTP HEADER`.
- 4D's automatic SOAP handling reads inputs declared via `SOAP DECLARATION` directly into method parameters/process variables (illustrated with a `ConvertFeetToMeters` method), but exposes none of the raw XML.
- `GET WEB FORM VARIABLES`, when called inside a process handling a Web Service request, splits the entire incoming SOAP message at the first equals sign into a name/value pair; reassembling `name + "=" + value` reconstitutes the full original SOAP XML, which can then be parsed with `Parse XML variable`.
- The note explicitly flags this as undocumented, unsupported behavior (though not expected to change), and warns it is limited by the usual 32,000-character bound on 4D text parameters and array elements.
- A full example, `soap_LogRequest`, invoked from the `On Web Authentication` database method, captures client/server IP, username, the `User-Agent` HTTP header, and the requested method name (extracted by walking two levels into the reassembled SOAP XML tree and stripping any namespace prefix) into a `[Logged_SOAP_Request]` record.
- A further example shows reading an "undeclared" SOAP input (`inRoundTo`) not bound via `SOAP DECLARATION`, useful when parameter lists evolve over a Web Service's lifetime or when distinguishing a missing input from one explicitly passed as a default/zero value.

## Featured Technology

- GET WEB FORM VARIABLES (undocumented full-SOAP-body reassembly behavior)
- GET HTTP HEADER for reading raw HTTP headers (e.g. SoapAction)
- SOAP DECLARATION for automatic input/output binding
- Is SOAP request function
- On Web Authentication database method for request logging
- Parse XML variable on a reassembled raw SOAP request

## Historical Commentary

**Status:** Superseded

This note (companion to TN 04-20 on SOAP responses) shows how to recover the complete, unmodified incoming SOAP request body inside a 4th Dimension Web Service method, exploiting an undocumented behavior of `GET WEB FORM VARIABLES` that splits the request only at the first equals sign, then reassembling it and re-parsing with `Parse XML variable`. It was used for logging, debugging SOAP exchanges, and reading inputs not declared via `SOAP DECLARATION` -- genuinely clever but explicitly reliant on undocumented behavior. Like its sibling note, this technique is tied to 4th Dimension's native SOAP web-service publishing system, which has been superseded industry-wide (and within 4D's own roadmap) by REST/JSON APIs built on ORDA (2017+); the specific undocumented `GET WEB FORM VARIABLES` trick is now mainly of historical interest for anyone still maintaining legacy 4D SOAP services.

**References to newer/updated information:**
- 4D's SOAP-based Web Service publishing has been superseded by REST APIs built on ORDA (introduced 2017+) as the primary modern integration path
- REST and JSON have broadly replaced SOAP as the dominant web-service standard industry-wide, reducing the practical relevance of SOAP-specific debugging techniques like this one
