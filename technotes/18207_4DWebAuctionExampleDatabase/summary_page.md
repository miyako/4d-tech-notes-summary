# Tech Note 01-44: The 4D Web Auction Example Database

**Author:** Not specified in source
**Published:** September 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=18207
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_41-45_(SEP)/01-44_Exploring_Auction_DB.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> 4D Web Auction illustrates a non-contextual web interface to a database. It demonstrates 4D's ability to parse an HTML page and dynamically replace 4D tags with data from 4D and present this data to the user in real time.

This Tech note also includes and discusses a quick method to help prevent browsers from caching pages.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the 4D Web Auction demo's non-contextual, tag-based dynamic web interface.

## Featured Technology

- 4D Tags
- Non-contextual web publishing
- Browser cache-busting technique

## Historical Context

Published September 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note walks through the 4D Web Auction demo, illustrating 4D's tag-based parsing of HTML pages to dynamically inject live database data for a non-contextual (stateless) web interface, plus a trick to discourage browser page caching. Tag-based HTML parsing for dynamic pages is a legacy 4D web-publishing pattern that has been superseded by REST/ORDA APIs paired with modern JS front ends, and dot-com-era e-commerce/auction demos like this one are now purely of historical interest.

**What has changed since:**

- 4D's web publishing model has moved from embedded-tag HTML parsing to REST/ORDA APIs consumed by JS front ends
- Modern HTTP cache-control headers/techniques have superseded ad hoc 4D-side cache-busting tricks
