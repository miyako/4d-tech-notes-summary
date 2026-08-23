# Tech Note: Integrating 4D and Office 2003

- **Asset ID:** 30789
- **Tech Note #:** 03-54
- **Published:** December 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Julien Feasson, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=30789
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_52-55_(DEC)/03-54_4D_and_Office_2003.hqx

## Overview

Julien Feasson (4D, Inc.) explores several ways 4th Dimension 2003 can integrate with Microsoft Office 2003's newly added native XML support, using a running scenario of a sales rep, "Robert," who wastes his Fridays re-entering the same data into Word reports, a CRM, and an Excel expense report.

## Key Points

- Introduces InfoPath 2003 as an offline-capable XML form client that, once online, uses Web Services to push data directly into a 4D database, eliminating manual re-entry into multiple systems.
- Breaks down Word 2003's WordprocessingML XML file format, showing the `<o:DocumentProperties>`, `<w:fonts>`, `<w:styles>`, and `<w:body>` elements that make up a saved-as-XML Word document.
- Demonstrates parsing a Word XML document from 4D using `Open document`, `DOCUMENT TO BLOB`, `Parse XML variable`, and chained `Get First XML element`/`Get Next XML element` calls to extract field values into 4D variables.
- Shows two approaches to generating Word documents from 4D: building the XML from scratch, or (the recommended, simpler route) populating a pre-designed XML template — illustrated by a student-grades report that duplicates a table row per student and fills in each subject's mark.
- Covers using 4D's built-in data export tool to write an XML file from a table (e.g., an Expenses table) that Excel 2003 can then directly import as a spreadsheet via its "Import XML Data" feature.
- Describes a live, real-time alternative: publishing a 4D-hosted SOAP Web service on port 8080, then using Microsoft's Web Service References Tool in the Excel VBA editor to generate a proxy class, so an auto-starting Excel macro (`MyCall.wsm_ExportToXL(ArrScience, ArrMath, ArrHistory, ArrGeography, ArrTotal)`) can pull the latest 4D data straight into a spreadsheet without any file export/import step.
- Frames all of this around eliminating duplicate data entry and improving accuracy for a fictional sales workflow spanning Word, Excel, a CRM, and an ERP system.

## Featured Technology

- Word 2003 / Excel 2003 WordprocessingML XML file formats
- 4D XML parsing commands (Parse XML variable, Get First/Next XML element)
- 4D data export to XML for Excel import
- 4D SOAP Web services (server side)
- Excel Visual Basic Web Service References Tool / SOAP proxy classes
- Microsoft InfoPath 2003

## Historical Commentary

**Status:** Obsolete

Using a fictional sales-rep scenario, this note shows four separate ways 4D 2003 could integrate with the newly XML-capable Office 2003 suite: parsing Word's WordprocessingML XML to extract data, generating Word/Excel XML documents from 4D data (from scratch or via templates) for reports and expense forms, exporting data as XML for direct Excel import, and publishing a 4D SOAP Web service that an Excel VB macro calls directly to pull live data into a spreadsheet. All of these mechanisms are now obsolete: Office moved to the zipped Office Open XML formats (.docx/.xlsx) in Office 2007, InfoPath itself was discontinued by Microsoft in 2014, and SOAP-based Excel/4D integration has been broadly displaced by REST/JSON APIs, though the general goal of scripted, structured data exchange between 4D and desktop productivity tools remains a common integration need addressed today through very different tooling.

**References to newer/updated information:**
- Microsoft Office moved to the Office Open XML formats (.docx/.xlsx/.pptx, a zipped XML package) starting with Office 2007, superseding the flat WordprocessingML/SpreadsheetML XML formats parsed and generated in this note
- Microsoft discontinued InfoPath (mainstream support ended 2014), the forms tool central to this note's "Robert" integration scenario
- SOAP-based Web Services integration between 4D and Office VBA macros has been broadly superseded by REST/JSON APIs in modern application integration
