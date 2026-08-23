# Tech Note: 2004 ODBC Primer

- **Asset ID:** 34536
- **Tech Note #:** 04-43
- **Published:** October 28, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=34536
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_41-45_(SEP)/04-43_2004_ODBC_Primer.hqx

## Overview

Jamras Komoncharoensiri (4D, Inc.) delivers a beginner-oriented primer on ODBC fundamentals -- the driver/data-source architecture and the SQL Access Group standard -- and then documents 4D 2004's full native ODBC command set for both manual (dialog-based) and programmatic SQL access to external data sources.

## Key Points

- Defines ODBC (Open DataBase Connectivity) as a cross-platform standard (Win32, UNIX, Mac OS, OS/2) that inserts a driver layer translating application queries into DBMS-specific commands, and contrasts "Model 1" (direct access to a database file such as Excel/Access) with "Model 2" (access mediated by a full DBMS).
- Covers creating a data source via the ODBC Data Source Administrator on Windows (Control Panel > Administrative Tools) versus the ODBC Administrator on Mac OS X (Applications:Utilities), noting Mac OS X requires installing a third-party ODBC driver since none ships by default.
- Explains that ODBC has been available to 4D since v6.0 via the 4D ODBC plug-in, and that 4D 2004 newly integrates native ODBC access directly into the User environment's Import ("Import > From ODBC Source...") and Export dialogs.
- Documents the complete native "External Data Source" command theme introduced in 4D 2004: `ODBC LOGIN`, `ODBC LOGOUT`, `ODBC SET OPTION`/`ODBC GET OPTION`, `ODBC EXECUTE`, `ODBC End selection`, `ODBC LOAD RECORD`, `ODBC CANCEL LOAD`, `ODBC SET PARAMETER`, `ODBC GET LAST ERROR`, `ODBC IMPORT`, `ODBC EXPORT`.
- Shows worked SELECT examples binding results to 4D arrays (`ODBC EXECUTE($sql;arComID;arComName;arComEmail)`) or directly to fields (`ODBC EXECUTE($sql;[Company Info]Company_ID;...)`), and INSERT examples using `<<arComID>>`/`<<[Company Info]Company_ID>>` tag substitution to bind values into the SQL text.
- Provides practical SQL tips for ODBC EXECUTE: using `*` to select all columns, `SELECT COUNT(1)` for row counts, and `DISTINCT` for de-duplicated result sets, plus notes on the difference between column-specified and column-omitted INSERT statement forms.

## Featured Technology

- ODBC (Open DataBase Connectivity) architecture and driver/data-source model
- 4D 2004 native ODBC commands (ODBC LOGIN, ODBC EXECUTE, ODBC LOAD RECORD, ODBC IMPORT/EXPORT)
- SQL parameter binding to 4D arrays and fields via ODBC EXECUTE
- ODBC-based SQL INSERT with <<fieldName>> tag substitution
- ODBC Data Source Administrator setup (Windows and Mac OS X)

## Historical Commentary

**Status:** Still relevant

Jamras Komoncharoensiri, writing for 4D Inc., provides a beginner-level primer on ODBC fundamentals (the driver/data-source model, Model 1 vs Model 2 architectures) and then walks through 4D 2004's new native ODBC command set -- ODBC LOGIN, ODBC EXECUTE, ODBC LOAD RECORD, ODBC IMPORT/EXPORT -- for both binding SQL results to 4D arrays/fields and performing parameterized INSERT statements. As a foundational explainer, the ODBC concepts remain accurate and the native command set described is still present in 4D today, so the primer's core content holds up well, though modern 4D projects increasingly favor native SQL, ORDA, or HTTP/REST-based integration over ODBC for new development, particularly for cloud data sources.

**References to newer/updated information:**
- 4D's native ODBC command set described here (ODBC LOGIN, ODBC EXECUTE, ODBC LOAD RECORD, etc.) remains part of the current 4D language
- 4D has since added a native SQL engine and ORDA/remote-datastore connectivity, which are now often preferred over ODBC for new external-database integrations
- The fundamental ODBC concepts (driver, data source, SAG/SQL Access Group standard) explained in this primer remain accurate today
