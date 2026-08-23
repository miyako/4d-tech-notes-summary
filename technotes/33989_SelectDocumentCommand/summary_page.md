# Tech Note: Using Command Select Document (2004)

- **Asset ID:** 33989
- **Tech Note #:** 04-37
- **Published:** September 16, 2004
- **Product / Version:** 4th Dimension 2004
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=33989
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_36-40_(AUG)/04-37_Select_Document.hqx

## Overview

Written by Jamras Komoncharoensiri, this note introduces Select document, a command new to 4D 2004 that replaced older file-selection approaches with a single, far more capable command for prompting users to choose files. The note documents the full syntax -- Select document(directory; fileTypes; title; options{; selected}) -- and walks through its parameters, including directory access paths (or a memorized path number), semicolon-delimited file-type filters, and a bitwise options parameter built from the constants Multiple files (1), Package open (2), Package selection (4), Alias selection (8), and Use Sheet Window (16). Six worked examples progressively demonstrate opening the dialog at a specific starting directory, filtering by file type (noting the differing Mac/Windows filter behavior), enabling multiple selections, allowing selection of aliases, and, on Mac OS X only, allowing selection of packages/bundles or items inside them by combining the Package and Alias option constants. The note closes by noting the command's flexibility comes entirely from combining these option constants.

## Key Points

- Select document(directory; fileTypes; title; options{; selected}) -> String returns the selected file path and can also populate an array of selected paths.
- The directory parameter accepts a path string, an empty string for the platform default (Documents on Mac OS X / My Documents on Windows), or a memorized access-path number.
- fileTypes is a semicolon-delimited filter list (e.g. "JPEG;TEXT"); adding * lets the user optionally reveal all files.
- The options parameter is a bitwise combination of Multiple files (1), Package selection (2), Alias selection (8), and Use Sheet Window (16) constants.
- Multiple files enables multi-selection with results returned in the arrDocument array parameter.
- Package selection and Package open are Mac OS X-only options for choosing a package (bundle) itself, or an item located inside one.
- Combining Package selection with Alias selection lets users select an alias pointing to a package and resolves to the absolute path of the package or its contents.

## Featured Technology

- Select document command (4D 2004)
- File-type filtering in file selection dialogs
- Multiple files / Alias selection / Package open / Package selection option constants
- Mac OS X package (bundle) selection

## Historical Commentary

**Status:** Partially Superseded

This note documents Select document as a genuinely new and more capable file-selection command for 4D 2004, and the command has remained part of the 4D classic language essentially unchanged in concept, so the core technique -- building an options bitmask from constants like Multiple files and Alias selection -- is still directly usable today. What has moved on are the specifics: modern macOS/Windows native file pickers look and behave differently than in 2004, and 4D has since layered additional document/file and ORDA-based file-handling commands on top of the same foundational command shown here.

**References to newer/updated information:**
- Select document remains part of the current 4D language and continues to serve as the standard command for prompting the user to choose one or more files
- The underlying native macOS/Windows file-selection dialogs have changed appearance and behavior considerably since 2004
- 4D has since added further document/file management and ORDA-based file-reference commands that complement Select document for modern workflows
