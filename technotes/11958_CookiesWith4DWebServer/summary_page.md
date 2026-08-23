# Tech Note: Using Cookies with 4th Dimension Web Server

- **Asset ID:** 11958
- **Tech Note #:** 00-17
- **Published:** April 1, 2000
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Eric Saltzen
- **Page URL:** https://kb.4d.com/assetid=11958
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_16-20_(APR)/00-17_Cookies.hqx

## Overview

Eric Saltzen (4D, Inc. Technical Support) explains the HTTP cookie protocol and builds "CookieMonster4D," a complete sample database that recognizes returning visitors and issues session cookies entirely by hand-parsing raw HTTP headers with 4th Dimension's web server.

## Key Points

- Explains the raw HTTP mechanics of cookies: a server sends `Set-Cookie: name=value; expires=...; path=/`, and a matching future request from the same browser includes `Cookie: name=value` in its header; cookies are invisible via "View Source" because they live in the HTTP header, not the HTML payload, accessible in 4D via the $2 parameter (distinct from SET HTTP HEADER, which writes to the response header).
- CookieMonster4D's single `On Web Connection` database method branches on the requested path ($1) via a Case statement: recognized site pages (root, several `/4DCGI/*.htm` links) trigger cookie parsing and session logic, while a second Case branch (`$1 = "/4DCGI/@"`) intercepts inline image requests and serves them with `DOCUMENT TO BLOB` + `SEND HTML BLOB`.
- Because 4D had no built-in cookie parser, the custom `ParseCookies` project method manually locates `"Cookie: "` in the raw header text and walks it with `Position`/`Substring`, splitting on `=`, `;`, and carriage-return delimiters to build parallel name/value text arrays and return a cookie count.
- If no matching `[WebVisitors]` record is found for the `primaryID` cookie, a unique 32-bit ID is generated from `(Current date - !01/01/2000!) * 86400 + Current time`, appended with `Milliseconds % 100` for centisecond precision, re-rolled in a `Repeat...Until` loop on collision, then a new `[WebVisitors]` record is created and `SET HTTP HEADER("Set-Cookie: primaryID=...; expires=Sat, 31-Dec-2005...; path=/")` issues the cookie before serving `index.htm` (built with `<!--4DVAR-->` template placeholders) to collect the visitor's name.
- On a matching returning visit (or after the name-entry form posts to `/4DCGI/AssignName`), the existing `[WebVisitors]` record is updated, `SET HTTP HEADER("")` clears the header (no new cookie needed), and the personalized `home.shtm` page — built with Dreamweaver/Flash and `4DVAR`/`4DCGI` placeholders — is served via `SEND HTML FILE`.
- HTTP header carriage-return/line-feed pairs are converted to `<br>` with `Replace string` before being displayed back to the visitor on the confirmation page, illustrating how to safely surface raw header text in rendered HTML.

## Featured Technology

- SET HTTP HEADER for issuing Set-Cookie response headers
- On Web Connection database method routing (via $1 request path)
- Manual HTTP Cookie header parsing (ParseCookies project method)
- SEND HTML FILE / SEND HTML BLOB for serving pages and inline assets
- 4DVAR / 4DCGI templating with Dreamweaver-generated HTML
- Unique cookie/session ID generation from Current date/time/Milliseconds

## Historical Commentary

**Status:** Partially superseded

This note explains how HTTP cookies work and demonstrates building a session-management system, "CookieMonster4D," entirely by hand in 4D v6.x: parsing the raw Cookie header out of the HTTP request text with custom string-processing code, generating a unique visitor ID from the current date/time plus milliseconds, issuing a Set-Cookie response via SET HTTP HEADER, and looking up/creating [WebVisitors] records to recognize repeat visitors. SET HTTP HEADER remains part of 4D and the general concept of cookie-based session tracking is unchanged, but manually parsing cookie headers with Position/Substring string surgery, as shown here, has been superseded by 4D's built-in web server session and cookie-handling commands introduced in later versions, which remove the need to hand-roll a ParseCookies method.

**References to newer/updated information:**
- SET HTTP HEADER remains part of the current 4D language for setting response headers including Set-Cookie
- Later 4D versions added dedicated cookie/session-handling commands and built-in web server session support, reducing the need for the manual HTTP-header string parsing (ParseCookies) shown in this note
- Modern 4D web applications more commonly use the built-in web server's session management or REST/ORDA-based approaches rather than hand-built Cookie header parsing
