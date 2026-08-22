# Tech Note 06-40: Enhanced DOM Functions

**Author:** David Adams
**Published:** November 3, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44608
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_40-43_(NOV)/06-40_Enhanced_DOM.zip

## Overview
This note packages a library of "DOM_" prefixed wrapper functions built on top of 4D 2004's native DOM XML commands, aiming to make XML tree navigation and reading safer and more convenient. It addresses three recurring problems: crashes/errors from invalid node references, missing whitespace trimming, and awkward attribute access — bundling fixes for all three into one sample database.

## Key Points
- DOM tree navigation commands (`DOM Get Parent XML element`, `DOM Get first child XML element`) rely on the `OK` system variable to signal reaching a non-existent node, which easily produces invalid node references.
- Calling native read commands (e.g., `DOM GET XML ELEMENT NAME`) on an invalid reference triggers a disruptive error dialog; the wrapper library suppresses this automatically and adds `DOM_ReferenceIsValid` for explicit checks.
- `DOM_GetElementValue` integrates optional whitespace cleaning (leveraging the `XML_CleanWhitespace` routine documented in a companion note, TN 06-42).
- `DOM Count XML attributes` is documented to crash certain 4D versions when called on the special `#document` node; `DOM_CountAttributes` provides a safe replacement.
- `DOM_AttributesToArrays` copies a node's attributes into paired name/value text arrays for convenience.
- Additional routines include `DOM_CountElementByName`, `DOM_ElementExists`, `DOM_FindElementByName`, `DOM_GetElementName`, and `String_EqualCaseSensitively` (for case-sensitive XML element name comparisons).
- Each routine's exact 4D signature and behavior is documented in a "Method Documentation" reference section; a demo screen in the sample database illustrates each feature.

## Featured Technology
- 4D DOM XML commands
- Custom 4D error-handler wrapping (`ON ERR CALL`-style pattern)
- XML whitespace trimming (XML_CleanWhitespace, from TN 06-42)

## Historical Context
Written for 4D 2004, this note predates 4D's own SQL engine (v11, 2007), Project Mode (v17, 2018), and ORDA. It's a "library of safety wrappers" style Tech Note, a common genre from this era when the native command set had rough edges that individual developers had to work around themselves before 4D addressed them upstream.

## Historical Commentary
**Status:** Obsolete

The specific bugs referenced (such as the #document attribute-count crash) have most likely been fixed in 4D long ago, and the DOM/SAX XML command family, while still present in modern 4D, is used far less today given the prevalence of JSON for data interchange. The broader pattern demonstrated — wrapping a fragile or incomplete native API in a small, well-documented, safer helper library — remains a sound and still-applicable software engineering practice, even though the specific commands are dated.
