# Tech Note 03-3: Building a Web Services Client using 4D: The Fed Ex® SOAP serve

**Author:** Frank Chang, 4D Inc. Technical Support
**Published:** January 31, 2003 | **Product/Version:** 4D v | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25620
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_01-05_(JAN)/03-03_building_ws_client.exe

## Overview
TN 03-3 demonstrates 4D 2003's newly introduced SOAP/WSDL web-services client capability by building a working FedEx package-tracking client against a real public SOAP endpoint, using the Web Services Wizard to auto-generate the RPC calling code.

## Key Points
- Introduces SOAP and WSDL concepts and 4D 2003's new built-in Web Services client support.
- Uses the Web Services Wizard in Design Mode to discover a WSDL and auto-generate an RPC project method.
- Demonstrates calling a real public SOAP service (xmethods.net's FedEx tracker) with a string parameter and string return.
- Sample database models Shipments and linked Shipment History tables to track status changes over time.
- Includes optional SMTP email notifications of tracking status updates.

## Featured Technology
- SOAP
- WSDL
- Web Services Wizard
- 4D 2003 Web Services (client)

## Historical Context
Published at the launch of 4D 2003, this was one of several notes promoting the version's new SOAP/XML/Web Services feature set, in the pre-ORDA, pre-REST-API era when SOAP/WSDL was the dominant way to integrate with external web services.

## Historical Commentary
**Status:** Obsolete

This note captures a genuinely significant moment for 4D — the introduction of native SOAP web services client support — but the specific approach (WSDL/SOAP, the Web Services Wizard, and the public xmethods.net FedEx demo endpoint) is now obsolete: xmethods.net's public demo services have long been decommissioned, and REST/JSON with 4D's later HTTP and JSON-parsing commands (and ORDA for data access) have largely superseded SOAP-based integration in current 4D applications.
