# Tech Note: Authenticating Web Service Requests

- **Asset ID:** 34276
- **Tech Note #:** 04-40
- **Published:** October 7, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=34276
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_36-40_(AUG)/04-40_Authenticate_Web_Svcs.hqx

## Overview

David Adams explains that since SOAP defines no standard authentication approach, different Web services expect credentials in different parts of the message -- and shows the three distinct 4th Dimension 2004 commands (AUTHENTICATE WEB SERVICE, SET WEB SERVICE OPTION, SET WEB SERVICE PARAMETER) that place credentials in the HTTP header, the SOAP header, or the SOAP body, respectively.

## Key Points

- Breaks down a SOAP request's anatomy into HTTP Headers, HTTP Body (containing the full SOAP Envelope), an optional SOAP Header section, and the mandatory SOAP Body, using one illustrative message that includes fake credentials in all three locations simultaneously for demonstration.
- Shows `AUTHENTICATE WEB SERVICE("username";"password")` called before `CALL WEB SERVICE` to add a standard HTTP Basic `Authorization: BASIC ...` header, and notes its limitation: there is currently no way to set arbitrary custom HTTP headers for outgoing SOAP client requests.
- Documents `SET WEB SERVICE OPTION` (new in 4D 2004) for adding SOAP header values, built with `DOM Create XML Ref`/`DOM Create XML element`/`DOM SET XML ELEMENT VALUE` and passed via the `Web Service SOAP Header` option constant -- noting that calling it more than once only keeps the last value, so multiple header values must be built into one XML structure first.
- Shows `SET WEB SERVICE PARAMETER` used to pass credentials as ordinary SOAP body parameters (e.g. `SET WEB SERVICE PARAMETER("name";$1)`), stressing there is nothing special about these values from 4D's or SOAP's perspective -- it's entirely the receiving Web service's choice to treat them as authentication data.
- Provides a clear mental model (diagram-style callouts) mapping each message location to its corresponding command, useful for quickly determining which 4D command a given Web service's documented authentication requirement calls for.
- Notes the compatibility requirement that SOAP-header-based authentication via SET WEB SERVICE OPTION requires 4th Dimension 2004 or later.

## Featured Technology

- AUTHENTICATE WEB SERVICE command (HTTP Basic auth header)
- SET WEB SERVICE OPTION with a SOAP header XML reference
- SET WEB SERVICE PARAMETER for SOAP-body-based credentials
- SOAP message anatomy (HTTP headers, HTTP body, SOAP envelope/header/body)
- DOM Create XML Ref / DOM Create XML element / DOM SET XML ELEMENT VALUE

## Historical Commentary

**Status:** Partially superseded

David Adams explains the three distinct places a SOAP Web service might expect authentication credentials -- the HTTP Authorization header, an optional SOAP header block, or ordinary SOAP body parameters -- and maps each to the specific 4th Dimension 2004 command needed to set it: AUTHENTICATE WEB SERVICE, SET WEB SERVICE OPTION, and SET WEB SERVICE PARAMETER respectively, since SOAP itself defines no standard authentication mechanism. This is a precise, still-technically-accurate explanation of SOAP client authentication concepts as implemented in 4D's original Web Services client commands; the commands described remain in 4D for legacy SOAP consumption, but authenticating to modern Web APIs (mostly REST with OAuth2/API keys/bearer tokens) is now handled via 4D's HTTP Client commands instead, making the specific command set here largely legacy while the conceptual message-anatomy explanation remains a useful reference.

**References to newer/updated information:**
- 4D's HTTP Client commands (added v13, 2012) are now the standard way to authenticate against modern REST APIs (bearer tokens, API keys, OAuth2) rather than the SOAP-specific commands described here
- AUTHENTICATE WEB SERVICE, SET WEB SERVICE OPTION, and SET WEB SERVICE PARAMETER still exist in 4D for legacy SOAP web-service client scenarios
- SOAP itself remains without a standardized authentication mechanism, so the note's underlying explanation of why different services need different approaches is still conceptually accurate
