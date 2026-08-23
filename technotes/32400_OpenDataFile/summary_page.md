# Tech Note: Open Data File

- **Asset ID:** 32400
- **Tech Note #:** 04-17
- **Published:** April 29, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Frank Chang, 4D Technical Support
- **Page URL:** https://kb.4d.com/assetid=32400
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_16-20_(APR)/04-17_Open_Data_File.hqx

## Overview

Frank Chang demonstrates letting end users programmatically browse to and open a different 4D data file with the current structure file, using `OPEN DATA FILE`, `Select Folder`, and `DOCUMENT LIST`, avoiding the manual Alt/Option-key launch procedure and enabling multi-data-file/personalized-database scenarios.

## Key Points

- The sample database's `On Startup` method determines the current data file name via a `Get_Name` project method that parses the path using the platform-correct delimiter (`\\` on Windows, `:` on Mac), obtained from `Data file` and `PLATFORM PROPERTIES`.
- The `Select Folder` command opens the OS's native folder-picker dialog with an optional prompt message, returning the chosen path; `DOCUMENT LIST` then populates a text array with every file in that folder.
- A `Do_Loop`/`Build_List` helper filters the folder listing down to files matching the platform's 4D data file extension (`.4dd` on Windows, `.data` on Mac), populating a scrollable list of valid data files for the user to pick from.
- The `Open` button passes the selected file to an `Open_Data_File` method, which warns the user if they selected the data file already in use, then calls a `ReStart` method wrapping the single `OPEN DATA FILE` call.
- `OPEN DATA FILE` takes the absolute (or same-folder relative) path to the desired data file and, when executed, shuts down and relaunches 4D against the current structure file bound to that data file -- eliminating the need to hold Alt/Option at launch.
- The note also covers the WEDD resource: using 4D Customizer Plus to set a matching signature value on both the structure file and each intended data file, so 4D rejects mismatched pairings at open time.

## Featured Technology

- OPEN DATA FILE command
- Select Folder command
- DOCUMENT LIST command
- Data file command
- Platform-aware path parsing (Windows \\ vs. Mac : delimiter)
- WEDD resource binding via 4D Customizer Plus

## Historical Commentary

**Status:** Partially superseded

This note shows how to let end users switch between multiple 4D data files sharing the same structure file at runtime -- letting them browse a folder, pick a `.4dd`/`.data` file, and re-launch via the `OPEN DATA FILE` command -- instead of requiring them to hold Alt/Option at launch. It also covers binding structure and data files together with the WEDD resource in 4D Customizer Plus so mismatched files are rejected. The core `OPEN DATA FILE` command and the general pattern of programmatically switching data files remain part of current 4D (now typically paired with modern project-based structure/data separation), so the fundamental technique is still usable, though the platform-detection code (`PLATFORM PROPERTIES`, manual path-delimiter parsing) and the WEDD-resource/4D Customizer Plus workflow reflect classic-mode 4D file structures that Project Mode databases (2018+) handle differently.

**References to newer/updated information:**
- OPEN DATA FILE remains a supported 4D command for switching data files at runtime
- 4D Customizer Plus and the WEDD-resource binding mechanism described here are tied to classic 4D structure files; Project Mode databases (introduced 2018) organize structure and data differently
- Modern 4D code favors cross-platform path handling (e.g. Get 4D folder, File/Folder objects) over manual delimiter parsing shown in this note
