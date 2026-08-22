# Tech Note 01-09: Importing From a Watched Folder

**Author:** Not specified in source document
**Published:** February 28, 2001 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12150
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_06-10_(FEB)/01-09_Watched_Folder_Import.exe

## Overview
A system for having 4D monitor (watch) a user-selected folder and periodically import or process its contents automatically. This Tech Note addresses a practical automation need: having a 4D application monitor, or 'watch,' a folder on a hard drive and periodically import or otherwise process whatever files appear inside it, without requiring manual intervention each time.

## Key Points
- It shows how, using just a handful of commands, developers can let end users choose which folder to monitor and then use one of 4D's background processes to perform the periodic checking and processing on an ongoing basis.
- The featured technology is 4D's classic process model combined with file-system enumeration commands, aimed at developers building semi-automated data ingestion pipelines — for example, watching a drop folder for new import files from an external system — a use case that remains common in business applications today.

## Featured Technology
- Folder monitoring (polling)
- 4D processes
- Automated document import

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Still relevant

This note builds a folder-watching system using 4D processes to periodically poll a user-chosen directory and import or otherwise process its contents — a pattern still very much in use for automated file ingestion today. The general architecture (a background process polling a folder on an interval) remains valid, though the specific file-system commands used to enumerate and select folders in this era have since been supplemented by 4D's more modern, object-oriented File and Folder classes, which offer richer, more portable file-system APIs than were available in 2001.

**Related updates since:**
- 4D's later File and Folder classes provide a more modern, object-oriented API for folder enumeration and monitoring than the raw commands available in this 2001-era note
- The core pattern of a background process polling a folder for automated import remains a standard architecture in current 4D applications

