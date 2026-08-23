# Tech Note: All About Help

- **Asset ID:** 29720
- **Tech Note #:** 03-35
- **Published:** July 29, 2003
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=29720
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_31-35_(JUL)/03-35_All_About_Help.hqx

## Overview

Jamras Komoncharoensiri (4D Inc. Technical Support) surveys every help mechanism available to 4th Dimension 6.8/2003 developers -- from command-syntax lookup via 4D Explorer Help to full Microsoft Help and Apple Viewer documentation, database-specific contextual help, and lightweight Help Tips -- along with exact per-platform installation instructions for each.

## Key Points

- 4D Explorer Help (the `4D Help.rsr` file placed in the platform's active 4D folder) surfaces command syntax directly in the Method editor via Tab/F1 and in the 4D Explorer preview pane; the note documents distinct active-4D-folder locations for each supported Windows and Mac OS version.
- 4D Help in Microsoft Help (`.HLP`) format documents over 500 4D commands plus a Quick Start guide; placing multiple help files (4D, Compiler, View, Internet Commands, etc.) in the Win4DX/Mac4DX folder makes them all available under the Help menu, including for connected 4D Client sessions.
- 4D Help in Apple Viewer format (for Mac OS 9.x/X) requires manually copying a decompressed 'Help 4th Dimension' folder into the application package's Contents/Resources folder, with an additional alias-creation step required specifically on Mac OS 9.
- 4D Contextual On-line Help is a per-database customized help file offering database-specific 'How to' guidance, distinct from the generic 4D command reference help.
- Covers 4D's on-line HTML documentation as a further reference channel, alongside the lighter in-form Help Tip and Dynamic Help Message object properties for contextual, per-object guidance without a full help system.
- Notes explicit compatibility caveats, such as the Microsoft Help viewer application needing separate installation on Mac OS 9.x for `.HLP` files to display.

## Featured Technology

- 4D Explorer Help (4D Help.rsr)
- Microsoft Help format (.HLP)
- Apple Viewer help format
- 4D Contextual On-line Help
- Help Tip / Dynamic Help Message object properties

## Historical Commentary

**Status:** Historical Interest Only

This note is a thorough, practical reference for the surprisingly fragmented help ecosystem 4D developers had to navigate in 2003 -- juggling resource-fork-based command help, Microsoft's .HLP format, Apple's Viewer format, and lightweight tips, each with its own installation quirks. All of these specific mechanisms (4D Help.rsr, .HLP files, Apple Viewer help folders) are now purely of historical interest, since modern 4D applications overwhelmingly favor web-based help/documentation, tooltips backed by web areas, or externally hosted documentation sites rather than any of the native in-app help formats emphasized here.

**References to newer/updated information:**
- Modern 4D applications commonly use web-based help systems, web-area-backed tooltips, or externally hosted documentation rather than the native 4D Explorer Help/.HLP/Apple Viewer help formats described in this note
- 4D's own current documentation is delivered online rather than through the .HLP/Apple Viewer file formats this note explains how to install
