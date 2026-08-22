# Tech Note 05-41: Case-Sensitive Operations in 4th Dimension

**Author:** David Adams
**Published:** December 13, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=40931
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-41_Case_Sensitive_Ops.zip

## Overview
4th Dimension's language and database engine treat case (and diacritical) variants of a letter as equal by default. This note explains why that behavior becomes a problem in specific situations — especially XML, which mandates case-sensitive element/attribute names — and provides code for genuinely case-sensitive comparisons and searches.

## Key Points
- Situations needing case-sensitivity: strict name validation, matching paths on case-sensitive volumes, and comparing/validating XML element/attribute names.
- Sample code covers: case-sensitive alpha/text comparison, case-sensitive array comparison/search/count, exact BLOB comparison, and accelerated case-sensitive text search via an optimized QUERY BY FORMULA alternative or stored hashes (via the HashTools component).
- Introduces a "speed mode" parameter for pointer-based comparison routines, noting the time/speed trade-off only matters at larger data sizes.
- Recommends testing performance in compiled mode.
- Explicitly part of a related-notes cluster: TN 05-42 (efficient scanning), TN 05-43 (HashTools component), TN 05-44 (hash-optimized search).

## Featured Technology
- Case-sensitive string/array/BLOB comparison routines
- XML element/attribute name case-sensitivity
- Hash-optimized case-sensitive search (HashTools)

## Historical Context
This note reflects a mid-2000s inflection point where 4D developers were newly grappling with XML and SOAP-era web services, which exposed a real gap in 4D's case-insensitive engine. 4D has since added native case-sensitive comparison/search options directly to the language and query engine, reducing (though not eliminating) the need for the custom workaround routines documented here; the explanation of *why* case-sensitivity matters for XML remains accurate and useful background.
