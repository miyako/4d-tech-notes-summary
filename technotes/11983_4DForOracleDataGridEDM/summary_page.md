# Tech Note: 4D for Oracle in DataGrid's Enterprise Data Module - Beta 1

## Overview
- **Technical Note 00-41**
- **Author:** Sebastian Frey, Sextant Technologies, Inc.
- **Published:** September 1, 2000
- **Product/Version:** 4D Oracle v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the sixth installment in Sebastian Frey's technical series documenting the internals of the Beta 1 release of DataGrid, a third-party data-administration application built on 4D's Enterprise Data Module (EDM) framework. Where the EDM architecture itself splits into a high-level layer (covered in an earlier note in the series) and several low-level, source-specific layers, this note zooms into one such low-level layer: 4D for Oracle, one of several plug-ins in 4D's Connectivity Products suite (alongside the 4D Open Suite, 4D ODBC, and the ODBC Driver for 4D Server). It explains that 4D for Oracle requires the Oracle client OCI libraries (version 7.3 or higher) to be separately installed, notes the platform quirk that Macintosh OCI libraries had to be specially requested from Oracle rather than downloaded, and lists the plug-in's core capabilities: connecting to one or many Oracle instances, interrogating schemas and tables, querying and sorting records, receiving data into local 4D fields/arrays/variables, and inserting/updating/deleting records. It also covers Oracle-specific preference settings exposed in DataGrid, including Asynchronous Mode (a feature unique to 4D for Oracle, not available in 4D ODBC), Auto Commit Modifications, and the 'Use OD Execute object' option. The featured technology is the 4D for Oracle connectivity plug-in as consumed through DataGrid's EDM abstraction layer.

## Featured Technology
- 4D for Oracle plug-in
- DataGrid Enterprise Data Module (EDM)
- Oracle OCI client libraries

## Historical Context
This note is the sixth in Sextant Technologies' DataGrid series, documenting how the 4D for Oracle plug-in (part of 4D's Connectivity Products suite) was integrated as a low-level data source under DataGrid's Enterprise Data Module. Both DataGrid (a third-party Sextant Technologies product) and the 4D Connectivity Products suite of that era (4D for Oracle, 4D Open Suite) are long defunct, and connecting 4D to Oracle today is typically done through modern ODBC/JDBC-style connectivity or dedicated current-era plug-ins rather than this specific 2000-era plug-in and Oracle OCI 7.3 client library combination, making this note historically interesting but not practically applicable.

## What's Changed Since
- DataGrid (the Sextant Technologies application this note documents) and its Enterprise Data Module are long discontinued third-party products
- The specific 4D for Oracle plug-in and Oracle OCI 7.3-era client library requirements described here are obsolete; connecting modern 4D applications to Oracle uses newer connectivity approaches

