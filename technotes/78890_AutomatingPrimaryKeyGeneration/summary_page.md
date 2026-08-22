# Tech Note 22-05: Automating Primary Key Generation

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** March 17, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78890
**Download:** https://kb.4d.com/DLTN/TN/2022/22-05_Automating-PK.zip

## Proposition
4D's structure editor cannot bulk-create primary keys for pre-v14 databases; this note provides a SQL-system-table-based component to detect and auto-generate missing primary keys across an entire database in one pass.

## Key Points
- **Problem**: the standard primary key manager only detects, not creates, missing PKs for databases originating from v14+.
- **System tables**: _USER_TABLES, _USER_CONSTRAINTS (CONSTRAINT_TYPE='P'), and _USER_CONS_COLUMNS drive detection since there's no direct ORDA/native command for this.
- **hasPrimaryKey / getTablesWithoutPK**: methods that scan every table and build a collection of tables missing a primary key.
- **ALTER TABLE automation**: ADD field, MODIFY ... ENABLE AUTO_GENERATE (UUID) or AUTO_INCREMENT (Longint), then ADD PRIMARY KEY, all issued via EXECUTE IMMEDIATE inside SQL blocks.
- **Editable listbox UI**: lets developers review/rename fields and choose UUID vs. Longint before committing changes.
- **Bulk operation**: turns what could be a multi-hour manual task (hundreds of tables) into a one-click automated pass.
- **Positioned as a project-mode/ORDA migration enabler**: primary keys being mandatory for ORDA make this directly relevant to modernization projects.

## Featured Technology
- 4D SQL engine (Begin SQL/End SQL)
- System tables (_USER_TABLES, _USER_CONSTRAINTS, _USER_CONS_COLUMNS)
- ALTER TABLE (ADD/MODIFY/DROP PRIMARY KEY)
- AUTO_GENERATE (UUID) / AUTO_INCREMENT

## Best Practices Highlighted
1. Use SQL system tables rather than manual structure-editor clicks when bulk-auditing schema constraints.
2. Default to UUID primary keys for new auto-generated keys unless Longint auto-increment is specifically required.
3. Always provide a review step (listbox) before running irreversible ALTER TABLE operations on production schemas.

## Context / Positioning
This note supports 4D's broader push to get developers off binary-mode legacy databases and onto ORDA/project mode, addressing one of the concrete technical blockers (missing primary keys) that stands in the way of that migration.

## Historical Commentary
**Status:** Still Relevant

Still relevant today: primary keys remain a hard requirement for ORDA, and 4D has not added a built-in bulk PK-generation tool to the structure editor since this was published, so the SQL-based component approach remains a valid, still-needed workaround for legacy database modernization. The underlying SQL system tables and ALTER TABLE syntax used here are stable, long-standing 4D SQL engine features unlikely to have changed. This is a durable, still-useful utility note for anyone migrating an old 4D database.
