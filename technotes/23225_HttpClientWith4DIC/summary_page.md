# Tech Note 02-05: HTTP Client with 4D and 4D Internet Commands

**Author:** Not specified in source document
**Published:** February 28, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=23225
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/Windows/TN_2002_05-09_(FEB)/02-05_HTTP_Client_with_4D.exe

## Overview
A protocol-level Tech Note building an HTTP Client from scratch in 4D using 4D Internet Commands, covering URL parsing, request/response handling, and Base64-based Basic Authentication.

## Key Points
- Builds a working HTTP Client in 4D from first principles using 4D Internet Commands.
- Covers URL parsing, request construction/sending, and response interpretation.
- Demonstrates Base64 encoding of username/password for HTTP Basic Authentication.

## Featured Technology
- 4D Internet Commands
- HTTP protocol
- Base64 encoding

## Historical Context
4D Internet Commands was 4D's classic plug-in for TCP/IP and Internet protocol access, before 4D gained more built-in, higher-level HTTP client commands natively in the core language.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

4D has since incorporated native, higher-level HTTP client commands directly into the core language, superseding the need to hand-build an HTTP client at the protocol level as shown here, though the underlying HTTP fundamentals this note teaches (request/response structure, Basic Auth encoding) remain accurate and educationally valuable today.
