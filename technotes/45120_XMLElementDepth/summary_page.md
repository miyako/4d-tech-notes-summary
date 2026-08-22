# Tech Note 07-01: Getting an XML Element's Depth

**Author:** David Adams
**Published:** January 9, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45120
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_01-04_(JAN)/07-01_XML_Element_Depth.zip

## Overview
This is the first Tech Note of the 2007 calendar year and the first in a short run of small XML DOM utility notes. It documents a `DOM_GetNodeLevel` routine that returns how deep an XML element sits within its tree (root = level 1), a function missing from 4D's native DOM command set.

## Key Points
- Motivates the need for a depth function with examples: formatting a hierarchical list display by bolding/bracketing nodes at particular levels, deciding which tree levels should become new database records, ignoring elements at certain levels, and indenting textual tree dumps proportional to depth.
- `DOM_GetNodeLevel` walks upward from the target node via repeated `DOM Get parent XML element` calls, incrementing a counter for each valid, non-`#document` ancestor found.
- Uses the same custom `ON ERR CALL` error-trapping pattern (save/restore prior handler and Error state) seen throughout this family of XML tech notes, to safely stop at the top of the tree or on invalid references.
- Sample database includes a `Test_GetNodeLevel` harness exercising good nodes, bad nodes, and the `#document` node.

## Featured Technology
- 4th Dimension DOM XML commands
- `DOM Get parent XML element`
- Custom `ON ERR CALL` error trapping pattern

## Historical Context
Published January 9, 2007, this note kicks off a cluster of closely related small XML DOM utility notes (07-01 through 07-04) released over the following weeks, all predating 4D v11's native SQL engine and reflecting the classic Design-Mode-only 4D era.

## Historical Commentary
**Status:** Superseded

4D's classic DOM XML command set, while retained for backward compatibility, is less central to modern 4D development given the platform's later native JSON support. The ancestor-counting technique for computing tree depth, however, is a simple and generic algorithm that remains valid for any tree-structured data, XML or otherwise.
