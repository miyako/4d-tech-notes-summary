# Tech Note 07-36: 4D Live Window JavaScript Part 2 – Injection

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** September 11, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Windows only
**Page:** https://kb.4d.com/assetid=47487
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_35-38_(SEP)/07-36_4DLW_JavaScript_Inject.zip

## Overview
The second part in a series on 4D Live Window (4DLW) JavaScript integration, this note shows how to "inject" arbitrary JavaScript into any page — local or remote — displayed inside a 4DLW plug-in area using the `Web_JavaScriptExecute` command, added in 4DLW 1.1.

## Key Points
- `Web_JavaScriptExecute(Area; Script)` executes literal JavaScript text passed in `Script`; passing only a function name is treated as a reference, not a call.
- JavaScript execution via 4DLW is supported on Windows only — Mac OS's WebKit browser layer was too unstable and could crash the database.
- The demo shows injecting script into a bundled local HTML file (change heading, change image, add table border, hide entire document).
- It also demonstrates injecting script into a live remote page — the 4D Knowledgebase search page — to restyle colors and hide the sidebar/breadcrumb trail.
- Firebug (Firefox) is recommended for identifying DOM element IDs and CSS classes on unfamiliar pages, with a caveat that 4DLW's actual rendering engines (IE on Windows, Safari on Mac) expose different DOM/CSS APIs than Firefox.
- A legal caution is raised about modifying third-party web pages/APIs (e.g., Google Maps) without checking the terms of use.

## Featured Technology
- 4D Live Window (4DLW) plug-in
- 4D Web 2.0 Pack
- `Web_JavaScriptExecute` command
- Firebug DOM/CSS inspection

## Historical Context
Published in the 2007 era of the subscription-based 4D Web 2.0 Pack, shortly before 4D v11 introduced native SQL support. The note predates Project Mode and ORDA entirely, and relies on embedding a native OS browser control inside a 4D window — a very different model from today's web tooling.

## Historical Commentary
**Status:** Obsolete

4D Live Window and the entire 4D Web 2.0 Pack have been discontinued, so the specific plug-in, its `Web_JavaScriptExecute` API, and the Windows-only limitation described here no longer apply to any current 4D product. Firebug itself was retired years ago in favor of built-in browser DevTools. The broader concept — embedding a native browser view and manipulating its content via script — persists in modern embedded webview technologies, but this note offers no directly reusable guidance for current 4D development.
