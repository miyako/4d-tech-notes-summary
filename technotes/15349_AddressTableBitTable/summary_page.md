# Tech Note 01-30: At the Core of the Data: The Address Table and Bit Table

**Author:** Not specified in source
**Published:** June 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=15349
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_26-30_(JUN)/01-30_Core_of_the_Data.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> Knowing the internal mechanisms used by 4D to retrieve records, as well as how data is stored based on the platform, is interesting for many reasons. This knowledger enables you to prepare your data for a cross-platform environment and understand the operations involved with recovering damaged data.

In this article, we are going to continue our tour at the heart of 4D's data file. We recommend that you read the previous technical note, TN 01-29. That article described the basic principles which we are about to explain in depth.

## Key Points

Based on the available teaser text, this note is: a deep-dive into 4D's internal Address Table and Bit Table data structures, continuing from TN 01-29.

## Featured Technology

- 4D internal data file format
- Address table / Bit table structures
- Cross-platform data storage internals

## Historical Context

Published June 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note (a follow-up to TN 01-29) goes deeper into 4D's proprietary internal data-file mechanisms — the Address Table and Bit Table structures used to locate and track records — explaining cross-platform storage considerations and damaged-data recovery. 4D's internal data file format has been substantially re-engineered multiple times since 2001 (notably with the 4D v11 SQL engine and the later 64-bit engine), so these specific internal structures no longer describe the current file format, making this note purely of historical/archival interest for understanding 4D's early engine design.

**What has changed since:**

- 4D's internal data file architecture was substantially redesigned in 4D v11 SQL (~2007) and again with the 64-bit engine (~4D v13)
- Current data recovery/repair tooling in 4D operates on a materially different internal file structure than described here
