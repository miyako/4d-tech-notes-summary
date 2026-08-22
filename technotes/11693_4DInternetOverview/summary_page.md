# Tech Note 96-11: 4D and The Internet, An Overview

**Author:** David Adams
**Published:** March 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11693
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_11-15_(MAR)/96-11_4D_and_the_Internet.exe

## Overview
Serving as the umbrella overview for a March 1996 series of 4D Internet-focused Tech Notes, this note surveys the ways 4D developers of the time could participate in the fast-growing Internet and World Wide Web, from adding interactivity to static sites through to building complete Internet servers entirely in 4D.

## Key Points
- **Adding interactivity:** pair an off-the-shelf server (e.g. WebSTAR) with 4D-driven custom features (search, data collection, image maps) via AppleEvent-based CGI bridges like **NetLink/4D** or **System 7 Pack**, avoiding slow AppleScript.
- **Managing/producing web pages:** use 4D's relational structures and language to automate site maintenance; ACI's own "Webster" database reportedly generated the entire ACI web site from data in about ten minutes.
- **Database publishing:** treat HTML generation as a form of structured export, from simple static pages to full dynamic search-driven delivery.
- **Internet client features:** integrate mail (POP3/SMTP), FTP, and web access into a 4D database using toolkits like **PDM Internet Tools**.
- **Running a full server in 4D:** build a Web, FTP, or mail server directly in 4D using low-level TCP/IP toolkits (**ITK**, **TCP ToolKit**) or complete third-party 4D-based server products (**NetWings**, **Web Server 4D**).
- **Serving 4D Server directly over the Internet:** 4D Server's native TCP/IP support allows direct Internet access; **4D Open for 4D** is recommended to reduce bandwidth for remote clients on slow connections.
- Includes a contact directory of contemporaneous third-party Internet toolkits/servers for 4D, a short recommended-reading list, and a glossary of CGI/HTML/HTTP/POP3/SMTP terms.

## Featured Technology
- CGI via AppleEvents (NetLink/4D, System 7 Pack)
- Third-party 4D Internet toolkits (ITK, PDM Internet Tools, TCP ToolKit)
- 4D-based Web servers (NetWings, Web Server 4D)
- 4D Server over TCP/IP; 4D Open for 4D
- WebSTAR / MacHTTP Macintosh web servers

## Historical Context
Published March 1996, at a time when the Web was five years old and growing exponentially, this note captures 4D's Internet strategy before it had any native web server or Internet Commands of its own — everything described relies on bridging 4D to external web servers via AppleEvents, or on third-party TCP/IP toolkits doing the heavy lifting, since 4D's own built-in web server and Internet Commands plugin were still roughly one to two years away.

## Historical Commentary
**Status:** Obsolete

Nearly every specific product and mechanism named in this note is now defunct: WebSTAR, MacHTTP, NetLink/4D, System 7 Pack, ITK, PDM Internet Tools, TCP ToolKit, NetWings, and Web Server 4D have all been discontinued, and the CGI-via-AppleEvents integration pattern was rendered unnecessary once 4D gained its own built-in web server and 4D Internet Commands plugin around 1997-1998. Modern 4D web development instead uses ORDA and REST APIs. That said, the note's core framing — that a relational database engine like 4D can be a powerful driver of dynamic, data-backed web content — remains a conceptually valid and enduring idea, even though every specific tool mentioned is gone.

