# Tech Note: Connecting to a 4D Server Using an Applet

- **Asset ID:** 11988
- **Tech Note #:** 00-48
- **Published:** October 1, 2000
- **Product / Version:** 4D Server 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar
- **Page URL:** https://kb.4d.com/assetid=11988
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_46-50_(OCT)/00-48_Connecting_Via_Applet.hqx

## Overview

Jonathan Baltazar (4D, Inc. Technical Support) explains how to connect a 4D Open for Java client interface to a 4D Server using a Java applet, and how to configure Java's security policy with Sun's policytool so the applet can connect across machines rather than only to its originating host.

## Key Points

- 4D Open for Java is a Java API/library that lets a standalone or applet-based Java program connect to a 4D Server; the note focuses specifically on the applet-based connection path (as opposed to a 4D client or web browser connection).
- Installation requires placing the database and all Java source/class/HTML files together in one folder (e.g. `Main:Athletes:Aci:` on Mac, `C:\...` on Windows) so the "Aci" folder containing 4D Open classes sits next to the `.java` file — omitting this causes 4D Open command-not-recognized compile errors.
- The applet is launched via `appletviewer filename.html` on Windows or by dragging the `.html` file onto Appletrunner on Macintosh; connecting works fine to `127.0.0.1` (same machine) but fails cross-machine because Java's SecurityManager, by default, only permits an applet to reconnect to the host that served its `.class` file.
- The fix (for testing) is Sun's `policytool` utility: create a `.java.policy` file in the user's home directory, use "Add Policy Entry" → "Add Permission" → select `AllPermission` from the Permissions dropdown, then save; this grants `CodeBase <ALL>` the `java.security.AllPermission` needed to bypass the restriction.
- If a differently named or located policy file is desired, the `java.security` file's `policy.url.N=` entries must be edited to add a path to it (e.g. `policy.url3=file:/test/4D.policy`).
- Macintosh applets do not require the policytool step at all — only Windows-hosted applets need it, per the note.
- Once configured, clicking Connect in the applet succeeds ("Successful Connection") and the interface can display records; the benefit over a browser-based or DOS-prompt connection is not re-typing the server's IP address each time.

## Featured Technology

- 4D Open for Java
- Java applets and the appletviewer/Appletrunner
- Java SecurityManager applet sandboxing
- Sun policytool for granting java.security.AllPermission
- .java.policy / java.security policy files
- Java class placement alongside a 4D Server database (Aci folder)

## Historical Commentary

**Status:** Obsolete

This note shows how to connect a Java applet client to a 4D Server across machines using 4D Open for Java, working around the JVM SecurityManager's default restriction that an applet can only reconnect to its originating host by using Sun's policytool to grant java.security.AllPermission for testing purposes. Both halves of this technique are extinct today: Java applets have been unsupported since major browsers dropped NPAPI plugin support in the mid-2010s, and 4D Open (the C/Java client API this note depends on) was discontinued long ago, so developers now reach 4D Server from external code through 4D's REST/ORDA web data server instead.

**References to newer/updated information:**
- Java applets are effectively extinct; all major browsers removed the NPAPI plugin support required to run them
- 4D Open (and 4D Open for Java specifically) has been discontinued; modern integrations with 4D Server use 4D's REST/ORDA data server instead
