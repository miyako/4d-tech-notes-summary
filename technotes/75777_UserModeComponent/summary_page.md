# Tech Note 09-21: User Mode Component

**Author:** Thomas Maul, 4D Germany
**Published:** May 28, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75777
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_18-21_(MAY)/09-21_UserMode.zip

## Proposition
This note delivers a component that recreates 4D's classic "User Mode" generic record browser/editor — with sort, query, report, import/export, and formula execution — as a reusable, installable feature that remains available even in built/compiled applications, with fine-grained per-table, per-feature access control.

## Key Points
- **Default behavior:** shows a list box of the first table's first 50 fields, with a toolbar popup to switch tables and a long click to enter edit mode.
- **Fully functional actions:** Delete, Order, Query, Show All/Show Selection, Report (with Export/Import dialog), and Execute (opening the formula editor, respecting `SET ALLOWED METHODS`).
- **UserMode_Show:** the main entry point; optionally accepts a table ID to open directly on a specific table.
- **UserMode_Access:** a per-table Boolean array controlling which of Show/Modify/New/Delete/Report/Import/Export/Execute are enabled — letting an admin see everything while a designer gets full access, for example.
- **UserMode_Forms:** assigns dedicated maintenance input forms per table (since normal application forms may block edits or auto-calculate values inappropriate for raw maintenance).
- Installed simply by dragging the component into the structure's component folder.

## Featured Technology
- 4D component architecture
- List box-based generic record browser/editor
- SET ALLOWED METHODS (formula editor security)
- Generic maintenance-mode UI (Show/Modify/New/Delete/Report/Import/Export/Execute controls)

## Best Practices Highlighted
1. Provide a dedicated, minimally-restrictive maintenance form (rather than reusing production forms) for raw record editing/troubleshooting.
2. Gate access to maintenance features per role (admin vs. designer vs. end user) using a configurable Boolean access array rather than hardcoding permissions.
3. Package reusable internal tooling as a component so it travels with, and works inside, compiled builds.

## Context / Positioning
Published to fill a practical gap — 4D's own Design-mode User Mode isn't available once an application is compiled — this note gave developers/support staff a portable, controllable maintenance tool suitable for production troubleshooting and data correction.

## Historical Commentary
**Status:** Still Relevant

This note provided a component recreating the classic 4D "User Mode" (a generic, table-driven record browser/editor with sort, query, import/export, and report capabilities) for use even in built/compiled applications where 4D's own Design-time User Mode is unavailable. The generic-maintenance-tool concept is timeless and the component architecture pattern shown is still valid.

The underlying list box, Quick Report, and formula editor building blocks are classic-language UI elements that remain fully functional; a similarly-purposed tool built today could optionally leverage ORDA for more flexible, entity-based data access rather than raw table/selection based commands, but the classic approach shown here still works as documented.
