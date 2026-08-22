# Tech Note: Serving Dynamic HTML Pages

## Overview
- **Technical Note 00-36**
- **Author:** Hugo Fournier, 4D, Inc. Technical Support
- **Published:** August 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note by Hugo Fournier demonstrates a simple, foundational method for publishing dynamic, data-driven HTML pages from a 4D database acting as an RDBMS-backed web server. The technique relies on 4D's non-contextual web publishing mode and specifically on triggering a 4D ACTION method directly from a URL, which then populates an HTML template stored in the database with live data before returning the assembled page to the browser using the SEND HTML BLOB command. The example database is built around a three-level hierarchical document structure — two levels of titles plus a body-text level — modeled through Templates, Chapters, and Paragraphs tables, with sample data drawn from extracts of the 4D Server documentation. Its stated technical scope covers defining a table structure that supports this hierarchical publishing scheme, invoking 4D ACTION from a URL, managing and populating an HTML template with data, and finally sending the resulting HTML via SEND HTML BLOB; the sample database defaults to redirecting links to the local 127.0.0.1 address but can be reconfigured with a real server IP for multi-machine testing. The featured technology is 4D's built-in web server combined with its non-contextual web publishing mode, representing the standard dynamic-web-publishing pattern available to 4D developers during the dot-com-boom era before REST/JSON-based web architectures existed.

## Featured Technology
- 4D ACTION in URL
- SEND HTML BLOB
- 4D non-contextual web mode

## Historical Context
This note demonstrates a foundational dynamic-web-publishing pattern for 4D's era: using 4D ACTION embedded in a URL to trigger a non-contextual web method that assembles an HTML template with data pulled from 4D fields, then returns it with SEND HTML BLOB. This template-and-BLOB style of dynamic HTML generation was the standard way to publish data-driven web pages from 4D at the time; today, equivalent needs are far more often served by 4D's REST/ORDA data server feeding modern JavaScript front ends, or by page-based web templating systems introduced in later 4D releases, making the specific technique here superseded even though the general concept of building HTML dynamically from data is timeless.

## What's Changed Since
- 4D's REST/ORDA data server and modern JavaScript front-end frameworks are now the more common way to serve data-driven web content from a 4D backend
- Later 4D releases introduced more structured, page-based web templating options beyond hand-assembling SEND HTML BLOB output from a 4D ACTION URL

