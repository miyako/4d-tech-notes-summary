# Tech Note: 4D Business Kit Goes Flash (Part II)

- **Asset ID:** 25589
- **Tech Note #:** 02-48
- **Published:** October 31, 2002
- **Product / Version:** 4D Business Kit 1.x
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=25589
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_46-50_(OCT)/02-48_4DBK_Goes_Flash_Pt%20II.hqx

## Overview

Jamras Komoncharoensiri continues the '4D Business Kit Goes Flash' series with practical design gotchas for building a Flash front-end against 4D Business Kit's URL-tag-based backend. He explains that since 4DBK only understands requests encoded entirely in a URL (not POST/GET body variables), each request is capped at 255 characters, requiring large submissions (like new-account signup) to be split into several smaller sequential requests. He covers ActionScript-level character encoding of spaces to plus signs (both directions), browser/Flash .swf caching problems and their workaround via a Random()-generated cache-busting URL parameter (since the 4DBKNoCache tag doesn't work inside an embedded Flash movie's private ActionScript), a periodic-polling technique to auto-refresh an in-movie shopping cart display after changes made in a companion floating HTML window, and finally explains why only cookie-based session IDs -- not 4DBK's URL-embedded session-ID alternative -- can be used to maintain session state with an embedded Flash movie.

## Key Points

- Explains the 255-character URL request limit: since 4DBK only recognizes complete instructions embedded in a URL (ignoring POST/GET body variables), a multi-field new-account submission is split into several separate `4daction/4DBKExecute/4DBKStoreSet/...;4DBKFieldSet/...;4DBKGo/result.html` requests sent one after another.
- Documents Flash's space-character handling: spaces must be encoded as `+` before sending data to 4DBK (and vice versa), shown with an ActionScript loop that walks a string character-by-character replacing spaces with `+` using `Substring`/`Ord`/string concatenation.
- Addresses .swf caching at two levels: runtime data caching (worked around by appending a `Random()`-generated numeric value to each `Load Variables` URL) and design-time movie caching (requiring manual cache clearing during development so the browser doesn't load a stale .swf).
- Notes that 4DBK's built-in `4DBKNoCache` tag (which returns a random `NC#####` code) only works when embedded directly in server-processed HTML, not inside a Flash movie's private ActionScript, so the same `Random()` technique must be reimplemented in ActionScript instead.
- Shows an automatic shopping-cart refresh pattern: after a user edits their order in a floating HTML window, the Flash movie plays a ~1-second, 16-frame loop that re-issues a `Load Variables` request each cycle to pull the latest order data.
- Explains that 4DBK offers two session-ID mechanisms (a `4DBK` browser cookie, or a session ID embedded directly into page URLs), but only the cookie mechanism works with an embedded Flash movie, since 4DBK cannot pre-process or rewrite URLs constructed internally by the movie's own ActionScript.

## Featured Technology

- Macromedia Flash ActionScript (Load Variables, Set Variable)
- 4D Business Kit URL action tags (4DBKExecute, 4DBKStoreSet, 4DBKFieldSet, 4DBKGo)
- 4DBKNoCache cache-busting tag
- 255-character URL request-length limit workaround
- Space-to-plus character encoding for Flash
- Cookie-based session persistence (4DBK cookie)

## Historical Commentary

**Status:** obsolete

Jamras Komoncharoensiri (4D, Inc. Technical Support) continues a two-part series on building Macromedia Flash front-ends for 4D Business Kit's e-commerce engine, covering practical gotchas: 4DBK's hard 255-character URL request limit (worked around by splitting a large account-creation request into several smaller ones), Flash's space/plus character encoding quirks, Flash and browser .swf caching problems (worked around with a Random()-generated cache-busting URL parameter, since the 4DBKNoCache tag can't be used inside embedded Flash movies), periodic polling to auto-refresh an in-movie shopping cart, and the fact that only cookie-based session IDs (not URL-embedded session IDs) work with an embedded Flash movie. Both Macromedia Flash and 4D Business Kit are long discontinued -- Flash was officially retired by Adobe at the end of 2020 and is unsupported by all modern browsers -- so this note's entire technical premise is obsolete, and it stands today purely as a historical record of early-2000s rich-client web development practices.

References to newer/updated information:
- Adobe officially discontinued Flash Player at the end of 2020, and no modern browser supports Flash content
- 4D Business Kit has also been discontinued for many years, so the 4DBKExecute/4DBKStoreSet/4DBKFieldSet/4DBKGo tag-based integration described here no longer applies to current 4D e-commerce development
