# Tech Note 01-40: Preventing Web Users from Downloading Pictures

**Author:** Not specified in source
**Published:** August 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16393
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_36-40_(AUG)/01-40_Preventing_Picture_DL.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This Tech Note illustrates an interesting way of integrating 4D and JavaScript to prevent a user from downloading an image via the download command. However, other ways of saving pictures locally are available to the determined user.

## Key Points

Based on the available teaser text, this note is: a JavaScript/4D integration trick intended to discourage web users from downloading a displayed picture.

## Featured Technology

- 4D built-in Web Server
- JavaScript/4D integration
- Web area image protection

## Historical Context

Published August 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Obsolete**

This note demonstrates a JavaScript trick combined with 4D's web server to make it harder for a casual user to download an image via the browser's built-in download command, while acknowledging determined users could still save it another way. Browser technology, image-protection expectations, and 4D's own web-serving mechanisms have all changed enormously since 2001, and the specific JavaScript-era anti-download tricks shown no longer meaningfully deter modern browsers, so this note is now of historical interest only regarding actual image protection.

**What has changed since:**

- Modern image protection (if attempted at all) relies on very different techniques (watermarking, CSS overlays, server-side access tokens) than 2001-era JavaScript tricks
- Browsers have long since made client-side download-prevention tricks largely ineffective
