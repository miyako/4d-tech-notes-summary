# Tech Note 04-50: Working with 4D and iCalendars

**Author:** Frank Chang, 4D Evangelist
**Published:** December 16, 2004 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=35197
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_49-50_(NOV)/04-50_4D_and_iCalendars.zip

## Overview
This note explains how to use 4D 2004 to act as a data-driven iCalendar/WebDAV server, allowing calendar client applications (Apple iCal, Microsoft Outlook, Mozilla Firefox's Calendar extension) to subscribe to and publish calendar events stored as native 4D data, rather than treating iCalendar only as a static import/export format.

## Key Points
- Reviews the iCalendar (.ics) file format per RFC 2445: VCALENDAR/VEVENT/VALARM component structure.
- 4D acts as a WebDAV server, handling client Get/Put/Delete-style requests for calendars.
- Uses new 4D 2004 commands GET HTTP HEADER, GET HTTP BODY, and SEND HTTP RAW DATA to work directly with raw HTTP traffic.
- HTTP Basic authentication credentials are extracted and Base64-decoded inside `On Web Authentication`.
- iCalendar files are built entirely in memory as BLOBs (never written to disk) and streamed back to clients.
- Incoming iCalendar text is chunked into a text array to handle payloads larger than 32K before being parsed into 4D records.
- Cross-references an earlier note (03-45) covering the reverse direction: parsing iCalendar files into 4D data.

## Featured Technology
- iCalendar format (RFC 2445)
- 4D Web Server used as a WebDAV server
- GET HTTP HEADER / GET HTTP BODY / SEND HTTP RAW DATA
- On Web Authentication database method
- BLOB-based in-memory file construction, Base64 decoding

## Historical Context
Published at the height of desktop calendar client adoption (iCal, Outlook, early Firefox Calendar extension), this note captures a pre-CalDAV moment when developers had to hand-build WebDAV semantics and raw HTTP handling to integrate 4D with calendar clients. CalDAV (RFC 4791) was standardized a few years later (2007), formalizing much of what this note improvises, and modern calendar integrations overwhelmingly use REST/JSON APIs instead of hand-rolled WebDAV blob serving. The HTTP-level commands referenced still exist in current 4D, but this specific architecture is now a historical curiosity rather than a recommended pattern.
