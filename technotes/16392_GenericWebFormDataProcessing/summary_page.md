# Tech Note 01-36: Creating a Generic Web Form Data Processing System

**Author:** Not specified in source
**Published:** August 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16392
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_36-40_(AUG)/01-36_Generic_Web_Form_DPS.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This technical note is the first of a two-part series on creating a relatively generic data processing system for handling data entered on a Web Form. The approach uses two databases: One gathers the data via the web and e-mails the data to the second database for storage and analysis. This tech note describes the first database.

## Key Points

Based on the available teaser text, this note is: part one of a two-database system for gathering web form data and emailing it to a second database for storage and analysis.

## Featured Technology

- 4D built-in Web Server
- Two-database architecture
- Email-based data transfer

## Historical Context

Published August 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note (part one of a two-part series) describes a generic system where one 4D database gathers data through a web form and emails it to a second database for storage and analysis. The architectural idea of separating a public-facing data-collection front end from a back-office storage/analysis system remains a valid pattern, but routing form submissions via email between two databases is a workaround that has been superseded by direct REST/ORDA API calls or database replication/sync mechanisms that didn't yet exist in 4D in 2001.

**What has changed since:**

- Direct REST/ORDA API calls between 4D databases or services have superseded email-based data hand-off as the standard mechanism
- 4D's later Sync feature and ORDA-based data synchronization provide more robust alternatives for moving data between systems
