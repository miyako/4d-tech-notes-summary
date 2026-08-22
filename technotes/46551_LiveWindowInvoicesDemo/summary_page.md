# Tech Note 07-20: 4D Live Window 1.1 - Invoices Demo Database

**Author:** Robert Molina, Technical Support Engineer, 4D Inc.
**Published:** May 23, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46551
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_17-21_(MAY)/07-20_4DLW_Invoices.zip

## Overview
This note explores an Invoices demo database showcasing 4D Live Window (4DLW) 1.1, a plug-in area for displaying and interacting with external HTML/PDF/Office documents inside a 4D form, highlighting the callback and navigation-filtering features new in the 1.1 release.

## Key Points
- 4DLW 1.0 recap: enables viewing arbitrary document formats (HTML, PDF, Word, Excel) in a 4D form without needing a separate single-format plug-in.
- 4DLW 1.1 additions: context menu/new window control, before/during/after-click callbacks to 4D, page-load-error callback, get/set content with custom encodings, and JavaScript evaluation in the loaded page.
- "v1.0-style" workflow demonstrated: pull an HTML template (Invoice.html) into a BLOB, set preferences via `Web_SetPreferences`, process embedded 4D HTML tags with `PROCESS HTML TAGS` (the same engine used by the 4D Web Server), save the result to disk, and display it via `Web_SetURL`, with a `DELAY PROCESS` to let the OS finish writing the file.
- New 1.1 capability demonstrated: clicking an invoice reference number inside the Live Window area opens the related [Invoices] record in a new process, via `Web_kNavigate` (cancels default navigation, calls a developer callback `W_BrowserNavigate`) combined with `Web_kNavigateFilter` (restricts allowed navigation URLs, e.g. to paths containing "/Browser/").
- Full "On Load" form event code is reproduced, including Mac-vs-Windows path separator handling.
- Notes 4D Web 2.0 Pack's subscription/fast-iteration model and points to the daxipedia wiki for updates.

## Featured Technology
- 4D Live Window (4DLW) plug-in, versions 1.0 and 1.1
- `PROCESS HTML TAGS`, `Web_SetPreferences`, `Web_SetURL` commands
- `Web_kNavigate` / `Web_kNavigateFilter` navigation-interception preferences
- 4D Web 2.0 Pack

## Historical Context
Published May 2007, this note documents a plug-in-based approach to embedding rich, HTML-styled document viewing and interaction inside a classic 4D desktop client form — an alternative to subforms and button-driven UIs of that era. It predates 4D v11's native SQL engine (later 2007), Project Mode (2018), and ORDA (2018), and reflects a period when embedding a browser-like control in a native form, rather than building the whole UI on the web, was a common technique.

## Historical Commentary
**Status:** Obsolete

4D Live Window as a standalone 4D Web 2.0 Pack plug-in has been discontinued along with the rest of that product line. Modern 4D offers built-in HTML/web-view form area objects for embedding web content directly in forms without a separate plug-in, and the broader industry and 4D's own tooling (Web Server, Qodly components) have shifted toward building entire UIs on the web rather than embedding HTML mash-ups inside desktop client windows, making the specific plug-in commands and workflow in this note no longer applicable.
