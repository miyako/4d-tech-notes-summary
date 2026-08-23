# Tech Note: The 4D remote FastCGI Component

- **Asset ID:** 27786
- **Tech Note #:** 02-31
- **Published:** July 31, 2002
- **Product / Version:** 4D 6.8.3
- **Platform:** Mac & Win
- **Author:** Julien Feasson, Software Engineer, 4D, Inc. Information Systems
- **Page URL:** https://kb.4d.com/assetid=27786
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_30-35_(JUL)/02-31_Remote_Fast_CGI.hqx

## Overview

Julien Feasson explains how the 4D remote FastCGI component lets a 4D database implement the FastCGI "responder" role, allowing any FastCGI-capable web server (illustrated with 4D WebSTAR V) to forward dynamic-content requests to a persistent 4D process instead of spawning a new CGI process for every hit. The note motivates the design by tracing the historical progression from CGI (simple, portable, but slow due to per-request process creation) through proprietary server APIs (fast, but insecure and platform/vendor-locked) to FastCGI (a full-duplex, protocol-based middle ground), then documents both the wire-level FastCGI record format and the simplified 4D-side API built on top of it.

## Key Points

- Traces the historical arc CGI → server APIs → FastCGI, explaining the performance and security trade-offs of each before positioning FastCGI as combining CGI's portability with near-API-level speed.
- Documents the FastCGI wire protocol's `FCGI_Record` C struct (version, type, requestId, contentLength, paddingLength, contentData, paddingData) and enumerates its record types: `FCGI_BEGIN_REQUEST`, `FCGI_ABORT_REQUEST`, `FCGI_END_REQUEST`, `FCGI_PARAMS`, `FCGI_STDIN`, `FCGI_STDOUT`, `FCGI_STDERR`, `FCGI_DATA`, `FCGI_GET_VALUES`, `FCGI_GET_VALUES_RESULT`.
- Explains the three defined FastCGI roles: `FCGI_RESPONDER` (build an HTML response, like plain CGI), `FCGI_AUTHORIZER` (auth decisions), and `FCGI_FILTER`; the 4D component implements only the responder role.
- The 4D-side API is reduced to four functions: `FCGI_Accept(RemoteHost;LocalPort)` (blocks awaiting a request, populates variables), `FCGI_Send(Text)` (returns the response), `FCGI_ValueVar(EnvVarName)`, and `FCGI_ValueParam(ParameterName)`.
- The canonical 4D FastCGI script shape is a blocking loop: `While(FCGI_Accept(RemoteHost;LocalHost)) ... my script ... FCGI_Send(MyResponse) End while`.
- `FCGI_Accept` populates the arrays `FCGI_Name`/`FCGI_Value` (environment variables) and `FCGI_ParamName`/`FCGI_ParamValue` (POST parameters), plus the raw `FCGI_StdinData` string.
- Includes a full working sample "echo" method that loops on `FCGI_Accept("10.99.255.241";80)`, builds an HTML page listing all environment variables and parameters, and returns it via `FCGI_Send`.
- Documents error codes -35 (missing 4D Web License) and -36 (wrong 4D version), and gives 4D WebSTAR V configuration steps (a "[FastCGI][Begins with][/FCGI]..." action rule, enabling "Allow UNIX CGI and FastCGI execution").
- Requires 4D v6.8.1 or later, a valid 4D Web License, and 4D Internet Commands v6.8.

## Featured Technology

- FastCGI protocol (FCGI_Record structure)
- 4D remote FastCGI component
- FCGI_Accept / FCGI_Send API functions
- FCGI_ValueVar / FCGI_ValueParam API functions
- 4D WebSTAR V web server integration
- CGI vs. server-API vs. FastCGI architecture comparison

## Historical Commentary

**Status:** Obsolete

This note documents a genuinely clever piece of engineering for its time: implementing the FastCGI responder role directly inside 4D (via FCGI_Accept/FCGI_Send and related functions) so 4D could sit behind any FastCGI-capable web server, such as 4D WebSTAR V, as a persistent process rather than a per-request CGI. It reflects an era when 4D's own web serving was primitive and developers had to bridge to external web servers for performance. FastCGI-based bridging of this kind is now essentially obsolete for 4D web work, since 4D has shipped a fast, built-in, natively multi-threaded web server for many versions, eliminating the need to proxy requests through a separate FastCGI layer. The general architectural lesson -- isolating request handling in a persistent process instead of spawning one per request -- remains valid computer-science knowledge but is no longer something 4D developers need to implement themselves.

References to newer/updated information:
- 4D's built-in web server (developed extensively since the mid-2000s through current versions) natively serves dynamic content with high performance, removing any need for a separate FastCGI bridge component
- The 4D remote FastCGI component and its FCGI_Accept/FCGI_Send API described here are not part of modern 4D and are not maintained
