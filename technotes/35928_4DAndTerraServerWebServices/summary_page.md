# Tech Note: Using 4D with TerraServer USA Web Services

- **Asset ID:** 35928
- **Tech Note #:** 05-05
- **Published:** February 3, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thang Nguyen
- **Page URL:** https://kb.4d.com/assetid=35928
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_05-11_(FEB)/05-05_TerraServer_Web_Services.hqx

## Overview

Thang Nguyen (4D Technical Support Engineer) demonstrates consuming Microsoft/USGS's TerraServer-USA SOAP web service — a large repository of aerial photography and topographic imagery — from a 4D 2004 database, using 4D's SOAP Wizard to generate proxy code from the service's WSDL and DOM XML commands to build requests and parse responses.

## Key Points

- Explains SOAP's XML envelope (Header + Body) and contrasts synchronous, tightly-coupled RPC-style messages against document-driven, loosely-coupled DOC-style messages — TerraService uses DOC style.
- WSDL describes a web service's operations/parameters; 4D's Web Service Wizard consumes a WSDL (here, http://terraservice.net/TerraService2.asmx?WSDL) to auto-generate proxy method source code.
- Demo database covers 5 of TerraService's 16 methods: ConvertLonLatPtToNearestPlace, ConvertPlaceToLonLatPt, GetAreaFromPt, GetPlaceList, and GetTileMetaFromLonLatPt.
- Each method builds a request document with DOM Create XML Ref/DOM Create XML element/DOM SET XML ELEMENT VALUE, sends it via SET WEB SERVICE PARAMETER("XMLIn";...) and CALL WEB SERVICE(url; SOAPAction; method; namespace; Web Service Manual), then reads back results via GET WEB SERVICE RESULT and DOM Parse XML variable/DOM Find XML element/DOM GET XML ELEMENT VALUE.
- ON ERR CALL is layered around each generated method to surface connection or service errors gracefully (e.g. alerting the user if TerraServer-USA can't be reached).
- The example UI offers Navigate Map, Select Image (Topo vs. Photo imagery), and Search City options, letting users click to zoom the US map or jump to a location by city/state/country.
- References an earlier note, '03-53 Web Services Intro,' for general SOAP/web-service background.

## Featured Technology

- 4D SOAP Wizard (Web Service Wizard) code generation from WSDL
- CALL WEB SERVICE / SET WEB SERVICE PARAMETER / GET WEB SERVICE RESULT
- DOM XML commands (DOM Create XML Ref, DOM Create XML element, DOM Find XML element, DOM GET/SET XML ELEMENT VALUE)
- TerraServer-USA SOAP/WSDL API (ConvertLonLatPtToNearestPlace, ConvertPlaceToLonLatPt, GetAreaFromPt, GetPlaceList, GetTileMetaFromLonLatPt)
- DOC-style SOAP messaging vs. RPC-style

## Historical Commentary

**Status:** Obsolete

Thang Nguyen demonstrates consuming a real external SOAP web service — Microsoft/USGS's TerraServer-USA aerial-imagery API — from 4D 2004 using the 4D SOAP/Web Service Wizard to auto-generate proxy methods from the service's WSDL, manually building the request XML via DOM commands and parsing the response the same way. This is a solid, working example of classic SOAP/XML web-service consumption that was mainstream in the mid-2000s enterprise integration world; both the specific TerraServer-USA service and the SOAP/WSDL-heavy integration style it demonstrates have since faded from relevance — REST/JSON APIs now dominate web-service integration, and TerraServer-USA itself was retired years ago — so the note is a snapshot of a bygone integration pattern more than a directly reusable technique today, though 4D's DOM XML and SOAP commands themselves remain available for legacy or XML-heavy integrations.

References to newer/updated information:

- TerraServer-USA, the specific web service this note integrates with, has been retired for years and the demo database can no longer reach a live service
- REST/JSON APIs consumed via 4D's native HTTP Client and JSON commands (available since roughly 4D v14-15) have largely superseded SOAP/WSDL-based integration for new development
- 4D's SOAP Wizard, CALL WEB SERVICE, and DOM XML commands remain part of current 4D for legacy SOAP-based integrations
