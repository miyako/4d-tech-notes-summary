# Tech Note 05-28: User Preferences

**Author:** Not specified in available source
**Published:** August 26, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=38908
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_28-29_(AUG)/05-28_User_Preferences.exe

## Overview
Second in a Tech Note series building a customizable example database, this note extends the earlier "User Changeable Output Form" note by saving the user's selected output form columns and other user-changeable variables to a preferences table so choices persist across sessions.

## Key Points
- Builds directly on the July 2005 Tech Note "User Changeable Output Form"; readers are expected to have that note's context.
- Adds persistence of output form column selections and other user preference variables to a database table.
- The note describes only the new preferences-storage code, deferring to the prior note for the output form mechanics themselves.

## Featured Technology
- Output form column/preference persistence
- A dedicated preferences table in the classic 4D data model
- Classic 4D variables and arrays used to save/restore UI state

## Historical Context
**Status:** Superseded

Storing user preferences as discrete fields in a preferences table was the standard classic-language approach in 2005, but it has since been largely superseded by storing preferences as a single JSON object or BLOB, which scales far more gracefully as the set of preferences grows or changes shape. Modern 4D applications benefit from native JSON support and object/collection data types (introduced in later 4D versions) that make this kind of flexible settings persistence considerably simpler than hand-managing individual table fields. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and its example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
