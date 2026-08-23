# Tech Note: Introduction to 4D for MySQL and 4D for PostgreSQL

- **Asset ID:** 34930
- **Tech Note #:** 04-47
- **Published:** November 23, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=34930
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_46-48_(OCT)/04-47_4D_for_MySQL-Postgres.hqx

## Overview

Jamras Komoncharoensiri (4D Evangelist) introduces 4D 2004's two new native connectivity plug-ins, 4D for MySQL and 4D for PostgreSQL, which talk directly to each database's own API/wire protocol -- bypassing ODBC entirely -- for improved performance and simpler setup versus the existing 4D ODBC plug-in or native ODBC commands.

## Key Points

- Frames MySQL and PostgreSQL as the two most popular open-source DBMSs and contrasts the generic-but-slower ODBC approach (Pros: generic, widely supported, portable; Cons: performance drawback, driver required, learning curve) with the new direct plug-ins.
- Covers 4D for MySQL's 28 high-level commands (Mac OS Mach-O and Windows), showing `MySQL_Connect`/`MySQL_Execute` for INSERT/DELETE/UPDATE statements built either with hard-coded values or via parameter binding using `MySQL_AddStringParameter`/`MySQL_AddLongIntParameter` and %1/%2/%3 tags (essential for BLOBs/pictures).
- Shows the `MySQL_Select`/`While(MySQL_NextRow(...)=1)`/`MySQL_Get<Type>Field`/`MySQL_CloseSelect` loop pattern for retrieving one row at a time into 4D arrays, and notes `MySQL_ErrorCode`/`MySQL_ErrorString` for error handling.
- Covers 4D for PostgreSQL's 46 low-level commands, explaining that all sessions go through a single `PGSQL_Execute` command and that callers must inspect `PGSQL_GetResultStatus` for `PGRES_COMMAND_OK` (non-SELECT) versus `PGRES_TUPLES_OK` (SELECT, requiring `PGSQL_GetRowCount`/`PGSQL_Get<Type>Value` result handling).
- Notes both plug-ins are supported on Mac OS (Mach-O) and Windows and can be used with 4th Dimension, 4D Runtime, 4D Server, and 4D Client.
- Positions the plug-ins as complementary to, not a replacement for, the existing 4D ODBC plug-in/native ODBC commands -- useful specifically when the back end is known to be MySQL or PostgreSQL and direct, non-ODBC access is desired.

## Featured Technology

- 4D for MySQL plug-in (native MySQL API, no ODBC layer)
- 4D for PostgreSQL plug-in (native PostgreSQL API, no ODBC layer)
- MySQL_Connect / MySQL_Execute / MySQL_Select / MySQL_NextRow / MySQL_Get<Type>Field commands
- MySQL_Add<Type>Parameter bound-parameter SQL execution
- PGSQL_Connect / PGSQL_Execute / PGSQL_GetResultStatus / PGSQL_Get<Type>Value commands

## Historical Commentary

**Status:** Superseded

Jamras Komoncharoensiri, a 4D Evangelist, introduces two brand-new 2004 connectivity plug-ins, 4D for MySQL and 4D for PostgreSQL, that talk directly to each database's native wire protocol instead of going through a generic ODBC driver layer, promising better performance and no ODBC data-source setup. This was the primary way to get fast, direct MySQL/PostgreSQL access from 4D in the mid-2000s; the technique has since been superseded by 4D's built-in SQL engine and, more relevantly for external databases, by native remote datastore/ORDA connectivity and modern SQL commands added in later 4D versions, making these older MySQL/PostgreSQL plug-ins largely legacy artifacts for anyone building on current 4D releases.

**References to newer/updated information:**
- 4D has since added its own embedded SQL engine (4D SQL) as well as native remote datastore/ORDA-based connectivity for external databases in later versions
- The command-based MySQL_/PGSQL_ plug-in APIs described here are legacy 4D 2004-era interfaces rather than the current recommended approach for external DB connectivity
- Direct native plug-ins for MySQL/PostgreSQL still exist in 4D's ecosystem in some form, but current projects more commonly favor 4D's built-in SQL or REST/ORDA integration patterns
