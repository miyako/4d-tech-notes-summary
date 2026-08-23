# Tech Note: The ButtonMaker Example Database

- **Asset ID:** 19047
- **Tech Note #:** 01-47
- **Published:** October 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=19047
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_46-49_(OCT)/01-47_ButtonMaker_Example.hqx

## Overview

Jonathan Baltazar (4D, Inc.) documents the ButtonMaker example database, originally created by Jeremy Sullivan of HD Industries, which uses 4D Chart's offscreen-drawing API to render custom, beveled HTML button graphics on the fly and stream them to the browser as GIFs based on user-submitted attributes -- a self-contained demonstration of server-side dynamic image generation entirely within 4D.

## Key Points

- The On Startup database method calls Gen4D_Startup, which maps Windows file types (JPEG/GIF) via MAP FILE TYPES and, on first run, pre-generates two reference GIFs -- stylechart.gif (text style samples) and colorchart.gif (the full 256-color CT palette) -- into the WebFolder using CGI4D_ButtonStyleChart/CGI4D_ButtonColorChart if they don't already exist.
- CGI4D_ButtonStart sends buttons.html with default parameter values (font Trebuchet_MS, bevel 2, color 8, size 18, text "Example", style 11, width 120, height 25); submitting the form re-sends the page with the user's chosen values via CGI4D_ButtonsSendButtonPage and Gen4D_ReturnWebVariables.
- The core CGI4D_ButtonMaker method parses '/'-delimited parameters out of the request URL with GEN4D_ParseParams, converts them to 4D Chart values (CT Font number, CT Index to color), and delegates the actual button-shape drawing to CGI4D_ButtonCreateButton.
- CGI4D_ButtonCreateButton draws a beveled 3D button using CT Draw rectangle for the outline and CT Array to polygon for four angled highlight/shadow strips (top, bottom, left, right) computed from lighter/darker RGB variants of the chosen button color, then an inset accent rectangle and fill rectangle for the button face.
- The finished offscreen area is converted with CT Area to picture, then PICTURE TO GIF and SEND HTML BLOB(...;".gif") stream the result straight back to the browser as an inline image, with no image file ever written to disk for a live request.
- CT ON ERROR/ON ERR CALL wire up Gen4D_WebErrorChart and Gen4D_WebError so 4D Chart drawing errors and general script errors are caught and reported via ALERT rather than crashing the web process.

## Featured Technology

- 4D Chart offscreen areas (CT New offscreen area / CT Area to picture)
- PICTURE TO GIF
- SEND HTML BLOB for dynamically-generated images
- 4DACTION URL parameters for passing button attributes
- GET WEB FORM VARIABLES
- CT Draw rectangle / CT Array to polygon for beveled button rendering

## Historical Commentary

**Status:** Obsolete

This note walks through the ButtonMaker example database (created by Jeremy Sullivan of HD Industries), which used 4D Chart's offscreen-drawing commands to render a beveled, colored, labeled button image on the fly and stream it back to the browser as a GIF via SEND HTML BLOB, with attributes passed through 4DACTION URL parameters. It's an inventive dot-com-era trick for server-side dynamic image generation entirely inside 4D, but 4D Chart was discontinued as a companion product years ago, so this exact approach can no longer be reproduced in current 4D. Modern equivalents (CSS/SVG buttons, client-side canvas rendering, or external image-generation services) have made server-generated GIF buttons obsolete as a web design technique.

References to newer/updated information:
- 4D Chart (the CT ... offscreen-area/drawing command set used throughout this note) was discontinued as a companion product in later 4D versions
- Dynamic button/graphic generation for the web is now handled client-side with CSS/SVG or by external image services rather than server-rendered GIFs
