# Tech Note 05-38: Mirroring in version 2004

**Author:** Kent Wilbur, Manager Information Systems, 4D, Inc.
**Published:** November 20, 2005 | **Product/Version:** 4D 2004 (2004.3) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=40491
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_37-39_(NOV)/Mirroring_2004.zip

## Overview
4D 2004.3 introduced two new language commands enabling database mirroring — keeping a second, identical database running in parallel so a failure can be recovered from in minutes by promoting the mirror. This note explains the commands and demonstrates a working mirroring system.

## Key Points
- Mirroring predates 2004 as a 4D Backup plug-in feature; 2004 initially shipped without it, and 2004.3 restored it via new commands, now supporting cross-platform mirror machines (the only hard requirement being that the mirror never independently modifies data).
- **New log file** function closes, renames, and creates a fresh segmented log file (e.g., `MyDatabase[0739-0001].4BL`) on the primary server, returning the path of the closed segment.
- **INTEGRATE LOG FILE** applies a transferred log segment on the mirror server.
- The example database transfers log segments to the mirror using a 4D SOAP call, chosen for simplicity and built-in success/failure reporting.
- Also demonstrates custom Client-Server communication for remotely modifying mirroring preferences stored in an XML preferences file.
- Explicitly framed as an introduction to the commands, not a turnkey production solution — developers must adapt it.

## Featured Technology
- 4D 2004.3 mirroring commands (New log file, INTEGRATE LOG FILE)
- Log file / segmented log file transfer
- 4D SOAP (custom client-server log transfer)
- XML-based preference storage

## Historical Context
Database mirroring as a concept remains part of 4D's architecture, but this note's DIY approach — hand-built SOAP transfer, manual log segment management, XML preference files — predates any later, more automated high-availability features 4D introduced. 4D SOAP itself reflects the SOAP-era web-services approach that has since given way to REST-based integration in modern 4D applications, making the specific implementation technique here largely superseded.
