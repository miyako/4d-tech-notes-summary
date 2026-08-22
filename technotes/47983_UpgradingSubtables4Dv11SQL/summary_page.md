# Tech Note 07-42: Upgrading Subtables to 4D v11 SQL

**Author:** Josh Fletcher, Technical Support Engineer; Jean-Yves Fock-Hoon, QA Manager
**Published:** November 6, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47983
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_42-45_(NOV)/07-42_Upgrading_Subtables.zip

## Overview
This note explains what happens to subtables — a legacy 4D data structure — when a database is converted to 4D v11 SQL, which removed the ability to create new subtables entirely. It distinguishes single-level from multi-level subtable scenarios, which are handled very differently during migration.

## Key Points
- Single-level subtables (owned directly by a "real" table) are auto-converted by 4D v11 SQL into standard related tables, with a new foreign-key field and a special, non-recreatable many-to-one relation preserving backward compatibility.
- Existing subtable-oriented code continues to work after conversion thanks to this special relation, but developers are advised to migrate the code to standard related-table logic over time.
- Post-conversion behavior changes: total table count increases; subrecords no longer auto-load with the parent record; `RECEIVE RECORD` still supports legacy formats but the v11 SQL `SEND RECORD` no longer exports subrecords and uses an incompatible new format.
- Multi-level (nested) subtables are **not supported at all** — any data in subtables beyond the first level is lost on conversion, requiring manual extraction beforehand.
- A community-contributed, open-source component ("SendReceiveRecord.4dbase" by Thomas Maul, 4D Germany) is bundled to provide synchronization methods compatible with the special subtable relation, working around the new SEND RECORD's dropped subrecord support.

## Featured Technology
- 4D Subtables (single-level vs. multi-level)
- Automatic subtable-to-related-table conversion mechanism
- `SEND RECORD` / `RECEIVE RECORD` commands
- Community "SendReceiveRecord" open-source component

## Historical Context
Published in November 2007 as part of the wave of Tech Notes accompanying 4D v11 SQL's launch, this note documents a one-time, structural migration challenge specific to that version: the elimination of subtables in favor of standard related tables, alongside the introduction of 4D's native SQL engine. This predates Project Mode and ORDA by roughly a decade.

## Historical Commentary
**Status:** Obsolete

Subtables have not existed in any creatable form in 4D since version 11 (2007), and any database that needed this migration would have completed it many 4D versions ago; there is essentially no active 4D codebase today still facing this issue. The note is preserved purely for historical/archival interest as a record of a significant one-time architectural transition in 4D's history, alongside the shift to related tables (and, much later, ORDA relations) as the standard way to model one-to-many data.
