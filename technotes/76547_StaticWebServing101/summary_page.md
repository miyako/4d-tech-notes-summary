# Tech Note 12-07: Static Web Serving 101

**Author:** Darrell Draper, Technical Services Team Member, 4D Inc.
**Published:** March 28, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76547
**Download:** https://kb.4d.com/DLTN/TN/2012/12-07_StaticWebServer101.zip

## Proposition
This introductory Tech Note teaches the fundamentals of serving static HTML content with the 4D built-in Web Server, covering Web Root configuration, URL structure, enabling the server, and basic caching/compression, as part one of a planned multi-part series.

## Key Points
- Defines Web Content broadly and explains the Web Root folder plus how the default home page is determined.
- Covers URL anatomy in depth: absolute vs. relative URLs and the distinction between URIs and URLs.
- Walks through enabling the 4D Web Server and building a basic "Hello World" static page.
- Explains Web caching from both server-side and browser-side perspectives.
- Discusses HTTP compression and its bandwidth benefits.
- Explicitly sets up later notes in the series covering dynamic content, session management, and security.

## Featured Technology
- 4D built-in Web Server
- Web Root and default home page configuration
- HTTP URL structure (absolute/relative, URI vs URL)
- Web server and browser caching
- HTTP compression

## Best Practices Highlighted
1. Understand the difference between absolute and relative URLs to avoid broken links when deploying.
2. Configure server-side caching appropriately to balance freshness and performance for static assets.
3. Enable compression to reduce bandwidth for served static content.

## Context/Positioning
Published as the opening installment of a planned 4D Web Server series in 2012, this note established the fundamentals developers needed before tackling the more advanced dynamic web-serving topics 4D promised to cover next.

## Historical Commentary
The foundational web concepts here — URL structure, caching, compression, and how the 4D Web Server serves static files from Web Root — remain accurate and directly applicable today, as HTTP fundamentals are timeless and 4D's static file serving has not fundamentally changed. The broader context has shifted, however: modern web architectures often offload pure static content to CDNs, and within 4D applications static assets are now typically served alongside REST/ORDA-backed dynamic APIs rather than 4D's Web Server being the sole delivery mechanism.

**Status:** Current
