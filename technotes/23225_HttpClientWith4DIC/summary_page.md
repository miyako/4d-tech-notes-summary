# Tech Note: HTTP Client with 4D and 4D Internet Commands

- **Asset ID:** 23225
- **Tech Note #:** 02-05
- **Published:** February 28, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Julien Feasson, Software Engineer, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=23225
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_05-09_(FEB)/02-05_HTTP_Client_with_4D.hqx

## Overview

Julien Feasson builds a working HTTP client in 4D from first principles using the 4D Internet Commands plug-in, at a time before 4D had native HTTP client support, combining a thorough protocol-level primer with a functioning demo database that sends requests, parses responses, and handles Basic Authentication and chunked encoding.

## Key Points

- Explains URL anatomy using `http://www.4D.com:80/` as the running example: protocol scheme, hostname, port (defaulting to 80), and document path.
- Walks through a sample raw request (`GET / HTTP/1.1` plus `Accept-Language`, `User-Agent`, `Host`, `Connection: Keep-Alive` headers) line by line, explaining what each header communicates to the server.
- Documents all HTTP 1.1 methods -- GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS, CONNECT -- and the three header categories (General, Request, Entity headers), with detailed notes on Accept, Accept-Charset, Accept-Encoding, Accept-Language, Authorization, Cookie, Host, If-Modified-Since, User-Agent, Content-Encoding, Content-Language, Content-Length, Content-Type, and Last-Modified.
- Details HTTP Basic Authentication: encoding a `username:password` string in Base 64 for the `Authorization: BASIC ...` header, illustrated with `Authorization: BASIC dXNlcm5hbWU6cGFzc3dvcmQ=`.
- Explains Transfer-Encoding: chunked as the only encoding HTTP 1.1 formally supports, previewing the Base 16 decoding needed to reassemble a chunked response body.
- The accompanying demo database implements a two-form "4D HTTP Client": an HTTP browser window for entering a URL and viewing results, built to demonstrate building a request, parsing a URL, using Basic Authentication (Base 64), sending/receiving via the 4D Internet Commands, interpreting HTTP response headers, and parsing a chunked body (Base 16 decoding).

## Featured Technology

- 4D Internet Commands plug-in
- HTTP request/response construction
- URL parsing
- HTTP Basic Authentication (Base 64 encoding)
- Chunked transfer encoding (Base 16 decoding)
- HTTP header parsing

## Historical Commentary

**Status:** Superseded

Julien Feasson's note builds a functioning HTTP client from scratch in 4D using the 4D Internet Commands plug-in, covering URL parsing, manual construction of GET/response cycles, Base 64-encoded Basic Authentication, and Base 16 decoding of chunked response bodies. 4D has since added native, higher-level HTTP client commands directly into the core language, which handle GET/POST, headers, cookies, and authentication without hand-parsing raw protocol text, making this note's specific low-level implementation superseded for production use; however, the HTTP protocol fundamentals it carefully explains (request/response structure, headers, Basic Auth encoding, chunked encoding) remain accurate and still useful as a learning reference today.

References to newer/updated information:
- 4D has since introduced native, higher-level HTTP client commands in the core language, removing the need to hand-build requests and parse chunked responses via the 4D Internet Commands plug-in as shown here
- The HTTP protocol concepts explained (headers, methods, Basic Auth, chunked encoding) remain technically accurate and still educationally useful
