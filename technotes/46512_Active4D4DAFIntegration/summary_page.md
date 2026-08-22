# Tech Note 07-19: Integrating Active4D and the 4D Ajax Framework

**Author:** Jason T. Slack, Technical Support Engineer, 4D Inc.
**Published:** May 18, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46512
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_17-21_(MAY)/07-19_A4D-4DAF_Integration.zip

## Overview
This note explains how to run Active4D — a third-party ASP-style scripting language and HTTP server for 4D, not developed or supported by 4D Inc. — alongside 4D's own 4D Ajax Framework (4DAF) in a single database, since the two frameworks' default installation instructions conflict.

## Key Points
- Active4D is explicitly flagged as a third-party product (by Aparajita's World), assuming the reader already knows Active4D development; 4D provides no support for it.
- A custom nine-step installation is required: install the 4DAF component via 4D Insider, ensure the "4D Pack" plug-in is present, copy the 4DAF's "dax" folder into Active4D's required "web_decoy" web root, install the 4DAF Support folder, configure 4DAF while skipping the standard guide's step 5, and keep the web root set to "web_decoy" per Active4D's requirement.
- Key integration point: the `On Web Connection` method is modified so requests tagged with the literal marker `"@DAX@"` route to `DAX_DEV_OnWebConn`, while all other requests fall through to Active4D's own generated code (if/else or Case of).
- `Active4D.ini` is the main Active4D configuration file; changes require restarting 4D to take effect.
- Example-specific tweaks shown: setting `default page`/`executable extensions` in Active4D.ini, auto-authenticating a "Guest" user in `DAX_DevHook_Login`, and renaming the 4DAF Client index pages to "admin".
- Includes a FlowersDemo video and `web\display.a4d` source as concrete illustrations; suggests use cases like shopping carts and member portals.

## Featured Technology
- Active4D (third-party ASP-style scripting language / HTTP server for 4D)
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- `On Web Connection` request routing
- 4D Insider (component installation tooling)

## Historical Context
Published May 2007, this note is a snapshot of the fragmented early 4D web-development ecosystem, where a community/third-party ASP-style layer (Active4D) and 4D's own in-house rich-web framework (4DAF) both competed for the same web server slot in a 4D database, requiring manual request-routing glue code. It predates 4D v11's native SQL engine (later 2007), Project Mode (2018), and ORDA (2018).

## Historical Commentary
**Status:** Obsolete

Both halves of this integration are long defunct: Active4D as a third-party product is no longer maintained or available, and 4D Web 2.0 Pack / the 4D Ajax Framework were discontinued by 4D itself. The specific installation steps, `On Web Connection` routing trick, and Active4D.ini configuration described here have no current application; modern 4D web development is built entirely on 4D's own Web Server and Qodly component tooling rather than mixing third-party ASP-style layers with a proprietary Ajax framework.
