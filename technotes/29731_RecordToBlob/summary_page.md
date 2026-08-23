# Tech Note: Record to BLOB

- **Asset ID:** 29731
- **Tech Note #:** 03-26
- **Published:** June 26, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Olivier Deschanels
- **Page URL:** https://kb.4d.com/assetid=29731
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_26-30_(JUN)/03-26_Record_to_BLOB.hqx

## Overview

Olivier Deschanels (4D S.A.) presents a hand-built, versioned binary format for packing an entire 4D record into a BLOB field -- filling a gap left by the lack of any native 4D command for record-to-BLOB serialization -- useful for archiving, database-to-database record transfer, or template-record storage.

## Key Points

- Rejects the document-based SEND RECORD + DOCUMENT TO BLOB approach as too slow and file-dependent, opting instead for a custom byte-packed format written directly into a BLOB variable.
- Defines a 16-byte BLOB header: the 4-byte ASCII marker "ENRG", a routine-version byte, a record-count/compression byte, and 9 reserved bytes for future format evolution, followed by an offset table when multiple records share one BLOB.
- Per-field metadata (an integer type code plus, for variable-length types, a longint length) is written before the field values themselves, enabling schema drift detection when restoring records into a table whose structure has since changed.
- The `EVB_Store_Record` method loops over `Count fields`/`Field`/`Type` and uses `INTEGER TO BLOB`, `LONGINT TO BLOB`, `TEXT TO BLOB`, `REAL TO BLOB`, and `PICTURE TO BLOB` (via an intermediate PICT-format sub-BLOB) to serialize every supported field type using Macintosh byte ordering.
- The companion `EVB_Restore_Record` method walks the same structure to rebuild field values, and includes fallback coercions (e.g. numeric-to-boolean, alpha/text interchange) when a stored field's type no longer matches the current table's field type.
- Explicitly out of scope: changes in field order and subtable (related) field types are not handled by the described technique.

## Featured Technology

- BLOB byte-level packing (INTEGER TO BLOB / LONGINT TO BLOB / TEXT TO BLOB / REAL TO BLOB)
- Custom self-describing binary record format
- SET BLOB SIZE / COPY BLOB
- PICTURE TO BLOB for embedded images
- Field introspection (Type, Count fields, Field)

## Historical Commentary

**Status:** Superseded

In 2003, hand-packing records into BLOBs byte-by-byte was the only realistic way to get compact, structured record serialization in 4D, and this note's versioned, self-describing header design was a genuinely careful piece of engineering for its era. That need has since been almost entirely superseded by 4D's native Object and Collection data types together with JSON serialization commands (JSON Stringify/Parse, entity selections, etc.), which provide a far simpler, more maintainable way to serialize record-like data without manual offset arithmetic. The technique remains historically instructive for understanding 4D's low-level BLOB commands, but no team would build this today.

**References to newer/updated information:**
- 4D's native Object/Collection data types and JSON serialization commands (JSON Stringify, JSON Parse, etc.) now provide a much simpler way to serialize structured record data than manual BLOB packing
- ORDA entity selections offer a further modern alternative for capturing and transferring structured record data between 4D databases
