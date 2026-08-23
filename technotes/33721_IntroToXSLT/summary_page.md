# Tech Note: Introduction to XSLT

- **Asset ID:** 33721
- **Tech Note #:** 04-34
- **Published:** August 26, 2004
- **Product / Version:** 4th Dimension 2003.4
- **Platform:** Mac & Win
- **Author:** Julien Feasson (Software Engineer, 4D Inc.)
- **Page URL:** https://kb.4d.com/assetid=33721
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_31-35_(JUL)/04-34_Intro_to_XSLT.hqx

## Overview

Written by Julien Feasson, this note introduces XSLT support that was new to 4th Dimension 2004, framed against the mid-2000s rise of XML as a data-interchange standard. After explaining what XSLT is and how it lets developers separate raw XML data from its presentation, the note covers two ways to use it in 4D: through the User-mode Export dialog, where end users can select a supplied XSL stylesheet to transform exported data into HTML, Word, Excel, PDF, or other formats either at export time or via an embedded link resolved later by the viewing application; and programmatically, via three new commands -- APPLY XSLT TRANSFORMATION (applies a stylesheet to an XML document or blob variable and writes a document or blob result), SET XSLT PARAMETER (passes runtime parameters into the stylesheet, e.g. to filter displayed data by year), and GET XSLT ERROR (retrieves detailed transformation error messages including line/column information for debugging). A bundled XSLTDemo database demonstrates all three usage patterns: two static transformations selecting different report years, a parameterized single-stylesheet variant using SET XSLT PARAMETER, and an ON ERR CALL-guarded transformation that deliberately errors to showcase GET XSLT ERROR.

## Key Points

- 4D 2004 introduced three new commands: APPLY XSLT TRANSFORMATION, SET XSLT PARAMETER, and GET XSLT ERROR for programmatic XML/XSLT transformations.
- APPLY XSLT TRANSFORMATION(XML_Path;XSL_Path;HTML_Path) accepts documents or blob variables for both the XML source and XSL stylesheet and can output a document or blob.
- SET XSLT PARAMETER("Year";$1) passes a runtime value into the XSL stylesheet, letting one stylesheet dynamically filter/select which data to display instead of maintaining separate stylesheets per case.
- GET XSLT ERROR retrieves the XSLT processor's error message plus the row/column of the failure, intended to be captured via an ON ERR CALL handler around APPLY XSLT TRANSFORMATION.
- The Export dialog's XML tab offers 'Refer to existing XSL' (apply the transformation at export time to produce HTML/Word/Excel/PDF/etc.) versus 'Insert a link to the XSL file' (defer the transformation to the viewing application/browser).
- The bundled XSLTDemo database's Apply2003XSLT/Apply2004XSLT/ApplyParamXSLT methods and a deliberately-erroring stylesheet demonstrate all three commands end to end, opening results in the default browser via OPEN WEB URL.

## Featured Technology

- APPLY XSLT TRANSFORMATION command
- SET XSLT PARAMETER / GET XSLT ERROR commands
- XSLT (XSL Transformations) applied to XML documents or variables
- Export dialog 'Refer to existing XSL' / 'Insert a link to the XSL file' options

## Historical Commentary

**Status:** Superseded

This note captures 4D's investment in native XML/XSLT tooling during the mid-2000s XML era, and the APPLY XSLT TRANSFORMATION, SET XSLT PARAMETER, and GET XSLT ERROR commands introduced here are still present and functional in current 4D. However, the broader industry has since moved from XML/XSLT to JSON for everyday data interchange and web APIs, and 4D itself added native JSON parsing and manipulation commands that most modern 4D developers reach for instead of XSLT transformations for routine format-conversion tasks, leaving XSLT mostly relevant to legacy XML-centric workflows or specialized document-generation pipelines.

**References to newer/updated information:**
- 4D added native JSON support to its language, which now handles most lightweight data-interchange needs that XSLT once served
- Industry-wide, JSON has largely replaced XML/XSLT as the default format for web APIs and data exchange
- The APPLY XSLT TRANSFORMATION, SET XSLT PARAMETER, and GET XSLT ERROR commands remain in the current 4D language for XML-centric transformation and reporting scenarios
