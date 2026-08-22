# Tech Note 07-32: 4D Deployment Options for Wide Area Networks

**Author:** Jason T. Slack, Technical Support Engineer, 4D Inc.
**Published:** August 15, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47269
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_30-34_(AUG)/07-32_4D_WAN_Options.pdf

## Overview
This note surveys architectural approaches for accessing a 4D Client/Server database over a Wide Area Network, since native 4D Client/Server was designed and supported for LAN environments only.

## Key Points
- **Web-based (officially supported):** Web 1.0 static pages via 4D's integrated web server; the 4D Ajax Framework ("Web 2.0 Pack") for richer, Ajax-style interactivity; and XML-based Web Services via SOAP or REST (the latter using 4D Internet Commands).
- **Server-centric (not officially supported, but widely used):** Microsoft Terminal Services or Citrix Presentation/Desktop Server, which keep the actual 4D Client↔Server link on a fast LAN while remoting only the visual desktop over the WAN.
- **Remote desktop (not officially supported):** VNC and Apple Remote Desktop take over a single existing desktop session, limiting use to one remote user at a time.
- **WAN optimization tips (unsupported territory):** avoid server-heavy commands like `SELECTION TO ARRAY`, scope queries tightly, and raise client/server timeouts.
- Only the web-based deployment options carry official 4D support for WAN use; the rest are customer-proven but unsupported.

## Featured Technology
- 4D Client/Server
- 4D Web Server, 4D Ajax Framework, SOAP/REST Web Services
- Microsoft Terminal Services, Citrix
- VNC, Apple Remote Desktop

## Historical Context
Published in August 2007 for 4D v2004, shortly before 4D v11 introduced native SQL, this note reflects an era when remote/cloud-friendly database architectures were far less mature, and thin web clients or remoted desktops were the main ways to bridge LAN-only client/server software across a WAN.

## Historical Commentary
**Status:** Still relevant

The specific mention of the 4D Ajax Framework/Web 2.0 Pack is now obsolete since that product line was discontinued, and 4D's networking and remote-access capabilities have since evolved. However, the note's central architectural framework — choosing between a thin web client, a remoted server-side desktop (Terminal Services/Citrix), or a fully remoted single-user desktop (VNC/ARD) — remains a genuinely useful and broadly applicable way to reason about deploying any client/server database application across a WAN today.
