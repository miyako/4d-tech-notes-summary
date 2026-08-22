# Tech Note 05-17: Upgrading Older Databases

**Author:** Daniel Do, Technical Support Engineer, 4D, Inc.
**Published:** May 5, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37172
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_17-20_(MAY)/05-17_Upgrading_Older_DBs.pdf

## Overview
This Tech Note is a detailed, practical guide for upgrading very old 4D databases (version 2 through 6.x, originally run on classic Mac OS 8.6/9) forward to 4D 2003 or 2004, covering tooling, legacy plug-in/external removal, platform transport, and data recovery.

## Key Points
- General upgrade principles: jump straight to the target version when possible, delay any Mac→Windows platform change until last, never run very old 4D on newer operating systems, and always back up (compressed) before starting.
- Pre-3.2-era "externals" (predecessor to plug-ins) must be manually removed using ResEdit and/or the External Mover utility before upgrading; specific Mac resource types (4BND, 4BNX, 4Dte, STR#, THM#, FON#, CURS) are identified and explained.
- 4D Transporter is required to move pre-2004 databases from Mac to Windows.
- A full worked example walks through upgrading a corrupted version 2 database: changing Mac creator/type codes, opening in successive demo-mode 4D versions to convert structure/data files, and using 4D Tools' recover-by-tag to fix corruption.
- A troubleshooting section catalogs common problems: data corruption (recover by tag), structure corruption (repair via 4D Tools or isolate via fresh data file test), and form/object corruption (resave or copy-paste affected objects).

## Featured Technology
- 4D version 2/3/6.x → 2003/2004 upgrade path
- ResEdit (Mac OS 9 resource editor) and External Mover utility
- 4D Transporter (Mac-to-Windows database transport)
- 4D Tools recover-by-tag data recovery
- Mac file creator/type code conventions per 4D version
- Legacy externals/plug-in resource types (4BND, 4BNX, 4Dte, STR#, THM#, FON#)

## Historical Context
**Status:** Historical interest only

Virtually every specific tool and environment this note relies on — ResEdit, Mac OS 9/Classic, 4D Transporter, and the exact version 2 through 6.8 upgrade chain — has been discontinued for many years and cannot run on any current hardware or OS, and any database still requiring this specific migration path would have needed to complete it roughly two decades ago. 4D has since undergone far larger structural changes of its own, most notably the introduction of Project Mode (v17, 2018), which replaced the binary structure file model this note assumes entirely. The note's general principles (always back up before upgrading, use recover-by-tag for corruption, isolate structure vs. data issues) remain sound engineering practice, but its concrete instructions are strictly of historical interest today.
