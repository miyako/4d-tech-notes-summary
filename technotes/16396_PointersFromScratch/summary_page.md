# Tech Note 01-39: Pointers from Scratch

**Author:** Not specified in source
**Published:** August 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16396
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_36-40_(AUG)/01-39_Pointers_from_Scratch.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This technical note describes many aspects of pointers in detail. The main purpose of this tech note is to introduce the concept of pointers to those who are unfamiliar with them.

## Key Points

Based on the available teaser text, this note is: an introduction to the concept and mechanics of pointers in 4D's classic language.

## Featured Technology

- 4D Pointers
- Classic language fundamentals

## Historical Context

Published August 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This introductory note explains the concept and mechanics of pointers in 4D's classic language for developers unfamiliar with them. Pointers remain a core, unchanged part of 4D's classic language today, used for indirect variable/field/array access and passing references between methods, so this note's fundamental explanations are still directly applicable to anyone learning or working in classic 4D code, even in a modern Project Mode database.

**What has changed since:**

- Pointers remain fully supported and largely unchanged in current 4D versions
- 4D's later object/collection types offer reference-like semantics as an alternative to pointers in many modern use cases
