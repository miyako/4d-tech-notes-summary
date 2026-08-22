# Tech Note 04-12: Returning Data Through SOAP

**Author:** David Adams
**Published:** March 25, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=31928
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_10-15_(MAR)/04-12_ReturningDataThruSOAP.zip

## Overview
This Tech Note explains how 4th Dimension methods published as SOAP Web Services can return more than the single `$0` result parameter available to locally-called methods — instead returning `$0` plus any number of process variables and arrays via the `SOAP DECLARATION` command, comparable to returning a full record instead of a single field.

## Key Points
- SOAP requests/responses are XML-encoded messages handled transparently by the native 4D Web server (receiving, type conversion, security, dispatch, binding, response formatting).
- Prerequisites for Web Services: the 4D Web server running, the "Allow Web Services Requests" preference enabled, and "Offered as a Web Service" set on the method.
- The `$0` parameter is returned automatically as `FourD_arg0` in the SOAP response XML.
- `SOAP DECLARATION` lets a method bind process variables and arrays to custom-named XML output elements, and can be called multiple times per method.
- Only `$0`, process variables, and process arrays can be used as SOAP outputs — fields, local variables/arrays, literals, and interprocess variables/arrays are **not** supported.
- Full data-type mapping table provided (BLOB→base64Binary, Boolean→boolean, Date→date, Integer/Longint→int, Real→float, StringVar/Text→string, Time→time); pictures require conversion to BLOB first; time arrays are stored as longint arrays.
- Example database demonstrates every supported type via matching Web Service methods and SOAP client proxy methods, configurable via a `requestGetAccessURL` helper method and a configurable port (default 8080).
- Practical guidance: run client and server in separate 4D copies for realistic testing; the `Compiler_Web` method auto-binds inputs but not outputs; several rules-of-thumb for correct `SOAP DECLARATION` usage (must be called directly in the Web Service method, legal XML names required, ignored when called locally).

## Featured Technology
- 4D Web Services (SOAP) via the native 4D Web server
- `SOAP DECLARATION` command
- `Get Soap info` / SOAP request-response XML model
- 4D-to-XML/SOAP data type conversion

## Historical Context
Published in March 2004 for 4D v2003.3, this is a substantive, reference-quality note documenting 4D's early SOAP Web Services return-value architecture in detail, including concrete XML listings and full data-type support tables. It predates 4D's native SQL engine (v11 SQL, ~2007) and ORDA (v16, 2018), reflecting a purely procedural, SOAP/XML-centric approach to exposing data over the web. While historically valuable for understanding 4D's web-services evolution, the SOAP DECLARATION-based technique itself has been superseded by 4D's later REST/JSON web services support, which is now the standard integration approach for new development.
