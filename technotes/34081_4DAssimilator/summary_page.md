# Tech Note: Using 4D 2004 Assimilator

- **Asset ID:** 34081
- **Tech Note #:** 04-38
- **Published:** September 23, 2004
- **Product / Version:** 4D ODBC 2004
- **Platform:** Mac & Win
- **Author:** Sean Le
- **Page URL:** https://kb.4d.com/assetid=34081
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_36-40_(AUG)/04-38_Assimilator.hqx

## Overview

This technical note, written by Sean Le, documents the 4D 2004 Assimilator, a wizard-style utility built entirely on 4D's ODBC Plug-in commands to let developers migrate an existing ODBC-accessible database into a 4D database without manually recreating its structure. The note walks through the low-level ODBC Plug-in methods underlying the tool -- odbc_m_GetDataSources (using ODBC_SQLDataSources), odbc_m_GetDatabaseName (ODBC_SQLAllocConnect/ODBC_SQLConnect/ODBC_SQLGetInfo), odbc_m_GetTableList (ODBC_SQLTables/ODBC_SQLBindCol/ODBC_SQLFetch), odbc_m_GetFieldList (ODBC_SQLColumns), and odbc_m_CreateRecords/odbc_m_createtable, which prepares and executes a SELECT * query and then uses the 4D Pack command AP Add table and fields to build the destination 4D table structure. It then walks through the Assimilator's own three-tab wizard UI (Tables, Records, Preferences) for selecting a data source, choosing tables to clone, and setting conflict-handling and import-mode preferences, followed by verification steps in 4D's Design and User modes. The note positions this as a low-level, generic solution that works with any ODBC-compliant database rather than one built for a specific vendor's format.

## Key Points

- The 2004 Assimilator was built entirely from 4D ODBC Plug-in commands, so it works with any database that exposes an ODBC driver.
- odbc_m_GetDataSources calls ODBC_SQLDataSources with SQL_FETCH_FIRST then SQL_FETCH_NEXT to enumerate available ODBC data sources and drivers.
- odbc_m_GetDatabaseName chains ODBC_SQLAllocConnect, ODBC_SQLConnect, and ODBC_SQLGetInfo (InfoType 16 = SQL_DATABASE_NAME) to identify the connected database.
- odbc_m_GetTableList and odbc_m_GetFieldList use ODBC_SQLTables/ODBC_SQLColumns with ODBC_SQLBindCol to retrieve table names and field name/type/length metadata.
- odbc_m_CreateRecords prepares a 'SELECT * FROM table' statement via ODBC_SQLPrepare/ODBC_SQLExecute and imports rows record by record with CREATE RECORD/SAVE RECORD.
- The 4D Pack command AP Add table and fields programmatically creates the destination table structure in 4D from the retrieved ODBC field metadata.
- The Assimilator wizard UI offers Tables/Records/Preferences tabs, letting users choose which tables to clone and whether to import, clone-as-new, replace, or append records.

## Featured Technology

- 4D 2004 Assimilator utility
- 4D ODBC Plug-in low-level commands (ODBC_SQLDataSources, ODBC_SQLConnect, ODBC_SQLTables, ODBC_SQLColumns, ODBC_SQLFetch)
- 4D Pack command AP Add table and fields
- ODBC data source cloning into 4D structures

## Historical Commentary

**Status:** Obsolete

The 2004 Assimilator packaged 4D's ODBC Plug-in commands into a convenient point-and-click migration wizard at a time when developers otherwise had to write this ODBC plumbing by hand, as the note itself demonstrates method by method. The named Assimilator utility and the classic ODBC Plug-in command set it relies on are no longer part of current 4D distributions, so the tool itself is obsolete, though the underlying need -- migrating external SQL data into 4D -- persists today via 4D's built-in SQL engine, ODBC-based table imports, and code-based data import via the 4D language.

**References to newer/updated information:**
- The 4D 2004 Assimilator utility and its supporting ODBC Plug-in command set (ODBC_SQLDataSources, ODBC_SQLConnect, ODBC_SQLTables, etc.) are not part of current 4D releases
- Modern 4D databases typically import external data via the native SQL engine, ODBC/JDBC connections, or scripted import using current 4D language commands rather than a dedicated Assimilator tool
- 4D's later ORDA layer offers a further, more modern route for connecting external data sources without a migration wizard
