# Tech Note 99-47: Building Interactive Graphic Interfaces with 4D Draw, Part II

**Author:** Not specified
**Published:** November 1, 1999 | **Product/Version:** 4D Draw v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11878
**Download:** https://kb.4d.com/f/DLTN/TN/1999/Windows/TN_1999_47-50_(NOV)/99-47_Graphic_Interfaces_2.exe

## Overview
This is Part II of a multi-part series on building interactive graphic interfaces with 4D Draw. While Part I covered creating 4D Draw vector graphics and converting bitmap images, Part II focuses on the code of the example database, specifically the validation of BMP pictures before they are processed for bitmap-to-vector tracing.

## Key Points
- Continues from Part I's explanation of creating 4D Draw vector graphics for interactive interfaces
- Focuses on BMP document validation: confirming the file is in the correct format before processing
- Uses the "v65Trace" example database which features four main functions: Convert Picture to BMP, BMP Picture Properties, Trace BMP Picture, and 4D Draw Window
- Emphasizes robust input validation to prevent errors during the tracing process

## Featured Technology
- 4D Draw (plug-in for vector graphic manipulation)
- BMP file format parsing and validation
- Bitmap-to-vector conversion techniques
- ACI_Pack plug-in commands

## Historical Context
**Status:** Obsolete

This note is part of the 4D v6.5 era (1999) and relies entirely on 4D Draw, a plug-in that has been discontinued from the 4D product line. The full PDF archive was stored as a Windows self-extracting .exe installer and could not be extracted in this environment (error: NO_PDF_IN_ARCHIVE_TEASER_ONLY), so only the on-page teaser text is available. The BMP validation and bitmap-to-vector concepts are historically interesting as examples of creative low-level programming within the 4D language, but modern developers would use built-in image handling, SVG support, or external graphics libraries rather than manual BLOB-level BMP parsing.
