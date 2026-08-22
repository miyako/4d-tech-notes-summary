# Tech Note 96-13: Simplifying and Optimizing HTML Construction

**Author:** David Adams
**Published:** March 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11867
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_11-15_(MAR)/96-13_Simplifying_HTML.exe

## Overview
Written as 4D developers began using 4D to produce HTML for the World Wide Web — whether generating static pages, acting as a CGI processor, or serving as a Web server itself — this note proposes storing reusable HTML templates as data records rather than hardcoded string concatenation in 4D procedures, dramatically simplifying maintenance and improving performance.

## Key Points
- Naive HTML concatenation in 4D code is tedious, error-prone, requires recompilation to change output, and is difficult to test or localize.
- Solution: store HTML blocks as text in [HTMLBlocks] records containing placeholder tokens (e.g. `^Title`, `^Body`), edited/tested in an HTML editor and browser before pasting into 4D.
- `Replace string` swaps placeholders for dynamic values at runtime, faster than rebuilding the whole block, and replaces all instances of a token by default.
- A generalized `HTMLBlock` procedure uses numbered insertion targets and 4D's parameter indirection (`${n}` syntax with `Count parameters`) to accept any number of substitution values from sources like user input, other records, calculations, or CGI/HTTP request data.
- An `InitHTMLBlocks` startup routine preloads frequently used blocks marked `AutoLoad` into arrays for fast in-memory access, falling back to a database search otherwise.
- Blocks can be nested (e.g. embedding a "Page Stamp" sub-block inside a "Standard Page" block) to compose more complex pages.
- Centralizing HTML in records means global changes (e.g., adding a footer) require editing one record instead of many procedures — also easing localization.
- The technique is presented as general enough to apply to other structured markup languages (e.g. QuarkXPress tags, FrameMaker Interchange Format).

## Featured Technology
- HTML generation from 4D (CGI processing and early 4D-as-Web-server use cases)
- `Replace string` command
- Parameter indirection (`${n}`) for variadic procedures
- [HTMLBlocks] table-driven templating with array caching

## Historical Context
Published in March 1996, this note predates 4D's dedicated built-in Web Server and 4D Internet Commands plugin (which arrived roughly 1997-1998), reflecting an era when developers had to build their own web-serving/CGI plumbing on top of 4D's core procedural language. Procedures here would later be renamed Methods starting with 4D v6 (1997). The specific ${n} parameter-indirection and array-caching mechanics are tied to classic 4D syntax predating object notation and collections, but the underlying idea — separating template data from generation logic and substituting placeholders efficiently — is a templating pattern that persists conceptually in modern web development, even though today's 4D web/ORDA/REST approaches would implement it very differently.
