# Tech Note 07-04: Testing if an XML Node Has Relatives

**Author:** David Adams
**Published:** January 30, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45338
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_01-04_(JAN)/07-04_XML_Node_Relatives.zip

## Overview
This note fills a gap in 4th Dimension's native DOM XML commands by providing routines to test whether an XML node has ancestors, children, or siblings — information often needed for tree-walking algorithms, hierarchical display formatting, or custom XML import logic.

## Key Points
- **DOM_NodeHasChildren:** returns True if `DOM Get first child XML element` succeeds and yields a valid reference.
- **DOM_NodeHasAncestors:** returns True if a valid parent exists, but explicitly excludes the synthetic `#document` node (an artificial node above the true root holding version/encoding info) from counting as an ancestor.
- **DOM_NodeHasSiblings:** checks both previous and next sibling directions before concluding a node has no siblings.
- All three depend on a shared `DOM_ReferenceIsValid` helper (carried over from Tech Note 06-40) and `DOM_StartCustomErrorHandling`/`DOM_StopCustomErrorHandling` routines that install a temporary `ON ERR CALL` handler so invalid-reference errors are trapped rather than crashing the routine.
- Sample database includes a `Test_NodeHasRelatives` test harness exercising good nodes, bad nodes, and the `#document` node with pass/fail alerts.

## Featured Technology
- 4th Dimension DOM XML commands
- `DOM Get first/parent/previous sibling/next sibling XML element`
- Custom `ON ERR CALL` error trapping pattern

## Historical Context
Published January 2007, shortly before 4D v11 introduced native SQL, this note is part of a run of small, focused DOM XML utility notes from this era, building directly on the error-handling pattern established in earlier notes like 06-40.

## Historical Commentary
**Status:** Superseded

The specific DOM XML commands are 4D's classic, pre-JSON/pre-ORDA XML API and are much less central to modern 4D development, which now has native JSON support and more contemporary data-access patterns. The defensive-programming technique demonstrated — wrapping error-prone low-level API calls with a custom error handler to safely probe conditions — remains a broadly useful and still-applicable coding pattern regardless of the specific API involved.
