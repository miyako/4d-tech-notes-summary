# Tech Note: 4D and salesforce.com

- **Asset ID:** 35693
- **Tech Note #:** 05-03
- **Published:** January 20, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jonathan Le
- **Page URL:** https://kb.4d.com/assetid=35693
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_01-04_(JAN)/05-03_4D_and_salesforce.com.hqx

## Overview

Jonathan Le (Technical Support, 4D, Inc.) explains how 4D 2004 can act as a SOAP client against salesforce.com's sforce Web Services API, walking through the Web Services Wizard's proxy-stub generation, a fully annotated login SOAP request/response, and a bundled sforce Toolkit (Template, Component, Object Library) that lets developers bind 4D table fields to salesforce.com objects and add drag-and-drop CRM buttons to any form.

## Key Points

- Explains the sforce API's core operations (create, delete, describeGlobal, describeSObject, query, queryMore, retrieve, search, update, login, etc.) and how salesforce.com's object-oriented model (Sforce Objects, Custom Objects) maps conceptually to 4D tables and records.
- Shows how the 4D Web Services Wizard consumes a WSDL (local or remote) to auto-generate proxy stub methods that build the SOAP request using `DOM Create XML Ref`, `DOM Create XML element`, and `DOM SET XML ELEMENT VALUE`, then dispatch it with `SET WEB SERVICE PARAMETER` and `CALL WEB SERVICE`.
- Provides a full worked example of the mandatory "login" call: the raw HTTP/SOAP request and response text, the `proxy_login` method code that builds the `<login>` XML block from username/password parameters, and the follow-up code using `GET WEB SERVICE RESULT`, `DOM Parse XML variable`, and `DOM Find XML element` to extract the returned Server URL, Session ID, and User ID needed for all subsequent calls.
- Documents the four essential Web Service commands (`SET WEB SERVICE PARAMETER`, `CALL WEB SERVICE`, `SET WEB SERVICE OPTION`, `GET WEB SERVICE RESULT`) and the DOM XML commands used to construct/parse SOAP messages.
- Describes the sforce Toolkit bundled with the note: a Template and Component for quickly wiring up salesforce.com integration, plus an Object Library of drag-and-drop buttons (create/add/delete/modify against a selection of records) bound to specific table fields via a Bind Tool, with the Id field mapping being mandatory.
- Notes that since 4D 2003/2004 added native Web Service commands and encoding support, the older 4D Internet Toolkit plug-in is no longer required for this kind of integration.

## Featured Technology

- sforce (salesforce.com) SOAP Web Services API
- 4D Web Services Wizard (proxy stub generation)
- SET WEB SERVICE PARAMETER / CALL WEB SERVICE / SET WEB SERVICE OPTION / GET WEB SERVICE RESULT
- DOM XML commands (DOM Create XML Ref, DOM Find XML element, DOM GET XML ELEMENT VALUE)
- sforce Toolkit (Template, Component, Object Library) for 4D

## Historical Commentary

**Status:** Superseded

Written by Jonathan Le of 4D's Technical Support team, this note walks through 4D 2004's new Web Services commands by building a working salesforce.com integration, including a fully worked SOAP login exchange and a bundled Object Library/Template/Component toolkit for binding 4D tables to sforce objects. It captures the SOAP/WSDL era of enterprise web-services integration that 4D supported starting in 2003-2004. The specific sforce API version and toolkit are long obsolete -- Salesforce has moved through many generations of SOAP and REST APIs since 2005 -- and 4D's own web-service story has shifted heavily toward native HTTP Client commands and JSON for REST integration, though the CALL WEB SERVICE/SOAP commands described here still exist in 4D for legacy SOAP consumers.

**References to newer/updated information:**
- Salesforce has replaced the 2004-era sforce SOAP API with many newer SOAP and REST API versions since 2005
- 4D has since added native HTTP Client commands and JSON support, which are now the preferred way to integrate with modern (mostly REST-based) cloud services
- The legacy CALL WEB SERVICE/SET WEB SERVICE PARAMETER/DOM XML command set described here still exists in 4D for consuming SOAP web services
