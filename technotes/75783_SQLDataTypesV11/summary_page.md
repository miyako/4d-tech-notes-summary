# Tech Note 09-22: SQL Data Types in 4D v11 SQL

**Author:** Chris Visaya, Technical Services Team Member, 4D Inc.
**Published:** June 4, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75783
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_22-26_(JUN)/09-22_sqlDataTypes.pdf

## Proposition
This note is a concise reference for how standard SQL column types map to 4D's native field types when using 4D v11 SQL's Data Definition Language to create tables and fields programmatically.

## Key Points
- **Full type mapping table:** VARCHAR→Text, REAL→Real, NUMERIC→Int 64-bit, FLOAT→Real, SMALLINT→Integer, INT→Longint, BIT/BOOLEAN→Boolean, BLOB→BLOB, CLOB/TEXT→Text, TIMESTAMP→Date/Time, DURATION/INTERVAL→Time, PICTURE→Picture.
- **VARCHAR(n)** creates a bounded alpha field up to 255 characters; specifying more triggers an error; omitting the size creates a full Text field.
- **VARCHAR, TEXT, and CLOB** all ultimately create 4D Text fields, but **CLOB fields are not indexable**, mirroring their traditional RDBMS role as external large-object text storage.
- Fields created via SQL DDL behave **identically** to fields created through the Structure editor — fully interoperable with classic structure tools.
- Numeric precision nuances (Real vs. Int 64-bit vs. Numeric/Float) and Boolean/Duration/Timestamp handling are documented for developers new to the mapping.

## Featured Technology
- 4D v11 SQL Data Definition Language (CREATE TABLE)
- SQL-to-4D type mapping (VARCHAR, TEXT, CLOB, NUMERIC, TIMESTAMP, DURATION, etc.)
- 4D field types (Text, Real, Integer, Longint, Boolean, BLOB, Picture, Date/Time, Time)

## Best Practices Highlighted
1. Use CLOB deliberately (and accept the indexing tradeoff) only when large, non-indexed text storage is genuinely needed.
2. Specify a bounded VARCHAR(n) rather than an unbounded Text field when a hard length limit is meaningful to the data model.
3. Treat SQL-created and Structure-editor-created fields as fully interchangeable — no special handling needed for one versus the other.

## Context / Positioning
Published shortly after 4D introduced its SQL engine, this note gave developers a quick, authoritative type-mapping reference to avoid guesswork when adopting SQL-based structure creation for the first time.

## Historical Commentary
**Status:** Still Relevant

This note documented how 4D v11 SQL's newly introduced SQL Data Definition Language mapped standard SQL column types onto 4D's native field types — a genuinely useful reference at a time when SQL-based structure creation was new to 4D developers. This type-mapping information is still accurate today, since 4D's SQL engine and underlying field type system have remained fundamentally the same.

ORDA-based entity models are now often the preferred way to model and access 4D data day-to-day, with SQL DDL/DML serving as an alternate, still fully-supported access path rather than the primary one.
