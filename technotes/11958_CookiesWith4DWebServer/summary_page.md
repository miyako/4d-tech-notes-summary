# Tech Note: Using Cookies with 4th Dimension Web Server (TN 00-17)

**Author:** Not specified in source document
**Published:** April 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11958
**Download:** https://kb.4d.com/DLTN/TN/2000/Windows/TN_2000_16-20_(APR)/00-17_4D_and_Cookies.exe

## Overview
This Tech Note covers a foundational explanation and sample database showing how to set and read HTTP cookies from 4D's built-in web server to maintain client-side state.

## Key Points
- It describes the classic mechanics of cookies: a server returning an HTTP response can include a name=value pair for the client to store, along with domain/path scoping information describing which future URLs should include that value when requesting from the server again, quoting the origin story that cookies are so named for "no compelling reason" according to Netscape.
- The note's proposition is to provide, via its accompanying sample database, a foundation for building an "intelligent" web site — one that can recognize returning visitors and maintain a more personalized, ongoing relationship with them rather than treating every request as anonymous and stateless.
- This sits within 4D's active investment in web/e-commerce capability during the 2000 dot-com boom, when the built-in 4D Web Server was a key differentiator for building dynamic, database-backed web sites entirely inside 4D without external CGI languages.
- The featured technology is squarely the 4th Dimension Web Server's cookie-setting and cookie-reading commands, paired with general HTTP protocol concepts (state objects, domain/path scoping, and request/response headers) that any web developer of the era needed to understand.
- Because the download links are no longer functional and only the teaser paragraph survives in this archive, the exact 4D commands and sample database mechanics used to implement the cookie logic are not preserved here.
- Nonetheless, the note captures an important early-web-era 4D capability: giving a 4D database direct, first-class control over HTTP session state without relying on external web/application server middleware, a notable feature for its time even as the specific implementation has since been superseded by 4D's much more capable modern web server.

## Featured Technology
- 4th Dimension Web Server
- HTTP cookies
- CGI-style server-side state
- Web session management

## Historical Context
This note introduces HTTP cookie handling via 4th Dimension's own built-in web server, letting a 4D-powered web application store and retrieve client-side state — a core building block for personalization and session tracking during 4D's active push into web/e-commerce features around the dot-com era. The specific mechanics of 4D's classic web server and its cookie API are long since superseded by 4D's modern web server (built on newer HTTP handling and standard REST/session mechanisms), but the underlying concept of using cookies for client-side session state remains a standard, still-relevant web development technique used across any web platform, including current 4D web apps. Related updates since: 4D's built-in web server has been substantially modernized multiple times since 2000, including current REST/session and HTTPS support far beyond the classic CGI-era cookie API described here; Cookie-based client state remains a standard web technique conceptually, but is now typically combined with modern session tokens, REST APIs, and HTTPS rather than the classic 4D web server mechanics of this note. The full Tech Note PDF/text could not be recovered for this archive entry because the linked archive was an old Windows self-extracting .exe installer that could not be extracted without a Windows environment; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
