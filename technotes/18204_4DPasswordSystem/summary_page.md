# Tech Note 01-41: Understanding the 4D Password System

**Author:** Not specified in source
**Published:** September 30, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=18204
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_41-45_(SEP)/01-41_4D_Password_System.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The purpose of this technical note is to give you a better understanding of the 4D password system and how to use it. This Technical note will not cover the 4D password system and web services.

## Key Points

Based on the available teaser text, this note is: an explanation of how the classic 4D password and access-privileges system works.

## Featured Technology

- 4D password/access privileges system
- User and Group management

## Historical Context

Published September 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note explains the fundamentals of 4D's built-in password and access-privileges system (excluding its interaction with 4D's web services) as it existed in v6.7. The conceptual model of Users, Groups, and access privileges is still present in current 4D versions, but the underlying security mechanisms (password hashing, session/token-based web authentication) have been substantially strengthened and modernized since 2001, so the specific implementation details in this note are outdated even though the high-level concepts remain recognizable.

**What has changed since:**

- 4D's password hashing and storage mechanisms have been modernized considerably since the 2001 era
- Modern 4D web/REST authentication (session tokens, OAuth-style flows) is far more developed than the web-security model excluded from this 2001 note
