# Tech Note: Complex Input Types with Web Services

- **Asset ID:** 29817
- **Tech Note #:** 03-43
- **Published:** September 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Dave Dell'Aquila
- **Page URL:** https://kb.4d.com/assetid=29817
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_40-43_(SEP)/03-43_ComplexInputTypesInWS.hqx

## Overview

Dave Dell'Aquila, Senior 4D Evangelist, explains the difference between RPC-style and Doc-style ('complex') SOAP web service calls in 4D 2003, and how to manually build the request body a Doc-style web service expects when 4D's Web Services Wizard can't fully automate it. RPC-style services get a fully auto-generated proxy method via SET WEB SERVICE PARAMETER/CALL WEB SERVICE, but Doc-style services expect one XML-described blob parameter that the developer must construct by hand and pass to CALL WEB SERVICE in 'Web Service Manual' mode.

## Key Points

- 4D's Web Services Wizard fully automates RPC-style SOAP calls, auto-generating a proxy method built on SET WEB SERVICE PARAMETER (to set each argument) and CALL WEB SERVICE / GET WEB SERVICE RESULT (to send and retrieve results)
- Doc-style ('complex') web services are flagged in the Wizard by a small icon and expose only a single input parameter (and optionally a single output parameter) that is itself an XML fragment
- For Doc-style calls, the developer must manually build the exact XML that belongs inside the SOAP-ENV:Body element — 4D still wraps it in the envelope, namespaces, and Body tags automatically
- TEXT TO BLOB (with the Text without length option) converts a hand-built XML request string into the BLOB parameter expected by the Wizard-generated proxy method
- CALL WEB SERVICE's fourth parameter, Web Service Manual, tells 4D to insert the caller-supplied BLOB directly into the SOAP-ENV:Body rather than auto-building it from individual SET WEB SERVICE PARAMETER calls
- The response to a Doc-style call comes back as a raw BLOB (just the SOAP body) that the developer must parse manually, unlike RPC-style responses which GET WEB SERVICE RESULT can extract by field name
- Recommends the free generic SOAP test client at soapclient.com/soaptest.html to inspect the exact request XML a WSDL-described service expects before hand-coding it

## Featured Technology

- 4D Web Services Wizard (WSDL analysis / proxy method generation)
- SET WEB SERVICE PARAMETER / CALL WEB SERVICE
- RPC-style vs. Doc-style ('complex') SOAP parameters
- TEXT TO BLOB for manual SOAP body construction
- Web Service Manual mode of CALL WEB SERVICE
- soapclient.com generic SOAP test client

## Historical Commentary

**Status:** Superseded

This note captures a genuinely useful, era-appropriate technique for the moment SOAP web services stopped being fully wizard-generatable — manually building a Doc-style SOAP body and shuttling it through CALL WEB SERVICE's manual mode. Since then, SOAP itself has been broadly superseded by REST/JSON as the default web service protocol, and 4D added native HTTP client commands that make calling modern JSON/REST APIs far simpler than constructing hand-written SOAP envelopes. CALL WEB SERVICE and the SOAP commands referenced here still exist in 4D for legacy SOAP interoperability, but they are no longer the default way to consume a web service.

**References to newer/updated information:**
- 4D introduced native HTTP Client commands (4D v13, 2012, and later expanded) that make calling REST/JSON web services far simpler than constructing SOAP envelopes by hand
- REST/JSON has broadly replaced SOAP as the default web service protocol for new integrations
- CALL WEB SERVICE and the SOAP-related commands used in this note remain available in current 4D for legacy SOAP interoperability
