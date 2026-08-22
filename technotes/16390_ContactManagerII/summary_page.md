# Tech Note 01-35: Contact Manager II

**Author:** Not specified in source
**Published:** July 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16390
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_31-35_(JUL)/01-35_Contact_Manager_II.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This is the second technical note on the Contact Manager example database. The purpose of Part II of this technical note is to take a closer look at how the interface is managed in the calendar of the sample database. Part I explained how objects were placed and displayed in the calendar.

## Key Points

Based on the available teaser text, this note is: part two of a look at how the Contact Manager example database's calendar interface is managed.

## Featured Technology

- Calendar UI construction
- Form object placement/display
- Example database (Contact Manager series)

## Historical Context

Published July 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This is the second in a series on the Contact Manager example database, focusing specifically on how the calendar interface's display is managed, following an earlier note (Part I) that covered placing and displaying the calendar's objects. The general technique of building a custom calendar view from form objects is a pattern developers still sometimes need today, even though modern 4D development would more likely reach for a List Box, a plug-in calendar component, or a web-based calendar widget rather than hand-managing individual form objects as shown here.

**What has changed since:**

- Modern 4D calendar UIs are more commonly built with List Box objects, dedicated calendar plug-ins, or web/JS calendar components
- The underlying object-placement techniques from classic Design Mode forms still function in current 4D versions
