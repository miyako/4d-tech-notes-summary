# Tech Note 09-07: 4D v11 SQL Assimilator

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** February 17, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75182
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_05-08-(FEB)/09-07_4D_v11_SQL_Assimilator.zip

## Proposition
Documents 4D v11 SQL Assimilator, a component-based migration wizard that uses 4D's new native SQL engine to reproduce tables and import data from third-party SQL databases or older 4D databases into a new or existing 4D v11 SQL database.

## Key Points
- **Native-SQL implementation:** unlike prior Assimilator versions that depended entirely on the 4D ODBC/ODBC Pro plugins, this one reads external system tables using 4D's own native SQL parser, connecting directly to 4D v11 SQL Server without ODBC.
- **Broad source support:** works with MySQL 5, SQL Server 2000, MS Access (via ODBC), and other 4D v11 SQL or pre-v11 4D databases.
- **Component-only footprint:** Assimilator adds no permanent methods to the host database, so it can be installed just for a migration and then removed.
- **Type-mapping caveats:** flags special-character issues in table/column names and notes vendor-specific type quirks (e.g., MySQL's ENUM maps to a sized 4D Alpha field).
- **Three-page Wizard:** table/field selection (with unsupported SUBTABLE/UNDEFINED fields auto-excluded), a record preview page, and an Action Preferences page controlling create/replace behavior and per-cycle batch import size.
- **Tunable batch import:** a size-based "ruler" auto-calculates records-per-cycle, with a manual lock option to set an exact byte-per-cycle value.

## Featured Technology
- 4D v11 SQL Assimilator component using native 4D SQL to read system tables of external databases
- ODBC-based connections to MySQL, SQL Server 2000, MS Access; direct connection to 4D v11 SQL Server
- Wizard UI for table/field selection, record preview, and cycle-based (chunked) batch import
- Automatic table/data-type migration into a new or existing 4D v11 SQL structure

## Best Practices Highlighted
1. Test and adjust an assimilation on a disposable empty host database before running it against the final target.
2. Rename table/column names containing special characters after assimilation to avoid trouble with 4D's native SQL engine.
3. Review data types of assimilated fields (especially variable-size types like BLOB/TEXT/ENUM) rather than assuming automatic type mapping is exactly what you want.
4. Tune "records per cycle" based on available memory rather than importing an entire large table in a single pass.

## Context / Positioning
Positioned as a rewrite of a long-standing 4D productivity tool (dating to 1999) to showcase and stress-test 4D v11 SQL's brand-new native SQL engine on the practical, high-value task of database migration.

## Historical Commentary
**Status:** Deprecated

This note captures 4D's first all-native-SQL migration tool, built specifically to interoperate with 2009-era database versions (SQL Server 2000, MySQL 5, Access) via ODBC/DSN connections and vendor-specific system-table parsing.

4D's SQL engine and connectivity options have advanced considerably since, and the specific vendor versions and ODBC-centric workflow this component targets are long outdated. While the general need for one-time data migration into 4D remains, current developers would typically use up-to-date ODBC/SQL connectivity, dedicated migration scripts, or ORDA-based remote data access rather than this specific legacy Assimilator component.
