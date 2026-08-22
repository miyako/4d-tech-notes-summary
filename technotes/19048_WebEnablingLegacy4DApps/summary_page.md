# Tech Note 01-46: Web-Enabling Legacy 4D Applications

**Author:** Not specified in source
**Published:** October 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19048
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2001/windows/tn_2001_46-49_(oct)/01-46_legacy_web-enabling.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This tech note is an provides an overview of what's involved in updating client-server 4D databases so they can be accessed via the internet. Although other approaches are discusssed, the use of semi-dynamic pages using 4D tags is covered most thoroughly.

## Key Points

Based on the available teaser text, this note is: an overview of approaches for exposing client-server 4D databases to the internet, focused on 4D-Tags-based semi-dynamic pages.

## Featured Technology

- 4D Tags
- Semi-dynamic web pages
- 4D built-in Web Server
- Client-server web publishing

## Historical Context

Published October 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note surveys approaches for exposing an existing client-server 4D database to the internet, focusing mainly on semi-dynamic HTML pages built with 4D Tags served by 4D's built-in Web Server. 4D Tags and the built-in web server still exist and function in current 4D versions, but 4D's web strategy has since shifted decisively toward REST APIs built on ORDA combined with modern JavaScript front ends (or low-code Qodly Studio apps), making tag-embedded HTML page generation a legacy pattern rather than the recommended approach for new web-enabling projects.

**What has changed since:**

- 4D's REST/ORDA APIs (introduced 4D v16-17) are now the standard way to expose 4D data to web/mobile clients
- Qodly Studio offers a low-code alternative for building modern web front ends against 4D data
