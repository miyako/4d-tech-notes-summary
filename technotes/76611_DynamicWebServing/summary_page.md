# Tech Note 12-13: Dynamic Web Serving

**Author:** Darrell Draper, Technical Services Team Member, 4D Inc.
**Published:** June 29, 2012 | **Product/Version:** 4D v13.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76611
**Download:** https://kb.4d.com/DLTN/TN/2012/12-13_DynamicWebServing.zip

## Proposition
The second Tech Note in a multi-part 4D Web Server series, this document explains how to generate dynamic web content and receive submitted form data using 4D's built-in Web Server mechanisms.

## Key Points
- Covers three ways to build "semi-dynamic" pages: 4D Tags (HTML comments expanded server-side), 4DScript, and 4DAction, with pros/cons of each.
- Explains fully dynamic content generation via 4DCGI and the On Web Connection database method, including inspecting connection parameters.
- Provides a "Which Method to Choose" decision guide comparing the different content-generation techniques.
- Covers receiving Web content back from the browser: building input forms and validating submitted data before storage.
- Positioned as part two of a series, following a static-serving primer and preceding planned notes on session management and security.

## Featured Technology
- 4D Tags / 4DScript / 4DAction / 4DCGI
- On Web Connection database method and its parameters
- 4D built-in Web Server (v13)
- HTML input forms with server-side validation

## Best Practices Highlighted
1. Choose the lightest-weight content-generation method (4D Tags) when only minor dynamic substitutions are needed, reserving 4DCGI/On Web Connection for full dynamic page generation.
2. Validate all incoming Web form data before storing it in the database.
3. Structure Web Server logic incrementally, building from static to semi-dynamic to fully dynamic content as requirements grow.

## Context/Positioning
Published for 4D v13.1 in 2012, when 4D's built-in Web Server was actively promoted as a way to build database-driven websites without external server-side languages, this note filled out a planned documentation series addressing the full spectrum of static-to-dynamic web publishing.

## Historical Commentary
The classic content-generation mechanisms covered here (4D Tags, 4DScript, 4DAction, 4DCGI, On Web Connection) still exist and function in current 4D, but 4D's web strategy has moved decisively toward REST APIs built on ORDA and modern client-side JavaScript frameworks, or low-code tools like Qodly Studio, for new web and mobile development. Directly embedding 4D tags/CGI logic in server-generated HTML is now considered a legacy pattern rarely chosen for greenfield projects.

**Status:** Partially superseded
