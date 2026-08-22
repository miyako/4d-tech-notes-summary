# Tech Note 05-16: Handling Pictures

**Author:** Not specified in available source
**Published:** April 25, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37047
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_12-16_(APR)/05-16_Handling_Pictures.exe

## Overview
This Tech Note explains how 4D reads and displays native picture formats (PICT, BMP, GIF, JPEG, PSD, PSP) via QuickTime, and shows how to use PICTURE TO BLOB to convert a picture between formats in order to manipulate its raw bytes directly.

## Key Points
- READ PICTURE FILE and SAVE PICTURE TO FILE rely on QuickTime to support the range of "standard" picture formats of the era.
- A picture file, like any file, is fundamentally a sequence of bytes; knowing the native format lets you read/create at the byte level and apply direct transformations.
- Distinguishes between a picture's original format and a working format chosen for editing/transformation.
- PICTURE TO BLOB converts a picture to and from QuickTime-supported formats, enabling byte-level manipulation.

## Featured Technology
- READ PICTURE FILE / SAVE PICTURE TO FILE commands
- PICTURE TO BLOB command
- QuickTime-based picture format conversion engine
- Byte-level (BLOB) picture data manipulation

## Historical Context
**Status:** Obsolete

This note's picture-format-conversion technique depended entirely on Apple's QuickTime framework, which Apple has since fully discontinued (including QuickTime for Windows, around 2016), making the specific mechanism described here non-functional in any current environment. 4D itself moved away from a QuickTime dependency for picture handling in later versions, introducing native picture format support that doesn't require QuickTime to be installed. PICTURE TO BLOB remains part of the current 4D language for byte-level picture access, but the underlying format-conversion pathway this note describes is obsolete. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
