# Tech Note 01-52: Printing Arrays

**Author:** Not specified in source
**Published:** November 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19051
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_50-53_(NOV)/01-52_Printing_Arrays.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> Arrays are a powerful feature of 4D. They are often used to create summaries of data, such as reports, built from 4D records. However they cannot be printed directly from within 4D. This technical note describes a simple technique for printing data in arrays using variables and the PRINT FORM command. It can be used to print any type of array data.

## Key Points

Based on the available teaser text, this note is: a technique for printing array data using form variables and the PRINT FORM command.

## Featured Technology

- 4D Arrays
- PRINT FORM
- Report generation from array data

## Historical Context

Published November 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note explains a workaround for a real classic-language limitation — arrays cannot be printed directly — by mapping array data into form variables and using PRINT FORM to render it. This general variable/PRINT FORM technique still functions in current 4D versions, though today a List Box bound to a collection or array, or 4D Write Pro, would often be a more convenient way to lay out and print the same tabular data.

**What has changed since:**

- List Box objects (with array or collection data sources) now offer a more direct way to display and print tabular array data
- 4D Write Pro provides richer document-based printing options than plain PRINT FORM
