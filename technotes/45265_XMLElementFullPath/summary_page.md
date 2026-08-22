# Tech Note 07-03: Getting an XML Element's Full Path

**Author:** David Adams
**Published:** January 24, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45265
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_01-04_(JAN)/07-03_Get_XML_Full_Path.zip

## Overview
This note documents a `DOM_GetFullPath` routine that computes the full hierarchical path to any XML node (e.g., `/contacts/contact/business/phone/area_code/`) using 4D's native DOM commands, solving the ambiguity problem created by repeated element names appearing at different points in a tree.

## Key Points
- Explains why full paths matter: elements like `<phone>`/`<area_code>`/`<number>` can appear multiple times under different parents (e.g., `<business>` vs `<home>`), so the path disambiguates otherwise identical node names.
- Native `DOM Find XML element` requires the path to be known in advance and can't express suffix-style patterns (e.g., "ends with /phone/area_code/ regardless of ancestors") — this note's routine works bottom-up instead, suiting generic tree-walking code.
- `DOM_GetFullPath` starts at a node and repeatedly calls `DOM Get parent XML element`, prepending each ancestor's name, until it reaches the root or an invalid/`#document` node, returning an empty string for null/invalid input.
- Uses the same custom `ON ERR CALL`-based error trapping pattern as companion notes to safely handle invalid references without crashing.
- Notes that XML paths/names are case-sensitive, cross-referencing Tech Note 05-41 for case-sensitive comparison utilities.
- Sample database includes a `Test_GetFullPath` test harness.

## Featured Technology
- 4th Dimension DOM XML commands
- `DOM Get parent XML element`, `DOM Find XML element`
- Custom `ON ERR CALL` error trapping pattern

## Historical Context
Published January 2007, this is one of a cluster of small, focused XML/DOM utility Tech Notes released in this period, predating 4D v11's native SQL and reflecting the classic Design-Mode-only 4D development era.

## Historical Commentary
**Status:** Superseded

4D's classic DOM XML command set, while still present for backward compatibility, has been overtaken by native JSON support and more modern data-interchange approaches in current 4D development. The bottom-up path-building technique itself — walking parent references to construct a location string — is a generic, still-valid tree-traversal pattern applicable to any hierarchical data structure, XML or otherwise.
