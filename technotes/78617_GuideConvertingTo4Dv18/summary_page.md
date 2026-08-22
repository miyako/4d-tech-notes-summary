# Tech Note 20-24: Guide for Converting to 4Dv18 and Newer

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** December 29, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78617
**Download:** https://kb.4d.com/DLTN/TN/2020/20-24_v18ConvertionGuide.pdf

## Proposition
4D v18 dropped 32-bit compatibility entirely, forcing databases built in v17 and earlier to be updated before running on modern, 64-bit-only operating systems. This Tech Note is a checklist-style migration guide covering backup strategy, the conversion process itself, and the follow-up fixes (primary keys, Unicode mode, subtables, obsolete commands, PICT images, 4D View/Write) needed to get an older database running cleanly on v18+.

## Key Points
- **Backup first, always**: conversion of the structure (.4DB) and data (.4DD) files is irreversible; keep a complete pre-conversion copy of everything.
- **Primary key assistant**: ORDA requires every table to have a primary key; v18 prompts a "Run assistant" flow to add missing ones.
- **Unicode mode & object notation**: two Compatibility settings (Design > Database Settings) that must generally be enabled for ORDA dot notation to work and for accented characters to be preserved.
- **Subtables are obsolete (since v11)**: must be replaced with standard related tables; find them by searching for "subrecord" commands in Design mode.
- **Obsolete `_O_` commands**: searchable in Design mode; F1 on any hit opens documentation suggesting the modern replacement.
- **PICT images unsupported (since v14)**: a provided `UTIL_ConvertPICTs` utility method converts the Picture Library to PNG (run against the old 32-bit database, then drag images into the new one).
- **4D View/Write are 32-bit-only**: there is no 1:1 command mapping to 4D View Pro/4D Write Pro; expect a rewrite, and consult 4D Summit 2020 migration sessions.
- **Naming conventions**: avoid spaces/dots in table, field, form, and method names to prevent ORDA dot-notation syntax errors (bracket notation `ds["Table 1"]` is the fallback).

## Featured Technology
- ORDA primary key requirement and Primary Key Manager
- Unicode mode / object notation compatibility settings
- Subtable-to-relation migration
- Obsolete command (`_O_`) detection via Find in Design
- `UTIL_ConvertPICTs` picture library conversion utility
- 4D View Pro / 4D Write Pro (as 4D View/Write successors)

## Best Practices Highlighted
1. Always create and retain a full backup before converting, since the process cannot be reversed.
2. Convert and validate incrementally — expect bigger version jumps (e.g., v12 to v18) to require substantially more remediation than smaller ones (e.g., v17 to v18).
3. Search systematically for obsolete constructs (`_O_` commands, subtables, PICT images) rather than waiting for runtime failures.
4. For heavy 4D View/Write usage, budget real rewrite time rather than expecting a mechanical translation to the Pro versions.

## Context / Positioning
This note captures a genuine industry inflection point: the end of 32-bit OS support forced 4D (and its customer base) to fully commit to 64-bit, which in turn required finishing the deprecation of long-legacy constructs (subtables, PICT images, non-ORDA-compliant tables) that had lingered in older databases for years. It shows 4D actively steering developers toward ORDA (primary keys, object notation) as a mandatory rather than optional adjustment, and toward the Pro versions of View/Write as the only forward path.

## Historical Commentary
**Status:** Obsolete

The specific 32-bit-to-64-bit conversion problem this note solves is now essentially a non-issue: all currently supported 4D versions have been 64-bit-only for years, and any database still requiring this exact guide today would be extraordinarily old (pre-v18) and would face a far longer modernization path than described here — including migrating from binary/Design mode to Project mode (a separate, larger transition that started around v17R5–18) and potentially multiple generations of ORDA, 4D Write Pro, and 4D View Pro changes. The underlying advice about removing truly obsolete constructs (subtables, `_O_` commands, PICT images) remains historically accurate and instructive for understanding 4D's evolution, but is no longer an active concern for any database built in the last several years. Developers converting an old database today should consult 4D's current, more comprehensive conversion documentation rather than relying solely on this note.
