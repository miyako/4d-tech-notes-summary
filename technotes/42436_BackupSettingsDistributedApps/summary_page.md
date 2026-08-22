# Tech Note 06-13: Backup Settings for Distributed Applications

**Author:** Jean-Yves Fock-Hoon, QA Manager, 4D Inc.
**Published:** March 31, 2006 | **Product/Version:** 4D Backup v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42436
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_09-13_(MAR)/06-13_Backup_Settings.zip

## Overview
This note solves a common distributed-application deployment problem: a Backup.XML file created during development bakes in a machine-specific backup destination path, causing an unwanted "select a folder" dialog when the built application runs on another machine for the first time. It presents a templating approach to pre-seeding custom backup settings without this problem.

## Key Points
- **The problem:** testing 4D Backup on a dev machine auto-creates a Backup.XML file with a hard-coded local destination path; moving the built application elsewhere invalidates that path, and 4D forces a folder-picker dialog before it can proceed.
- **Simplest fix (default settings only):** don't copy Backup.XML when deploying — 4D will regenerate a fresh default file with no path conflict, but this forfeits any custom backup settings (archive retention, extra files, scheduling, etc.).
- **Two ways to pre-seed custom settings:** (1) building the XML directly via 4D's native XML-parsing commands, which is workable but brittle since it must track any future changes to 4D Backup's XML schema; (2) the recommended approach — maintain a Backup.XML2 template file using 4D HTML/merge tags, processed at startup with `PROCESS HTML TAGS`, then saved as the live Backup.XML.
- **Deployment workflow:** copy Backup.XML2 (not Backup.XML) to the built application; in `On Startup`/`On Server Startup`, locate the Preferences folder via the Extras folder path (`Get 4D folder`), use `Test path name` to check whether Backup.XML already exists, and if not, either silently generate it, prompt for a destination folder, or show a full Advanced Backup Settings dialog (a working example is included in the sample database).
- **Complete settings reference:** the note tabulates every settings variable (e.g., `BKP_at_CompressionRate`, `BKP_rbSched_Weeks`) against its Backup.XML tag (e.g., `<CompressionRate>`, `<Weekly>`), covering retry/timeout, restore/log-integration automation, compression/redundancy/interlacing/segment sizing, included files, destination folder, and hourly/daily/weekly/monthly scheduling.

## Featured Technology
- 4D Backup system and its Backup.XML project file format
- `PROCESS HTML TAGS` command for template-based XML generation
- `On Startup` / `On Server Startup` database methods
- `Get 4D folder` and `Test path name` commands for locating/checking Preferences files
- 4D's native XML-parsing commands (presented as the less-preferred alternative)

## Historical Context
Published in 2006 for 4D v2004/4D Backup, this note predates 4D's SQL engine (v11, 2007), Project Mode (2018), and ORDA. 4D Backup, 4D Write, 4D View, and similar companion products of this era have all evolved substantially since (e.g., 4D Write Pro in 2016, 4D View Pro in 2018), and backup/preferences file handling in current 4D releases should be checked against up-to-date documentation.

## Historical Commentary
**Status:** Superseded

The templating pattern this note demonstrates — maintaining a merge-tag template file processed at startup rather than hard-coding XML-building logic — is a genuinely useful, still-instructive software engineering technique that would translate to many configuration-file scenarios today. However, it is entirely built around 4D Backup's classic Backup.XML project file schema and startup-method conventions from the 4D 2004 era, so the specific variable/tag mappings and file-location logic described should be re-verified against current 4D Backup and 4D Server documentation before being applied to a modern application.
