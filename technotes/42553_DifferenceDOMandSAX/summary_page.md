# Tech Note 06-14: Difference between DOM and SAX

**Author:** Yvan Ayaay, Technical Support Engineer, 4D Inc.
**Published:** April 7, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42553
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_14-17_(APR)/06-14_Dif_btw_DOM_Sax.zip

## Overview
This note explains and contrasts 4D's two XML parsing/manipulation modes — DOM (in-memory tree, random access) and SAX (streaming events, linear access) — with matched code examples for creating and parsing the same sample XML document in each mode.

## Key Points
- **Core tradeoff:** DOM loads an entire XML document into an in-memory tree, enabling fast, random (forward/backward, parent/sibling/child) navigation and full read/write modification, but can be memory-prohibitive for very large documents.
- **SAX's model:** SAX never holds the full document in memory; it streams through it top-to-bottom, emitting events (start tag, end tag, data, etc.) as it goes — scaling to arbitrarily large documents but restricted to strictly linear, read-only traversal.
- **Choosing between them:** DOM suits smaller files or complex/random data access needs; SAX suits very large files or single-pass sequential extraction; otherwise it can come down to programming style preference.
- **Creating XML in DOM:** build an in-memory tree with `DOM Create XML Ref`, `DOM Create XML element`, and `DOM SET XML ELEMENT VALUE`, using stored element references to attach children/siblings, then export with `DOM EXPORT TO FILE`.
- **Creating XML in SAX:** open a document reference and issue a strictly ordered, manually-balanced sequence of `SAX OPEN XML ELEMENT` / `SAX ADD XML ELEMENT VALUE` / `SAX CLOSE XML ELEMENT` calls, ending with `CLOSE DOCUMENT`.
- **Parsing in DOM:** `DOM Parse XML source` builds the tree; elements are located and walked with `DOM Find XML element`, `DOM GET XML ELEMENT VALUE`, and sibling-traversal commands, optionally using XPath notation.
- **Parsing in SAX:** documents must be opened read-only (`Open document`) — 4D warns of conflicts with the underlying Xerces library if opened read-write during SAX parsing — then `SAX Get XML node` is called in a loop, checking returned event constants (XML Start Element, XML DATA, XML End Document, etc.) to drive extraction via `SAX GET XML ELEMENT`/`SAX GET XML ELEMENT VALUE`.

## Featured Technology
- 4D DOM (Document Object Model) XML command set
- 4D SAX (Simple API for XML) command set
- XPath-based element navigation (DOM mode)
- Xerces XML library (4D's underlying XML engine)

## Historical Context
Published in 2006 for 4D v2004, this note predates 4D's SQL engine (v11, 2007), Project Mode (2018), and ORDA, and reflects an era when XML was the dominant structured-data interchange format in 4D development, well before native JSON support matured in later 4D versions.

## Historical Commentary
**Status:** Still relevant

The core DOM-versus-SAX conceptual distinction (in-memory random-access tree vs. streaming linear-access events) is standard, durable computer science that remains accurate today, and 4D's classic DOM/SAX command sets described here are still present in the 4D language. What has shifted since 2006 is emphasis: modern 4D development increasingly reaches for native JSON parsing/collections or 4D's SQL engine for structured data tasks that might once have defaulted to XML, so this note's specific commands remain valid but somewhat less central to everyday 4D work than they were in 2006.
