# Tech Note 05-18: cURL - HTTP Client, Get and Post, FTP and Much More, Using 4D 2004

**Author:** Not specified in available source
**Published:** May 10, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37215
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_17-20_(MAY)/05-18_cURL_and_4D_2004.exe

## Overview
This Tech Note shows how to control the cURL command-line tool from 4D 2004, using the newly introduced LAUNCH EXTERNAL PROCESS command, to add HTTP(S)/FTP(S) client capabilities (GET, POST, cookies, auth, form submission) to a 4D application.

## Key Points
- cURL is a free, open-source, cross-platform tool supporting HTTP(S) GET/POST, cookies, Referrer/User-Agent headers, authentication, and automatic web-form filling.
- It also supports FTP(S) and other protocols beyond HTTP.
- Requires no installation on Windows and is already present on Mac OS X.
- Controlled from 4D via the new LAUNCH EXTERNAL PROCESS command introduced in 4D 2004.

## Featured Technology
- cURL command-line HTTP/FTP client
- LAUNCH EXTERNAL PROCESS (new in 4D 2004)
- External-process-based integration pattern for adding networking capability to 4D

## Historical Context
**Status:** Superseded

Shelling out to cURL via LAUNCH EXTERNAL PROCESS was a clever and practical workaround in 2005 for 4D's lack of a built-in HTTP client, but 4D introduced native HTTP Client commands in 4D v13 (2012), making this specific workaround largely unnecessary for straightforward HTTP GET/POST needs today. LAUNCH EXTERNAL PROCESS itself, however, remains part of the current 4D language and continues to be a valid, commonly used technique for invoking other external command-line tools where no native 4D equivalent exists. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
