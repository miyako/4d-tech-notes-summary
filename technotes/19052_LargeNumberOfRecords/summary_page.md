# Tech Note 01-51: Handling a Large Number of Records

**Author:** Not specified in source
**Published:** November 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19052
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_50-53_(NOV)/01-51_Large_Num_of_Records.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> 4D has a limit of 16 million records per table. This tech note describes how you can speed up databases with a large number of records and how you can exceed this limit in some cases.

## Key Points

Based on the available teaser text, this note is: guidance on speeding up databases with very large record counts and working around the classic 16-million-record table limit.

## Featured Technology

- 4D data file architecture
- Record count limits
- Performance optimization
- Indexing

## Historical Context

Published November 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note discusses the then-current 16-million-record-per-table ceiling in 4D and techniques for improving performance and working around the limit. 4D's data engine has been substantially rearchitected since 2001 (including the move to a 64-bit engine around 4D v13), which raised or removed many of these classic record-count and file-size ceilings, so the specific limit cited is outdated even though the general performance techniques (proper indexing, selection management) remain conceptually useful.

**What has changed since:**

- 4D's 64-bit data engine (introduced circa 4D v13) substantially raised classic record/file-size limits
- General 4D indexing and selection-performance best practices from this era still apply conceptually
