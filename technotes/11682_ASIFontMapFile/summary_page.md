# Tech Note 96-03: Understanding the ASIFONT.MAP File

**Author:** Christopher Chapman
**Published:** January 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11682
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_01-05_(JAN)/96-03_ASIFONT.MAP.exe

## Overview
This Tech Note explains ASIFONT.MAP, the font-substitution lookup file that 4D for Windows uses to map Macintosh font names and font families onto their nearest Windows equivalents whenever a 4D database is ported from Mac to Windows. It covers the file's default contents and how to add custom font mappings for fonts not covered by the built-in table.

## Key Points
- The default ASIFONT.MAP contains entries such as `times(20):Times New Roman(Roman)`, `helvetica(21):Arial(Modern)`, `courier(22):Courier New(Modern)`, `geneva(3):MS Sans Serif(Swiss)`, and several others sufficient for most standard fonts.
- Custom font mappings are sometimes required, especially when a database uses non-standard/custom fonts.
- **Step 1:** Confirm the font is properly installed and prints correctly on both Macintosh and Windows.
- **Step 2:** On the Macintosh, use ResEdit on a copy of the System file to find the font's name and its FOND family resource ID number (e.g. Geneva = FOND ID 3).
- **Step 3:** On Windows, use a shareware utility or the Microsoft Windows SDK to inspect the `.FNT` file and determine the Windows font name and font family.
- **Step 4:** Combine the details into a single line of the format `Macintosh Font Name(FOND ID):Windows Font Name(Family Name)`, append it to ASIFONT.MAP with Notepad, and save.
- The ASIFONT.MAP file must reside in the same directory as `4D.EXE` to take effect.

## Featured Technology
- ASIFONT.MAP font-substitution lookup file
- Cross-platform (Macintosh-to-Windows) 4D database porting
- ResEdit (for inspecting classic Mac OS FOND font resources)

## Historical Context
Published in January 1996, this note reflects the reality of 4D's early cross-platform story, when 4D for Windows ran atop the Altura Mac2Win compatibility layer and font names/IDs had to be manually reconciled between the classic Mac OS's FOND-resource-based font system and Windows' font naming conventions. There was no shared, standardized font-naming or Unicode text layer between the two platforms at this time.

## Historical Commentary
**Status:** Obsolete

The entire ASIFONT.MAP mechanism — and the ResEdit-based FOND resource inspection process it depends on — is a product of a pre-Unicode, pre-TrueType-standardization era of cross-platform computing. Modern operating systems and current 4D versions rely on standardized font naming and Unicode-aware text handling, eliminating the need for a manual Mac-to-Windows font substitution table. ResEdit itself and classic Mac OS FOND resources have been obsolete for decades, and the Altura Mac2Win porting layer this note implicitly depends on is no longer part of any current 4D product.

