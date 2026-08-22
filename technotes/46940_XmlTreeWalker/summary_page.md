# Tech Note 07-27: Reading XML Made Easy with the XmlTreeWalker

**Author:** David Adams
**Published:** July 11, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46940
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_26-29_(JUL)/07-27_XML_Tree_Walker.zip

## Overview
This note supplements Technical Note 07-25 (The XML Tools Component) by explaining, in more depth, the XmlTreeWalker sub-system that automates DOM tree traversal in 4D. It targets developers who avoid XML/DOM work because writing recursive tree-navigation code feels complicated.

## Key Points
- 4D supports XML via two engines: SAX (stream-based) and DOM (tree/hierarchical).
- A single command, `DOM Parse XML variable`, parses an entire document into an in-memory DOM tree.
- Manually navigating a DOM tree (top-down, bottom-up, or level-by-level) normally requires recursion, which the note calls inherently hard, citing Steve McConnell's *Code Complete*.
- The XmlTreeWalker performs the traversal internally and calls back to a single method, `XmlTreeWalker_OnNode`, once per node, passing node reference, action label, element name, value, full path, and nesting level.
- Developers dispatch on the action label (e.g. "Dump") inside a `Case of` block to implement only the node-specific logic they need — described as being "like a for loop" over a flattened version of the tree.
- A worked example shows creating a walker with `XmlTreeWalker_Create`, running it with `XmlTreeWalker_Run`, and cleaning up with `XmlTreeWalker_Delete` and `XmlUtil_CloseXMLSafely`.
- The note claims this pattern let a developer extract iTunes library track data in about ten minutes despite iTunes' awkward XML format.
- The bundle includes the XML Tools component, its source code database, and an example database with a "Custom Walk" demo page.

## Featured Technology
- XML Tools component (`XmlTreeWalker_*` routines)
- 4D native DOM XML commands (`DOM Parse XML variable`, etc.)
- Callback/dispatch (Case of) pattern for per-node handling

## Historical Context
Published in mid-2007, this note predates 4D v11's native SQL engine (2007 later release), Project Mode (2018), and ORDA (2018); it reflects the classic 4D procedural language and Design Mode-only era. The callback-per-node traversal idea remains a reasonable pattern conceptually, but the specific XML Tools component and its APIs are tied to 4D 2004-era conventions and have been superseded both by improvements to 4D's native XML/DOM command set and, more broadly, by the industry-wide shift toward JSON as the default data-interchange format, which reduced how often 4D developers need to hand-roll XML tree-walking code at all.

## Historical Commentary
**Status:** Superseded

The XmlTreeWalker pattern is a sound, still-understandable technique for simplifying DOM traversal, but its concrete implementation as a third-party-style component tied to 4D 2004 has been superseded by both later native 4D XML/DOM improvements and the general move away from XML toward JSON in modern application data exchange.
