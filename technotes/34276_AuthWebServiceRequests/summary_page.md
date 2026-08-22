# Tech Note 04-40: Authenticating Web Service Requests

**Author:** Not specified in source
**Published:** October 7, 2004 | **Product/Version:** 4th Dimension v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=34276
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_36-40_(AUG)/04-40_Authenticate_Web_Svcs.exe

## Overview
This note explains how 4th Dimension 2004 supports authenticating calls to third-party SOAP-based Web services, since the SOAP 1.1/1.2 standards themselves leave authentication undefined and each provider handles it differently.

## Key Points (from available teaser)
- SOAP 1.1 and 1.2 standards do not define a standard authentication mechanism.
- Many commercial/security-sensitive Web services require credentials with each request, using varying approaches.
- Method 1: HTTP Basic username/password via `AUTHENTICATE WEB SERVICE`.
- Method 2: Credentials passed as SOAP header values via `SET WEB SERVICE OPTION`.
- Method 3: Credentials passed as standard SOAP input parameters via `SET WEB SERVICE PARAMETER`.
- Compatibility note: setting SOAP headers requires 4th Dimension 2004 or later.

## Featured Technology
- AUTHENTICATE WEB SERVICE command
- SET WEB SERVICE OPTION command
- SET WEB SERVICE PARAMETER command
- SOAP 1.1 / 1.2 web services

## Historical Context
**Note:** Only the on-page teaser paragraph was recoverable for this Tech Note; the full PDF and example database were not accessible (old archive format not retrievable in this environment), so worked examples of each authentication method cannot be reproduced here. SOAP-based web services and their bespoke authentication schemes have since been broadly superseded by REST/JSON APIs using standardized authentication methods such as OAuth and API keys, making this note primarily of historical interest today.
