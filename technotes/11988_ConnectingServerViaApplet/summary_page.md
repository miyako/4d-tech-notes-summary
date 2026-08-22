# Tech Note: Connecting to a 4D Server Using an Applet

## Overview
- **Technical Note 00-48**
- **Author:** Unknown / not specified
- **Published:** October 1, 2000
- **Product/Version:** 4D Server v6.7
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note focuses narrowly on the connection experience for a 4D Open for Java client, rather than on teaching how to build a full Java application against 4D Open. Its proposition is that launching the client as a Java applet (started via Sun's policytool utility) is more convenient for end-users than connecting via a web browser or a DOS/command prompt, because it spares the user from manually typing the 4D Server's IP address every time, and because policytool-based launches start noticeably faster than waiting ten seconds or more for an interface to load through other connection routes. The note frames this purely as a usability/deployment improvement layered on top of the existing 4D Open for Java API rather than a new capability, and it is explicitly scoped to the client connection step rather than data access patterns. The featured technology is the 4D Open for Java client API combined with the Java Runtime Environment's applet and policy-tool infrastructure of that era. Because only the teaser abstract for this note survives (the original download was an old Windows self-extracting installer that could not be extracted here), the specific applet code and policytool configuration steps could not be recovered.

## Featured Technology
- 4D Open for Java
- Java applets
- policytool (Java security policy)

## Historical Context
This note shows how to use a Java applet, launched via Sun's policytool for faster local security-policy handling, as a convenient front end for connecting a 4D Open for Java client to a 4D Server without retyping the server's IP address each time. Java applets have been essentially dead technology since major browsers removed NPAPI/plugin support in the mid-to-late 2010s, and 4D Open itself has been discontinued, so both the specific mechanism and the underlying API this note relies on are entirely obsolete today; developers now reach 4D Server from external code via modern web/REST-based approaches instead.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- Java applets are effectively extinct; all major web browsers removed the NPAPI plugin support required to run them years ago
- 4D Open (the C/Java client API this note depends on) has been discontinued; modern integrations with 4D Server use 4D's REST/ORDA data server instead

