# Tech Note 11-29: Integrating OpenSearch with 4D v12

**Author:** Sonya Rackwitz, Technical Services Team Member, 4D Inc.
**Published:** December 16, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76452
**Download:** https://kb.4d.com/DLTN/TN/2011/11-29_IntegratingOpenSearch.zip

## Proposition
This Tech Note explains how to integrate the OpenSearch standard with a 4D Web Server so end users can search a 4D database's data directly from their browser's built-in search box, using a Wikipedia-article sample database to demonstrate the full round trip.

## Key Points
- **OpenSearch background:** a collection of simple XML-based formats adopted by Chrome, Firefox, Internet Explorer, and Camino to let search engines integrate into the browser UI.
- **Description document anatomy:** covers the required ShortName, Description, Image, and URL elements of the OpenSearch XML description file.
- **Discoverability:** shows how to make the 4D-hosted search provider discoverable so a browser can add it as a search option.
- **Server-side implementation:** builds keyword indices, parses the incoming search string into keywords, and constructs a query using DISTINCT VALUES and related commands.
- **Result delivery:** demonstrates sending HTML result pages back to the browser in response to OpenSearch queries.
- **Sample database:** a Wikipedia-article dataset used to make the technique concrete and testable.

## Featured Technology
- OpenSearch description document (XML)
- 4D Web Server (built-in HTTP server)
- SQL/query-based keyword search against a Wikipedia sample database

## Context / Positioning
Published for 4D v12 in late 2011, this note showcased 4D's built-in Web Server as capable of participating in standard browser search integrations, appealing to developers who wanted their 4D-hosted content to feel like a first-class citizen of the contemporary web browsing experience.

## Historical Commentary
**Status:** Partially Superseded

OpenSearch itself is a standards-based browser-search-plugin protocol that never became core 4D API, so nothing here technically broke, but the underlying implementation relies on 4D's classic built-in Web Server and record-selection-based keyword indexing rather than any REST/ORDA data layer.

A modern equivalent would expose the same OpenSearch description document from a 4D REST/ORDA endpoint instead of hand-rolled HTML/XML page generation, and browser support for OpenSearch itself has waned industry-wide since 2011, independent of anything 4D did.
