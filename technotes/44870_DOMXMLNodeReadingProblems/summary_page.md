# Tech Note 06-44: Avoiding Problems Reading DOM XML Nodes

**Author:** David Adams
**Published:** December 5, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44870
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_44-45_(DEC)/06-44_Testing_XML_Nodes.zip

## Overview
This foundational note explains why 4th Dimension's DOM XML navigation commands normally produce references to invalid, non-existent nodes when moving off the edges of a tree, and documents four escalating strategies to safely handle this without crashing when reading node names, values, or attributes.

## Key Points
- 4D 2004 has two XML command suites, DOM and SAX; this note covers only DOM.
- **Strategy 1 — Test the OK system variable:** DOM navigation commands set `OK` to 0 on reaching an invalid node, letting tree-walking code detect the boundary before reading node data.
- **Strategy 2 — Use optional name/value parameters:** navigation commands like `DOM Get first child XML element` accept optional out-parameters for name/value, avoiding the risk entirely for the common read case (though not for attributes or generic tree walks).
- **Strategy 3 — Install a custom `ON ERR CALL` handler:** necessary whenever code counts/reads attributes without first checking `OK`.
- **Strategy 4 — Write a general node-validation routine:** the note's `DOM_ReferenceIsValid` installs a temporary error handler, attempts to read the element name, and reports validity based on whether an error occurred or the name is empty.
- **Special case:** calling `DOM Count XML attributes` on the synthetic `#document` node (an artificial node above the true root holding version/encoding info) can cause some 4D versions to quit unexpectedly; the note's `DOM_CountAttributes` routine detects and special-cases this before calling the native function.
- Establishes the `DOM_ReferenceIsValid`/`DOM_StartCustomErrorHandling`/`DOM_StopCustomErrorHandling` routines reused across sibling XML tech notes in this series.

## Featured Technology
- 4th Dimension DOM XML commands
- `OK` system variable
- Custom `ON ERR CALL` error handling
- `DOM Count XML attributes` / `#document` node special-casing

## Historical Context
Published December 2006, shortly before 4D v11's native SQL engine arrived, this note is the technical foundation underlying the error-handling pattern reused throughout several other 2006–2007 XML Tech Notes (05-41, 06-43, 07-01 through 07-04).

## Historical Commentary
**Status:** Superseded

4D's classic DOM XML command set is legacy relative to the platform's later native JSON support, and the specific crash bug described (around `#document` and `DOM Count XML attributes`) is tied to specific old 4D versions. However, the defensive-programming principles taught here — validate before dereferencing, prefer safe optional-parameter APIs when available, and guard against undocumented edge cases — are durable software engineering practices that remain broadly applicable well beyond XML or even 4D itself.
