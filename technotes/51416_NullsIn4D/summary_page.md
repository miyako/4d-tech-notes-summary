# Tech Note 08-38: NULLS in 4D v11 SQL

**Author:** Chris Visaya, 4D Inc. Technical Services  
**Published:** October 30, 2008 | **Product/Version:** 4D v11 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51416  
**Download:** https://kb.4d.com/DLTN/TN/2008/MacOS/TN_2008_35-39_(OCT)/08-38_NULLS_in_4D.pdf

## Overview

4D v11 SQL introduced comprehensive support for NULL values—a SQL concept representing unknown or missing data, distinct from empty strings or zeros. This technical note explains the philosophical and practical reasons for using NULLs, how they work in 4D v11's field properties, language commands, and SQL operators, and why they are essential for correct aggregate function behavior in databases. Understanding NULLs is critical for developers upgrading from pre-SQL versions of 4D, where this concept was not formally supported.

## Key Points

- **What is a NULL?**
  - A NULL is a value that exists but whose content is unknown.
  - Conceptually different from an empty string (""), zero (0), or false (FALSE).
  - Example: In an address form, if a user leaves "Address Line 2" blank, should it be stored as NULL (unknown) or as an empty string (intentionally blank)?

- **Why Use NULLs? Aggregate Functions Example:**
  - Youth soccer league: 6 of 8 teams report end-of-season goal scores; Teams 7 and 8 do not report.
  - **If NULLs are used for unreported scores:**
    - AVG(score) = 19.83 (sum of 6 reported scores ÷ 6 teams = 119 ÷ 6).
    - COUNT(score) = 6 (unreported NULLs are excluded).
    - MIN(score) = 10 (the true minimum among reported teams).
  - **If zeros are used instead:**
    - AVG(score) = 14.875 (sum of 6 reported + 2 zeros ÷ 8 teams = 119 ÷ 8) — mathematically incorrect.
    - COUNT(score) = 8 (includes zero-defaults).
    - MIN(score) = 0 (artificially injected, not representative).
  - NULLs ensure mathematical correctness; defaulting to zero corrupts aggregate calculations.

- **Field Properties for NULL Management:**

  - **Reject NULL value input:**
    - Prevents NULL insertion at the database engine level (from both user input and code).
    - Different from "Mandatory" field property (which operates at data entry level only).
    - Does not retroactively remove existing NULLs.
    - If enabled and a NULL insert is attempted, an error is raised: "Null value cannot be inserted in field…"

  - **Map NULL values to blank values:**
    - Allows NULL insertion but converts display/access to type-specific defaults:
      - Alpha/Text → Empty String ("")
      - Numeric (Integer, Long Integer, Integer 64 bits, Real, Float) → 0
      - Date → 00/00/00
      - Time → 0:00:00
      - Boolean → FALSE
      - Picture → Empty Picture
      - Blob → Empty Blob
    - Important: The underlying NULL is preserved; if "Map NULL to blank" is toggled off later, the field reverts to NULL state (not the displayed default value).
    - Example: A query `QUERY([Table_2]; [Table_2]ID=0)` with "Map NULL to blank" OFF returns no records, even though NULL fields display as 0 in the table view.

  - **Neither property checked (default):**
    - NULLs are fully supported and preserved.
    - Fields display their default values on screen (0 for numeric, "" for text, etc.).
    - Underlying NULL state is maintained for SQL operations.

- **4D Language Commands for NULLs:**

  - **IS FIELD VALUE NULL(field):**
    - Returns TRUE if the field contains a NULL value.
    - Returns FALSE if the field contains any non-NULL value (including the default value).
    - Example: `$var:=Is field value Null([Table_2]Name)` returns TRUE even if Name displays as "".

  - **SET FIELD VALUE NULL(field):**
    - Explicitly sets a field to NULL.
    - Must be followed by `SAVE RECORD(table)` to persist.
    - Example: `SET FIELD VALUE NULL([Table_2]ID)` sets the ID field to NULL.

  - **Important Limitation:**
    - The 4D language does NOT support NULLs in variables or in non-field contexts.
    - When a NULL from a field is copied to a variable or another field, it is automatically converted to the field's default value.
    - Example: `$var:=[Table_2]ID` where ID is NULL results in `$var = 0` (not NULL).

- **SQL Commands for NULLs:**

  - **IS NULL / IS NOT NULL operators:**
    - `SELECT * FROM Table_2 WHERE ID IS NULL` — returns records with NULL ID.
    - `SELECT * FROM Table_2 WHERE ID IS NOT NULL` — returns records without NULL ID.
    - Example from note:
      ```sql
      SELECT ID FROM Table_2 WHERE ID IS NULL INTO :table_3.id
      ```
    - Unlike the 4D language, SQL operations on NULLs (via INTO a field) preserve NULL state.

  - **Aggregate Functions with NULLs:**
    - `COUNT(field)` — counts non-NULL values only (NULLs excluded).
    - `SUM(field)` — sums non-NULL values; NULL entries do not contribute.
    - `AVG(field)` — averages non-NULL values only.
    - `MIN(field)` — returns minimum non-NULL value.
    - `MAX(field)` — returns maximum non-NULL value.
    - Example (youth soccer league):
      ```sql
      SELECT SUM(score) FROM SoccerLeague INTO :$var
      -- Result: 119 (6 reported scores; 2 NULLs excluded)
      
      SELECT AVG(score) FROM SoccerLeague INTO :$var
      -- Result: 19.83 (119 ÷ 6 teams)
      
      SELECT COUNT(score) FROM SoccerLeague INTO :$var
      -- Result: 6 (only non-NULL scores counted)
      
      SELECT MIN(score) FROM SoccerLeague INTO :$var
      -- Result: 10 (true minimum)
      ```

- **Critical Distinction: Display vs. Storage:**
  - NULLs display as their default values in 4D forms and tables (0, "", etc.).
  - Internally, the NULL state is preserved.
  - Querying for the default value (e.g., `QUERY([Table];[Table]field=0)`) does NOT match NULL fields.
  - Must use `IS FIELD VALUE NULL` (4D language) or `IS NULL` (SQL) to detect NULLs.
  - This is a common source of confusion for developers new to 4D v11 SQL.

- **Designer's Choice:**
  - Developers decide whether to use NULLs based on application requirements.
  - For fields where "unknown" is distinct from "empty" or "zero", use NULLs (keep both properties unchecked).
  - For fields where "unknown" should be treated as a default value, enable "Map NULL to blank values".
  - For fields where "unknown" is not allowed, enable "Reject NULL value input".

## Featured Technology

- NULL values in SQL databases
- Field properties: "Reject NULL value input" and "Map NULL values to blank values"
- 4D language commands: IS FIELD VALUE NULL, SET FIELD VALUE NULL
- SQL operators: IS NULL, IS NOT NULL
- Aggregate functions: COUNT, SUM, AVG, MIN, MAX with NULL semantics
- SQL queries with BEGIN SQL / END SQL
- Database design patterns for data integrity

## Historical Context

Published October 2008 for 4D v11 SQL, this note addresses one of the most fundamental and often-misunderstood aspects of SQL databases. For 4D developers upgrading from earlier versions (v6, v9, v10), NULL support was a new and sometimes confusing feature. The youth soccer league example is pedagogically brilliant: it demonstrates in concrete terms why NULLs matter and what happens when developers incorrectly substitute defaults like zero. This note was essential reading for every 4D developer adopting v11 SQL, and remains valuable for anyone designing databases with 4D or SQL systems.

## Historical Commentary

**Status:** Still Relevant

The core concepts of NULL values and their behavior in SQL remain completely unchanged from 4D v11 SQL through modern 4D versions. NULL semantics are fundamental to SQL and have not evolved; queries using IS NULL and aggregate function behavior are identical today.

**Related Updates:**
- **ORDA (4D v2018+):** Introduces typed entity classes and Optional types, providing a higher-level abstraction over raw NULLs. Developers working with ORDA entities typically don't directly interact with NULLs; they work with typed attributes and validation rules instead. ORDA internally handles NULL semantics correctly (e.g., when loading from SQL).
- **Validation Frameworks:** Modern ORDA includes constraint and validation systems that can prevent NULL values or apply complex business rules, reducing reliance on low-level field properties like "Reject NULL value input".
- **SQL Layer:** The underlying SQL engine's NULL handling is identical; developers who write raw SQL (via ORDA queries, REST endpoints, or direct SQL execution) use IS NULL and aggregate functions exactly as described in this note.
- **Data Integrity:** Modern 4D emphasizes data type safety through ORDA entity classes (Optional types in TypeScript-like type definitions), which make NULL handling more explicit than it was in pre-ORDA 4D.

For developers working with 4D v11 SQL directly (without ORDA), this note remains 100% relevant and accurate. For modern ORDA developers, understanding NULL semantics is still important when writing queries, but the day-to-day interface is more abstract and type-safe.
