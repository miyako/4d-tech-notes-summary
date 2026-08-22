# Tech Note 01-21: 4D Chart on the Web in Non-Contextual Mode

**Author:** Not specified in source document
**Published:** June 4, 2001 | **Product/Version:** 4D Chart v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=14004
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_21-25_(MAY)/01-21_4D_Chart_on_the_Web.exe

## Overview
A technique for serving both field-stored graphs and interactively created 4D Chart graphs on the web using Non-Contextual Mode, updating the older TN 98-13. This Tech Note discusses how to serve two categories of chart imagery from a 4D web site: graphs stored directly in database fields, and 4D Chart graphs generated interactively at request time.

## Key Points
- It positions itself explicitly as an update to an earlier note, TN 98-13, which had only addressed serving graphs in 4D's original Contextual Mode; this note instead reworks the same goal using v6.5's newer Non-Contextual Mode web server, reflecting the platform's rapid evolution of web-serving options in this period.
- The featured technology is the 4D Chart plug-in combined with the 4D Web Server's Non-Contextual request handling, aimed at developers who needed to publish data-driven or interactively built charts as part of a 4D-served web site without relying on the older contextual session model.

## Featured Technology
- 4D Chart (plug-in)
- 4D Web Server (Non-Contextual Mode)
- Graph serving (field-stored and interactive)

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note updates an earlier Tech Note (98-13) on serving 4D Chart graphs to the web, moving the technique from the original Contextual-Mode-only approach to 4D v6.5's newer Non-Contextual Mode web server. Both the 4D Chart plug-in and Contextual/Non-Contextual Mode web serving concepts it depends on have been fully discontinued or replaced in current 4D: 4D Chart was retired long ago, and 4D's own web serving strategy moved to REST/ORDA-based services, making the entire technique obsolete for present-day development.

**Related updates since:**
- The 4D Chart plug-in itself has been discontinued; charting today is typically handled via 4D View Pro or embedded JavaScript charting libraries in web front-ends
- 4D's web serving model has moved from Contextual/Non-Contextual Mode toward REST APIs built on ORDA, superseding this note's serving technique entirely

