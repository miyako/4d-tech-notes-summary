# Tech Note 04-20: Reading a Full SOAP Response

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** May 20, 2004 | **Product/Version:** 4th Dimension v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32705
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_16-20_(APR)/04-20_Full_SOAP_Response.exe

## Overview
This Tech Note addresses 4th Dimension 2003 and later's native support for building Web Service clients, where method calls generate SOAP (Simple Object Access Protocol) messages sent over HTTP to a SOAP-enabled remote service that could be written in .NET, Java, 4th Dimension, or virtually any other contemporary language or framework. By default, 4D's Web Service client system automatically handles the considerable complexity of parsing, navigating, and converting values between XML/SOAP formats and native 4D data types, per the strict formatting and encoding rules defined by the interlocking SOAP/XML standards. The note explains that some developers need or prefer to read raw incoming SOAP responses directly rather than relying on this automatic conversion, and shows how to do so using the complexType parameter of the CALL WEB SERVICE command to capture and extract values from the raw response. This reflects the early-to-mid 2000s SOAP/XML-web-services era, when SOAP was the dominant standard for machine-to-machine service integration across enterprise platforms, well before REST and JSON became the default lightweight alternative. The note targets 4D developers building Web Service client integrations who need finer control over SOAP response handling than the default automatic conversion provides.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- A guide to reading raw incoming SOAP responses directly using the complexType parameter of CALL WEB SERVICE, for cases where 4th Dimension's automatic XML-to-4D conversion isn't sufficient.

## Featured Technology
- CALL WEB SERVICE command
- SOAP (Simple Object Access Protocol)
- 4D native Web Service client

## Historical Context
**Status:** superseded

This note documents an advanced technique for reading raw SOAP responses in 4th Dimension's native Web Service client, reflecting the SOAP-centric web-services standard that dominated enterprise integration in the early-to-mid 2000s. SOAP itself has since been broadly superseded by REST and JSON as the default approach for web service integration industry-wide, and 4D's own web services direction has moved decisively toward REST APIs (particularly via ORDA, introduced 2017+), though the CALL WEB SERVICE command and SOAP client capability described here likely still exist in current 4D for legacy integration needs.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
