# Tech Note 07-43: 4D v11 SQL Maintenance and Security Center

**Author:** Jason T. Slack, Technical Support Engineer, 4D Inc.
**Published:** November 14, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=48064
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_42-45_(NOV)/07-43_4Dv11SQL_MSC.pdf

## Overview
This note introduces the Maintenance and Security Center (MSC), 4D v11 SQL's new consolidated interface for repairing, maintaining, and reporting on database structure and data files, replacing several previously separate tools.

## Key Points
- MSC sections: Information, Activity Analysis, Verify, Backup, Compact, Rollback, Restore, Repair.
- Consolidates the old "About" dialog, Open Database dialog features, backup preferences, and the entire standalone 4D Tools application (which no longer exists as of 4D v11 SQL).
- **Standard Mode:** database opens normally, Design/Application environments remain accessible; only Information, Activity Analysis, Verify, Backup, and Restore are available.
- **Maintenance Mode:** required for Compact, Rollback, and Repair; Design/Application access is blocked; entered automatically if the structure/data file is damaged.
- Ways to invoke MSC: Help menu, MSC toolbar button (Design mode), custom "Open MSC" menu action, `OPEN SECURITY CENTER` command, or the OS-level file-open dialog.
- Compact/Repair/Rollback/Restore are restricted to Administrator or Designer accounts.
- Information page: Program/Tables tabs mirror the old About box; new Data/Structure tabs graphically show file space usage (used vs. free) with warning icons; Structure tab is available only in 4D Developer and 4D Server.

## Featured Technology
- Maintenance and Security Center (MSC)
- `OPEN SECURITY CENTER` command
- Database Verify/Backup/Compact/Rollback/Restore/Repair operations
- Replacement of the standalone 4D Tools application

## Historical Context
Published alongside 4D v11 SQL's broader overhaul introducing the native SQL engine, this note documents a significant consolidation of 4D's database administration tools into a single, mode-aware interface — a design that persisted (in evolved form) through many subsequent 4D versions, well before Project Mode or ORDA existed.

## Historical Commentary
**Status:** Superseded

The MSC concept, its standard/maintenance mode split, and the `OPEN SECURITY CENTER` command remain part of 4D's toolset in spirit, so this note's high-level structure is still useful background. However, the actual MSC interface has been revised multiple times in the years since 2007, so specific screens, tabs, and workflows described here should be expected to differ from the MSC found in current 4D versions.
