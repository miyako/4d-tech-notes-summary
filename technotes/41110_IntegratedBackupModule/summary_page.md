# Tech Note 05-46: 4D 2004 Integrated Backup Module

**Author:** Yvan Ayaay, Technical Support Engineer, 4D, Inc.
**Published:** December 22, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41110
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-46_Integrated_Backup.zip

## Overview
Backup and restore, previously handled by the separate 4D Backup plug-in, were integrated directly into 4D 2004 (4th Dimension and 4D Server). This note walks through configuring and triggering the new integrated module manually, automatically, and programmatically.

## Key Points
- **Backup Settings:** general options (keep last N backups, skip unmodified data, transaction/failure handling policies) and Archive options (segmenting, compression, optimization/redundancy).
- **Configuration Settings:** what's included in a backup (structure file, data file, extra files/folders), destination folder, last-backup info, and log file management.
- **Three trigger methods:** manual (File menu), automatic (Scheduler page, with flexible hour/day/week frequency), and programmatic (the Backup command plus On Backup Startup/Shutdown Database Methods).
- **Log file:** records all data changes and transactions after a full backup, enabling incremental recovery.
- **Automatic restore:** can detect database damage, restore the last backup, integrate the last log file, and relaunch the database without user intervention.

## Featured Technology
- 4D 2004 integrated Backup/Restore module
- Backup preferences (General Settings, Archive, Scheduler)
- Log file / Backup Journal
- Backup command, On Backup Startup/Shutdown Database Methods

## Historical Context
This note captures a genuine architectural shift for 4D — moving backup/restore from an external plug-in into the core application in 4D 2004. The fundamental concepts (structure+data backups, log-file-based incremental recovery, a scheduler) remain the backbone of 4D's backup system today, but the specific preferences dialogs and exact command set shown have been refined across many subsequent 4D releases, so developers should treat this as a historical snapshot of the *first* implementation rather than a current how-to.
