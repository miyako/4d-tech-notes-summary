# Tech Note 03-26: Record to BLOB

**Author:** Not specified in source document
**Published:** June 26, 2003 | **Product/Version:** 4D v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=29731
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_26-30_(JUN)/03-26_Record_to_BLOB.exe

## Overview
A Tech Note describing a technique for serializing an entire 4D record into a BLOB, addressing a gap in the classic 4D language's built-in command set.

## Key Points
- Addresses the lack of a built-in 4D command to convert an entire record's data into a BLOB.
- Describes a general technique for record-to-BLOB serialization (and, implicitly, the reverse).

## Featured Technology
- BLOB serialization
- Record storage techniques

## Historical Context
Written before 4D had native object/collection field types or built-in JSON serialization, when BLOB was the primary generic container for arbitrary structured data; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

The specific need this note addresses has been largely superseded by 4D's later native Object/Collection data types and JSON serialization commands, which now provide a far more natural, structured way to serialize record-like data than manual BLOB packing, making this note's technique obsolete for new development though still historically instructive.
