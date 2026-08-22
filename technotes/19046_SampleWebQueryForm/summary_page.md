# Tech Note 01-48: Sample Web Query Form

**Author:** Not specified in source
**Published:** October 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19046
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_46-49_(OCT)/01-48_Web_Query_Form.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This Tech Note examines a web-based query form for 4th Dimension 6.7 based on a stock symbol database. Two sample HTML forms are given, a simple one with a single text field and an advanced form that partially emulates 4D's built in Query editor. The techniques illustrated can be expanded upon and easily adapted for use in your own databases.

## Key Points

Based on the available teaser text, this note is: an example of building simple and advanced HTML web query forms against a 4D database.

## Featured Technology

- 4D Tags
- HTML web forms
- 4D built-in Web Server query emulation

## Historical Context

Published October 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note builds a web-based search form against a stock-symbol database, offering both a simple single-field HTML form and a more advanced one that partially emulates 4D's native Query Editor, all served through 4D's tag-based web publishing. The underlying idea of a web search form against 4D data remains universally relevant, but the specific 4D Tags/HTML-embedded implementation shown is a legacy technique that has been superseded by REST/ORDA-backed APIs consumed by modern JavaScript search UIs.

**What has changed since:**

- REST/ORDA-based search and filtering APIs have replaced 4D-Tags-driven HTML query forms in modern 4D web development
- 4D's own Query Editor concept lives on in the classic language, but web-facing search UIs are now typically client-side JS apps calling REST endpoints
