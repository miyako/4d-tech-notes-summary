# Tech Note 01-49: Under the Hood of the GenericEval Database

**Author:** Not specified in source
**Published:** October 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19045
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_46-49_(OCT)/01-49_GenericEval_Database.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The GenericEval database is capable of configuring itself by reading tagged input data. It can convert the tags to fieldnames and retype fields as needed. This Tech Note reviews the methods that perform the crucial operations.

## Key Points

Based on the available teaser text, this note is: a look at the methods behind the self-configuring, tag-driven GenericEval example database.

## Featured Technology

- Self-configuring database structure
- Tagged data import
- Dynamic field retyping

## Historical Context

Published October 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note explains the GenericEval example database's approach to self-configuration: reading tagged input data, converting tags into field names, and retyping fields as needed at runtime. The general challenge of building flexible, generically-configurable data-handling methods is still a relevant design pattern in 4D today, though modern 4D applications would more likely represent such dynamic, tag-driven data using objects/collections and ORDA rather than manipulating classic-language field structures directly.

**What has changed since:**

- 4D's object/collection data types (introduced circa 4D v14-16) now offer a more natural way to represent dynamically-tagged, schema-flexible data than classic field manipulation
- ORDA's dynamic attributes provide an alternative to hand-built generic field-retyping logic
