# Tech Note 01-26: Authenticating Access to a Secure Area within a Web Site

**Author:** Not specified in source document
**Published:** June 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=15345
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_26-30_(JUN)/01-26_Web_Authentication.exe

## Overview
A survey of approaches to gating access to a secure area of a 4D-served web site, including the built-in 4D password system and the On Web Authentication method. This Tech Note reviews several approaches, current as of 4D v6.7, to the common problem of restricting a portion of a web site to authorized users only.

## Key Points
- It uses the WebExam example database to illustrate one concrete implementation, and separately discusses techniques built around 4D's classic built-in password system (accounts and groups managed inside the 4D structure) as well as the On Web Authentication database method, a hook that lets a database method intercept and validate web authentication requests before granting access.
- Because this predates any modern token-based or HTTPS-session-cookie authentication pattern, the note's solutions are necessarily built entirely on 4D's own Contextual Mode web server session handling of the period.
- The featured technology is thus a combination of the 4D Web Server's session/authentication hooks, the classic password system, and example-database-driven illustration, aimed at developers building password-protected sections of an otherwise public 4D web site during the dot-com-era rise of 4D-based web publishing.

## Featured Technology
- 4D Web Server (Contextual Mode)
- 4D password system (built-in user/group accounts)
- On Web Authentication database method
- WebExam example database

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note surveys techniques for restricting access to portions of a 4D-served web site circa 2001, centered on 4D's then-current Contextual Mode web server, the classic built-in 4D password/account system, and the On Web Authentication database method. The general problem — gating access to protected web resources — is timeless, but every specific mechanism described (4D's classic password system, Contextual Mode session handling, On Web Authentication) has been superseded by modern web authentication approaches (HTTPS, session tokens/JWT, REST-based APIs) and by 4D's own move away from Contextual Mode web serving toward REST/ORDA-based web services, making this note obsolete as a practical recipe today.

**Related updates since:**
- 4D's web serving model has shifted decisively from Contextual/Non-contextual Mode to REST APIs built on ORDA plus modern client-side frameworks
- Web authentication today is typically implemented via HTTPS session cookies, tokens (JWT/OAuth), or platform identity providers rather than 4D's classic built-in password/account system
- 4D's built-in password system itself has evolved considerably since this era with stronger hashing and session management options

