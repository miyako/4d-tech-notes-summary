# Tech Note: The 128th Byte

- **Asset ID:** 15348
- **Tech Note #:** 01-29
- **Published:** June 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Olivier Deschanels
- **Page URL:** https://kb.4d.com/assetid=15348
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_26-30_(JUN)/01-29_The_128th_Byte.hqx

## Overview

Olivier Deschanels (4D, S.A.) opens a technical deep-dive series on 4D's internal data storage architecture, explaining the rationale for 4D's single-file design and the block-based structure of that data file, including how each record's header and "microstructure" enable lazy, low-cost structure and type changes.

## Key Points

- Contrasts 4D's single-file data storage (`.data` on Mac OS / `.4DD` on Windows, since Version 2 — Version 1 US used multiple files) against multi-file database architectures, citing simpler backup, avoidance of OS open-file limits, better data-integrity resilience against misplaced files, and engine-managed (not OS-level) fragmentation as advantages.
- Notes the significant space waste of fixed-length-record architectures used by some competing systems (e.g., an 80-char alpha field at 20% average fill wastes ~6.1 MB across 100,000 records) versus 4D's variable-length field storage.
- Explains the data file is divided into fixed 128-byte blocks; a record's on-disk size is always a multiple of 128 bytes, made up of a 22-byte header (marker, checksum, last-cache-save data, table/record number, sizes, indicators), a per-record "microstructure" (4 bytes per field: 1 byte type + 1 reserved + 2 bytes offset), and the actual field data with no inter-field separators or padding for unused alpha characters.
- The microstructure functions as a snapshot of the table's structure as of the record's last save; on load, 4D compares the record's microstructure to the live table structure and only then applies pending field additions (default values) or type conversions (e.g., an Alpha-to-Real conversion equivalent to `Num`), so structure edits in Design mode cost nothing until existing records are actually touched.
- Because of this microstructure mechanism, fields can never be deleted in 4D's classic engine (only their type changed) — deleting a field would leave the structure and stored microstructures permanently inconsistent, an unmanageable problem for deployed applications receiving incremental updates.
- Demonstrates `APPLY TO SELECTION([MyTable];[MyTable]MyField:=[MyTable]MyField)` as a one-line way to force every record in a selection to be re-saved immediately, picking up a pending field/type change right away (e.g., before running a search that depends on the new type) instead of waiting for records to be touched individually.

## Featured Technology

- Single-file 4D data file architecture (.data / .4DD)
- 128-byte block-based record storage
- Record header, microstructure, and data layout
- Automatic structure/microstructure comparison on record load
- Automatic field-type conversion on load
- APPLY TO SELECTION for forcing immediate record conversion

## Historical Commentary

**Status:** Obsolete

This note is a genuinely illuminating explanation of 4D's classic (pre-SQL-engine) record storage format — its 128-byte blocks, record headers, and per-record microstructure — that clarified real, practical consequences for developers (like why fields can't be deleted, and how to force pending structure changes to apply). That classic storage engine was superseded by 4D's SQL/CoreData-based engine (from 4D v11 SQL onward, 2007), which uses a different internal data organization, so the specific block/microstructure mechanics no longer describe how current 4D databases are stored on disk. The note is preserved value chiefly as a historical explanation of the classic engine's design philosophy and constraints.

**References to newer/updated information:**
- 4D replaced its classic 128-byte-block data engine with the 4D SQL/CoreData storage engine starting around 4D v11 SQL (2007)
- Field deletion restrictions and manual structure-conversion techniques described here (e.g., forcing conversion via APPLY TO SELECTION) reflect the classic engine and do not describe current 4D storage internals
- The single-file .4DD/.data deployment/backup simplicity philosophy described has been preserved conceptually in later 4D storage engines
