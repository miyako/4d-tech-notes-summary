# Tech Note 02-46: Referential Integrity

**Author:** Not specified in source document
**Published:** October 31, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25587
**Download:** https://kb.4d.com/DLTN/TN/2002/Windows/TN_2002_46-50_(OCT)/02-46_Referential_Integrity.exe

## Overview
A Tech Note explaining how 4D automatically enforces referential integrity, including cascading record deletion, based on relational constraints defined in the database structure.

## Key Points
- Explains that 4D automatically enforces referential integrity constraints from the structure file.
- Covers cascading deletion of related records when a "one" side record is deleted.

## Featured Technology
- 4D relational constraints
- Cascading delete behavior

## Historical Context
Reflects classic 4D's structure-defined automatic relations model in Design Mode, where referential integrity behavior was configured at the structure level.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Still Relevant

The fundamental referential integrity concepts described here remain fully valid in current 4D, though ORDA's relation attributes (introduced in 4D v17+) provide an additional, more modern way to define and navigate these relationships alongside the classic structure-level automatic relations this note discusses.
