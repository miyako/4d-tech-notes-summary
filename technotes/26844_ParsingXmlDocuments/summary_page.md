# Tech Note: Parsing XML Documents

- **Asset ID:** 26844
- **Tech Note #:** 03-06
- **Published:** February 28, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Dave Dell'Aquila
- **Page URL:** https://kb.4d.com/assetid=26844
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_06-10_(FEB)/03-06_Parsing_XML_Documents.hqx

## Overview

Dave Dell'Aquila, Sr. 4D Evangelist, introduces a general-purpose technique for parsing any XML document using the new XML commands shipped in 4th Dimension 2003, aimed at developers who will increasingly encounter XML through Web Services and other data exchange. After framing XML as hierarchically structured and therefore straightforward to traverse programmatically, the note builds a small toolkit: an arrayAppend helper method for growing arrays element by element, an XML_Open method that calls Open document and Parse XML source to obtain a root element reference, and a recursive XML_Parse(elementRef) method that uses Get First XML element to descend into children and Get Next XML element to move across siblings, calling itself at each new node until the whole tree has been visited — with a companion XMLgetElementInfo method using GET XML ELEMENT NAME and GET XML ELEMENT VALUE to record each element's name and value into parallel text arrays. The technique is then extended to attributes, using Count XML attributes and GET XML ATTRIBUTE BY INDEX to populate two-dimensional arrays (one row per element) that can later be copied out per-element with COPY ARRAY. Finally, the note connects this generic parser to 4D 2003's new client-side Web Services support: for DOC-style Web Services (illustrated with a hypothetical Google search service) that return a complex type as a BLOB, Parse XML variable can operate directly on the BLOB (bypassing the 32K text-variable size limit) to obtain a root reference and feed it straight into the same XML_Parse routine, with CLOSE XML releasing parser memory once done.

## Key Points

- A small, reusable toolkit is built from three methods: `arrayAppend` (appends a value to the end of an array via `INSERT ELEMENT`), `XML_Open` (calls `Open document` then `Parse XML source` to get a root element reference and initializes element-name/element-value text arrays), and the recursive `XML_Parse(elementRef)` traversal method itself.
- The traversal algorithm alternates `Get First XML element` (to descend into a node's first child, recursing into `XML_Parse` again if found) with `Get Next XML element` (to move to the next sibling at the current level) inside a `Repeat...Until` loop, visiting every node in the document depth-first.
- Each visited element's name and value are captured via `GET XML ELEMENT NAME` / `GET XML ELEMENT VALUE` in a companion `XMLgetElementInfo` method and appended to parallel arrays using the earlier `arrayAppend` helper.
- The technique is extended to attributes with `Count XML attributes` and `GET XML ATTRIBUTE BY INDEX`, populating two-dimensional `attributeName2DArray`/`attributeValue2DArray` arrays (one row per element) that can later be sliced out per-element with `COPY ARRAY`.
- For DOC-style Web Services results (illustrated with a Google search service returning a BLOB), `Parse XML variable` is used directly on the BLOB — bypassing 4D's 32K text-variable size limit — to obtain a root reference that feeds straight into the same `XML_Parse` routine, with `CLOSE XML` releasing parser memory afterward.

## Featured Technology

- Parse XML source / Parse XML variable commands
- Get First XML Element / Get Next XML element tree traversal
- GET XML ELEMENT NAME / GET XML ELEMENT VALUE
- Recursive depth-first XML_Parse traversal algorithm
- GET XML ATTRIBUTE BY INDEX / Count XML attributes for 2D attribute arrays
- CLOSE XML for freeing parser memory
- DOC-style Web Services BLOB parsing (e.g. Google Web Service example)

## Historical Commentary

**Status:** Partially Superseded

As one of the earliest 4D Tech Notes covering the brand-new 2003 XML parser commands, this note gives a clean, reusable recursive traversal pattern (XML_Parse/XMLgetElementInfo/arrayAppend) that many 4D developers likely built on directly for years, and correctly anticipates that Web Services responses would be a major use case for it. The low-level Get First/Next XML Element traversal API it teaches is still present in current 4D and technically usable, but 4D has since added considerably higher-level XML and JSON tooling (including native JSON parsing, the XML DOM-oriented commands, and ORDA/entity-based structured data handling) that make hand-rolled recursive element-by-element traversal unnecessary for most modern integration work, especially since most new Web Services and APIs use JSON rather than XML/SOAP.

References to newer/updated information:
- 4D has since added native JSON parsing commands, which have become the more common choice for modern Web/REST API integration compared to the XML/SOAP pattern shown here
- The low-level Get First/Next XML Element traversal commands are still present in current 4D, but higher-level XML/JSON tooling now reduces the need to hand-write a recursive traversal routine like the one in this note
