# Tech Note 08-43: Database Schemas and Security

**Author:** Timothy Aaron Penner, 4D Inc. Technical Services  
**Published:** December 10, 2008 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51814  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_42-44_(DEC)/08-43_Database_Schemas.zip

## Overview

4D v11 SQL Release 3 introduced SQL schema support as a fine-grained security mechanism for external database connections. Prior to v11.3, access control for ODBC and SQL connections was configured globally through SQL Preferences, applying uniformly to all tables. The schema feature enables developers to partition tables into named schema containers and assign per-schema access rights to 4D groups, providing a standards-based SQL approach aligned with how other SQL databases handle multi-user security.

## Key Points

- **Schema concept:** A schema is a logical grouping of database tables. Every database has a mandatory DEFAULT_SCHEMA that cannot be deleted or renamed; it holds all legacy tables upon upgrade to v11.3.
- **Access rights:** Each schema can grant one 4D group one of three access levels: `READ` (data only), `READ_WRITE` (data only), or `FULL` (data and structure).
- **SQL commands for schema management:**
  - `CREATE SCHEMA mytest;` — creates a new schema
  - `ALTER SCHEMA mytest RENAME TO test;` — renames an existing schema
  - `GRANT READ ON test TO TeamMembers;` — assigns read access
  - `GRANT READ_WRITE ON test TO TeamLeaders;` — assigns read-write access
  - `GRANT ALL ON test TO Managers;` — assigns full access
  - `REVOKE READ_WRITE ON test;` — revokes (sets to NOBODY)
  - `DROP SCHEMA test;` — deletes a schema (tables revert to DEFAULT_SCHEMA)
- **Table assignment:** Use `ALTER TABLE [Table_1] SET SCHEMA test;` or the Inspector panel in Structure Editor to assign a table to a schema.
- **Scope of protection:** Schemas control only external access (ODBC, direct SQL connections). Code executed within 4D (Begin SQL/End SQL blocks, SQL EXECUTE, QUERY BY SQL) always has full access regardless of schema permissions.
- **Group name syntax:** Group names with spaces or accented characters must be enclosed in brackets: `[admins!]`
- **EVERYBODY limitation:** 4D v11.3 does not allow GRANT to the EVERYBODY pseudogroup; a workaround is to create a custom group containing all users, or recreate the schema to reset it to EVERYBODY defaults.
- **Sample component:** The note includes a componentized schema editor utility with a GUI, callable via `SE_OPEN_SCHEMA_EDITOR`, allowing non-SQL developers to add, modify, and delete schemas visually.

## Featured Technology

- SQL schemas (4D v11 SQL Release 3+)
- External connection security (ODBC, pass-through)
- 4D group-based access control
- GRANT/REVOKE SQL commands
- DEFAULT_SCHEMA management
- Structure Editor Inspector panel enhancements

## Historical Context

Published December 2008, this note addresses a major feature added to 4D v11 SQL Release 3 to improve multi-user database security for businesses adopting 4D's integrated SQL engine. Schemas provided a familiar, SQL-standard way to partition and protect table access—critical for shared environments and external integrations. The note also reflects the era's emphasis on componentized solutions: developers could leverage the included schema editor component directly in their applications.

## Historical Commentary

**Status:** Superseded

The schema architecture described here remains partially relevant in modern 4D, but has been largely superseded by evolving security models. Modern 4D versions (v17+) introduced Project Mode, ORDA, and REST-based security, which shifted the focus away from SQL-level schema permissions toward object-relational and API-level role management. While the general concept of schema-based partitioning is still valid, modern 4D developers typically use the built-in Design Center role-based security system or application-level access control rather than manual schema GRANT/REVOKE commands. The sample component architecture is also deprecated; current design practices favor using 4D's native tooling rather than helper components.

**Related Updates:**
- ORDA (Object-Relational Data Model, v2018+) and Project Mode introduced a higher-level security abstraction based on entity class permissions rather than SQL schemas.
- Web/REST security evolved to use dedicated role-based authorization systems independent of SQL schema permissions.
- The componentized UI pattern for schema management is obsolete; modern 4D provides integrated design tools (Design Center) for security configuration.
- Modern 4D's SQL engine retains schema support for backward compatibility with existing databases but does not encourage new schema-based access control strategies.
