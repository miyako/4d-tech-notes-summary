# Tech Note 01-42: How to generate a pathname document in 4D

**Author:** Not specified in source
**Published:** September 30, 2001 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=18205
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_41-45_(SEP)/01-42_Generate_Pathname_Doc.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The purpose of this technical note is to show you how you can generate a pathname document automatically.

## Key Points

Based on the available teaser text, this note is: a technique for automatically generating a document referenced by a full pathname in 4D.

## Featured Technology

- 4D document/pathname commands
- File system automation

## Historical Context

Published September 2001 for 4D v6.5, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This short note shows how to automatically generate a document referenced by a full pathname in 4D, a foundational file-handling task. The classic-language document and pathname-handling commands it relies on remain part of current 4D versions and function essentially the same way today, making the core technique still directly applicable, even as 4D has since added higher-level File/Folder object commands for more structured file-system access.

**What has changed since:**

- 4D later introduced object-based File and Folder commands (circa 4D v16+) offering a more structured alternative to raw pathname string manipulation
- Classic document/pathname commands from this era remain supported for backward compatibility
