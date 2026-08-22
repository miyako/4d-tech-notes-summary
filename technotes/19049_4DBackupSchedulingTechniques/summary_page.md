# Tech Note 01-50: 4D Backup Commands and Scheduling Techniques

**Author:** Not specified in source
**Published:** November 30, 2001 | **Product/Version:** 4D Backup v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=19049
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2001/windows/tn_2001_50-53_(nov)/01-50_4d_backup_scheduling.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> This technical note explains how to use 4D Backup commands in single user and multiple user databases. It demonstrates the basic use of the 4D Backup commands and a strategy on how to create a customer backup scheduler that can be used in 4D Client and 4D single applications. The purpose of this technical note is to give the reader a better understanding of how to work with the 4D Backup language commands. There will be no discussion about mirroring in this technical note.

## Key Points

Based on the available teaser text, this note is: a guide to using 4D's classic Backup commands to build a custom single- and multi-user backup scheduler.

## Featured Technology

- 4D Backup language commands
- 4D Client/4D Server backup scheduling
- Single vs multi-user backup

## Historical Context

Published November 2001 for 4D Backup v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note demonstrates using 4D's classic Backup language commands to build a custom backup scheduler for single-user and client-server databases, deliberately excluding mirroring. The core classic-language backup commands and the idea of scripting a custom backup schedule remain valid in current 4D versions, though 4D Server now ships with a more capable built-in Backup Manager/preferences UI, and many production deployments today also layer in infrastructure-level (disk/cloud) backup strategies alongside 4D's native mechanism.

**What has changed since:**

- 4D Server's Backup Manager and Backup.4DPreferences/XML configuration have matured considerably since 2001
- Cloud/infrastructure-level snapshot backups are now commonly used alongside or instead of purely classic-language backup scheduling
