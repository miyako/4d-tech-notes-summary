# Tech Note 01-15: The OPEN WEB URL Command

**Author:** Not specified in source document
**Published:** March 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13097
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_11-15_(MAR)/01-15_OPEN_WEB_URL.exe

## Overview
A walkthrough of the OPEN WEB URL command's ability to launch the default browser, mail client, or ftp/help handler for a given URL type. This Tech Note explains the OPEN WEB URL command, which connects to an external URL using whatever application the user's computer has configured as the default handler for that URL type.

## Key Points
- Beyond simple http/https links opened in a web browser, the note shows how the same command can be used to compose email messages via the user's default mail client (mailto: links), connect to ftp sites, and even open local HTML-based help pages installed on the user's computer — essentially any URL scheme with a registered default application.
- It carefully flags the prerequisite that the appropriate application must be installed and set as the default handler for each URL type used (e.g., a configured default web browser for http, a configured mail client for mailto), and notes that while multiple compatible applications can be installed, 4D will always defer to whichever one is set as the system default.
- The featured technology is this single, general-purpose command and the OS-level default-application resolution it relies on, aimed at developers who want to integrate seamlessly with whatever browser/mail/ftp tools an end user already has configured.

## Featured Technology
- OPEN WEB URL command
- Default application URL handling (http, mailto, ftp, file/help)

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Still relevant

This note documents the OPEN WEB URL command, which hands a URL of any supported scheme (http, mailto, ftp, local help files) off to the user's default registered application. The command itself remains part of 4D's current classic language essentially unchanged in purpose, and the general pattern of delegating URL handling to OS-level default applications is still exactly how modern operating systems work, making this note's core content still directly applicable today.

**Related updates since:**
- OPEN WEB URL remains a supported command in current 4D versions for launching URLs via the OS default application
- Default-application URL handling is now even more standardized across modern operating systems (deep links, custom URL schemes) than in the Mac OS 9 / Windows 98-2000 era this note targets

