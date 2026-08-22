# Tech Note 06-28: Conversion to 4D 2004

**Author:** 4D, Inc./4D S.A.
**Published:** July 14, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43643
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_27-30_(JUL)/06-28_Conversion_to_2004.pdf

## Overview
A large, compiled migration guide — assembled from various technical notes, tech-tips, and product documentation — walking developers through converting 4D databases from older versions (as far back as 2.x/3.x) up through 6.x/2003 into 4D 2004, and documenting the architectural, compatibility, and feature changes introduced by 2004.

## Key Points
- Upgrade principles: recent versions can convert directly to 2004; very old databases (v3 or earlier) should pass through an intermediary version (6.5/6.7) first; cross-platform migrations should upgrade on the original platform before switching OS.
- Warns against running very old 4D versions on modern operating systems due to data-integrity risk.
- Documents 4D 2004's structural change separating structure and data files into "resource fork"/"data fork" components, plus new folder layout and relocated Preferences folder.
- Describes a new plug-in architecture, loading priority, and license activation model.
- Covers compatibility considerations: structure, Web features, menu bars, platform-specific preferences/forms, window sizing, system highlight colors, ASCII filters.
- Notable integration milestone: 4D 2004 folds previously separate companion tools directly into the core product — 4D Insider functionality, 4D Customizer features, 4D Backup enhancements, and 4D ODBC — plus three newly bundled plug-ins.
- Catalogs numerous new 2004 features: a new Formula editor, harmonized list operations across modes, the brand-new List Box object with new commands/events, new form events, and new 4D Write/4D View features.
- Documents modified, renamed, and new language commands, plus modified and added keyboard shortcuts.

## Featured Technology
- 4D database structure/data file conversion process
- 4D 2004 resource fork/data fork file architecture
- Integrated 4D Insider, 4D Customizer, 4D Backup, 4D ODBC
- 4D List Box object (introduced in 2004)

## Historical Context
Published in 2006, this note documents the specific migration path into 4D 2004 — a major architectural release for its era that consolidated several previously separate companion tools into the core product. It predates 4D v11's 2007 SQL engine by a year, and by well over a decade predates Project Mode (v17, 2018) and ORDA, none of which are addressed here.

## Historical Commentary
**Status:** Obsolete

As a version-specific migration guide targeting the jump from pre-2004 4D versions to 2004, this note has been entirely superseded by numerous subsequent version-to-version migration guides covering all of 4D's later major releases. Its value today is purely historical: it documents a pivotal moment when 4D consolidated companion products (Insider, Customizer, Backup, ODBC) into the core application and introduced the List Box object, both notable milestones in 4D's product evolution.
