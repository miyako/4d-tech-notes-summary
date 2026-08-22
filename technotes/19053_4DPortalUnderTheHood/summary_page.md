# Tech Note 01-54: Under the Hood of the 4D Portal 1.0.1 Database

**Author:** Not specified in source
**Published:** December 30, 2001 | **Product/Version:** 4D Portal v6.7.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19053
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2001/windows/tn_2001_54-57_(dec)/01-54_configuring_4d_portal.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This Technical note explains how 4D Portal 1.0.1 works and how to configure it.

## Key Points

Based on the available teaser text, this note is: an explanation of how the 4D Portal 1.0.1 companion product works and how to configure it.

## Featured Technology

- 4D Portal
- Portlet architecture
- Intranet portal framework

## Historical Context

Published December 2001 for 4D Portal v6.7.1, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note documents the internal configuration of 4D Portal 1.0.1, a companion intranet-portal product from 4D's dot-com-era product lineup that bundled portlet-style widgets on top of a 4D database. 4D Portal itself was discontinued long ago and has no equivalent in the current 4D product line, so this note is now of historical interest only, illustrating an early attempt at a customizable web dashboard rather than any technique still in active use.

**What has changed since:**

- 4D Portal was discontinued as a product; no direct successor exists in 4D's current lineup
- Modern 4D web/mobile dashboards are typically built with REST/ORDA APIs plus a JS framework or Qodly Studio instead of a bundled portal product
