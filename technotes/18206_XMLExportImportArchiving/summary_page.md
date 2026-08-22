# Tech Note 01-43: XML based Export/Import for Archiving Data

**Author:** Not specified in source
**Published:** September 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=18206
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_41-45_(SEP)/01-43_Archiving_Data_in_XML.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This technical note describes a generic method to export and import data using the XML format. For example, this allows you to perform:

long term data archiving 
database defragmentation 
controlled repair of damaged databases 
major release update tool 
drop field/drop table functionality 
It is not a generic XML Import tool; it cannot be used to open any XML file.

## Key Points

Based on the available teaser text, this note is: a generic technique for exporting and importing 4D data in XML format for archiving, defragmentation, and schema migration.

## Featured Technology

- 4D XML commands
- Data archiving
- Database defragmentation
- Schema migration (drop field/table)

## Historical Context

Published September 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note describes a generic (not universal) XML export/import scheme for 4D data, useful for long-term archiving, defragmentation, controlled repair of damaged databases, and structural migrations like dropping fields or tables. XML import/export commands remain part of 4D's classic language today, and the underlying archiving/migration use cases are still relevant, though modern 4D projects increasingly also use JSON (native since 4D v15/16) and ORDA-based data transfer for similar import/export and migration needs.

**What has changed since:**

- 4D added native JSON parsing/serialization (circa 4D v15-16), now often preferred over XML for data interchange
- ORDA provides additional entity-based mechanisms for moving and migrating data between structures
