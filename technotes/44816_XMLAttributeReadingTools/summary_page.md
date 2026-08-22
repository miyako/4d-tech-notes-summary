# Tech Note 06-43: Enhanced Tools for Reading XML Attributes

**Author:** David Adams
**Published:** November 29, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44816
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_40-43_(NOV)/06-43_Reading_XML_Attr.zip

## Overview
This note packages a richer, safer utility layer around 4D's three native DOM XML attribute commands (count, get-by-index, get-by-name), addressing crash risks and adding convenience features for matching and extracting attribute data.

## Key Points
- **DOM_AttributesToArrays** — copies an XML node's attribute names and values into a pair of text arrays.
- **DOM_CountAttributes** — a safer wrapper around `DOM Count XML attributes` that avoids the crash caused by counting attributes on the synthetic `#document` node and handles invalid references gracefully.
- **DOM_GetAttributeNameWithValue** / **DOM_GetAttributeValueWithName** — look up an attribute in either direction (by value → name, or by name → value), case-insensitive by default for values.
- **DOM_HasAttributeNamed**, **DOM_HasAttributeNameAndValue**, **DOM_HasAttributeWithValue** — boolean existence tests; attribute names are always compared case-sensitively (as required by the XML spec), values are case-insensitive by default.
- Shared internal helpers **DOM_ReferenceIsValid**, **DOM_ReferenceIsValidOnError**, **DOM_StartCustomErrorHandling**, **DOM_StopCustomErrorHandling** install/restore a custom `ON ERR CALL` handler around risky DOM calls.
- Includes a **String_EqualCaseSensitively** utility for the case-sensitive name comparisons XML requires.
- Explicitly documents and works around the same `#document`-node attribute-count crash risk detailed in the companion note "Avoiding Problems Reading DOM XML Nodes."

## Featured Technology
- 4th Dimension DOM XML commands (`DOM Count XML attributes`, `DOM GET XML ATTRIBUTE BY INDEX`, `DOM GET XML ATTRIBUTE BY NAME`)
- Custom `ON ERR CALL` error handling
- `DOM_AttributesToArrays` and related `DOM_*` attribute utility routines

## Historical Context
Published November 29, 2006, this note is a direct companion to the slightly later Tech Note 06-44 ("Avoiding Problems Reading DOM XML Nodes"), reusing and extending the same error-trapping foundation, all predating 4D v11's native SQL engine.

## Historical Commentary
**Status:** Superseded

The specific native DOM XML attribute commands wrapped here are legacy relative to 4D's later native JSON support, and the particular crash bugs worked around are tied to old, specific 4D versions. Nonetheless, the note's overall approach — building a safer, more convenient utility library on top of a fragile, low-level native API — is a durable and still-common software design pattern, independent of the specific technology involved.
