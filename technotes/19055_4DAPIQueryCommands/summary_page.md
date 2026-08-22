# Tech Note 01-56: Using the 4D API Query Commands

**Author:** Not specified in source
**Published:** December 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19055
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_54-57_(DEC)/01-56_4D_API_Query_Commands.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This technical note describes how to go about using API commands to create 4D Queries inside a plug-in. This technical note will also look at the two different ways to create a query. One is to use the built in 4D Query Dialog, while the other is to use the build in 4D Query commands. These would be similar to the "QUERY" command in 4D.

## Key Points

Based on the available teaser text, this note is: a guide to invoking 4D's Query Editor and QUERY-style commands from within a compiled C plug-in.

## Featured Technology

- 4D Plug-in API (C-based)
- QUERY command
- 4D Query Editor dialog

## Historical Context

Published December 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note explains how a compiled C plug-in could programmatically invoke 4D's query mechanism, either via the built-in Query Editor dialog or the classic QUERY-style API commands, in the pre-Unicode, 32-bit plug-in API era. The classic QUERY command family it discusses is still present in 4D's language today, but the plug-in API itself has been substantially revised since (Unicode, 64-bit, Universal Binary), and ORDA's dot-notation entity queries now offer a more modern alternative to constructing query criteria programmatically.

**What has changed since:**

- 4D's Plug-in API was significantly overhauled for Unicode/64-bit support starting around 4D v11 SQL
- ORDA (introduced 4D v17, 2018) provides object/entity-based querying as an alternative to classic QUERY chains
