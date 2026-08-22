# Tech Note 07-45: An Introduction to SQL

**Author:** Chris Visaya, Technical Support Engineer, 4D Inc.
**Published:** December 5, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=48275
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_42-45_(NOV)/07-45_SQL_Intro.zip

## Overview
This note is a beginner-friendly introduction to SQL as newly, natively integrated into 4D v11 SQL, aimed at 4D developers unfamiliar with SQL. It maps SQL terminology onto familiar 4D concepts and demonstrates the three main ways to write SQL directly inside 4D methods.

## Key Points
- Terminology mapping: SQL row = 4D record, SQL column = 4D field, SQL table = 4D table.
- Sample database `BeginnerSQL.4dbase` included, showing SQL code and its results (in a list box or alert) side by side.
- `QUERY BY SQL`: runs a simple SELECT while still producing a standard 4D Current Selection; can be paired with `SET QUERY DESTINATION` to target a named set.
- `Begin SQL` / `End SQL`: enclose full, multi-statement SQL scripts (semicolon-separated), storing results into 4D variables, fields, arrays, or tables; does not create a Current Selection.
- `EXECUTE IMMEDIATE`: used within a Begin SQL/End SQL block to run a dynamically built SQL string assembled from 4D variables at runtime.
- Syntax notes: `/* */` comments inside Begin SQL/End SQL blocks vs. the standard 4D back-quote elsewhere; SQL in 4D is case-insensitive and whitespace-insensitive.
- Introduces the SELECT statement as the SQL analog (not identical) to 4D's QUERY command.

## Featured Technology
- 4D v11 SQL's native, integrated SQL engine
- `QUERY BY SQL` command
- `Begin SQL` / `End SQL` blocks
- `EXECUTE IMMEDIATE` for dynamic SQL

## Historical Context
Published in December 2007, this note documents the developer on-ramp to what was, at the time, the single largest change to the 4D language: the introduction of a native SQL engine in 4D v11, ending 4D's prior reliance on purely its own procedural/set-based query language (with ODBC as the only route to external SQL databases). This predates Project Mode (introduced in v17, 2018) and ORDA (2018+); at this point, all 4D development happened in binary Design Mode.

## Historical Commentary
**Status:** Still relevant

The three SQL invocation mechanisms taught here — `QUERY BY SQL`, `Begin SQL`/`End SQL`, and `EXECUTE IMMEDIATE` — remain part of the 4D language today largely unchanged in concept, so this note's fundamentals are still a reasonably accurate mental model for how SQL and 4D interoperate. That said, 4D has continued to develop its SQL engine since 2007, and many developers today would also consider ORDA as a higher-level, object-oriented alternative for data access rather than writing raw SQL.
