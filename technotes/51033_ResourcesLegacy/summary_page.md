# Tech Note 08-33: Resources: 4D 2004 vs 4D v11 SQL

**Author:** Jesse Pina (Technical Services Team Member, 4D Inc.)  
**Published:** September 12, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51033  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_32-35_(SEP)/08-33_Resources.zip

## Overview

This Technical Note documents a major architectural shift in resource management between 4D 2004 (and earlier) and 4D v11 SQL, transitioning from Macintosh resource fork-based storage to a modern, file-based resource system aligned with Mac OS X standards. The note serves as both a technical reference for the two systems and a migration guide for developers upgrading from legacy versions to 4D v11 SQL, with sample databases illustrating both converted and upgraded database approaches.

## Key Points

**Resource Forks in 4D 2004**
- Resources were stored in `.RSR` files using Macintosh resource forks
- 4-character resource types: STR (single string), STR# (string list), TEXT (text block), PICT (picture), cicn (color icon), CURS (cursor), 4DK# (custom constant)
- Accessed via Resource theme commands: Get string resource, Get indexed string, Get text resource, Get picture resource, Get icon resource, Get resource
- Could be used directly in form objects via syntax `:ResourceNumber,ElementNumber` (e.g., `:15000,5` for element 5 of string resource 15000)
- Used in menus, buttons, window titles, list items, help tips, text objects

**File-Based Resources in 4D v11 SQL**
- Strings (STR, STR#, TEXT) stored as individual XLIFF files in the Resources folder
- Images (PICT, cicn, CURS) stored as individual files (.jpg, .png, .gif, etc.) in the Resources folder
- Custom constants (4DK#) now stored in plug-ins only
- XLIFF format adopted for standardized localization (Sun XML Localization Interchange Format)

**XLIFF Format Advantages**
- Standardizes localization across platforms and applications
- Separates content from localization metadata
- Better integration with third-party translation tools
- Aligns with Mac OS X and industry best practices

**Backward Compatibility**
- 4D v11 SQL includes compatibility mechanisms allowing legacy .RSR resources to continue functioning
- Converted databases (from 4D 2004 to v11 SQL) can still use old-style resources through the Open Resource File command
- Developers are recommended to upgrade resources to the new file-based architecture, though old-style resources remain supported during the transition

**Migration Paths**
- **Converted Database:** Original 4D 2004 database converted to v11 SQL; continues to use .RSR file if compatibility is needed
- **Upgraded Database:** Database fully migrated to v11 SQL architecture; resources converted to XLIFF and individual files

**Sample Databases**
- Example_4D2004.4DB: Demonstrates resource fork usage in legacy 4D 2004
- Example_Converted.4DB: Shows compatibility approach (v11 SQL with .RSR file)
- Example_Upgraded.4DB: Shows full migration to file-based resources

## Featured Technology

- Resource fork architecture (Macintosh OS legacy)
- XLIFF (XML Localization Interchange Format)
- File-based resource storage
- Resource compatibility and migration
- Mac OS X standards compliance
- Localization infrastructure

## Historical Context

Published in September 2008, this note reflects Apple's definitive move away from resource forks as a platform standard and 4D's corresponding architectural decision to embrace file-based resources and XLIFF as the modern standard for application localization and resource management. The note positions the v11 SQL approach as a necessary modernization while acknowledging the practical need for backward compatibility during the transition from legacy codebases.

## Historical Commentary

**Status:** Historical Interest Only

This note documents a one-time architectural transition from Mac OS 9-era resource fork technology to modern standards-based XLIFF localization. Once 4D v11 SQL established the file-based resource model, the architecture has remained stable through all subsequent 4D versions. Resource forks are no longer accessible or used in modern macOS or 4D; this note serves primarily as historical documentation of how 4D modernized its resource infrastructure. Developers encountering legacy 4D 2004 databases would need to consult this note to understand the migration path, but for any 4D version from v11 SQL onward, the file-based XLIFF/picture file approach is the only relevant standard.
