# Tech Note 14-18: Using SQL in a 4D Database Application

**Author:** Timothy Tse, Technical Services Team Member, 4D Inc.
**Published:** December 19, 2014 | **Product/Version:** 4D v14.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77197
**Download:** https://kb.4d.com/DLTN/TN/2014/14-18_UsingSQLIn4D.pdf

## Proposition
This note lays out, feature by feature, how to perform the same data-definition and data-manipulation tasks in 4D using either its native command language or its built-in SQL engine — covering table creation/alteration/deletion, record selection/creation/deletion/update, and one-to-many and many-to-one relationships — giving developers a direct reference for translating between the two paradigms.

## Key Points
- **Two parallel toolkits:** every operation is shown twice — once with native 4D commands, once with equivalent embedded SQL statements.
- **Data definition covered:** Create Table, Alter Table, Drop Table, and Truncate Table in both 4D and SQL forms.
- **Data manipulation covered:** selecting, creating, deleting, and updating records via both paradigms.
- **Relationships in both worlds:** explains 'One' and 'Many' table roles and shows how to establish and query one-to-many/many-to-one relationships using both native relate-one/relate-many mechanisms and SQL joins.
- **Positioning:** frames SQL as an additional, standards-based access layer atop 4D's native relational engine, useful for developers with existing SQL skills or SQL-based tooling/integrations.
- **Practical reference structure** (parallel 4D/SQL code blocks per topic) makes it easy to look up 'how do I do X in the other language.'

## Featured Technology
- 4D SQL engine (embedded SQL)
- 4D native commands (CREATE TABLE/ALTER TABLE equivalents, QUERY, CREATE RECORD, relations)
- Side-by-side 4D-vs-SQL comparison

## Context / Positioning
Published December 2014 for 4D v14.3, well before ORDA existed; at this time, developers choosing to interact with 4D data programmatically from a query/relational mindset had exactly two options — native 4D language commands or embedded SQL — with no object/entity-based data layer yet available.

## Historical Commentary
**Status:** Still Relevant

4D's embedded SQL support and native command equivalents described here still exist and work in current 4D releases, so nothing in this note is technically broken or removed — it remains a legitimate reference for developers using either approach.

That said, since ORDA's introduction, many new 4D projects favor entity selections and `.query()`/class-based data access over both the native-command and SQL approaches shown here for day-to-day CRUD and relationship traversal, making this note a solid but no-longer-primary way to interact with 4D data.
