# Tech Note: XML – An Introduction to Extensible Markup Language

- **Asset ID:** 30583
- **Tech Note #:** 03-48
- **Published:** November 30, 2003
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=30583
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_48-51_(NOV)/03-48_XML_An Introduction.hqx

## Overview

Frank Chang, of 4D Technical Support, provides a from-scratch introduction to XML for 4D developers: what it is (a syntax for creating markup languages, derived from SGML, distinct from and less rigid than HTML), the grammar of processing instructions and declarative statements, how to attach a CSS style sheet directly to an XML document for browser display, and how to use XSLT to transform an XML document into XHTML. It closes with book recommendations and a pointer to a related, more advanced Tech Note (#26844) on parsing XML in 4D.

## Key Points

- Explains XML's relationship to SGML and contrasts it with HTML: XML describes data and lets authors define their own tags, while HTML only describes how to display predefined tags
- Covers the mandatory XML prologue (`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>`), processing instructions, and DOCTYPE declarative statements
- Demonstrates styling a raw XML document directly in a browser using a linked CSS style sheet via `<?xml-stylesheet type="text/css" href="..."?>`
- Introduces XSLT as a transformation language, with the `<xsl:stylesheet>`/`<xsl:transform>` root element and the W3C namespace declaration
- Walks through a complete names.xml + names.xsl example using `<xsl:template match="/">`, `<xsl:for-each select="people/name">`, and `<xsl:value-of select="..."/>` to render an HTML table
- Points to a companion, code-level Tech Note (KB #26844, 'Parsing XML Documents') for actually parsing XML from 4D methods, since this note is scoped to XML/XSLT fundamentals only
- Recommends further reading: Beginning XML (David Hunter), Special Edition Using XML (David Gulbransen et al.), and XSLT (Doug Tidwell)

## Featured Technology

- XML syntax (elements, attributes, PIs, DOCTYPE)
- XML prologue and encoding declarations
- CSS styling of raw XML documents
- XSLT transformations (xsl:stylesheet / xsl:template)
- xsl:for-each / xsl:value-of
- SGML lineage and DTD/XML Schema validation

## Historical Commentary

**Status:** Still Relevant

The XML/XSLT fundamentals covered here are still accurate today, and 4D still ships native XML parsing and generation commands that build directly on these concepts. However, XML's role as the default data-interchange format for web/API integrations has been substantially displaced by JSON since the early 2000s, so a developer encountering XML today is more likely to be dealing with legacy systems, document formats, or specific enterprise/XSLT-based publishing pipelines rather than a typical new web API.

**References to newer/updated information:**
- JSON has become the dominant lightweight data-interchange format for web/API use cases since the mid-2000s, though XML remains common in documents and legacy/enterprise integrations
- 4D's native XML commands (introduced around this era) are still present and supported in current 4D
