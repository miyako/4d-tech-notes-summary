# Tech Note: User Preferences

- **Asset ID:** 38908
- **Tech Note #:** 05-28
- **Published:** August 26, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Larry Sharpe
- **Page URL:** https://kb.4d.com/assetid=38908
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_28-29_(AUG)/05-28_User_Preferences.hqx

## Overview

Larry Sharpe's second Tech Note in his example-database series extends the prior "User Changeable Output Form" note by persisting output-form column preferences — and several other per-user settings — into a new [xPreferences] table, so choices survive a restart of the database.

## Key Points

- Preferences are stored per user and per preference type (Startup View, Data Entry, CompanyList, PeopleList) as a single BLOB field in the [xPreferences] table, allowing arbitrary variable sets without schema changes as long as Save and Load stay in sync.
- The original single preferences method is split into three: xPreferences_Users (menu entry point that opens the edit dialog), xPreferences (the workhorse method handling Load/Save/Defaults/DefineVars via a Case of on `$command`), and xPreferences_Processes (a stub for a future server-process preferences note).
- The [xPreferences]EditPrefs form uses a page 0 with a Tab Control and a username popup (which also lists "Server" settings in Client/Server mode); switching pages or users automatically saves the current page's preference variables before loading the new set.
- xOutput_Columns (renamed from Output_Columns in the prior note) now calls the xPreferences method to persist the user's column/format/alignment choices into the data file instead of only holding them in interprocess variables.
- The `Current user` 4D command is used to key preference records per login name; the note notes this could be replaced with a fixed value to share one preference set across all users if per-user preferences aren't desired.
- On Startup runs xOutput_Columns("OnStartup") and xPreferences("OnStartup"), then xPreferences("Load") to check for and launch a configured startup view; On Server Startup loads server-specific preferences (elaborated in the following Tech Note on Server Processes).

## Featured Technology

- xPreferences table with BLOB-based preference storage
- Case of ($command) method dispatch pattern
- Tab Control form navigation
- Current user command for per-user keying
- On Startup / On Server Startup database methods
- Persisted output-form column customization

## Historical Commentary

**Status:** Superseded

This note extends the prior output-form-customization note by persisting user preferences as a single BLOB per record rather than one column per preference value, a pragmatic technique for the classic 4D language that lets preference schemas evolve without altering table structure. The pattern still works today, but it has largely been superseded by storing preferences as JSON objects (via JSON Stringify/Parse or 4D's object/collection types), which is more flexible, human-readable, and easier to inspect or migrate than an opaque BLOB. The general idea of centralizing per-user settings in a dedicated table remains sound design practice.

**References to newer/updated information:**
- Modern 4D applications typically persist user preferences as JSON objects (via JSON Stringify/Parse or native object storage) rather than opaque BLOB fields, making the data far easier to inspect, version, and extend
- ORDA and 4D's object/collection data types, introduced in later versions, make flexible, schema-less preference structures much simpler to implement than this classic per-record BLOB approach
