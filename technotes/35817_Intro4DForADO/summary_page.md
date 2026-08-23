# Tech Note: Introduction to 4D for ADO

- **Asset ID:** 35817
- **Tech Note #:** 05-04
- **Published:** January 27, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Sean Le
- **Page URL:** https://kb.4d.com/assetid=35817
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_01-04_(JAN)/05-04_Intro_4D_for_ADO.hqx

## Overview

Sean Le (Technical Support Engineer, 4D Inc.) introduces the 4D for ADO plug-in, which lets a 4D 2004 database (Windows or Mac) query external RDBMSs such as SQL Server, Oracle, Sybase, and MS Access via Microsoft's ADO interface over either ODBC or OLE DB, using a DBGateway_-prefixed 4D command set.

## Key Points

- 4D for ADO reaches most Windows-hosted RDBMSs (MS SQL Server, Oracle 8i/9i, Sybase ASE, MS Access) and ADO.Net-accessible sources (e.g. LDAP) from a 4D 2004 database on Windows or Mac.
- Explains ODBC (Driver Manager + per-database Driver, configured via OS-level ODBC administration tools) versus OLE DB (newer, COM-based, covers non-SQL data too) as the two layers ADO can sit on top of.
- Documents ADO's Connection, Command, and Record Set objects, with sample ODBC and OLE DB connection strings for both SQL Server and Oracle.
- DBGateway_Connect("server"; connStr) → connection ID (0 = failed) and DBGateway_Close(connID) manage the connection lifecycle.
- DBGateway_Execute runs INSERT/UPDATE/DELETE statements, either with literal values or via index-tag placeholders (%1) bound with DBGateway_AddTextParameter; errors are checked with DBGateway_ErrorCode/DBGateway_ErrorString.
- DBGateway_Select(connID; sql) returns a select reference ID; DBGateway_NextRow loops through result rows while DBGateway_GetTextField (plus sibling commands like DBGateway_GetPictureField/DBGateway_GetBlobField) reads each column, and DBGateway_CloseSelect releases the select.
- Positions the plug-in as a way to avoid hand-building custom ODBC/OLE DB integration code, giving 4D developers direct SQL access to the broader Windows RDBMS ecosystem.

## Featured Technology

- 4D for ADO plug-in
- DBGateway_Connect / DBGateway_Close
- DBGateway_Execute (INSERT/UPDATE/DELETE) and parameter binding via DBGateway_AddTextParameter
- DBGateway_Select / DBGateway_NextRow / DBGateway_GetTextField / DBGateway_CloseSelect
- ODBC and OLE DB connection strings for MS SQL Server and Oracle

## Historical Commentary

**Status:** Superseded

Sean Le, a 4D Technical Support Engineer, introduces the 4D for ADO plug-in, which let a 4D 2004 database (Windows or Mac) reach external RDBMSs — SQL Server, Oracle, Sybase, MS Access, and more — through Microsoft's ADO layer over either ODBC or OLE DB, using a DBGateway_-prefixed command set for connecting, executing statements, binding parameters, and iterating SELECT results. This was a significant integration capability in the mid-2000s when ADO/ODBC/OLE DB were the dominant Windows-centric database access standards, but 4D has since built out its own native, cross-platform SQL connectivity layer, making a Windows-only ADO bridge plug-in largely redundant for new development; it remains a relevant reference only for legacy databases still using this specific plug-in to reach older ODBC/OLE DB-only data sources.

References to newer/updated information:

- 4D's native external SQL data source support and ORDA-based remote datastore connections have superseded the need for the 4D for ADO plug-in in most current 4D development
- ADO/OLE DB is a legacy, Windows-only Microsoft technology that has itself been largely superseded industry-wide by ODBC, native database drivers, or modern data-access layers
