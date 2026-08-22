# Tech Note 01-19: Talking 'Trash' – Understanding the Trash and the Recycle Bin

**Author:** Not specified in source document
**Published:** April 30, 2001 | **Product/Version:** 4D | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13194
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_16-20_(APR)/01-19_Talking_Trash.exe

## Overview
A technique for locating the Trash (Mac OS) and Recycle Bin (Windows) folders and moving processed documents into them instead of permanently deleting them with DELETE DOCUMENT. This Tech Note addresses a common file-management concern in 4D applications: many databases manipulate external documents and, once processing is complete, simply delete them using the DELETE DOCUMENT command — an operation that cannot be undone.

## Key Points
- As an alternative, the note proposes moving those documents into the operating system's Trash (on Mac OS) or Recycle Bin (on Windows) instead, so that they can be retrieved later if a mistake is made.
- It walks through how to determine the correct platform-specific paths to these special folders/directories, and how to programmatically move a document into them rather than deleting it outright.
- The featured technology is cross-platform file-system path resolution and document manipulation in classic 4D, aimed at developers who want a safer, more forgiving document-deletion workflow for end users.

## Featured Technology
- Trash (Mac OS) / Recycle Bin (Windows) paths
- DELETE DOCUMENT alternative
- Cross-platform document management

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Partially_superseded

This note explains how to determine the OS-specific paths to the Trash (Mac OS) and Recycle Bin (Windows) and move documents there instead of permanently removing them with DELETE DOCUMENT, giving users a way to recover accidentally processed files. The underlying need — moving files to the OS trash rather than permanently deleting them — remains a legitimate pattern today, and the general approach is still conceptually sound, but 4D's later File/Folder object-oriented classes (introduced well after this note) provide more modern, higher-level APIs for this kind of file-system interaction than the raw path-construction technique shown here.

**Related updates since:**
- 4D's later File and Folder classes (introduced in more recent 4D versions) offer higher-level, more portable file-system operations than manually constructing OS-specific Trash/Recycle Bin paths
- Both macOS and Windows have evolved their trash/recycle-bin storage locations and APIs considerably since Mac OS 9 / Windows 98-2000, so any hardcoded paths from this note would need updating regardless

