# Tech Note: 4D WebSTAR API

- **Asset ID:** 26847
- **Tech Note #:** 03-08
- **Published:** February 28, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Dave Batton
- **Page URL:** https://kb.4d.com/assetid=26847
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_06-10_(FEB)/03-08_4D_WebSTAR_API.hqx

## Overview

Dave Batton of Datacraft, Inc. documents the 4D WebSTAR API, a 4D component that lets a 4th Dimension developer talk to the WebSTAR Admin Server the same way the official WebSTAR Admin Client application does, in order to build a custom administration interface for the WebSTAR V web/mail/FTP server suite. The API exposes roughly 50 commands prefixed WSAC_, covering session management (WSAC_LoginDialog, WSAC_Login, WSAC_CloseSession, WSAC_Quit), a ready-made admin window (WSAC_AdminWindow) that duplicates the stock Admin Client, and detailed administrative categories: web server settings such as routing and cache flushing (WSAC_WebSrv_GetRouting/SetRouting, WSAC_WebSrv_FlushCache), FTP user accounts (WSAC_FTP_GetUsers/SetUsers), mail and post office user management (WSAC_Mail_GetPostOffices, WSAC_PostOff_GetUsers/SetUsers), and an extensive web security subsystem covering realms, allow/deny lists, user lists, authentication types, and permissions (the WSAC_Security_* family). Installation requires 4D 6.8.2+ and WebSTAR 5.2.x, plus the 4D View plug-in and three bundled free plug-ins (4D Internet Commands, Expat4D, and TextProperties), and the component is installed into a structure file via 4D Insider's Install/Update Components command. The note is explicitly labeled an alpha release, tested only on Mac OS X, with known UI issues in the bundled Admin Window replica but no known problems in the underlying API itself.

## Key Points

- The 4D WebSTAR API is a 4D component (installed via 4D Insider's Components menu) exposing roughly 50 `WSAC_` commands that let a 4D developer talk directly to the WebSTAR Admin Server, the same protocol used by the official WebSTAR Admin Client application.
- Session management commands (`WSAC_LoginDialog`, `WSAC_Login`, `WSAC_CloseSession`, `WSAC_SessionState`, `WSAC_Quit`) establish and tear down authenticated sessions, while `WSAC_AdminWindow` reproduces the entire stock WebSTAR Admin Client UI inside a 4D window.
- Web server administration commands cover host routing (`WSAC_WebSrv_GetRouting`/`SetRouting`), web hosts (`WSAC_WebSrv_GetWebHosts`/`SetWebHosts`), and cache control (`WSAC_WebSrv_FlushCache`, `WSAC_WebSrv_GetCacheInterval`/`SetCacheInterval`).
- FTP and mail administration is covered by `WSAC_FTP_GetUsers`/`SetUsers` and the `WSAC_Mail_GetPostOffices` / `WSAC_PostOff_GetUsers`/`SetUsers` command families, while an extensive security API (`WSAC_Security_*`) manages web realms, allow/deny lists, user lists, authentication types, and granular permissions.
- Requirements include 4D 6.8.2+, WebSTAR 5.2.x, the 4D View plug-in (not bundled, due to size), and three bundled free plug-ins (4D Internet Commands, Expat4D, TextProperties); the API itself is reported bug-free at the time of writing, though the bundled Admin Window UI replica has several noted rough edges (Mac OS 9/Windows incompatibility, uncached form layouts, mouse-state bug after list clicks).

## Featured Technology

- 4D component architecture (installed via 4D Insider Components menu)
- WebSTAR Admin Server session/login API (WSAC_Login, WSAC_LoginDialog)
- WebSTAR Admin Client UI replication (WSAC_AdminWindow)
- Web hosting, routing, and cache administration (WSAC_WebSrv_* commands)
- FTP and mail/post-office account management (WSAC_FTP_*, WSAC_PostOff_*)
- Web security realms, allow/deny lists, and permissions (WSAC_Security_*)
- Dependencies: 4D View, 4D Internet Commands, Expat4D, TextProperties plug-ins

## Historical Commentary

**Status:** Obsolete

This note documents an ambitious, near-complete programmatic front end to WebSTAR's Admin Server — covering web routing, FTP, mail, and security realm management through roughly 50 commands — reflecting a period when 4D and WebSTAR (both then owned by related companies) were closely integrated. WebSTAR as a product line has been discontinued for many years, and 4D's own built-in web server (introduced not long after this note and steadily expanded since) made a separate WebSTAR server and its administration API unnecessary for 4D-based web deployments. As a result, this component and its ~50 WSAC_ commands are of historical interest only for understanding how 4D-WebSTAR integration worked, but are not usable with any currently supported server software.

References to newer/updated information:
- WebSTAR has been discontinued for many years, making the WSAC_ API described here nonfunctional against any current server
- 4D's own built-in web server, expanded substantially since 2003, has long eliminated any practical need to run or administer a separate WebSTAR server from a 4D application
