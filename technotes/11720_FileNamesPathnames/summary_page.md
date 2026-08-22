# Tech Note 96-41: File Names and Pathnames

**Author:** ACI US Technical Support
**Published:** September 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11720
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_37-41_(SEP)/96-41_PathNames.exe

## Overview
This Technical Note explains the differing file-naming and pathname conventions between Windows and Macintosh circa 1996, then provides two reusable, platform-independent 4D utility routines for extracting a document's short name and pathname from a long file path.

## Key Points
- **Windows rules:** DOS limited names to 8 characters + ~3-character extension; Windows NT/95 supported up to 255 characters; paths use `DriveLetter:\Dir\...\Dir\`.
- **Macintosh rules:** Flat 31-character name limit regardless of OS version; paths use `VolumeName:Folder:...:Folder:`.
- **Example database ("Paths & Names"):** demonstrates opening a document and displaying its extracted name/pathname (noting Windows strips the extension from the "name"), and saving multiple numbered documents to a chosen folder.
- **Key commands/variables:** the `Document` process variable (returned by standard open/save dialogs) and `MAP FILE TYPES` (converts between Mac file types and Windows extensions).
- **Headline routines:** `Path to name` (extracts short document name, stripping the pathname and, on Windows, a 3-character extension) and `Path only path` (extracts everything up to and including the last path separator).
- **Caveat:** `Path to name` assumes 3-character Windows extensions and needs modification for shorter/longer extensions (e.g., `.c`).

## Featured Technology
- MAP FILE TYPES command
- Cross-platform file naming/pathname handling
- 4D Insider

## Historical Context
**Status:** Obsolete

This note's specific file-naming constraints — classic Mac OS's 31-character limit and DOS's 8.3 extension assumption — are entirely obsolete on modern operating systems, which support long file names uniformly on both Mac and Windows. The broader engineering discipline it demonstrates, writing platform-abstraction utility code so that cross-platform 4D applications behave consistently, remains a conceptually sound practice, even though 4D's current document- and path-handling commands have been substantially updated since 1996.
