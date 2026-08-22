# Tech Note 11-15: SQL Dumps in 4D v12

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** May 12, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76331
**Download:** https://kb.4d.com/DLTN/TN/2011/11-15_SQL_Dumps_in_4D_v12.zip

## Proposition
This Tech Note covers how to perform SQL dumps in 4D v12 — exporting a database's data in standard SQL-statement format, analogous to mysqldump/exp/pg_dump — and how to re-import that data, completing a gap left by 4D v11 SQL's original SQL engine.

## Key Points
- **Historical gap:** 4D v11 SQL introduced a powerful SQL engine but no dump/export capability; v12 fills that gap.
- **SQL EXPORT DATABASE:** exports a SQL dump of the entire database's data.
- **SQL EXPORT SELECTION:** exports a SQL dump of just the current selection of a specified table.
- **SQL EXECUTE SCRIPT:** imports a previously exported SQL dump back into 4D.
- **Complete worked sample:** a sample database, full-database export example, table-selection export example, import example, sample structure definition, and sample SQL dump file.
- **Use cases:** positions SQL dumps as useful for backup, migration, and interoperability with other SQL-based tooling.

## Featured Technology
- SQL EXPORT DATABASE and SQL EXPORT SELECTION commands
- SQL EXECUTE SCRIPT command for re-importing SQL dumps
- 4D v12 embedded SQL engine

## Context / Positioning
Published in mid-2011 as 4D v12 built on the SQL engine introduced in v11 SQL, this note filled a practical gap (no dump/export tooling) that developers had encountered since 4D's SQL capabilities first appeared.

## Historical Commentary
**Status:** Still Relevant

The SQL EXPORT DATABASE/SELECTION and SQL EXECUTE SCRIPT commands documented here are still present and functional in current 4D, so this note's core technique remains a valid way to export and re-import SQL-format data dumps.

It is a niche but still-useful capability, primarily relevant when interoperating with other SQL-based systems or performing bulk data migrations; day-to-day CRUD and reporting workflows in modern 4D projects would more commonly rely on ORDA rather than manual SQL dumps.
