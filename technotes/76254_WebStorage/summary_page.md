# Tech Note 11-02: Web Storage

**Author:** Rudolf Psenicnik, Technical Services Team Member, 4D Inc.
**Published:** February 4, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76254
**Download:** https://kb.4d.com/DLTN/TN/2011/11-02_Web_Storage.zip

## Proposition
This note surveys the state of offline browser storage circa 2011 and introduces the HTML5 Web Storage API as the modern, cross-browser-compatible replacement for older, inconsistent offline-storage hacks. It explains the API's structure for storing key/value data pairs, walks through a local storage example with working code, and shows how to view currently stored offline data using each major browser's developer tools (Chrome, Safari, Firefox). A sample application demonstrates using 4D replication over HTTP to populate web storage with data pulled from a 4D database, along with the initialization and data access code needed to wire it together. The note is aimed at 4D web developers who need offline-capable web front-ends.

## Key Points
- Surveys the past, present, and future (as of 2011) of offline browser data storage approaches.
- Introduces the HTML5 Web Storage API and its key/value structured-data model.
- Provides a working local storage example with accompanying sample code.
- Shows how to inspect currently stored offline data in Chrome, Safari, and Firefox developer tools.
- Demonstrates using 4D replication via HTTP to feed data from a 4D database into browser web storage.
- Covers initialization and data-access code for a small web storage-backed demo app.

## Featured Technology
- HTML5 Web Storage API (localStorage)
- 4D replication via HTTP feeding browser-side offline storage
- Cross-browser inspection of stored data (Chrome, Safari, Firefox)

## Best Practices Highlighted
- Prefer the standardized HTML5 Web Storage API over legacy/proprietary offline-storage hacks for cross-browser consistency
- Use browser developer tools to verify stored offline data during development

## Context / Positioning
Published in 2011 just as HTML5 Web Storage was becoming broadly supported across major browsers, this note helped 4D web developers adopt the new standard for building offline-capable web front-ends backed by 4D data.

## Historical Commentary
**Status:** Still Relevant

The HTML5 Web Storage API (localStorage/sessionStorage) described here is a web standard that is still fully supported by all modern browsers and remains a valid, current technique for client-side offline data persistence, independent of any 4D-specific product changes. The 4D-side replication-over-HTTP mechanism used to populate it, however, is dated compared to 4D's modern REST/ORDA-based data access, which would be the more idiomatic way to feed browser-side storage today.
