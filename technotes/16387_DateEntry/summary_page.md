# Tech Note 01-31: Date Entry

**Author:** Not specified in source
**Published:** July 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16387
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_31-35_(JUL)/01-31_Date_Entry.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The Date Entry example database demonstrates how, by using a set of routines, the Date entry field can be more flexible for the end user. By tabbing into a field, a User can set the date using the special function keys.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the Date Entry example database's function-key-driven flexible date input.

## Featured Technology

- Custom date-entry form routines
- Function-key input handling

## Historical Context

Published July 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note presents the Date Entry example database, which uses a set of custom routines and special function keys to make date-field entry more flexible for end users tabbing into a field. This specific function-key-driven UI trick reflects a 2001-era UI paradigm; modern 4D applications typically use built-in date pickers, calendar pop-ups, or List Box date columns for more discoverable and accessible date entry, making the exact technique shown here obsolete even though flexible date entry remains a valid usability goal.

**What has changed since:**

- 4D form objects now commonly use built-in date/calendar picker controls rather than custom function-key-driven entry routines
- Modern UI/UX conventions favor discoverable calendar widgets over hidden function-key shortcuts
