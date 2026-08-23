# Tech Note: Data formatting

- **Asset ID:** 36473
- **Tech Note #:** 05-10
- **Published:** March 10, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=36473
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-10_Data_Formatting.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D) explains 4D's lazy on-disk record-reformatting behavior: changing a field's type does not immediately rewrite existing records, only records explicitly resaved afterward, which is both a safety net and a performance optimization but can slow down operations like SELECTION TO ARRAY when a table ends up with a mix of old and new record formats. He provides a bulk resave routine to force every record back into a consistent, current format.

## Key Points

- 4D allows changing a field's type (e.g. Alpha to Real) without export/re-import, but the stored record bytes are not rewritten unless that record is explicitly modified and resaved — until then, the display value is merely reinterpreted/converted on the fly.
- Demonstrated with a live example: retyping a field from ALPHA to REAL shows a 0 value (Num of the old string), but resaving other fields on the record does not overwrite it, and retyping back to ALPHA recovers the original text — proving the underlying bytes were untouched.
- This lazy behavior is a deliberate optimization: 4D avoids needlessly reformatting/resaving an entire large record when a change doesn't require it, and doubles as a safeguard letting you "undo" an accidental type change.
- Downside: mixed record formats within one table cause SELECTION TO ARRAY (and similar) to fall back from an optimized internal path to a slower traditional conversion path — benchmarked in the note as measurably slower until all records are resaved.
- Provides a bulk-resave loop using Count tables/Table/Count fields/Field/GET FIELD PROPERTIES to iterate every table and field, calling SAVE RECORD after forcing a no-op-equivalent modification per type (empty string append for Alpha/Text, +0 for numeric/Date/Time, reassignment for BLOB/Picture, OR FALSE for Boolean).
- Documents an undocumented (and explicitly unsupported) 4D 2004 technique using GET FIELD TITLES and the Field function to enumerate and resave subtable subfields, noting it does not work for nested subtables (which 4D no longer supports) and that GET FIELD PROPERTIES won't work on such subfield pointers.
- Warns that legacy databases upgraded across many 4D versions (v2 through 2004) are especially prone to record/structure mismatches, and recommends periodic full resaves alongside 4D Tools-based recovery to guard against performance loss and corruption risk.

## Featured Technology

- On-the-fly field type change without export/re-import
- Lazy record reformatting on SAVE RECORD
- SELECTION TO ARRAY performance impact of mixed record formats
- GET FIELD TITLES for subtable/subfield introspection (undocumented in 4D 2004)
- Bulk record resave loop (Table/Table name/Count tables/Count fields)
- 4D Tools data recovery vs. record reformatting

## Historical Commentary

**Status:** Historical Interest Only

Jean-Yves Fock-Hoon (QA Manager) explains a subtle but important 4D internals behavior: changing a field's type does not retroactively reformat already-saved records, only records that are explicitly re-saved after the change, which is both a safety net and a performance optimization but can silently leave a table with mixed on-disk record formats that slow down operations like SELECTION TO ARRAY. The note's practical fix — a loop that reloads and re-saves every record/field, with type-specific handling including an undocumented GET FIELD TITLES-based subfield-resave technique — addressed a real classic-4D data hygiene problem that is largely specific to the legacy 4D record storage engine described; it remains useful background for anyone maintaining very old 4D databases carried forward from the 2004-era engine, though the specific optimization behavior is an implementation detail of the classic (non-SQL, pre-64-bit) storage engine and less directly applicable to the modern 4D database engine.

References to newer/updated information:

- Describes internal behavior of the classic (pre-SQL, pre-64-bit) 4D record storage engine; modern 4D's storage engine has changed substantially since the 4D v13/64-bit transitions, so exact performance characteristics may differ
- The general principle of resaving records after a structural change to normalize on-disk format remains valid guidance conceptually for database maintenance in any era of 4D
