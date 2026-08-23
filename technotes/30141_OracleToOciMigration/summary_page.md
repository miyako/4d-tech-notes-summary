# Tech Note: Migrating from 4D for Oracle to 4D for OCIusing OCI Mapper

- **Asset ID:** 30141
- **Tech Note #:** 03-44
- **Published:** October 31, 2003
- **Product / Version:** 4D Oracle 2003
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=30141
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_44-47_(OCT)/03-44_MigratingTo4DForOCI.hqx

## Overview

Jamras Komoncharoensiri, a 4D Technical Support Engineer, explains how to migrate a database built on the older 4D for Oracle plug-in to the newer, lower-level 4D for OCI plug-in, using the OCI Mapper 2003 component as a compatibility shim that automatically redirects 4D for Oracle command calls to their 4D for OCI equivalents. The note compares the two plug-ins' capabilities, documents the 25 OCI Mapper commands (11 new in the 2003 release) that map to 4D for Oracle routines, and gives a step-by-step migration procedure using 4D Insider to install the component and retokenize existing methods.

## Key Points

- Compares 4D for Oracle (high + low-level commands, Oracle 7.x/8.x) against 4D for OCI (low-level only, Oracle client 8.1.6+, adds native LOB/CLOB/BLOB support)
- OCI Mapper 2003 is a 4D component that transparently redirects 4D for Oracle low-level command calls to their 4D for OCI equivalents, avoiding a manual line-by-line rewrite
- Documents 25 mapped low-level commands in total (e.g., OD BIND TOWARDS 4D, OD BIND TOWARDS SQL, OD Create cursor, OD Login), with 11 newly added in the 2003 release (OD Execute SQL, OD COMMIT, OD ROLLBACK, OD GET SERVER LIST, OD SET NB MODE, etc.)
- Migration procedure: open in 4D Insider, install the OCI_Mapper component, add OCI_TOOL_INITVAROCI to the On Startup method, retokenize all affected methods, then replace the plug-in files in the Win4DX/Mac4DX folders
- Shows a concrete before/after SQL INSERT example using OD Set SQL in cursor / OD BIND TOWARDS SQL, unchanged by the migration once OCI Mapper is in place
- Notes that automatic tokenization of migrated methods was expected to be integrated into a future 4th Dimension release

## Featured Technology

- 4D for Oracle plug-in (legacy)
- 4D for OCI plug-in
- OCI Mapper 2003 component/framework
- OD Execute SQL / OD BIND TOWARDS SQL / OD BIND TOWARDS 4D
- OD Create cursor / OD Set SQL in cursor
- 4D Insider retokenization workflow

## Historical Commentary

**Status:** Obsolete

Both the original 4D for Oracle plug-in and this OCI Mapper migration framework are long-discontinued artifacts of 4D's early direct-database-plug-in era, and the specific OCI-level commands described here have no bearing on how 4D talks to Oracle today. Modern 4D-to-Oracle connectivity would use ODBC or 4D's native SQL/data-source connectivity rather than either of these legacy plug-ins, making this note of historical interest only for understanding how 4D's Oracle integration evolved in the early 2000s.

**References to newer/updated information:**
- The 4D for Oracle and 4D for OCI plug-ins, and the OCI Mapper component described here, are long discontinued legacy products
- Modern 4D-to-Oracle integration would typically use ODBC or other current data-source connectivity rather than either legacy plug-in
