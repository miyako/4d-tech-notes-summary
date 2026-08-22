# Tech Note 04-41: Reading a Full SOAP Request with 4th Dimension 2004

**Author:** Not specified in source
**Published:** October 14, 2004 | **Product/Version:** 4th Dimension v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=34361
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_41-45_(SEP)/04-41_Reading_SOAP_Request.exe

## Overview
This note explains how and why a 4th Dimension developer might read a full, raw SOAP request directly, bypassing the native Web server's automatic XML-to-4D-data-type binding used for standard SOAP-published methods.

## Key Points (from available teaser)
- 4th Dimension 2003+ natively publishes methods as SOAP web services with automatic XML parsing/conversion.
- Reasons to read raw SOAP requests instead include: debugging SOAP exchanges, logging requests, and reading inputs not auto-bound to 4D parameters.
- Also useful for distinguishing an empty-valued input from one entirely absent from the request.
- Can be done via 4D's native DOM Parse XML variable command or a third-party XML parser.
- Serves as a way to deepen understanding of SOAP request structure and 4D's SOAP-serving internals.

## Featured Technology
- SOAP (Simple Object Access Protocol) web services
- 4th Dimension native Web server SOAP publishing
- DOM Parse XML variable command
- Third-party XML parsing tools

## Historical Context
**Note:** Only the on-page teaser paragraph was recoverable for this Tech Note; the full PDF and example database were not accessible (old archive format not retrievable in this environment), so the specific code walkthrough is not reproduced here. SOAP-based web services have since become largely obsolete industry-wide, replaced by REST/JSON APIs, and 4D's own web-services direction has moved to REST built on ORDA, making this note's SOAP-specific advanced parsing technique primarily of historical interest today.
