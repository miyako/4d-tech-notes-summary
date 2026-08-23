# Tech Note: 4D and iCal

- **Asset ID:** 30140
- **Tech Note #:** 03-45
- **Published:** October 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac
- **Author:** Dave Dell'Aquila
- **Page URL:** https://kb.4d.com/assetid=30140
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_44-47_(OCT)/03-45_4D_and_iCal.hqx

## Overview

Dave Dell'Aquila, Senior 4D Evangelist, shows how 4D databases can interoperate with Apple's iCal calendaring application (new at the time on Mac OS X) by reading and writing the standard iCalendar (.ics) file format. The note surveys ways to publish iCal calendars (.Mac, iCal Exchange, or self-hosted via 4D WebSTAR V configured as a WebDAV server), then walks through 4D sample code — built around a line-by-line RECEIVE PACKET parsing loop — that turns .ics VEVENT blocks into 4D records and back again.

## Key Points

- Surveys three ways to publish an iCal calendar for others to subscribe to: a .Mac account, the free iCal Exchange third-party service, or self-hosting via 4D WebSTAR V configured as a WebDAV server
- Gives a concrete step-by-step for configuring 4D WebSTAR V's WebDAV support: subfolder on disk, Admin Client connection, realm setup, username/password, and authenticator selection
- Parses .ics files line-by-line using a RECEIVE PACKET($DocRef;$data;Char(10)) loop, matching BEGIN:VEVENT / END:VEVENT markers to know when inside an event block
- iCal_Data_To_Arrays extracts SUMMARY, DESCRIPTION, DTSTAMP, and UID content lines by locating the colon separator with Position(':';$Data) and taking the Substring after it
- Parses DTSTART/DTEND date-time values (YYYYMMDDTHHMMSS) into 4D date/time strings by substring-slicing year/month/day and reinserting colons into the time portion
- Describes the reverse process — writing Event records back out as BEGIN:VCALENDAR/BEGIN:VEVENT blocks and uploading them to a WebDAV server — for publishing 4D data as an iCal feed
- Suggests advanced applications such as triggering 4D BACKUP or a specific report print job from specially named iCal events ('Backup', 'Report:Sales1')

## Featured Technology

- iCalendar (.ics) file format / RFC 2445
- RECEIVE PACKET line-by-line parsing loop
- WebDAV publishing via 4D WebSTAR V
- RRULE recurrence rules
- DTSTART / DTEND / SUMMARY / UID content lines
- 4D WebMail iCal publishing

## Historical Commentary

**Status:** Still Relevant

The iCalendar (.ics) format is still a widely used, actively relevant standard today — Google Calendar, Outlook, and Apple Calendar all still speak it — so the core integration goal of this note remains valid. The specific 4D-side implementation, however, is dated: the manual RECEIVE PACKET line-parsing loop and hand-written substring date parsing shown here would today be handled more robustly with 4D's more capable text-processing and native date/time commands, and self-hosting WebDAV via 4D WebSTAR V is no longer a live recommendation since that product line has been retired.

**References to newer/updated information:**
- The iCalendar (.ics) standard remains in wide, active use across modern calendar applications
- 4D WebSTAR V, the WebDAV server used here for self-hosting calendars, has been discontinued; 4D's built-in web server and other modern hosting options would be used instead
- 4D has gained more capable text/string-parsing commands since 2003 that could simplify the manual line-by-line .ics parsing shown in this note
