# Tech Note: Talking 'Trash' – Understanding the Trash and the Recycle Bin

- **Asset ID:** 13194
- **Tech Note #:** 01-19
- **Published:** April 30, 2001
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Steve Hussey
- **Page URL:** https://kb.4d.com/assetid=13194
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_16-20_(APR)/01-19_Talking_Trash.hqx

## Overview

Steve Hussey (CEO, Alto Stratus LLC) explains how to give users a way to recover documents that a 4D database has processed, instead of permanently destroying them with `DELETE DOCUMENT`. The note shows how to determine the OS-specific path to the Mac OS Trash or Windows Recycle Bin and how to move a document into it, handling the platform differences in path delimiters, folder naming, and collision behavior.

## Key Points

- The `TRSH_Find` function uses `PLATFORM PROPERTIES($OS_Platform)` to branch: on Mac OS it takes `System folder(0)`, finds the volume name before the first colon, and appends `"Trash:"`; on Windows it finds the volume before the first backslash and appends `"Recycled\"`.
- On Windows 98 (still MS-DOS based), the Recycle Bin's actual on-disk directory is named `RECYCLED`, and files moved into it are renamed to short DOS-compatible names like `DC0`, `DC1.MP3`, `DC2.PDF`, with Windows maintaining an internal link back to the original names.
- On Mac OS, moving a file into the Trash can fail if a file of the same name already exists there, so the note uses `Test path name` to check for a collision and `DELETE DOCUMENT` on the existing Trash copy before calling `MOVE DOCUMENT`; on Windows no such check is needed since renamed files can't collide.
- `HFS_FileNameFromPath` extracts just the file name from a full path by choosing the platform delimiter (`:` on Mac OS, `\` on Windows), splitting the path into an array with `STR_Txt2AryPrs`, and returning the last array element.
- `DOCUMENT LIST(◊text_PathToTrash;scrl_Trash)` lists the current contents of the Trash/Recycle Bin, working identically on both platforms.
- The demo screen lets the user choose a file, then either delete it outright (with a confirmation dialog), move it to the Trash/Recycle Bin, or list the Trash/Recycle Bin's current contents; the author notes the code may need adjustment on Windows NT/2000.

## Featured Technology

- PLATFORM PROPERTIES command
- System folder path parsing (Trash / Recycle Bin path construction)
- MOVE DOCUMENT as a DELETE DOCUMENT alternative
- Test path name for collision detection
- DOCUMENT LIST for directory listing
- Cross-platform path delimiter handling (: vs \)

## Historical Commentary

**Status:** Obsolete

Steve Hussey's note explains how to derive the OS-specific path to the Mac OS Trash or Windows Recycle Bin from the System folder path, then use MOVE DOCUMENT instead of DELETE DOCUMENT so that processed files can still be recovered by the user afterward, with platform-specific handling for name collisions (Mac) versus DC0/DC1-style renaming (Windows). The underlying need -- giving users an undo path instead of permanently deleting files -- is still a sound pattern today, but the specific paths and OS internals described (classic Mac OS's colon-delimited Trash, Windows 98's DOS-era RECYCLED directory) are entirely obsolete, and 4D's later File/Folder class-based APIs offer a far more modern, higher-level way to do this kind of file-system interaction than manually parsing System folder() paths.

**References to newer/updated information:**
- 4D's later File and Folder classes provide higher-level, more portable file-system operations than manually constructing OS-specific Trash/Recycle Bin paths
- Both macOS and Windows have completely changed their trash/recycle-bin storage locations and internal implementations since the Mac OS 9 / Windows 98 era this note describes, so any hardcoded paths shown here no longer apply
