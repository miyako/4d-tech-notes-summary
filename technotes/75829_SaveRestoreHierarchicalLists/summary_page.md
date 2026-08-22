# Tech Note 09-26: How to Save and Restore 4D Hierarchical Lists

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** July 1, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75829
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_22-26_(JUN)/09-26_SaveRestoreHLists.zip

## Proposition
This note shows how to export and re-import 4D Hierarchical Lists (and their associated pictures) to/from XML or BLOB files, so that user customizations to lists survive a redeployment of the structure file — a scenario where they would otherwise be silently lost.

## Key Points
- **Root problem:** Hierarchical Lists live in the binary structure (`.4DB`) file; deploying a new structure to a client overwrites any user modifications to those lists.
- **XML export/import** (`HL_Export`, `HL_ExportSublist`, `HL_Import`, `HL_ImportSublist`) uses 4D's SAX XML commands and recursive methods, producing a human-inspectable/editable archive.
- **BLOB export/import** (`HL_Export_BLOB`, `HL_Import_BLOB`) offers a simpler, binary alternative.
- **Picture preservation** for list items handled separately via `PL_Export`/`PL_Import`.
- **Backup integration:** hooking `On Backup Startup Database Method`/`On Backup Shutdown Database Method` to automatically archive lists (and the Picture Library) as part of routine backups.
- **Recursion guidance:** careful stack sizing and loop-termination discipline needed when writing methods that walk arbitrarily deep list hierarchies.
- Distinguishes the in-memory language object (`ListRef`, a Longint ID) from the form-level list representation (referenced by object name), since only `ListRef`-based lists are handled by this Tech Note.

## Featured Technology
- 4D Hierarchical Lists (in-memory ListRef objects and form-level list objects)
- 4D SAX XML commands (XML export/import)
- BLOB to list / list to BLOB commands
- On Backup Startup/Shutdown Database Method hooks
- Recursive method design for nested list structures

## Best Practices Highlighted
1. Archive user-customizable structure elements (like Hierarchical Lists) as part of the backup cycle, not as an afterthought before a structure upgrade.
2. Prefer XML export when human inspection/editing of archived data may be needed; use BLOB export for a simpler, opaque round-trip.
3. Allocate sufficient process stack space before running recursive methods that traverse unknown depths of nested data.

## Context / Positioning
Published as practical guidance for a common but easy-to-overlook deployment risk in classic (Design Mode) 4D applications, this note gave developers a ready-to-use component and methodology to protect end-user customizations across structure updates.

## Historical Commentary
**Status:** Partially Superseded

This note addressed a real pain point of the classic Design-mode era: hierarchical lists were stored inside the binary structure (.4DB) file, so any user customization to a list was silently lost whenever a developer redeployed a new structure, forcing developers to build custom XML/BLOB export-import archiving around backups.

The underlying problem is substantially reduced today because 4D's Project mode (text-based .4DProject) makes structure elements diffable and versionable, and many list-like configuration needs are now more naturally modeled with ORDA entities or JSON preferences rather than binary hierarchical list objects — though the classic List/ListRef and SAX XML commands used here still exist and function for backward compatibility.
