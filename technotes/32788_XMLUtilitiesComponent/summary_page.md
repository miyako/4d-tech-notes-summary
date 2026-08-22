# Tech Note 04-21: The XML_Utilities Component

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** May 27, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32788
**Download:** https://kb.4d.com/ftp://@ftp.4d.com/ACI_TECHNICAL_NOTES/2004/Windows/TN_2004_21-25_(MAY)/04-21_XML_Utilities.exe

## Overview
This Tech Note describes the XML_Utilities component, built to add convenient helper functionality on top of 4th Dimension 2003's native XML commands for parsing, validating, navigating, and extracting values or attributes from XML documents. It lists four specific utility methods the component provides — xutil_CountOccurrences, xutil_ElementExists, xutil_GetValue, and xutil_StripWhitespace — designed to smooth over common, repetitive XML-handling tasks that would otherwise require more verbose native command sequences. Beyond its direct usefulness, the note emphasizes that the component's source code doubles as a worked example of how to use 4th Dimension 2003's native XML commands correctly, and is distributed both as a reviewable/modifiable source-code database and as an installable component via 4D Insider. The note first explains the component's basic modes of operation before documenting and demonstrating each individual function with examples. This reflects the mid-2000s emphasis on XML tooling within 4D and the broader component-based extensibility model (installable via 4D Insider) that was maturing at the time as an early step toward more modular, reusable code architecture. It targets developers already working with 4D's native XML commands who want higher-level convenience methods and example code to learn from.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- A description of the XML_Utilities component, which adds convenience utility methods (xutil_CountOccurrences, xutil_ElementExists, xutil_GetValue, xutil_StripWhitespace) on top of 4th Dimension 2003's native XML commands.

## Featured Technology
- XML_Utilities component
- 4th Dimension 2003 native XML commands
- 4D Insider component installation

## Historical Context
**Status:** superseded

This note documents a small community/vendor-style helper component that wrapped 4th Dimension 2003's native XML commands with convenience utilities and served as example code; 4D's native XML command set has since expanded considerably, and JSON has displaced much everyday structured-data handling that once relied on XML, reducing the practical need for this specific component. The general pattern of building small utility components on top of native commands and distributing them via a component-installation mechanism (the 4D Insider tool of that era, later superseded by 4D's evolving component architecture) remains a valid and still-used development practice.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
