# Tech Note: Free Form Object Storage

- **Asset ID:** 30595
- **Tech Note #:** 03-51
- **Published:** November 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Dave Dell'Aquila, Senior 4D Evangelist
- **Page URL:** https://kb.4d.com/assetid=30595
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_48-51_(NOV)/03-51_FreeFormObjectStorage.hqx

## Overview

Dave Dell'Aquila (Senior 4D Evangelist) presents a reusable "cObject" mechanism for storing arbitrary, loosely structured application settings (window positions, custom field names, user preferences, even pictures) without needing to create a dedicated table or field for every individual value.

## Key Points

- All logic lives in a single project method, `cObject`, dispatched by a `Case of` on its first text parameter: public operations `get`, `set`, `save`, `rename`, `delete`, and internal helpers `$load`, `$loadPref`, `$getPref`, `$setPref`, `$add`, `$new`, `loadForUpdate`, `unload`, `init`/`startup`.
- Data is stored in one `Objects` table: an indexed `CollectionName` field identifies a named group of settings (e.g., `Current user` or `Current machine owner`), with a `Members` subtable holding each individual `Members'Name` (subfield) and `Members'Data` (a BLOB).
- Values of any type are serialized generically using `VARIABLE TO BLOB`/`BLOB TO VARIABLE`, so the caller is responsible for reading into a variable of the correct type (the note stresses this point cannot be overemphasized).
- `cObject("get";collection;name;->variable)` auto-creates the collection and/or member with a default value if they don't already exist; `cObject("set";...)` assigns without saving, requiring an explicit `cObject("save")` to persist and unload the record.
- `loadForUpdate` provides basic multi-user safety by polling `Locked(◊objTablePtr->)` against a `Tickcount`-based timeout before acquiring the record `READ WRITE`.
- Demonstrated with two example dialogs: a simple per-user preferences form that loads four values (`popup 1`, `popup 2`, a checkbox, and a radio-button group) on `On Load` and saves them via a Save button's `On Clicked` script, and a second dialog letting users switch between multiple named collections on the fly via a popup, including a picture value.
- The full `cObject` source listing (marked "revision 9, 5/10/98") is included at the end of the note.

## Featured Technology

- VARIABLE TO BLOB / BLOB TO VARIABLE generic serialization
- Subtable-based collection/member data model
- cObject project-method "class" (get/set/save/rename/delete operations)
- READ ONLY / READ WRITE record locking with Locked()/Tickcount timeout polling
- Named collections keyed by Current user / Current machine owner

## Historical Commentary

**Status:** Superseded

This note designs a reusable "cObject" mechanism for storing arbitrarily-named, arbitrarily-typed pieces of data (window positions, custom field names, user preferences, pictures, etc.) without needing a dedicated table or field per setting, built around a Collection/Member subtable structure and the VARIABLE TO BLOB / BLOB TO VARIABLE commands to serialize any 4D variable type into a blob. It even includes a hand-rolled locking/timeout loop (Locked()/Tickcount polling) to make the mechanism safe in a multi-user context. The underlying motivation — avoiding rigid one-field-per-setting schemas — is now solved far more elegantly by 4D's native Object and Collection data types with built-in JSON support, which did not exist in 2003, making this specific blob-based subtable technique obsolete for new development even though the design pattern it teaches (a generic key/value settings store) remains a recognizable and still-useful idea.

**References to newer/updated information:**
- 4D later added a native Object/Collection data type and OB SET/OB GET-style commands plus full JSON support, providing a built-in, far simpler way to store free-form/unstructured data than the blob-in-subtable technique shown here
- 4D's ORDA/entity-based data model and modern locking commands have also evolved well beyond the manual Locked()/Tickcount polling loop used in this note's loadForUpdate operation
