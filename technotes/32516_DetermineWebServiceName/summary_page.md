# Tech Note: Determining the Name of a Requested Web Service

- **Asset ID:** 32516
- **Tech Note #:** 04-18
- **Published:** May 6, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=32516
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_16-20_(APR)/04-18_Determine_Web_Service_Name.hqx

## Overview

David Adams explains why 4th Dimension 2003's native `Get SOAP info` function cannot reliably return the requested Web Service name (only the method name), and provides custom code that instead extracts both names by parsing the optional `SoapAction` HTTP header.

## Key Points

- A SOAP request over HTTP includes a `SoapAction` header (e.g. `SoapAction: "Conversions#textToUppercase"`) and a SOAP-ENV:Body containing the method call; the Web Service name is configured in 4D via Preferences -> Web -> Web Services -> Web Service Name.
- `Get SOAP info(SOAP Method Name)` reliably returns the method name from the SOAP body, but `Get SOAP info(SOAP Service Name)` always returns an empty string in 4th Dimension 2003.2+ (and was unreliable/error-prone in earlier 2003 releases) because the Web Service name is never actually present in the SOAP XML body.
- The `SoapAction` HTTP header, when present, encodes both names as `"ServiceName#methodName"`; the note provides a `GetSoapAction` method that reads headers via `GET HTTP HEADER`, locates `SoapAction`, strips surrounding quotation marks, and splits the value at the `#` character.
- Higher-level wrapper functions `GetSoapAction_MethodName` and `GetSoapAction_WebServiceName` expose the service/method extraction with simple, defensive calls; `GetSoapAction` is written to avoid generating errors even when called in unexpected contexts (e.g. non-SOAP requests).
- Limitations are explicitly called out: `SoapAction` is optional and may be omitted by the SOAP client, there is no guarantee it matches the method actually invoked in the SOAP body, and the header was dropped entirely from the SOAP 1.2 specification (4th Dimension 2003, like most tools of the era, implements SOAP 1.1).

## Featured Technology

- Get SOAP info (SOAP Method Name / SOAP Service Name constants)
- SoapAction HTTP header parsing
- GET HTTP HEADER for reading incoming headers
- Custom GetSoapAction / GetSoapAction_MethodName / GetSoapAction_WebServiceName methods
- Find in array / Position / Substring string parsing

## Historical Commentary

**Status:** Superseded

This note explains a specific 4th Dimension 2003.2+ limitation -- that `Get SOAP info`'s `SOAP Service Name` constant unreliably returns the Web Service name because that name isn't actually present in the SOAP XML body -- and provides a custom routine that instead extracts both the service and method names by parsing the optional `SoapAction` HTTP header. It's a narrow but practical debugging/logging/security technique for that era's native 4D SOAP server. The underlying issue and workaround are specific to 4th Dimension's legacy SOAP-based Web Service publishing, which has since been superseded by REST APIs built on ORDA (2017+); the `SoapAction` header itself was also dropped from the later SOAP 1.2 specification, further limiting the technique's applicability outside legacy SOAP 1.1 contexts.

**References to newer/updated information:**
- 4D's SOAP-based Web Service publishing has been superseded by REST APIs built on ORDA (introduced 2017+)
- The SoapAction HTTP header this technique relies on was dropped from the SOAP 1.2 specification, limiting relevance to legacy SOAP 1.1 services
