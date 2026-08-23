# Tech Note: New 4D Pack 2004.1's Utility Commands

- **Asset ID:** 36562
- **Tech Note #:** 05-11
- **Published:** March 17, 2005
- **Product / Version:** 4D 2004.1
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=36562
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-11_4D_Pack_2004.1_Utility_Cmds.hqx

## Overview

Jamras Komoncharoensiri (4D Evangelist) documents three utility commands added to 4D Pack 2004.1 — AP Add table and fields, AP Create relation, and AP Get templates — that give developers programmatic control over building a database's tables, fields, and relations, previously only possible manually or via 4D Insider. A two-part example database demonstrates exporting a structure to XML and rebuilding it from scratch using the new commands.

## Key Points

- AP Add table and fields(tableName; fieldNamesArray; fieldTypesArray; fieldLengthsArray{; listFormTemplate{; detailFormTemplate}}) creates a table and its fields programmatically, returning the new table number (Count tables + 1 on success, 0 on invalid parameters); supports all field types except Subtable.
- Optional template parameters on AP Add table and fields apply named list/detail form templates that must already exist via the New Form Wizard.
- AP Create relation(sourceTableNum; sourceFieldNum; destTableNum; destFieldNum) — called as (manyTable, manyField, oneTable, oneField) — creates a relation with standard default properties (e.g. Auto relate one Off, Prompt if related one does not exist On), adjustable afterward via 4D's relation commands or the structure window.
- AP Get templates(templateNameArray) populates an array with the detail form template names available in the current database, handy for building a template picker UI.
- Originally motivated by 4D ODBC Pro's Assimilator tool, which uses AP Add table and fields to clone a table and its fields read from an external ODBC data source.
- Example database Part 1 (HR Manager) exports its tables/fields/relations to structure.xml using plain native 4D commands (no 4D Pack) via an "Export Structure to XML file" button.
- Example database Part 2 (New DB) recreates the entire structure from structure.xml by running the cln_ImportStructure method (via Execute Method, Ctrl+E/Cmd+E), using the new 4D Pack commands — new tables land stacked on top of one another and must be manually rearranged, and table numbering is offset by the database's default "Table 1".

## Featured Technology

- AP Add table and fields command
- AP Create relation command
- AP Get templates command
- 4D Pack plug-in (utility theme)
- Programmatic structure creation (tables, fields, relations)
- XML-based structure export/import for structure cloning

## Historical Commentary

**Status:** Superseded

This note introduces three then-new 4D Pack utility commands (AP Add table and fields, AP Create relation, AP Get templates) that let a 4D 2004.1 database programmatically create tables, fields, and relations at runtime — something previously only possible manually from the Design-mode structure window or via 4D Insider — illustrated with an example that exports a database's structure to XML and rebuilds it in a fresh database. Structure creation is largely irrelevant to modern 4D development, since current 4D (v17+) supports fully dynamic, code-first data models via ORDA and the dataclass/datastore APIs, making manual structure-window-equivalent commands like these far less central; the specific AP-prefixed 4D Pack commands themselves are effectively legacy/superseded territory today.

References to newer/updated information:

- 4D's ORDA/dataclass and datastore APIs (4D v17+) provide a modern, dynamic way to define and manipulate structure, largely superseding the need for these specific 4D Pack AP commands in new development
- 4D Pack as a distinct plug-in bundle has evolved considerably since 2005; consult current 4D documentation to confirm which of these specific AP-prefixed commands remain available in modern 4D versions
