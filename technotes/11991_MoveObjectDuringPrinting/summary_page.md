# Tech Note: Using MOVE OBJECT During Printing

## Overview
- **Technical Note 00-51**
- **Author:** Unknown / not specified
- **Published:** November 1, 2000
- **Product/Version:** 4D v6.7
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note documents a specific language enhancement introduced in 4D v6.7: the MOVE OBJECT and GET OBJECT RECT commands, previously usable only in display mode, could now also be used during printing, provided the print job was triggered via PRINT SELECTION, PRINT FORM, or PRINT RECORD (notably, PRINT LABEL was excluded). The proposition is that developers can use the same parameters and coordinate systems familiar from display-mode form manipulation — relative or absolute coordinates, with the '*' parameter flagging absolute mode — to dynamically reposition and resize objects while a form is being printed, enabling more flexible, data-driven print layouts. The note stresses a caveat: if absolute coordinates were used, developers needed to ensure that any resulting new coordinates remained valid, which is exactly why GET OBJECT RECT was correspondingly updated to also function during printing (so a developer could query an object's current print-time position/size before moving it). An example database was provided to illustrate the technique in practice. The featured technology here is core 4D language print-engine integration rather than any plug-in, reflecting the granular, command-level nature of many Tech Notes from this period. Only the teaser abstract for this note survives in this archive, since its full download was an old Windows self-extracting installer that could not be extracted here.

## Featured Technology
- MOVE OBJECT command
- GET OBJECT RECT command
- 4D print engine (PRINT SELECTION/PRINT FORM/PRINT RECORD)

## Historical Context
This note documents a 4D v6.7 enhancement that let developers reposition and resize form objects dynamically during PRINT SELECTION, PRINT FORM, and PRINT RECORD operations using MOVE OBJECT and GET OBJECT RECT. Both commands remain part of the current 4D language and the general technique of repositioning objects for print layouts is still valid, though many modern 4D reporting needs are now served by higher-level tools such as 4D Write Pro-based reports, making this a still-usable but somewhat lower-level approach today.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- MOVE OBJECT and GET OBJECT RECT remain part of the current 4D language for programmatic form/print layout control
- 4D Write Pro and other modern reporting tools now offer a higher-level alternative for many dynamic print/report layout needs that once required manual object repositioning

