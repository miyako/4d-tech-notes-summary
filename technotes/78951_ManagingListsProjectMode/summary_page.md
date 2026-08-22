# Tech Note 22-11: Managing Lists in Project Mode

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** June 21, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78951
**Download:** https://kb.4d.com/DLTN/TN/2022/22-11_ManagingListsinPM.zip

## Proposition
Project mode moved 4D's hierarchical lists into a lists.json file, which is read-only once an app runs compiled or as a remote client — silently breaking SAVE LIST. This note explains the failure condition and provides a table-backed loadList()/saveList() replacement that restores full read-write list management in every mode.

## Key Points
- **Project mode stores lists in Sources/lists.json**, not in the binary structure file — deliberately, to make lists trackable in Git alongside other project-mode source files.
- **SAVE LIST silently fails in compiled (.4DZ) or remote client-server mode** because those modes only have read access to the structure's JSON sources; Load list continues to work for reading.
- **Three conditions determine whether an app is affected**: running in project mode, running compiled or client-server, and actually calling SAVE LIST anywhere in the code (checkable via Find in Design).
- **convertListsJSONToRecords migrates existing lists.json entries into a new Lists table**, storing LONGINT-reference lists as BLOB (via LIST TO BLOB) and array/object-type lists as a Collection inside an Object field.
- **loadList(listName) and saveList(listSource; listName) are drop-in replacements** for Load list/SAVE LIST that query and update the Lists table instead, working correctly in every execution mode.
- **A bundled sample database demonstrates the failure and the fix side by side**, showing SAVE LIST silently discarding changes next to the table-backed methods correctly persisting them.

## Featured Technology
- Project mode lists.json
- SAVE LIST / Load list (classic commands)
- LIST TO BLOB / BLOB to list
- Custom loadList()/saveList() table-backed replacement

## Best Practices Highlighted
1. Audit any project-mode app for SAVE LIST usage before deploying it compiled or client-server, since the failure is silent and easy to miss during interpreted-mode testing.
2. Prefer storing mutable list data in a table (as this note recommends) rather than relying on lists.json for any list that must be writable at runtime.

## Context / Positioning
Published under 4D v19 R (June 2022), this note documents a real architectural side effect of 4D's multi-year transition from binary structure files to project mode's text/JSON-based source layout — a trade-off (Git-friendliness vs. runtime writability) that 4D's own technical support had to work around with a documented workaround rather than a product fix at the time.

## Historical Commentary
**Status:** still relevant

This limitation and workaround were specific to the early-to-mid project-mode era; whether 4D has since made lists.json writable in compiled/remote-client scenarios in a later release could not be confirmed with certainty here, so developers on current 4D versions should verify the current behavior of SAVE LIST before assuming this workaround is still required. Regardless, the table-backed loadList()/saveList() pattern itself remains a sound, still-valid technique for storing any kind of mutable configuration data that must survive in compiled/client-server deployments, independent of whether the original SAVE LIST limitation has since been addressed.
