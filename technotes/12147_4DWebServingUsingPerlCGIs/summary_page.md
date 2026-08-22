# Tech Note 01-07: 4D Web Serving Using Perl CGIs

**Author:** Not specified in source document
**Published:** February 28, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12147
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_06-10_(FEB)/01-07_Using_Perl_CGIs.exe

## Overview
A demonstration of integrating Perl CGI scripts with 4D's v6.7 web server to perform tasks (hit counters, guestbooks, form processing) not otherwise possible with 4D alone. This Tech Note explains how, starting with the release of 4D v6.7, 4D's web serving gained the ability to invoke CGIs (Common Gateway Interface scripts), a capability not available in earlier versions.

## Key Points
- It draws an explicit analogy between CGIs for web servers and plug-ins for 4D methods: both are called by their respective host (the web server or 4D) to perform a task and return an answer, which can be either a complete page or an HTML fragment inserted into the page 4D ultimately serves.
- CGIs of this era were frequently used for things like hit counters, guest books, and question/answer forms — tasks the note frames as the main reason to reach for a CGI: accomplishing something that 4D itself could not do directly.
- The sample database accompanying the note demonstrates five separate Perl CGI scripts, and while the author acknowledges some of them aren't examples of everyday practical use, their purpose is purely illustrative — showing how Perl CGIs can be invoked from 4D v6.7 via HTML tags, and where the CGI files need to be located on disk.
- The featured technology is therefore CGI/Perl integration with 4D's classic web server, representative of the broader late-1990s/early-2000s pattern of extending web servers with external scripting languages.

## Featured Technology
- CGI (Common Gateway Interface)
- Perl scripts
- 4D Web Server (v6.7 CGI integration)

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note demonstrates 4D v6.7's newly added ability to call external Perl CGI scripts from its web server, using five sample scripts (hit counters, guestbooks, form-processing) to show how CGI extends what 4D's own web-serving tags could do. CGI-based web architecture — spawning a separate script process per request — is now a largely obsolete pattern industry-wide, having been superseded first by application servers and now by REST APIs and modern back-end frameworks, and 4D itself no longer needs a CGI bridge for the kinds of tasks this note demonstrates, since its own language and web capabilities (and REST/ORDA) have absorbed most of that functionality directly.

**Related updates since:**
- CGI-based web integration has been broadly obsoleted industry-wide by application servers and REST APIs
- 4D's own web server and REST/ORDA capabilities now cover most of the task categories (form processing, dynamic content generation) that once required bridging out to external CGI scripts like Perl

