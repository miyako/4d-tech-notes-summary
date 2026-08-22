# Tech Note 12-03: 4D v13 REST Tester

**Author:** Josh Fletcher, Technical Account Manager, 4D Inc.
**Published:** January 31, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76478
**Download:** https://kb.4d.com/DLTN/TN/2012/12-03_REST_Tester.zip

## Proposition
This Tech Note explains REST architecture principles and demonstrates a companion REST Tester tool, built on 4D v13's new HTTP Client commands, that lets developers construct, run, and review REST API test calls from within 4D.

## Key Points
- Explains REST's defining constraints: client-server, stateless, cacheable, layered system, optional code-on-demand, uniform interface — and contrasts REST with SOAP.
- Provides worked examples: a Google REST search, a Flickr echo test, and Wakanda's Entity Catalog/REST support.
- Introduces the 4D v13 REST Tester tool, built on the brand-new 4D v13 HTTP Client commands.
- Uses the DIALOG(...;*) technique and a Web area for displaying test responses, with method abstraction for maintainability.
- Documents tester features: test definition with custom headers, response viewing, test history, fill/auto-fill, search/filter, delete, and list box copy.
- Includes example tests and a full usage walkthrough (run a test, check results, review history).

## Featured Technology
- 4D v13 new HTTP Client commands
- REST API concepts (client-server, stateless, cacheable, uniform interface)
- DIALOG(...;*) modal dialog technique
- 4D Web area for rendering test responses
- Wakanda Entity Catalog / REST support (comparative example)

## Best Practices Highlighted
1. Abstract HTTP call logic into reusable methods rather than inlining request code per test.
2. Persist test definitions and history so developers can iterate and compare results over time.
3. Use a Web area to render raw HTTP responses for quick visual inspection during testing.

## Context/Positioning
Published right as 4D v13 introduced its first-class HTTP Client commands, this note both educated developers on REST fundamentals (a still-emerging pattern at the time) and gave them a practical tool to exercise the new client capability against real-world REST APIs, including 4D's sibling platform Wakanda.

## Historical Commentary
The REST concepts explained here remain fundamentally accurate, and 4D's HTTP Client commands are still part of the current classic language, but the note's context has become historically dated in two ways: Wakanda, prominently referenced as a REST-capable platform, was discontinued years later, and 4D's own web services strategy has since moved to native REST APIs built on ORDA rather than developers hand-rolling REST calls via the HTTP Client commands demonstrated here.

**Status:** Partially superseded
