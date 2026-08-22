# Tech Note 01-53: Exploring 4D Portal's Reminder Portlet

**Author:** Not specified in source
**Published:** November 30, 2001 | **Product/Version:** 4D Portal v6.7.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19050
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_50-53_(NOV)/01-53_Reminder_Portlet.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The Reminder Portlet offers four types of Reminders — monthly, weekly, daily and once. As the name implies, monthly reminders are sent monthly, weekly reminders are sent weekly, daily reminders are sent daily, and once reminders are sent once on the exact date and time. In addition to sending reminders at the exact time, reminders can also be set to send at ten or five minutes before a reminder is due. Setting a reminder to a ten minute reminder will send a reminder at ten minutes before a reminder is due, five minutes before a reminder is due and when the reminder is actually due. A five minute reminder sends a reminder at five minutes before a reminder is due, and when the reminder is actually due. A None reminder simply sends when the reminder is due.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the scheduling logic behind 4D Portal's monthly/weekly/daily/once Reminder Portlet.

## Featured Technology

- 4D Portal
- Reminder Portlet
- Scheduled notification logic

## Historical Context

Published November 2001 for 4D Portal v6.7.1, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note details the scheduling logic behind 4D Portal's Reminder Portlet, covering monthly/weekly/daily/once reminder types and configurable lead-time alerts. Since 4D Portal itself was discontinued years ago, the specific portlet and its configuration options no longer exist in any supported 4D product, making this note of historical interest only, though the general reminder-scheduling logic pattern (recurring vs one-time triggers with lead-time offsets) remains a conceptually familiar problem in modern notification systems.

**What has changed since:**

- 4D Portal was discontinued as a product line
- Modern reminder/notification systems in 4D applications are typically built with the classic language's date/time commands or external push-notification services rather than a bundled portal component
