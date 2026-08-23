# Tech Note: Reading a Full SOAP Request with 4th Dimension 2004

- **Asset ID:** 34361
- **Tech Note #:** 04-41
- **Published:** October 14, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=34361
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_41-45_(SEP)/04-41_Reading_SOAP_Request.hqx

## Overview

David Adams shows how 4th Dimension 2004's new GET HTTP BODY command lets developers capture the full raw HTTP body of an incoming SOAP Web service request as text or BLOB -- replacing an older, undocumented reconstruction trick using GET WEB FORM VARIABLES -- and demonstrates using this for SOAP request logging and reading SOAP inputs not automatically bound by the language.

## Key Points

- Explains 4th Dimension's default SOAP-serving behavior: the SOAP-ENV:Body method name and inputs are automatically extracted and converted using `SOAP DECLARATION($n;Is <Type>;SOAP Input/Output;"name")`, illustrated with a ConvertFeetToMeters example method.
- Reviews the pre-2004 workaround (Technical Note 04-19) of reassembling the raw SOAP message from `GET WEB FORM VARIABLES` name/value array pairs, split at the first equals sign, and contrasts it with the simpler 4D 2004 approach.
- Documents `GET HTTP BODY(textOrBlobVariable)` as a single-line replacement that reads the entire incoming request body — recommending BLOB over text because text variables truncate at 32,000 characters — alongside `GET HTTP HEADER` for reconstructing the HTTP header section.
- Shows a complete SOAP request logging system built in the `On Web Authentication` database method, using `soap_LogRequest` to extract the User-Agent header, parse the SOAP body with `DOM Parse XML variable`/`DOM Get First XML element`/`DOM GET XML ELEMENT NAME` to find the invoked method name (stripping any namespace prefix at a colon), and persist client IP, server IP, user name, method name, and user agent to a `Logged_SOAP_Request` table.
- Demonstrates reading SOAP inputs that were never declared via `SOAP DECLARATION` -- e.g. an optional `inRoundTo` rounding parameter added to `ConvertFeetToMeters` -- via a `soap_GetRounding` method that parses the raw request XML directly using the `XML_Utilities` component's `xutil_GetValue` helper (from TN #04-21).
- Notes practical reasons for manual SOAP parsing over automatic binding: distinguishing an omitted input from an explicit default value, avoiding the requirement that all bound variables/arrays be declared in `Compiler_Web`, and supporting evolving parameter lists across the life of a Web service.

## Featured Technology

- GET HTTP BODY command (new in 4D 2004)
- GET HTTP HEADER command
- Is SOAP request function and SOAP DECLARATION-based automatic input binding
- DOM Parse XML variable / DOM Get First XML element / DOM GET XML ELEMENT NAME
- On Web Authentication database method for per-request SOAP logging

## Historical Commentary

**Status:** Historical interest only

David Adams explains how 4th Dimension 2004's new GET HTTP BODY command makes it trivial to capture the complete raw SOAP request received by 4D's built-in Web server -- superseding the undocumented GET WEB FORM VARIABLES workaround from Technical Note 03-21/04-19 -- and demonstrates practical applications such as full SOAP request logging in On Web Authentication and reading SOAP inputs that were never declared via SOAP DECLARATION. This is a deep, implementation-level technique tied to 4th Dimension's original built-in SOAP web-service server; that server architecture and its GET HTTP BODY/SOAP DECLARATION-based model have been superseded by 4D's modern HTTP Client-centric and REST/JSON-oriented web-service approach, making this note primarily of historical interest for anyone still maintaining a legacy 4D SOAP server.

**References to newer/updated information:**
- 4D's SOAP-serving architecture based on SOAP DECLARATION and the built-in Web server has been superseded by modern REST/JSON-based web-service patterns using 4D's HTTP Client and native JSON support
- GET HTTP BODY and GET HTTP HEADER still exist as general-purpose 4D Web server commands beyond SOAP-specific use cases
- New 4D web-service integrations are now typically built as REST endpoints rather than SOAP-based Web Services
