# Tech Note 07-24: 4DAF Video Player

**Author:** Joe Resuello, Technical Support Engineer, 4D Inc.
**Published:** June 20, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46775
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_22-25_(JUN)/07-24_4DAF_Video_Player.zip

## Overview
This Technical Note shows how to embed 4D Ajax Framework (4DAF) objects into a custom HTML page, resulting in a customizable video-player interface that plays clips from 4D Tech Tips and 4D Web 2.0 Pack demos, using minimal JavaScript and HTML.

## Key Points
- Warns explicitly that 4D Web 2.0 Pack, as a subscription product with frequent incremental releases, may make this note (based on 4DAF 1.1) obsolete faster than typical 4D documentation; points to daxipedia.4d.com for updates.
- Ships both a merged application (usable without a license) and a source database with the 4DAF component itself removed, since only licensed developers can build with it.
- The custom interface is built directly on the 4DAF Libraries, with the 4DAF Client used only for configuration purposes.
- Build steps: install the 4DAF component into the source database, create/configure a Selection with the ImageMatrix style via the Access Control tab, author a custom HTML page loading 4DAF's localization/compile scripts and stylesheet, add a DataFiller object, and embed an IFrame to play videos with URLs pulled from the database.
- Database and Project methods from the standard 4DAF installation guide were pre-implemented in the sample so the note can focus purely on the HTML/JS embedding technique.

## Featured Technology
- 4D Ajax Framework (4DAF) — ImageMatrix, DataFiller, IFrame objects
- 4D Web 2.0 Pack (subscription-based add-on)
- Custom HTML/JavaScript front ends over a 4D database

## Historical Context
Published June 2007 during the height of 4D's "Web 2.0" push, this note predates 4D v11's native SQL engine (later in 2007), Project Mode (2018), and ORDA (2018). The 4D Ajax Framework represented 4D's era-appropriate answer to building rich, JavaScript-driven web UIs, a role now filled by 4D's built-in Web Server and Qodly tooling.

## Historical Commentary
**Status:** Obsolete

The note's own warning that the fast-moving 4D Web 2.0 Pack could render it outdated proved true in the long run: 4D Web 2.0 Pack and the 4D Ajax Framework were discontinued years ago, and the daxipedia wiki referenced for updates is no longer a live resource. None of the concrete installation steps, client library calls, or UI object configuration described here apply to current 4D development, which instead relies on 4D's built-in Web Server and modern Qodly component tooling for rich web interfaces.
