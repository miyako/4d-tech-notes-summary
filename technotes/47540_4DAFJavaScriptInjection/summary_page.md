# Tech Note 07-37: 4D Ajax Framework JavaScript Injection

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** September 19, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47540
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_35-38_(SEP)/07-37_4DAF_Javasscript_Inject.zip

## Overview
This Tech Note explores how a Developer Defined Window (DDW) method in the 4D Ajax Framework (4DAF) can return JavaScript instead of HTML/data, and how that JavaScript can be "injected" into and executed within the current web page — either manually in a custom HTML page, or automatically as of 4DAF 1.2 in the built-in 4DAF Client.

## Key Points
- A DDW method returns a text string prefixed with `"JS:"` to signal JavaScript content.
- Back end: create the DDW via the `DAX_DevHook_DDW_Install` hook and `DAX_Dev_DDW_Create`, or through the 4DAF Control Panel.
- Client (4DAF Client) configuration: setting the DDW's target to "Portal" is enough — 4DAF 1.2 auto-parses and executes `JS:`-prefixed responses.
- Custom page configuration requires three manual steps: build the DDW URL (using the DDW id from `DDW.xml` and the session id), call it via `makeCall()`, and parse the XML response to extract and `eval()` the script.
- The bundled "Contacts" sample database demonstrates a DDW Portlet triggering a JS alert, and a custom `example.html` page that injects JavaScript to construct 4DAF Data Grids for different Views (Contacts/Appointments) without exposing view names in static markup.
- DDW response content is explicitly not validated by 4D or the 4DAF — developers must ensure returned script is valid.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- Developer Defined Windows (DDW)
- Data Grid (via `DataWindow` JS constructor)
- Manual XML response parsing and `eval()`-based JavaScript injection

## Historical Context
Published during the brief life of the subscription-based 4D Web 2.0 Pack, ahead of the SQL-enabled 4D v11 (2007) and long before Project Mode (v17) or ORDA (v17+). The 4DAF/DDW/Daxipedia stack referenced throughout has since been fully discontinued by 4D, replaced conceptually by 4D's native Web Server and, much later, Qodly-based tooling.

## Historical Commentary
**Status:** Obsolete

The specific 4DAF/DDW mechanism, the Daxipedia documentation site, and the pattern of manually parsing XML and calling `eval()` on server-supplied script are all obsolete: 4DAF and the Web 2.0 Pack no longer exist, and `eval()`-based script injection is now considered a security anti-pattern in modern web development. The broader idea of a server driving client-side behavior remains conceptually alive in other forms (e.g., server-driven UI updates), but this note has no direct practical relevance to current 4D development.
