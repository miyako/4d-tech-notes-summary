# Tech Note: Interaction between 4D 2003 and Microsoft Excel® (Web Services)

- **Asset ID:** 26846
- **Tech Note #:** 03-09
- **Published:** February 28, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Matthieu Chevrier
- **Page URL:** https://kb.4d.com/assetid=26846
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_06-10_(FEB)/03-09_4D_2003_and_Excel.hqx

## Overview

Matthieu Chevrier of 4D Inc. demonstrates how to expose data from a 4th Dimension 2003 database as a SOAP Web Service and consume it directly from Microsoft Excel, building a small Excel Add-In (.xla) using VBA and the Microsoft SOAP Toolkit (version 3.0 or later) as the client. On the 4D side, a single method, SOAP_GetDataForCategory, accepts a longint category argument declared with SOAP DECLARATION, validates it (throwing a SOAP fault via SEND SOAP FAULT for out-of-range values or empty result sets), queries a demo table of a few thousand generated records, and returns four parallel arrays (name, score, date of birth, category) populated with SELECTION TO ARRAY and individually declared as SOAP outputs; publishing only requires enabling Web Services in the database preferences and starting the 4D web server, after which the WSDL is auto-generated at a URL like http://yourip:8080/4dwsdl. On the Excel side, the note walks through installing the provided .xla Add-In (globally or per-user), configuring the remote WSDL URL through a small VBA UserForm, and generating a SOAP client stub class via the Toolkit's "Web Service Reference" wizard, with the actual call-and-populate logic living in a JustDoIt VBA module that invokes the remote method and writes the returned arrays into the active worksheet using Variant types. The note closes with practical caveats — VBA's SOAP client re-downloads and re-parses the WSDL on every session (a performance and reliability quirk), performance is best suited to small-to-medium datasets, and it suggests extending the pattern toward a fully generic connector, added security (SSL, login/ logout session tokens), and even a similar Word Add-In for mail-merge-style data pulls from 4D.

## Key Points

- A single 4D 2003 method, `SOAP_GetDataForCategory`, is published as a Web Service: it declares its longint input parameter with `SOAP DECLARATION(...;SOAP Input;"category")`, validates the value (throwing a `SEND SOAP FAULT(SOAP Client Fault;...)` if out of range), queries a demo table, and returns four parallel arrays (name/score/date/category) built with `SELECTION TO ARRAY` and each individually declared as SOAP outputs.
- Enabling the service server-side requires only checking a database preference (Web Services in the Web section), marking the method as published, and starting the 4D web server — after which 4D auto-generates a WSDL file (e.g. at `http://yourip:8080/4dwsdl`) describing the service.
- The Excel client is a VBA Add-In (.xla) with four parts: a `UserForm` dialog storing the remote WSDL URL in a `gServerURL` global, an `Init` module wiring `Auto_Open`/`Auto_Close` menu setup, a `JustDoIt` module (notably the `RunMenu1` method) that performs the actual SOAP call and writes results into the active worksheet via `ActiveCell`/`CurrentSheet.Cells`, and a generated stub class (`clsws_ExampleOfWebService`) produced by the Microsoft SOAP Toolkit's "Web Service Reference" wizard from the WSDL.
- A noted quirk: the VBA SOAP client re-downloads and re-parses the WSDL file every time its internal class is initialized, which the author flags as both a reliability feature and a performance/annoyance drawback, suggesting a locally cached WSDL file as a workaround.
- The note explicitly scopes itself to server-side (publishing) capability only, and suggests further extensions: a fully generic connector that discovers tables/fields at runtime, writing data back from Excel to 4D, adding SSL encryption and custom login/logout session tokens for security, and a similar Word Add-In for automated mail-merge-style imports.

## Featured Technology

- 4D 2003 server-side Web Services publication (SOAP/WSDL)
- SOAP DECLARATION command for input/output argument typing
- SELECTION TO ARRAY for returning multiple typed arrays over SOAP
- SEND SOAP FAULT for client/server error signaling
- Microsoft SOAP Toolkit 3.0+ client generation from WSDL
- Excel VBA Add-In (.xla) architecture (Auto_Open/Auto_Close, UserForm preferences)

## Historical Commentary

**Status:** Obsolete

This is a clear, practical walkthrough of 4D 2003's brand-new server-side SOAP publishing feature paired with a genuinely useful Excel VBA client Add-In, at a time when SOAP/WSDL was the standard way to expose structured application data to Office clients. That SOAP/WSDL approach has been broadly superseded across the industry by REST/JSON APIs, and modern Excel-to-database integration is far more likely to use Power Query, native REST connectors, or ODBC than a hand-built SOAP Toolkit client; 4D's own Web Services publishing has likewise moved toward REST-oriented and OData/ORDA-based data exposure. The specific VBA Add-In and 4D SOAP_GetDataForCategory pattern shown here would need a full rewrite to be useful with current Excel and 4D versions.

References to newer/updated information:
- REST/JSON has broadly replaced SOAP/WSDL as the standard way to expose data from a server (including 4D) to Excel and other Office clients
- Excel's Power Query and native REST/OData connectors have superseded custom VBA SOAP Toolkit Add-Ins for pulling external data into spreadsheets
- 4D's own Web Services capabilities have evolved toward REST-oriented data exposure (including ORDA-based data access) since this 2003-era SOAP publishing model
