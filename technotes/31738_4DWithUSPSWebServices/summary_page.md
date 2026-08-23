# Tech Note: Using 4D with United States Postal Service (USPS) Web Services

- **Asset ID:** 31738
- **Tech Note #:** 04-10
- **Published:** March 11, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Thang Nguyen, 4D Technical Support
- **Page URL:** https://kb.4d.com/assetid=31738
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_06-10_(MAR)/04-10_4D_With_USPS_Web_Services.hqx

## Overview

Thang Nguyen demonstrates integrating 4th Dimension with the USPS Web Tool Kit Domestic Rate Calculator by manually building an HTTP GET request embedding an XML payload, sending it over a raw TCP socket, and manually parsing the XML response to extract postage and zone information.

## Key Points

- The USPS Web Tool Kit API accepts requests as an HTTP GET whose query string embeds an XML payload (`GET /ShippingAPITest.dll?API=Rate&XML=<RateRequest ...>`), requiring a registered USERID/PASSWORD obtained via free USPS registration.
- Three project methods build the request: `usps_addHead_XML` (constructs the GET line, API name, and opening `<RateRequest>` tag with credentials, using `Char(34)` for quotes and `%20` for spaces), `generateXMLRequest1` (appends package details -- Service, ZipOrigination, ZipDestination, Pounds, Ounces, Container, Size, Machinable -- from nine parameters), and `usps_addTail_XML` (closes the tag and appends the `HTTP/1.1` terminator).
- The completed request is transmitted over a raw TCP connection: `TCP_Open("Production.ShippingAPIs.com";80;...)`, `TCP_Send`, a `Repeat...Until` loop of `TCP_Receive` calls accumulating the response until the connection state closes, then `TCP_Close`.
- `usps_ParseXML_Response` strips the leading HTTP headers from the raw response by locating the `"<?xml version="` marker with `Position`, then hands the remaining XML to the parser.
- `XML_Parser` recursively walks the response using `Parse XML variable`, `Get First/Next XML element`, and `GET XML ELEMENT NAME/VALUE`, extracting `Postage` (price) and `Zone` values (or a `Description` error message) into interprocess variables (`usps_price`, `usps_zone`, `errorCode`).
- The accompanying sample database offers List Form and Request Form dialogs for entering package details, viewing calculated postage per package, sorting and deleting saved calculations, all built around a single `[Package]`-style table recording each rate request and result.

## Featured Technology

- USPS Web Tool Kit XML/HTTP GET API (Domestic Rate Calculator)
- TCP_Open / TCP_Send / TCP_Receive / TCP_Close raw TCP commands
- Manual XML request construction (usps_addHead_XML, generateXMLRequest1, usps_addTail_XML)
- Manual XML response parsing (Parse XML variable, Get First/Next XML element)
- HTTP GET request construction over a raw TCP socket

## Historical Commentary

**Status:** Superseded

This note demonstrates integrating with the USPS Web Tool Kit's Domestic Rate Calculator by manually constructing an HTTP GET request embedding an XML payload, sending it over a raw TCP socket with `TCP_Open`/`TCP_Send`/`TCP_Receive`/`TCP_Close`, and manually parsing the XML response with 4D's native XML navigation commands to extract postage price and zone. It's a good illustration of building an HTTP/XML API integration entirely from low-level TCP primitives before 4D had native HTTP client or SOAP-consumption commands suited to this kind of REST-like GET API. This raw-TCP, hand-built-HTTP-request approach became unnecessary once 4D introduced native HTTP Client commands (4D v13, 2012) that handle GET/POST, headers, and response parsing directly; the specific USPS API endpoints and XML schema shown are also likely outdated given USPS has evolved its Web Tools API since 2004.

**References to newer/updated information:**
- 4D introduced native HTTP Client commands (4D v13, 2012) that handle GET/POST HTTP requests directly, making the raw TCP_Open/TCP_Send/TCP_Receive approach shown here unnecessary for HTTP-based API integration
- USPS has updated its Web Tools API and endpoints since 2004; the specific server names, XML schema, and registration process described are likely outdated
- 4D's native XML and JSON parsing commands have expanded since 2004, simplifying response parsing compared to the manual element-by-element walk shown here
