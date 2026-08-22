# Tech Note: Creating Referer Logs with 4D Web Server

## Overview
- **Technical Note 00-57**
- **Author:** Unknown / not specified
- **Published:** December 1, 2000
- **Product/Version:** 4D v6.7
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note offers a lightweight, ready-to-use technique for collecting Referer information — the HTTP header indicating which page referred a visitor to the current page — from a web site served by 4th Dimension v6.7's built-in web server. The proposition centers on placing a special tag, 4DSCRIPT/RefererGrabber, directly inside the HTML of any page whose incoming traffic source should be logged. For this tag to be processed, the note explains, the page's file name must use the '.shtml' extension, signaling to 4D's web server that the page contains server-side include elements (4D HTML tags) requiring server-side processing before being sent to the browser. A complete example database accompanies the note so developers can see the referer-logging mechanism working end to end without having to build it from scratch. The featured technology is 4D's built-in web server and its server-side-include-style HTML tag processing, an approach that reflects how site owners tracked visitor traffic sources in the years before third-party web analytics services became the default solution. Because only the teaser abstract for this note survives (the original download was an old Windows self-extracting installer that could not be extracted here), the underlying example code for the RefererGrabber mechanism could not be recovered.

## Featured Technology
- 4D Web Server
- 4DSCRIPT/RefererGrabber
- Server-side includes (.shtml)

## Historical Context
This note shows how to capture HTTP Referer information using a 4DSCRIPT tag embedded in server-side-include-enabled .shtml pages served by 4D's built-in web server, a common web-analytics need in the dot-com-boom era before dedicated web analytics platforms were widespread. The general need to track referer/traffic-source data remains relevant today, but it is now almost universally handled by external analytics services (Google Analytics and similar) or by modern web server/application log analysis rather than a bespoke 4D server-side-include tag, making this specific mechanism superseded.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- Referer/traffic-source tracking today is typically handled by external web analytics platforms rather than custom 4D server-side-include tags
- 4D's web server and server-side scripting model have evolved considerably since this v6.7-era .shtml/4DSCRIPT mechanism

