# Tech Note 07-25: The XML Tools Component

**Author:** David Adams
**Published:** July 3, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46866
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_22-25_(JUN)/07-25_XML_Tools_Component.zip

## Overview
This foundational Technical Note introduces the XML Tools component: a packaged set of roughly 70 public methods (drawn from 120+ internal ones) that wrap 4D's native DOM XML commands with higher-level, error-safe utilities, simplifying common XML reading, writing, searching, and display tasks. It serves as the prerequisite reference for the companion notes on XmlTreeWalker (07-27) and XmlTreeList (07-26).

## Key Points
- Commands are organized into themed groups: XmlNode Utilities (Node Information, Attributes, Relatives), XmlTreeWalker, XmlPath Utilities, XmlTree Utilities, XmlTreeList Utilities, XmlFind Utilities, general XML Tools Utilities, and XmlError.
- Packaging as a component (rather than raw source) reduces exposed surface area, simplifies updating logic shared across multiple Technical Notes/databases, and lets gateway methods handle comprehensive parameter validation once, keeping low-level routines lean.
- Recommends compiling the component for performance; internal tree-scanning uses recursion, which can exhaust stack space on deep XML in uncompiled databases (compilation greatly raises the safe recursion depth).
- Each exposed method has Explorer-comment documentation, plus a public "XML Tools Read Me" method and an internal "XML Tools Read Me Private" listing.
- Important caveat: 4D compares values case-insensitively by default, but XML element/attribute names are case-sensitive — the component always compares them case-sensitively internally (cross-referencing TN 05-41).
- Detailed reference for the XmlNode Utilities: Node Information group is included, covering routines such as XmlNode_GetName, XmlNode_GetValue, XmlNode_PutValueInPointer, XmlNode_GetCDATA/Length, XmlNode_GetFullPath, XmlNode_GetLevel, and XmlNode_MatchesConditions, each an error-safe alternative to a native DOM command.

## Featured Technology
- XML Tools component (XmlNode / XmlTree / XmlTreeWalker / XmlTreeList / XmlFind / XmlPath / XmlError utility groups)
- 4D native DOM XML commands (DOM Parse XML variable, DOM GET XML ELEMENT NAME, etc.)
- 4D component packaging and compilation

## Historical Context
Published July 2007 as the anchor note for a trio of XML-focused Technical Notes (07-25/26/27), this reflects the classic 4D 2004-era procedural language and component model, Design Mode-only development (Project Mode arrived only in 2018), and predates 4D v11's native SQL engine later that same year.

## Historical Commentary
**Status:** Superseded

The engineering principles behind this component — reducing public API surface, centralizing validation in gateway methods, and recommending compilation for recursive code — remain sound practices. However, the specific component, its 2004-era XML-focused APIs, and its dependence on DOM-style XML processing have been superseded both by later improvements to 4D's own native XML commands and by the broader industry shift toward JSON as the default data-interchange format, making this note primarily of historical interest today.
