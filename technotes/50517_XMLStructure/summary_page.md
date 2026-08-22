# Tech Note 08-26: XML Structure Import/Export in 4D v11 SQL

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** July 23, 2008 | **Product/Version:** 4D v11.1 | **Platform:** Mac & Win
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_25-29_(JUL)/08-26_XML_Structure.pdf

## Overview
A landmark feature introduced in 4D v11 SQL Release 1 (late 2007) was the ability to export a database's structure definition—tables, fields, indexes, relations, and metadata—to an XML file. This capability enabled developers to programmatically clone database structures, seed new databases from templates, and exchange structure metadata with external systems. This note provides both a deep XML foundation (necessary given widespread unfamiliarity with XML standards in the 2008 era) and detailed documentation of the 4D Structure Definition XML format.

## Key Points
- **Structure export, not backup:** A Structure Definition XML file encodes only schema (tables, fields, relations, indexes) and metadata; it contains zero data rows. It is unsuitable as a backup mechanism but excellent for structure cloning and cross-environment provisioning.
- **XML fundamentals:** The note covers XML basics (root elements, tag syntax, case sensitivity, entity references like `&lt;` and `&gt;`, well-formed vs. valid documents, and Document Type Definitions).
- **DOM vs. SAX parsing:** DOM loads the entire XML tree into memory, enabling random-access navigation; SAX streams elements one-at-a-time, conserving memory for large files. 4D's implementation supports both; the choice depends on file size and access patterns.
- **Apache foundation:** 4D's XML support is built on Apache Xerces (parsing/manipulation, DOM/SAX) and Xalan (XSLT transformations), open-source libraries widely used across the industry.
- **XPath notation:** Elements are addressed using XPath (e.g., `/root/element1/element2/element3`), enabling precise navigation and queries.
- **Structure Definition elements:** The exported XML includes `<base>` (root), `<table>` entries, `<field>` definitions, `<index>` specifications, `<relation>` definitions, and metadata tags (`field_extra`, `table_extra`, `editor_*_info`).
- **Commands for manipulation:** 4D provides DOM commands (DOM Create XML Ref, DOM Create XML Element, DOM EXPORT TO FILE, DOM CLOSE XML) and SAX commands (using document-themed operations like OPEN DOCUMENT, APPEND DOCUMENT, SEND PACKET) for working with XML.
- **XSLT transformation:** Developers can apply XSL stylesheets to transform Structure Definition XML into other formats (documentation, code generation, migration, etc.) using APPLY XSLT TRANSFORMATION and SET XSLT PARAMETER commands.

## Featured Technology
- XML (Extensible Markup Language)
- 4D v11 SQL Structure Definition format
- Apache Xerces (XML parsing library)
- Apache Xalan (XSLT transformation library)
- DOM (Document Object Model) API
- SAX (Simple API for XML)
- XPath query language
- XSLT (XML Stylesheet Language Transformations)

## Historical Context
Published in July 2008, as 4D v11 SQL matured, this feature was ahead of its time in enabling programmatic database structure manipulation. However, the technical community's embrace of XML has waned significantly since the 2010s, with JSON becoming the de facto standard for data interchange and configuration. The Structure Definition feature itself, while technically elegant, was never adopted at scale; most 4D developers continued to clone databases using the GUI or manual scripts. The broader REST and ORDA movements (v12 and v18 respectively) shifted 4D's architectural focus away from XML-centric interoperability.

## Historical Commentary
**Status:** Historical Interest Only

The XML Structure Export/Import feature remains functional in 4D v11 SQL and later, but is rarely used in modern practice. REST APIs (introduced in 4D v12, 2012) became the standard for interoperability, and ORDA (2018+) introduced native JSON serialization, rendering XML-based structure interchange largely obsolete. While the XML fundamentals documented here remain valid (XML is still used in enterprise systems, configuration files, and legacy code), the specific use case of structure-driven database provisioning has been superseded by infrastructure-as-code (IaC) tools, containerization (Docker), and modern database migration patterns. A developer needing to clone a 4D database structure today would use 4D's existing GUI tools, export/import via REST APIs (if v12+), or use ORDA with JSON serialization (if v18+), rather than manually craft XML Structure Definition files. The note is primarily valuable as a historical record of 4D's XML ambitions and as reference material for maintainers of legacy 4D v11 SQL systems.
