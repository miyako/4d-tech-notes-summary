# Tech Note 01-29: The 128th Byte

**Author:** Not specified in source
**Published:** June 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=15348
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_26-30_(JUN)/01-29_The_128th_Byte.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This article describes the internal structure of 4D's records. With this knowledge, you will be able to optimize the access to your data and better understand 4D's inner workings.

In order to store data, databases use specific files saved on a hard disk (or any other data storage device). Generally, database management systems use one file per table. In addition to that, they also need an additional file for each index (when developers have control over that parameter), or, in some cases, to describe a relation between two tables. This architecture's main advantage is to prevent you from mixing "apple and oranges" but it also quickly increases the number of disk files and it makes installations, updates, and backup increasingly difficult.

## Key Points

Based on the available teaser text, this note is: a description of the internal byte-level structure of 4D's records within its data files.

## Featured Technology

- 4D internal record structure
- Database file architecture fundamentals

## Historical Context

Published June 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note describes the internal byte-level structure of 4D's records within its data files, aimed at helping developers optimize data access and understand 4D's inner workings, including general database-architecture tradeoffs (one file per table plus per-index files versus a consolidated format). Because 4D's on-disk record and data-file format has been re-engineered multiple times in the decades since (v11 SQL engine, then the 64-bit engine), the specific byte-level structure detailed in this note no longer matches any current 4D file format, making it a historical snapshot of early 4D internals rather than a practical reference.

**What has changed since:**

- 4D's on-disk data/record format has been redesigned multiple times since 2001 (4D v11 SQL engine, later 64-bit engine)
- Modern 4D data file internals bear little structural resemblance to the format described in this note
