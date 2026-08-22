# Tech Note 99-34: Converting 4D Expressions

**Author:** ACI Technical Support
**Published:** August 1, 1999 | **Product/Version:** 4D v6.0.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11848
**Download:** https://kb.4d.com/DLTN/TN/1999/Windows/TN_1999_32-36_(AUG)/99-34_Convert_Expressions.exe

## Overview
A detailed solution for fixing syntax errors in 4D expressions embedded in plug-in areas (4D Write, Calc, Draw, Chart) during database migration from 4D version 3 to version 6.

## Key Points
- 4D expressions in plug-in areas may produce syntax errors after v3-to-v6 conversion
- Solution: create a '4DT5' resource (ID 128) to trigger automatic expression re-conversion
- On Startup method creates the resource only once, using a 'ToConvert' sentinel file
- UpDate method iterates all records, opening and re-saving plug-in areas to force re-evaluation
- Handles Mac OS (68K/PPC) and Windows platform differences (path names, .RSR resource files)
- Requires minimum 4D v6.0.6; does not apply to databases already converted to v6

## Featured Technology
- 4D v3 to v6 Migration
- 4D Write
- 4D Calc
- 4D Draw
- 4D Chart
- 4DT5 Resource
- Plug-in Expressions

## Historical Context
**Status:** Obsolete

This note addresses a very specific migration issue from 4D v3 to v6 — converting embedded 4D expressions in plug-in areas (4D Write, Calc, Draw, Chart). The 4DT5 resource mechanism and the entire v3-to-v6 conversion path are long obsolete; 4D Write itself was replaced by 4D Write Pro, and the resource-based architecture gave way to components and modern plug-in APIs. This note is purely of historical interest as a record of the migration challenges developers faced in the late 1990s.

### Related Updates
- 4D v3 and v6 are long discontinued
- 4D Write replaced by 4D Write Pro
- Resource-based architecture (4DT5 etc.) replaced by components and modern plug-in architecture
