# Tech Note: The XML_Utilities Component

- **Asset ID:** 32788
- **Tech Note #:** 04-21
- **Published:** May 27, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=32788
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2004/MacOS/TN_2004_21-25_(MAY)/04-21_XML_Utilities.hqx

## Overview

David Adams presents XML_Utilities, a small component of convenience methods built on top of 4th Dimension 2003's native XML commands, providing element counting, existence checks, value extraction, and whitespace cleanup, while doubling as a worked tutorial on recursive preorder traversal of parsed XML trees.

## Key Points

- Four public methods make up the component: `xutil_CountOccurrences` (counts occurrences of a named element), `xutil_ElementExists` (True/False existence check), `xutil_GetValue` (returns the text value of the Nth occurrence of a named element, optionally cleaned of whitespace), and `xutil_StripWhitespace` (removes tab/line-feed/carriage-return/space characters per the XML whitespace definition).
- The methods expect 16-character XML element references from `Parse XML source`/`Parse XML variable`, and the note stresses that callers remain responsible for calling `CLOSE XML` themselves since these utility functions do not.
- XML names are case-sensitive (unlike native 4D name comparisons, which also ignore diacriticals), so a private helper, `xutilStringsAreEqual`, performs a manual byte-by-byte ASCII comparison to correctly match XML semantics.
- The component walks XML trees using a "preorder" (top-to-bottom, left-to-right) traversal, and the note illustrates this with a fully worked sample XML document showing the exact node visitation order, occurrence numbers, and cleaned values.
- `xutil_CountOccurrences` and `xutil_GetValue` both use internal recursion (with a `firstCall` argument managing the recursive chain) to walk every branch of the tree; the note notes that a loop-plus-stack (array-based) approach is an alternative to recursion.
- The component is distributed both as a reviewable/editable source-code database and as an installable 4D Insider component, and its functions are directly reused by two related 2004 SOAP tech notes for parsing captured SOAP messages.

## Featured Technology

- xutil_CountOccurrences / xutil_ElementExists / xutil_GetValue / xutil_StripWhitespace
- 4th Dimension 2003 native XML commands (Parse XML variable, Get First/Next XML element, GET XML ELEMENT NAME/VALUE)
- Preorder (top-to-bottom, left-to-right) XML tree traversal via recursion
- Case-sensitive XML name comparison (xutilStringsAreEqual)
- Whitespace stripping per XML whitespace rules (tab/LF/CR/space)
- 4D Insider component installation

## Historical Commentary

**Status:** Superseded

This note documents David Adams' XML_Utilities component, a small set of recursive helper methods (`xutil_CountOccurrences`, `xutil_ElementExists`, `xutil_GetValue`, `xutil_StripWhitespace`) that wrap 4th Dimension 2003's native XML parsing commands to make locating and reading element values by name easier, while also serving as a worked example of recursive preorder tree traversal. It is directly referenced by two companion 2004 SOAP tech notes as the tool used to extract values from raw XML/SOAP responses, so it had real practical use in that era's Web Services workflows. 4D's native XML command set has since expanded considerably and JSON has displaced much everyday structured-data handling that once relied on XML, so this specific utility component is now largely of historical interest, though the recursive traversal technique and case-sensitive comparison logic it demonstrates remain instructive and technically sound.

**References to newer/updated information:**
- 4D's native XML command set has grown substantially since 2004, and many use cases XML_Utilities addressed can now be handled with fewer lines of native code
- JSON has displaced much of the everyday structured-data exchange that XML (and this component) once handled in 4D applications
- 4D Insider, the component-installation tool referenced here, has been superseded by 4D's later component and package management approaches
