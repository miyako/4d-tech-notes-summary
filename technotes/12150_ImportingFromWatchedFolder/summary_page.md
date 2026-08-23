# Tech Note: Importing From a Watched Folder

- **Asset ID:** 12150
- **Tech Note #:** 01-09
- **Published:** February 28, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Steve Hussey
- **Page URL:** https://kb.4d.com/assetid=12150
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_06-10_(FEB)/01-09_Watched_Folder_Import.hqx

## Overview

Steve Hussey, CEO of Alto Stratus LLC, implements a background 4D process that periodically polls a user-selected folder, imports any tab-delimited text files it finds into database records, and deletes each file once processed — a self-contained pattern for automated, unattended file ingestion.

## Key Points

- Select folder("Select the watch folder.") lets the user choose which directory to monitor, with the chosen path saved into the [Util_Preference_Application] table via SAVE RECORD.
- The Import_Mgr project method runs in its own process (launched with New process, 32,000 bytes of stack) and loops with DELAY PROCESS($PID;$Delay)/RESUME PROCESS($PID), pausing roughly sixty seconds between cycles (a $Timeout counter caps the demo at five iterations).
- Each cycle launches a fresh Import process (New process("Import";32000;"Import")) rather than reusing one, favoring implementation simplicity over efficiency, as the note itself acknowledges.
- DOCUMENT LIST($Path;atext_Files) enumerates the watched folder's contents into an array; Find in array(atext_Files;"Icon@") locates and DELETE ELEMENT removes the Mac OS invisible folder-icon file before processing.
- Each file is opened in read-only mode (Open document($FullPath;"";Read Mode)) so other processes can still access it concurrently, its contents read via RECEIVE PACKET($DocID;$Text;32700), and parsed into an array of tab-delimited values using the STR_Txt2AryPrs helper method (passed the text, a pointer to the results array, and Char(Tab) as separator).
- One [Imported_Value] record is created per parsed value, storing the source Document name, a sequence Number, and the Value; after processing, CLOSE DOCUMENT then DELETE DOCUMENT permanently removes the source file.

## Featured Technology

- New process / DELAY PROCESS / RESUME PROCESS
- Select folder command
- DOCUMENT LIST
- Open document / RECEIVE PACKET / CLOSE DOCUMENT / DELETE DOCUMENT
- STR_Txt2AryPrs tab-delimited text parsing

## Historical Commentary

**Status:** Partially Superseded

Written by Steve Hussey, CEO of Alto Stratus LLC, this note builds a folder-watching system using a dedicated 4D process that periodically wakes via DELAY PROCESS/RESUME PROCESS to poll a user-chosen directory (set with Select folder) and import any tab-delimited text files found, using DOCUMENT LIST, Open document, and RECEIVE PACKET before deleting each processed file. The general architecture — a background process polling a folder on an interval to ingest files — remains a valid, still-used pattern today, though the specific low-level document/folder commands used here have since been supplemented by 4D's more modern, object-oriented File and Folder classes and folder-watching capabilities, which offer richer, more portable file-system APIs than were available in 2001.

**References to newer/updated information:**
- 4D's later File and Folder classes provide a more modern, object-oriented API for folder enumeration and file access than the raw DOCUMENT LIST/Open document commands used in this 2001-era note
- The core pattern of a background process polling a folder for automated import remains a standard architecture in current 4D applications
