# Tech Note 04-07: 4D, iCal and Web Services

**Author:** Not specified in source teaser
**Published:** February 19, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=31358
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_05-09_(FEB)/04-07_iCal_Web_Services.exe

## Overview
This Tech Note shows how to schedule an iCal calendar event that triggers an AppleScript, which in turn communicates with a 4D database via 4D's SOAP Web Services — using calendar events as automation triggers for 4D business logic.

## Key Points
- 4D 2003 added Web Services support, allowing 4D methods to be called remotely.
- iCal 1.5.1 (Apple's built-in calendar app) gained the ability to trigger AppleScripts from calendar events.
- The latest AppleScript version at the time added support for calling Web Services directly.
- Combines these to let a scheduled iCal event execute an AppleScript that calls into 4D via Web Services.
- Outlines a few illustrative scenarios showing how the pattern could be applied.

## Featured Technology
- Apple iCal (calendar automation trigger)
- AppleScript (with Web Services calling support)
- 4D Web Services (SOAP)

## Historical Context
Only the on-page teaser paragraph for this asset could be recovered (the full archived PDF was not accessible in this environment), so this summary reflects only the note's stated scenario, not its exact AppleScript/4D code. Every specific technology named here is dated: Apple's original iCal app was eventually renamed/evolved into Calendar, that specific AppleScript Web Services feature is a niche legacy automation path, and 4D's SOAP Web Services have since been superseded by REST/JSON approaches. The broader idea of driving 4D logic from calendar-based or external automation triggers remains conceptually relevant, but essentially none of this note's specific technology stack is in active use today.
