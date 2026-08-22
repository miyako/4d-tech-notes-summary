# Tech Note: 4D Table Backups

**Author:** Not specified in source document
**Published:** June 4, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=14008
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_21-25_(MAY)/01-25_Contact_Manager_EDB_1.exe

## Overview
A cross-platform technique for backing up and restoring the contents of individual tables (or an entire database) using SEND RECORD and RECEIVE RECORD. This Tech Note addresses a common development-time need: the ability to back up the contents of one or several database tables so that data can be quickly and accurately restored after testing or after a coding error introduces bad data.

## Key Points
- Its solution builds on 4D's SEND RECORD and RECEIVE RECORD commands, which can save and reload the contents of records without the calling code needing detailed knowledge of the table or field structure, and which transparently handle 'fat' field types such as text and picture fields without any custom serialization code.
- The Tech Note packages these commands into a general, structure-agnostic implementation capable of backing up and restoring either individual tables or an entire database, and explicitly notes that the solution is cross-platform (Mac/Windows) by design.
- The featured technology is therefore centered on 4D's classic record-serialization commands rather than any UI or web feature, aimed at developers who want a lightweight, reusable backup safety net during active development rather than a full production backup strategy.

## Featured Technology
- SEND RECORD / RECEIVE RECORD commands
- Selective table backup and restore
- Cross-platform data serialization

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Superseded

This note builds a general-purpose selective backup/restore mechanism on top of 4D's SEND RECORD and RECEIVE RECORD commands, which serialize record contents (including 'fat' fields like text and pictures) independent of table/field structure knowledge. The core commands themselves are still part of 4D's classic language and technically still function, but for most practical backup/restore needs, developers today rely on 4D's native structured Backup/Restore feature, data export/import, or duplicating structures rather than hand-rolling table-level backup logic this way, making the specific implementation here a superseded pattern even though the underlying commands persist.

**Related updates since:**
- 4D's built-in Backup and Restore system (structured backup sets, log files, scheduled backups) is now the standard mechanism for full and partial data protection rather than custom SEND RECORD/RECEIVE RECORD scripts
- Modern data migration/export needs are often addressed with structured export formats (JSON, XML, CSV) rather than 4D's internal record-serialization commands

