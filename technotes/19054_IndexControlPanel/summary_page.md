# Tech Note: Index Control Panel

- **Asset ID:** 19054
- **Tech Note #:** 01-55
- **Published:** December 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hartman, MCP, 4D, Inc. Information Systems (co-authored with Kent Wilbur)
- **Page URL:** https://kb.4d.com/assetid=19054
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_57-61_(DEC)/01-55_Index_Control_Panel.hqx

## Overview

Steve Hartman presents a sample database, "Index Control Panel" (co-authored with Kent Wilbur), that solves a real pain point for compiled 4D databases: without design-environment access, rebuilding a field's index normally requires re-indexing an uncompiled copy and recompiling, so this control panel exposes a runtime UI and programmatic technique for toggling field indexes off and back on to force a rebuild.

## Key Points

- Choosing "Index Control Panel" from the File menu shows a form listing Table Names and Field Names with toggleable "X" marks; turning a table's mark off has no effect on its fields, but toggling a field's mark controls whether `SET INDEX` sets that field's index true or false.
- The documented re-indexing procedure is: turn off the field's "X", quit and relaunch the database, turn the "X" back on, then quit and relaunch again -- in 4D 6.7, toggling an index on a related field automatically triggers 4D to re-index and restore it.
- `M_INDEX_SetIndexes` first checks `Current user="Designer"` or `"Administrator"` for authorization, then (for 4D Client) uses `Count users` to ensure only one user is connected before allowing structural changes, to avoid conflicting concurrent index modifications.
- The method reads current index state from a `zStructure` table (with `TableNumber=0` representing table-name rows) via `QUERY` and `SELECTION TO ARRAY`, builds sorted table/field arrays, and displays the toggle dialog wrapped in `START TRANSACTION` / `VALIDATE TRANSACTION` / `CANCEL TRANSACTION`.
- A `"ModifyingStructureTable"` semaphore, checked with `Semaphore(...)` and cleared with `CLEAR SEMAPHORE`, prevents two users from editing the index structure simultaneously.
- The companion method `INDEX_ModifyIndexes` iterates the table and field arrays, resolves each field with `Field($aLTableNumber{$i};$aLFieldNumber{$j})`, and calls `SET INDEX($pField->;True)` or `SET INDEX($pField->;False)` based on the toggle state saved by the user.
- The note frames this as functionally similar to 4D Tools' index repair option, but usable directly at runtime without quitting to Tools, and thanks Kent Wilbur for his suggestions in co-authoring the sample database.

## Featured Technology

- SET INDEX command
- Compiled database index rebuilding without design access
- Table/field structure introspection (zStructure)
- Semaphore-based single-user protection
- SELECTION TO ARRAY / ARRAY TO SELECTION
- Designer/Administrator privilege checks (Current user)

## Historical Commentary

**Status:** Partially superseded

Steve Hartman (co-authored with Kent Wilbur) presents a sample database, Index Control Panel, that lets a Designer or Administrator toggle field indexes off and back on programmatically at runtime -- a workaround for compiled databases that otherwise have no design-environment access for re-indexing a field. The core building block, SET INDEX, remains a valid and still-used 4D command today, and the note's underlying goal (re-indexing a field without recompiling) is occasionally still relevant, but many later 4D versions and deployment models reduce the friction this note addresses, and a semaphore-protected, single-user, quit-and-relaunch workflow like this is a heavier and more manual approach than most current compiled-database maintenance practices would use.

References to newer/updated information:
- The SET INDEX command remains part of current 4D and is still the mechanism for programmatically enabling/disabling a field index
- Later 4D versions and structure-file update tooling have reduced how often developers need this quit-and-relaunch, semaphore-protected control panel workaround for compiled databases
