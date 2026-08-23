# Tech Note: Native ODBC in 4D

- **Asset ID:** 34847
- **Tech Note #:** 04-46
- **Published:** November 18, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Sati Hillyer
- **Page URL:** https://kb.4d.com/assetid=34847
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_46-48_(OCT)/04-46_Native_ODBC.hqx

## Overview

Sati Hillyer (4D Evangelist) demonstrates 4D 2004's new native ODBC support -- an updated Import/Export dialog and a set of native ODBC commands -- using Microsoft Excel as a Windows-only ODBC data source to show both manual (dialog-based) and programmatic import of external data into 4D without the separate 4D ODBC plug-in.

## Key Points

- Walks through preparing an Excel workbook as an ODBC-queryable "table" by naming a highlighted range (Insert > Name > Define), then registering it as a Windows User DSN through the ODBC Data Source Administrator's Microsoft Excel Driver.
- Shows the updated User-environment Import dialog's new "From ODBC Source..." option, which surfaces registered data sources, lets the user pick the target table/columns, preview field matches, and either create a new table or import into an existing one.
- Documents the new native command set added under the "External Data Source" theme: `ODBC LOGIN`, `ODBC LOGOUT`, `ODBC SET OPTION`/`ODBC GET OPTION`, `ODBC EXECUTE`, `ODBC End selection`, `ODBC LOAD RECORD`, `ODBC CANCEL LOAD`, `ODBC SET PARAMETER`, `ODBC GET LAST ERROR`, `ODBC IMPORT`, and `ODBC EXPORT`.
- Presents a full worked custom-menu demo: `GetTableNames`/`GetFieldNames` discover existing 4D table/field metadata, and `ImportUsingODBC` logs in with `ODBC LOGIN`, dynamically builds an `ODBC EXECUTE("select * from ...")` statement referencing the discovered field list, then loads records with `ODBC LOAD RECORD(ODBC All Records)`/`ODBC CANCEL LOAD` wrapped in `START TRANSACTION`/`VALIDATE TRANSACTION`.
- Notes an important limitation the demo only pulls data into an already-existing table with matching field count/order -- it does not create tables -- and that Excel cannot serve as an ODBC source on Mac OS X (though the same native commands work against any other ODBC-compliant Mac data source).
- Points to a companion "Assimilator" Tech Note describing the more advanced 4D ODBC plug-in, which can dynamically create tables from an external schema in addition to importing data.

## Featured Technology

- 4D 2004 native ODBC Import Dialog (Import > From ODBC Source)
- ODBC LOGIN / ODBC EXECUTE / ODBC LOAD RECORD commands
- Programmatic ODBC import into an existing 4D table
- Microsoft Excel as an ODBC data source (Windows only)
- START TRANSACTION / VALIDATE TRANSACTION around ODBC loads

## Historical Commentary

**Status:** Still relevant

Sati Hillyer, a 4D Evangelist, demonstrates 4D 2004's newly native ODBC support -- an updated Import dialog that can pull directly from any configured ODBC data source, plus new native commands (ODBC LOGIN, ODBC EXECUTE, ODBC LOAD RECORD, ODBC IMPORT/EXPORT) that let developers programmatically import data (illustrated end-to-end with a Windows-only Microsoft Excel ODBC data source) without needing the separate 4D ODBC plug-in. Native ODBC support and its command set remain part of 4D today for external-database access, so the core technique is still directly usable, though most new development for cloud/API-based external data now leans toward 4D's HTTP Client and native SQL/ORDA features rather than classic ODBC for anything beyond legacy or on-premises database connectivity.

**References to newer/updated information:**
- 4D's native ODBC commands (ODBC LOGIN, ODBC EXECUTE, ODBC LOAD RECORD, etc.) remain part of the current 4D language for external ODBC data source connectivity
- 4D has since added additional connectivity options (native SQL, ORDA/remote datastores, HTTP Client with JSON) that are now often preferred for non-legacy integrations
- The Excel-as-ODBC-source workflow described here is Windows-specific and reflects Excel's now largely legacy ODBC driver support
