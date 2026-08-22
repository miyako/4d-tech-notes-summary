# Tech Note 01-57: Inside the Report Demo Database

**Author:** Not specified in source
**Published:** December 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19056
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_54-57_(DEC)/01-57_Report_Demo.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The Report Demo example database is an intermediate-level database, written by Tad Michael Wheeler, of DataCraft. This simple database contains a hierarchical data structure with 3 tables, a structure that is very common in database design. The Report Demo example database is a basic database that demonstrates the usage of common reporting functions. It demonstrates one approach to creating a report, which is generated from the Many table. It uses break levels and accumulation to aid the developer in seeing what actually occurs when this type of report is generated. You can print preview the report and see which code is running where.

I will be discussing the following methods, and explaining how they are used in the Report Demo.

On Startup

ReportDemo_SpecialReport

ReportDemo_FormatName

Now that you have a brief idea of what the Report demo can do, and what I will be discussing in this tech note, lets start off by looking at the first method that is executed when launching the Report Demo database.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the classic Report Demo example database's break-level report generation methods.

## Featured Technology

- Break-level report processing
- PRINT FORM
- Example database (Report Demo by Tad Michael Wheeler)
- Report accumulation techniques

## Historical Context

Published December 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note walks through a classic break-level reporting technique (accumulation across a hierarchical 3-table structure) built in 4D's binary Design Mode. The fundamental break-level/PRINT FORM approach to generating reports from a sorted selection is still part of 4D's classic language and remains conceptually valid today, though most modern report UIs would instead lean on List Box-based reporting or 4D Write Pro document generation rather than hand-built break-level methods.

**What has changed since:**

- List Box and 4D Write Pro reporting have become the more common modern approach to formatted reports
- Project Mode text-based structures replaced binary .4DB/.4DC Design Mode files for new development
