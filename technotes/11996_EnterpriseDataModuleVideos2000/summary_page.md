# Tech Note: The Enterprise Data Module: The Videos2000 Example Database

- **Asset ID:** 11996
- **Tech Note #:** 00-59
- **Published:** December 2000
- **Product / Version:** 4D DataGrid Beta 1
- **Platform:** Mac & Win
- **Author:** Sebastian Frey
- **Page URL:** https://kb.4d.com/assetid=11996
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_56-60_(DEC)/00-59_EDM_Videos2000.hqx

## Overview

Sebastian Frey, Web Developer Tools Evangelist at 4D, Inc., uses the Videos2000 sample application to demonstrate the Enterprise Data Module (EDM), a Beta 1 DataGrid toolkit abstraction that lets one 4D code base query, display, and replicate data across the local 4D database, a remote 4D Server, Oracle, and ODBC sources through a uniform Model/Query API.

## Key Points

- EDM_ConnectionForType(EDM_kDataOdbc) / EDM_ConnectionForType(EDM_kDataOracle) open connections to remote sources using nearly identical code paths regardless of backend type.
- APP_VideoTablesCreateDrop executes canned SQL statements stored in the [APP_VideoSQL] table via EDM_OdbSqlExecute or EDM_OraSqlExecute to create or drop remote tables on ODBC or Oracle; 4D Open (4D Server) tables must instead be copied using 4D Insider since 4D Open has no remote CREATE TABLE capability.
- APP_VideoConstraintsOnOff is Oracle-only and queries the Oracle Data Dictionary's USER_CONSTRAINTS table to detect and toggle relational integrity constraints created for the Videos2000 tables.
- APP_VideoImportExport replicates data across four EDM Models (Customers, Tracking, and two Models for Videos — one holding all non-picture columns, one holding just the primary key plus the 'fat' MoviePoster picture as a one-row Model) by creating an EDM_QueryCreate/EDM_QueryRowsAllSelect query, paging through EDM_QueryPageGoto("Next"), loading each row with EDM_ModelArrayToVariable, checking existence via row-select-by-key methods, and saving with EDM_ModelRowSave.
- One-row Models (page size of 1) are used for 'fat' columns like BLOB/Picture fields that cannot be bound to arrays, loading data into Model variables directly instead of arrays.
- The classic 4D list-detail ('drill down') UI pattern is reconstructed on top of EDM by the DataGrid GRD_ 4D Calc grid modules: a double-click handled via SP ON EVENT/GRD_GridEventDoubleClick sets a drill-down event constant and calls EDM_QueryDrillDown to open the appropriate Detail form for the current row.

## Featured Technology

- Enterprise Data Module (EDM) Models and Queries
- EDM_ConnectionForType (4D Open / ODBC / Oracle)
- EDM_QueryCreate / EDM_QueryRowsAllSelect / EDM_QueryPageGoto
- EDM_ModelRowSave / EDM_ModelArrayToVariable
- DataGrid Launcher and GRD_/CAL_ list-detail UI modules

## Historical Commentary

**Status:** Obsolete

Written by Sebastian Frey, Web Developer Tools Evangelist at 4D, Inc., this note is the seventh in a series documenting the Beta 1 DataGrid/Enterprise Data Module (EDM) toolkit, using the Videos2000 sample application to show how one code base can query and replicate data across the local 4D database, a remote 4D Server (4D Open), Oracle, and ODBC sources through a uniform Model/Query API. EDM and DataGrid were an early, ambitious 4D connectivity abstraction layer that has since been entirely superseded by 4D's native SQL/ODBC/JDBC connectivity and, more fundamentally, by ORDA's data-source-agnostic entity/entity-selection model introduced in 4D v16 (2018), making this specific API obsolete, though the underlying goal of a unified way to query multiple backend data sources is now met natively.

**References to newer/updated information:**
- 4D's ORDA layer (introduced 4D v16, 2018) now provides a native, unified entity/entity-selection abstraction over multiple data sources, superseding the third-party EDM/DataGrid toolkit shown here
- 4D has since added native SQL, ODBC, and JDBC connectivity commands, removing the need for the EDM_OdbSqlExecute/EDM_OraSqlExecute-style wrapper methods demonstrated in this note
