# Tech Note 01-25: Contact Manager, Behind the code, Part I

**Author:** Not specified in source document
**Published:** June 4, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=14010
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_21-25_(MAY)/01-25_Contact_Manager_EDB_1.hqx

## Overview
A walkthrough of the forms and code behind the Calendar interface in 4D's Contact Manager example database (Part I of a two-part series). This Tech Note is the first of a planned two-part series examining the internals of 4D's Contact Manager example database, an application distributed to illustrate useful interface design and programming techniques.

## Key Points
- Part I focuses specifically on the Calendar interface: the forms and underlying method code that render and drive the calendar view within Contact Manager.
- The note is explicitly a code tour rather than a general-purpose technique guide — its value lies in exposing how a real, polished sample application handled a non-trivial UI component (a calendar) using period 4D tools.
- A planned second Tech Note (not part of this entry) was to cover how user interactions on that same Calendar form are managed.
- As a companion piece to a specific downloadable sample database rather than an independent technical topic, its featured technology is essentially "Contact Manager itself" — classic 4D form and method programming as applied to a calendar UI, offered to developers looking for concrete, real-world examples of interface construction from that era.

## Featured Technology
- Contact Manager example database
- Calendar form/interface design
- Classic-language form programming

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the original ftp download link for the full Tech Note and example database is dead, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Historical interest only

This is a code-walkthrough companion to 4D's Contact Manager example database, focused specifically on how its Calendar interface was built in classic-language, binary Design Mode forms circa 2001. As a documentation piece about a specific vintage sample application rather than a generalizable 4D feature, it is now chiefly of historical interest: the Contact Manager sample itself and its Design-Mode calendar-building techniques predate decades of subsequent UI/UX evolution in 4D (including calendar-oriented list box features and Project Mode), so it offers little direct practical value to a modern developer beyond illustrating period programming style.

**Related updates since:**
- 4D has since introduced richer native list box and form object capabilities that make hand-built calendar-grid interfaces like this one largely unnecessary
- The specific Contact Manager sample database referenced is no longer part of 4D's current example/download library

