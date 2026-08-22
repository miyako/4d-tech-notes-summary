# Tech Note 01-47: The ButtonMaker Example Database

**Author:** Not specified in source
**Published:** October 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19047
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_46-49_(OCT)/01-47_ButtonMaker_Example.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The ButtonMaker database is an example database that was created by Jeremy Sullivan of HD Industries. With the ButtonMaker, Jeremy shows you how you can use 4D and 4D Chart to create custom button graphics. By entering or selecting the desired values, you can create custom button graphics for your HTML pages. When all the attributes for the button have been entered, click on the submit button to view the newly created button.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the ButtonMaker example database, which uses 4D and 4D Chart to generate custom HTML button graphics.

## Featured Technology

- 4D Chart
- 4D + HTML button graphics generation
- Example database (Jeremy Sullivan, HD Industries)

## Historical Context

Published October 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note walks through an example database that used 4D Chart to programmatically generate custom HTML button graphics from user-entered attributes, a popular dot-com-era task of dynamically producing web imagery from a database. 4D Chart has since been discontinued as a companion product, and dynamic web graphics generation today is handled by client-side CSS/SVG/canvas techniques or external image-generation services rather than a 4D-hosted charting engine, making this note's specific approach obsolete.

**What has changed since:**

- 4D Chart was discontinued as a companion product
- Dynamic web graphics are now typically generated with CSS/SVG/canvas on the client or via external image-generation services rather than server-side 4D charting
