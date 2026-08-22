# Tech Note 06-10: Catalog Functions in ODBC Pro

**Author:** Noreddine Margoum, QA Engineer, 4D S.A.
**Published:** March 12, 2006 | **Product/Version:** 4D ODBC v2004 | **Platform:** Win
**Page:** https://kb.4d.com/assetid=42143
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_09-13_(MAR)/06-10_Catalog_ODBC_Pro.zip

## Overview
This note explains and demonstrates the "catalog" commands of the ODBC Pro plug-in — a family of ODBC_SQL* commands used to describe an external database's structure (tables, columns, keys, privileges, procedures, and data types) programmatically from 4D.

## Key Points
- Lists the full catalog command set: ODBC_SQLTables, ODBC_SQLColumns, ODBC_SQLStatistics, ODBC_SQLSpecialColumns, ODBC_SQLPrimaryKeys, ODBC_SQLForeignKeys, ODBC_SQLTablePrivileges, ODBC_SQLColumnPrivileges, ODBC_SQLProcedures, ODBC_SQLProcedureColumns, and ODBC_SQLGetTypeInfo.
- Two main use cases: building dynamic SQL requests at runtime, and optimizing queries by leveraging known relations/indexes.
- Explains primary key vs. foreign key concepts with a simple Employee/Service table example.
- Standard usage pattern for all catalog commands: allocate a statement handle (ODBC_SQLAllocStmt), call the catalog command, bind result columns by position (ODBC_SQLBindCol), fetch rows (ODBC_SQLFetch), then free the statement (ODBC_SQLFreeStmt).
- Provides full code examples for retrieving column privileges (ODBC_SQLColumnPrivileges) and column metadata — names, types, sizes (ODBC_SQLColumns).
- Includes a test database that lets a developer connect to any configured ODBC data source and interactively exercise every catalog command.

## Featured Technology
- ODBC Pro plug-in
- ODBC catalog/metadata introspection commands
- Dynamic SQL request construction
- 4D 2004 procedural language

## Historical Context
Published in 2006, this note predates 4D's own integrated SQL engine (introduced in 4D v11, 2007) and reflects an era when connecting 4D to external SQL databases required the standalone ODBC Pro plug-in with its dedicated command set. The concept of querying database catalog/metadata to build dynamic SQL remains a standard integration technique today, but the specific ODBC Pro plug-in and its ODBC_SQL* commands are a legacy layer distinct from 4D's later native SQL and ODBC connectivity features.

## Status
**Superseded** — the underlying concept (catalog-driven dynamic SQL) is still valid, but the specific plug-in and command set have been superseded by 4D's native SQL/ODBC capabilities introduced in later versions.
