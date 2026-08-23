# Tech Note: 4D WebSTAR API 2003.1

- **Asset ID:** 29734
- **Tech Note #:** 03-38
- **Published:** August 29, 2003
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Steve Hartman
- **Page URL:** https://kb.4d.com/assetid=29734
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_36-39_(AUG)/03-38_4D_WebSTAR_2003.1_API.hqx

## Overview

Steve Hartman (MCP, Information Systems, 4D, Inc.) documents the 4D WebSTAR API 2003.1 component, which exposes almost 50 WSAPI commands so a 4D database can administer a WebSTAR V server's mail, FTP, and security settings directly, eliminating the need to maintain the same information separately in both a 4D employee database and the WebSTAR Admin Client.

## Key Points

- The WSAPI component is installed via 4D Insider as a pure-4D-methods component; a [WSAPI] table must be linked (not copied) into the host database, and 4D Internet Commands must be present in the Win4DX/Mac4DX folders.
- The core login/logout pattern: `WSAPI_LoginDialog` (or `WSAPI_Login` for procedural credentials) returns a session ID, `WSAPI_GetSettingsGroup` selects a settings group, and the session ends with `WSAPI_CloseSession` followed by `WSAPI_Quit` to stop the API's background processes.
- `WSAPI_Admin_GetComponents` is used in the sample login method to read the names/versions of installed WebSTAR components (e.g. confirming the WebSTAR Admin Server version) via `ARRAY TEXT` output parameters and `Find in array`.
- The bundled "Employee Demo" database demonstrates per-department password-protected access (Designer, Administrator, Human Resources, Accounting, Manager, Information Systems) and a Sync button that uploads/downloads changed e-mail and FTP account settings between 4D and the WebSTAR Admin Server.
- Requirements: 4D 2003.1+ (or 4D Client/Server), a compatible 4D Internet Commands plug-in, WebSTAR 5.2+, and 4D Insider 2003.1+ for installation.
- The note stresses the API cannot grant privileges beyond what the logged-in WebSTAR user already has -- the WebSTAR Admin Server itself enforces authorization on every WSAPI call.

## Featured Technology

- 4D WebSTAR API (WSAPI) component
- WSAPI_Login / WSAPI_LoginDialog
- WSAPI_GetSettingsGroup
- WSAPI_Admin_GetComponents
- WSAPI_CloseSession / WSAPI_Quit
- 4D Insider component installation

## Historical Commentary

**Status:** Obsolete

This note documents a purpose-built API for administering 4D's own discontinued WebSTAR web server product from within a 4D database -- a niche but clever integration for its time that avoided duplicate data entry between an employee database and server administration. Because WebSTAR itself has been discontinued for many years and 4D's own built-in web server has long since become the standard way to serve 4D web content, both the WSAPI component and the administrative use case it served are now obsolete. The general pattern of session-based login/action/logout wrapping a remote administrative API remains a reasonable design, but there is no direct 4D successor to WSAPI itself.

**References to newer/updated information:**
- WebSTAR as a web server product has been discontinued for many years, and with it the WSAPI component described here
- 4D's own built-in web server has long since replaced the need for a separate WebSTAR server in 4D web deployments
