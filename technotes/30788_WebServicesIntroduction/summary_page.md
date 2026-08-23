# Tech Note: Web Services – An Introduction

- **Asset ID:** 30788
- **Tech Note #:** 03-53
- **Published:** December 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Frank Chang, Technical Support, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=30788
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_52-55_(DEC)/03-53_Web_Services_Intro.hqx

## Overview

Frank Chang (Technical Support, 4D, Inc.) provides a beginner's guide to Web Services in general and to 4th Dimension 2003's brand-new native support for publishing and consuming them, aimed at developers with no prior XML or SOAP background.

## Key Points

- Defines Web Services conceptually (interoperable machine-to-machine interaction over a network, described by WSDL, invoked via SOAP over HTTP) and lists real public examples: FedEx package tracking, Amazon search, and BabelFish translation.
- Explains the two SOAP messaging styles: synchronous, tightly-coupled RPC-style (parameters/return values wrapped in the SOAP Body per the WSDL contract) versus asynchronous, loosely-coupled DOC-style (an entire XML document is passed and processed without strict call/response semantics).
- Shows publishing a 4D method (a book-reservation example against `[BookStore]`/`[BoolReserve]` tables) as a server-side Web service: enable "Allow Web Service Request" once in database Preferences, then check "Offered as a Web Service" and "Published in WSDL" in that method's Method Properties.
- Demonstrates consuming an external Web service as a client via the Web Services Wizard, which auto-generates a proxy project method using `SET WEB SERVICE PARAMETER`, `CALL WEB SERVICE` (specifying the endpoint, service#method, and namespace), and `GET WEB SERVICE RESULT` — after which the service can be called just like any local project method.
- Lists the supported SOAP data types (Boolean, Blob, Date, Integer, Long Integer, Real, String, Text, Time, plus arrays of several types) and shows two ways to declare input/output parameters: Compiler commands (limited to one output) or the more flexible `SOAP DECLARATION` command, which requires matching declarations in the `Compiler_Web` method.
- Covers security: HTTP Authentication either via 4D's built-in password system (Use Password + Include 4D Password in Preferences) or a custom `On Web Authentication` method that checks `Is SOAP request` and validates credentials, plus SSL/HTTPS for encrypting the entire SOAP message including user IDs, passwords, and sensitive data like credit card numbers.
- Points readers to 4D's own example databases at http://www.4d.com/2003/integration.html and to www.xmethod.net for publicly available Web Services to experiment with.

## Featured Technology

- SOAP (RPC-style and DOC-style)
- WSDL
- 4D 2003 Web Services publishing ("Offered as a Web Service" / "Published in WSDL")
- Web Services Wizard (client proxy generation)
- CALL WEB SERVICE / SET WEB SERVICE PARAMETER / GET WEB SERVICE RESULT
- SOAP DECLARATION command
- On Web Authentication method / SSL (HTTPS) security

## Historical Commentary

**Status:** Superseded

This is a beginner-level, conceptual introduction to Web Services (SOAP/WSDL, RPC vs. DOC style) followed by a concrete walkthrough of 4D 2003's brand-new ability to publish 4D methods as SOAP Web services and consume external ones through the Web Services Wizard and generated proxy methods, including the SOAP DECLARATION command, supported data types, and both HTTP Authentication and SSL security options. As foundational documentation for a feature introduced in this exact release, it captures a pivotal moment in 4D's networking history, but the SOAP/WSDL paradigm it teaches has been broadly superseded industry-wide (and within 4D) by simpler REST/JSON-based HTTP APIs, so the specific commands and workflow described are now legacy even though the concept of exposing/consuming remote application logic remains as important as ever.

**References to newer/updated information:**
- REST/JSON APIs have become the dominant web integration style, largely displacing SOAP/WSDL industry-wide, including within 4D's own web services offerings
- 4D added native JSON parsing/generation and modern HTTP client/server commands well after this note, reducing reliance on the SOAP-specific commands (CALL WEB SERVICE, SOAP DECLARATION) documented here
- 4D's Web Services Wizard and WSDL-proxy-generation workflow described here remain present in 4D for legacy SOAP integrations but are not the primary path for new web integrations
