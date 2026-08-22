# Tech Note 06-39: Handling Web Logins

**Author:** David Adams
**Published:** October 17, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44441
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_38-39_(OCT)/06-39_Handling_Web_Logins.zip

## Overview
This note diagnoses and fixes a real usability gap in 4D 2004's built-in HTTP password support: when the browser's login dialog is cancelled, the visitor sees only a blank page rather than a helpful message, because 4D's On Web Authentication method always returns an empty HTTP 401 response with no content. The fix requires bypassing the automatic system and handling authentication manually.

## Key Points
- How HTTP Basic Auth really works: the *browser*, not the server, draws the login dialog; the server first sends a 401 status plus a `WWW-Authenticate` header and (optionally) error page content; if the dialog is cancelled, the browser shows whatever page content came with that original 401 response.
- 4D's On Web Authentication method always returns a bare 401 with no page body, so there's nothing to show when a login is cancelled — no code inside On Web Authentication can add page content to that specific response.
- Solution: accept all incoming requests provisionally inside On Web Authentication (return True unconditionally) and store the submitted user name/password, then perform the real authentication check — and, if needed, build a full custom 401 response with an HTML error page — inside On Web Connection and any method invoked via 4DACTION (since 4DACTION calls bypass On Web Connection).
- Two sample databases are provided: Web_Login_Default (illustrates the default blank-screen problem) and Web_Login_Custom (implements the full custom solution).
- Exact HTTP response headers (401 status, `WWW-Authenticate: Basic realm="..."`) are documented for reference.

## Featured Technology
- 4D Web Server hooks: On Web Authentication, On Web Connection, 4DACTION
- HTTP Basic Authentication (401 Unauthorized / WWW-Authenticate)
- Custom HTTP response construction in 4D

## Important Caveats Documented
- HTTP Basic Auth credentials are only base64-encoded, not encrypted — SSL/HTTPS is required for genuine security.
- Never enable the "Include 4D Passwords" web preference in a mixed Web/4D Client environment, since it would expose real 4D login credentials over the (typically unencrypted) web channel.
- Browsers cache and resend credentials for the life of the browser session, which complicates iterative testing (the note recommends quitting/restarting the browser or a Firefox extension to clear cached HTTP auth).
- Case-sensitivity of user name/password comparisons is left to the developer; a related Tech Note (05-41) on case-sensitive string operations is referenced.

## Historical Context
Published for 4D 2004, this note predates 4D's native SQL engine (v11, 2007), Project Mode (v17, 2018), and ORDA, and reflects 4D's original web server architecture built around On Web Authentication/On Web Connection method hooks and 4DACTION URLs — long before REST APIs, token-based auth, or the Qodly web stack existed in 4D.

## Historical Commentary
**Status:** Superseded

The HTTP Basic Authentication mechanics described (401 status codes, WWW-Authenticate headers, base64 encoding, the need for SSL) remain technically accurate today, but the specific 4D web server hooks used to work around the blank-screen limitation — On Web Authentication, On Web Connection, and 4DACTION — represent 4D's earliest web server architecture. Modern 4D web applications typically use session-based or token-based authentication schemes rather than raw HTTP Basic Auth workarounds, making this note's specific implementation approach dated even though its diagnosis of HTTP's mechanics is still correct.
