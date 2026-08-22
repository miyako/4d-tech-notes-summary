# Tech Note 96-41: Developing with 4D Server Part 3: Naming Conventions for Multi-Developer 4D Projects

**Author:** ACI US Technical Support
**Published:** August 1, 1996 | **Product/Version:** 4th Dimension v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11701
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_38-41_(AUG)/96-41_File_Names_Pathnames.exe

## Overview
Despite the title supplied with this note's metadata, its actual published content — titled "File Names and Pathnames" — covers platform-independent routines for extracting a file name from a full pathname string on Mac vs. Windows, plus the MAP FILE TYPES command for cross-platform document type association.

## Key Points
- **Platform path differences:** Mac OS uses colon-delimited HFS paths while Windows uses backslash-delimited paths, requiring platform-aware parsing logic.
- **Custom utility methods:** "Path to name" and "Path only path" routines split a full pathname string into its filename and containing-folder-path components, working correctly regardless of originating platform.
- **Era constraint:** DOS's 8.3 filename length limit had to be accounted for when documents moved between Mac and Windows systems.
- **MAP FILE TYPES command:** associates a Mac file's type/creator codes with a Windows file extension (and vice versa) so cross-platform documents are recognized correctly.
- **Example database:** demonstrates the routines via "Save Multiple" and "Test One Document" menu commands for hands-on testing.

## Featured Technology
- Path to name / Path only path global functions
- MAP FILE TYPES command
- Cross-platform (Mac/Windows) document naming and pathname conventions

## Historical Context
The manual pathname-parsing routines and legacy filename-length constraints (like DOS's 8.3 limit) documented here are obsolete: modern operating systems universally support long file names, and modern 4D ships built-in File and Folder objects with higher-level path manipulation methods, eliminating the need for hand-written pathname-parsing utilities like the ones presented. The MAP FILE TYPES cross-platform document-type concern is likewise far less prominent today given modern OS and file-manager improvements in recognizing file types across platforms.
