# Tech Note 07-02: Identifying an XML Document's Type

**Author:** David Adams
**Published:** January 17, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45180
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_01-04_(JAN)/07-02_XML_Types.zip

## Overview
This note explains how to identify what "type" of XML document has been parsed — since a generic parser can successfully read any well-formed XML but that doesn't mean the program understands its contents — using the four XHTML DTD variants (Strict, Transitional, Frameset, 1.1) as a concrete worked example with 4D's DOM commands.

## Key Points
- Frames the general problem: XML documents like WSDL, SVG, and XHTML are all valid XML but require completely different interpretation logic.
- `Demo_ReadXHTMLDocument` cascades four tests: (1) is the document well-formed XML, (2) is the root element name literally `html` (case-sensitive comparison via `CS_AlphasAreEqual` from Tech Note 05-41), (3) does the root element carry the `xmlns="http://www.w3.org/1999/xhtml"` namespace attribute, (4) do the DOCTYPE Public ID and System ID (read via `DOM Get XML information`) match one of the four defined XHTML DTDs.
- `DOM_GetRootElementReference` helper locates the true root element while skipping the synthetic `#document` node.
- Uses the same custom `ON ERR CALL` error-trapping pattern found throughout this family of XML tech notes.
- Explicitly notes the XHTML rules are just an illustrative example; the same layered approach (root name, namespace, DTD identifiers) generalizes to detecting other XML document types.
- Sample database includes a `Test_GetRootElementReference` test harness.

## Featured Technology
- 4th Dimension DOM XML commands
- `DOM Get XML information` (PUBLIC ID / SYSTEM ID)
- XHTML 1.0 Strict/Transitional/Frameset and XHTML 1.1 DTD identification
- Custom `ON ERR CALL` error trapping pattern

## Historical Context
Published January 2007, just before 4D v11 introduced native SQL, this note is doubly dated: both its underlying 4D DOM XML API and its worked example (XHTML's DTD-based document versioning) reflect mid-2000s web standards practice that HTML5 later abandoned in favor of a single simple doctype.

## Historical Commentary
**Status:** Obsolete

XHTML's DOCTYPE/Public-ID/System-ID-based versioning scheme was industry-wide superseded by HTML5, which doesn't use this identification method at all, making the concrete worked example obsolete. 4D's classic DOM XML commands are likewise legacy relative to modern 4D development (which includes native JSON support). The general layered document-type-sniffing strategy (root element, namespace, DTD/schema identifiers) remains conceptually sound for anyone still working with DTD-based XML formats, but has little direct applicability to current web development.
