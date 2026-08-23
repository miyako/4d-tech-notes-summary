# Tech Note 03-13: 4D Blogger and SOAP

- **Asset ID:** 23266
- **Tech Note #:** 03-13
- **Published:** March 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=23266
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_11-15_(MAR)/03-13_4D_Blogger_and_SOAP.hqx

## Overview

Jamras Komoncharoensiri (4D Technical Support) documents 4D Blogger's SOAP architecture — a WebLog Server and WebLog Client pair built in 4D 2003 that combine standard HTTP publishing with 4D's new built-in SOAP Web Services for a full-featured blogging system with authentication, search, and archiving.

## Key Points

- 4D Blogger consists of a WebLog Server (records/publishes logs via HTTP or SOAP) and a WebLog Client (a rich SOAP-based navigational client with a calendar view and a 4D Write log editor).
- The server publishes SOAP methods declared with `SOAP DECLARATION`, including `SOAP_CreateWebLog`, `SOAP_ModifyWebLog`, `SOAP_DeleteWebLog`, `SOAP_SetArchive`, `SOAP_Search`, `SOAP_SearchByDate`, and `SOAP_ReceiveMonthArchives`, each taking specific Is Text/Is LongInt/Is Date inputs and array or text outputs.
- Authentication for privileged SOAP calls (create/modify/delete/set-archive) is centralized in the `On Web Authentication` database method, which detects SOAP requests, checks the target method name, and validates credentials via `FN_isValidUser`.
- On the client, generated SOAP proxy methods are modified to install a `SOAP_Err_Handler` method (via `ON ERR CALL`) that inspects `Get Web Service error info` for SOAP fault codes (9910–9914) and HTTP status codes (401/403 trigger a login prompt and `AUTHENTICATE WEB SERVICE`; 302 indicates the service moved).
- A second client-side modification replaces the hard-coded server IP address baked into generated proxy methods (e.g. `"http://127.0.0.1/4DSOAP/"`) with an interprocess variable `<>domain`, so the client can connect to any WebLog Server address.
- Archive management (`SOAP_SetArchive`, `SOAP_ReceiveMonthArchives`) lets the Administrator set an archive cutoff period and retrieve bulk archived logs by month as a single text blob.

## Featured Technology

- 4D 2003 SOAP Web Services (client and server)
- SOAP DECLARATION (SOAP Input/Output parameters)
- On Web Authentication database method
- AUTHENTICATE WEB SERVICE
- Get Web Service error info / ON ERR CALL error handling
- 4D Write log editor integration
- 4D Blogger WebLog Server/Client architecture

## Historical Commentary

**Status:** Obsolete

This note documents 4D Blogger, an early-2000s blogging platform built with 4D that combined standard HTTP publishing with 4D 2003's brand-new built-in SOAP Web Services stack for its rich client (create/modify/delete posts, search, archive management, all as SOAP methods with custom authentication and error handling). It is a genuinely useful worked example of 4D's early SOAP server- and client-side APIs — declaring SOAP inputs/outputs, wiring authentication through On Web Authentication, and handling SOAP faults via Get Web Service error info — but the specific product (4D Blogger) and its SOAP-based Blogger/MetaWeblog-style protocol are long defunct, as virtually all modern blogging and CMS platforms now use REST/JSON APIs instead of SOAP.

References to newer/updated information:
- 4D Blogger itself was discontinued long ago and SOAP-based blogging APIs of this style have been superseded industry-wide by REST/JSON content APIs
- 4D's SOAP client/server commands demonstrated here (SOAP DECLARATION, AUTHENTICATE WEB SERVICE) still exist in 4D but 4D now also offers native REST/JSON HTTP handling that is generally preferred for new web service integrations
