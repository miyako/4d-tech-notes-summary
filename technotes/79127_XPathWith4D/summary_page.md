# Tech Note 23-03: Hands-on practice with XPath with 4D

**Author:** Olivier Marolleau & Anouar Moustarih, Technical Services Engineer, 4D SAS & 4D Morocco.
**Published:** February 23, 2023 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79127
**Download:** https://kb.4d.com/DLTN/TN/2023/23-03_XPathWith4D.zip

## Proposition
XPath has been available in 4D since v11 but was long incomplete and underused, even though it can drastically shorten code for navigating and extracting data from XML documents. With a stabilized "standard XPath" implementation since v18R3, this note demonstrates practical, real-world XPath usage via 4D's DOM commands.

## Key Points
- **Two incompatible implementations:** the legacy "XPath 4D" (implicit relative root, e.g. `"root/test2"`) vs. the standard XPath since v18R3 (explicit root required, e.g. `"/root/test2"`); mixing them silently fails to find matches.
- **Seven XML node types:** element, attribute, text, namespace, processing instruction, comment, and root — each located and returned as a UUID-like reference by DOM commands.
- **Root and atomic values:** the root comes from `DOM Parse XML source/variable` or `DOM Read root/parent XML element`; atomic (childless/parentless) values come from `DOM READ XML ELEMENT VALUE`/`DOM READ XML ATTRIBUTE BY NAME`.
- **Node relationships without XPath are verbose:** children need `DOM Read first child XML element`, siblings need `DOM Read previous/next sibling XML element`, and descendants require nested manual traversal loops.
- **XPath collapses traversal:** a single `DOM Find XML element($root; "/bookstore//book")` call retrieves all matching descendant nodes that would otherwise need a hand-written recursive loop.
- **XPath syntax essentials:** node selection paths, `[...]` predicates for conditional matching, wildcards for unknown nodes, axes for relative navigation, and operators; 4D XPath queries always return a node-set on a match.
- **Real-world example 1:** reading a database's publication name from `settings.4DSettings` via an attribute XPath expression (`/preferences/com.4d/server/network/options/@publication_name`).
- **Real-world example 2:** using `EXPORT STRUCTURE` plus `DOM Find XML element($root; "/base/table")` and `DOM Get next sibling XML element` to extract the id/uuid/name of every table in the live structure.

## Featured Technology
- **XPath (standard, v18R3+)** — the modern, W3C-compliant query language 4D supports via DOM for navigating XML trees.
- **DOM Find XML element** — the core command accepting an XPath expression to locate one or more nodes.
- **DOM Parse XML source / DOM Parse XML variable** — entry points that load an XML file or in-memory XML string into the DOM for querying.
- **EXPORT STRUCTURE** — exports a 4D database's live schema as XML, used here as a practical XPath target.

## Best Practices Highlighted
1. Be explicit about which XPath implementation (legacy "XPath 4D" vs. standard XPath) the code targets, since expressions are not interchangeable between them.
2. Prefer XPath expressions with `DOM Find XML element` over manual recursive child/sibling traversal when extracting nested or repeated XML nodes.
3. Use attribute-targeting XPath expressions (`@attributeName`) to fetch specific settings/metadata values directly instead of parsing whole elements.

## Context / Positioning
Published as 4D's XML/DOM tooling matured through the standard XPath implementation introduced in v18R3, this note reflects 4D's ongoing investment in structured-data interoperability (XML alongside JSON/REST), giving developers a more standards-aligned and less error-prone way to introspect 4D's own XML-based settings and structure files as well as third-party XML data.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
