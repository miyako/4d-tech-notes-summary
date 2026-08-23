# Tech Note: Connected Multimedia Apps with 4D and Flash

- **Asset ID:** 31597
- **Tech Note #:** 04-09
- **Published:** March 4, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Omid Tavallai, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=31597
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_05-09_(FEB)/04-09_Connected_Multimedia.hqx

## Overview

Omid Tavallai demonstrates pairing a 4th Dimension 2003 database with a Macromedia Flash MX Professional 2004 front-end via 4D's SOAP Web Services, using a simple demo built for the 2003 4D Summit Conference: a `Sessions` table of conference presentation names is randomly displayed against an animated Flash backdrop, with the data pulled live from 4D each time the Flash movie loops.

## Key Points

- The 4D database contains one table, `Sessions`, with a `Name` field (HTML-formatted); a method `getSessionName` uses `ALL RECORDS`, `Random%`, and `GOTO SELECTED RECORD` to return a random session name as SOAP output (`SOAP DECLARATION($0;Is Text;SOAP Output;"session_name")`).
- The method is exposed as a Web Service by checking "Offered as a Web Service" and "Published in WSDL" in Method Properties, and the WSDL is published from 4D's built-in web server after setting the Web Publishing TCP port to 8080 (reachable at `http://127.0.0.1:8080/4dwsdl`).
- On the Flash side, a `WebServiceConnector` component (Data Components palette) points at the WSDL URL and the `getSessionName` operation, binding its "result" output as HTML text to a Label component (Result), which requires the 4D `Name` field to already contain HTML markup since the Label offers no separate formatting.
- Because Flash only invokes a Web Service connector once by default, the only ActionScript needed is a single trigger call — `this.FlashDemo.trigger();` — placed in the first timeline frame, so each loop of the movie (which loops automatically by default) re-fetches a new session name.
- The finished Flash file can be published as a Macintosh or Windows standalone executable, or as a browser-playable .SWF, all from the same Publish Settings dialog, provided the 4D database is running in the background.
- The note frames this as a low-code way to build a rich, custom Flash client (or prototype/demo) over an existing 4D backend, useful for client/management demos or vertical-market interfaces.

## Featured Technology

- 4D 2003 SOAP Web Services (method published as Web Service/WSDL)
- Macromedia Flash MX Professional 2004 WebServiceConnector component
- 4D built-in Web server (WSDL publishing on port 8080)
- ActionScript trigger() call for looped data refresh
- Flash Label component with HTML text binding
- Cross-platform standalone Flash app / .SWF publishing

## Historical Commentary

**Status:** Obsolete

This note demonstrates pairing a 4th Dimension 2003 SOAP Web Service backend with a Macromedia Flash MX Professional 2004 front-end via Flash's WebServiceConnector component, using a simple 'getSessionName' method published from a demo shown at the 2003 4D Summit Conference. The technique was clever for its era but is now entirely obsolete: Adobe discontinued Flash Player at the end of 2020 and no modern browser or OS supports SWF content, so the Flash client half of this demo cannot run at all today. The 4D side (publishing a method as a SOAP Web Service) is also dated, since 4D has since moved toward REST/JSON-based web services for this kind of client integration.

References to newer/updated information:
- Adobe officially discontinued Flash Player at the end of 2020, and no current browser or OS can run the Flash/.SWF client described in this note
- 4D's SOAP-based Web Services approach used here has been superseded by REST/JSON web services in modern 4D development
- Rich client/backend integration patterns similar in spirit are now built with modern web or mobile frameworks calling 4D's REST APIs, rather than Flash and SOAP
