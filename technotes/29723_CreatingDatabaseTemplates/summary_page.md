# Tech Note: Creating Database Templates

- **Asset ID:** 29723
- **Tech Note #:** 03-33
- **Published:** July 29, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Dave Dell'Aquila
- **Page URL:** https://kb.4d.com/assetid=29723
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_31-35_(JUL)/03-33_Creating_DB_Templates.hqx

## Overview

Dave Dell'Aquila (4D, Inc. Senior Evangelist) documents 4th Dimension 2003's new database-template feature, explaining exactly which resource-fork entries (name, description, preview picture, and data-file list) must be added -- using ResEdit -- to turn any existing database structure into a selectable template in the Create Database dialog.

## Key Points

- Templates appear on the Create a Database tab of the Open/Create Database dialog alongside 'New Blank Database'; selecting one previews its interface and description before creating a new database from it.
- Template structure files must live in a '4D Templates' folder placed next to the 4D application (.exe on Windows, or the software package on Mac OS).
- Hard requirements to become a valid template: no plug-ins may be used (since all templates share one directory), and the structure must ship with an accompanying datafile (`.data` on Mac OS, `.4DD` on Windows).
- Four specific resources at ID 14000 must be added to the structure file using ResEdit: an `STR ` (with trailing space) resource for the template's display name, a `TEXT` resource for its description (up to 32,767 characters), a `PICT` resource (ideally 171x256 pixels) as a preview image, and an `STR#` resource listing expected data-file names for Mac and Windows.
- Because templates cannot bundle plug-ins directly, the note proposes a workaround: store a distinctively named plug-in folder (e.g. `Orders.Mac.4DX`) inside the Templates folder and have the new database's startup method detect and copy it into place using `Test path name`, `FOLDER LIST`, `Application file`, `CREATE FOLDER`, and `COPY DOCUMENT`.
- Once converted, a template database remains fully usable as a normal database, and any subsequent changes to its structure/data are reflected in future databases created from it.

## Featured Technology

- 4th Dimension 2003 Open/Create Database template dialog
- 4D Templates folder
- Resource-fork template metadata (STR/TEXT/PICT/STR#, ID 14000)
- ResEdit resource editing
- Plug-in-free template limitation

## Historical Commentary

**Status:** Obsolete

This resource-fork-based template mechanism was tied tightly to classic 4D Design Mode's binary structure files and Mac-style resource forks, and it is now entirely obsolete: current 4D (Project Mode, introduced in v17/2018) represents structures as plain text files that are version-control-friendly and has its own, unrelated mechanisms for scaffolding new projects (including starter/sample projects and simple file copying). The specific ResEdit-based STR/TEXT/PICT/STR# resource technique described here would not work with any modern 4D version, though the underlying goal -- giving developers a reusable, ready-made starting point for new projects -- remains a valid and common workflow need.

**References to newer/updated information:**
- 4D's Project Mode (introduced in v17, 2018) replaced binary structure files and resource-fork metadata with plain text project files, making this note's ResEdit-based template mechanism inapplicable to current 4D
- Modern project scaffolding in 4D is typically done via starter/sample projects or simple file-based copying rather than a resource-driven Open Database template list
