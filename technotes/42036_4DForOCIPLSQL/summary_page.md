# Tech Note 06-09: 4D for OCI PL/SQL

**Author:** Noreddine Margoum, QA Engineer, 4D SA.
**Published:** March 3, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42036
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_09-13_(MAR)/06-09_4D_for_OCI_PL-SQL.zip

## Overview
This note demonstrates calling Oracle PL/SQL functions and procedures from a 4D application via the low-level 4D for OCI plug-in, using two deliberately simple examples: a recursive factorial function and a user/date/time-reading procedure.

## Key Points
- Briefly introduces PL/SQL as SQL extended with procedural control structures, without attempting to teach the language in depth.
- Example 1: a recursive PL/SQL "Factorial" function, created on the Oracle server via CREATE OR REPLACE FUNCTION, then invoked, then dropped.
- Example 2: a "READINFO" procedure returning the connected Oracle user, server date, and server time via SELECT ... INTO ... FROM DUAL.
- Both 4D project methods follow the same OCI lifecycle: OCIEnvCreate → allocate error handle → OCILogon → OCIStmtPrepare/OCIStmtExecute to define the routine → a second statement to run an "anonymous" PL/SQL block calling it → OCIBindByName to bind 4D variables as BIND_IN/BIND_OUT parameters → OCIStmtExecute → drop the routine → free all handles.
- Emphasizes that the BIND_IN/BIND_OUT flag on OCIBindByName is the key mechanism controlling data flow direction between 4D and PL/SQL.
- A companion test database contains both methods; developers must substitute their own Oracle connection credentials.

## Featured Technology
- 4D for OCI plug-in
- Oracle PL/SQL (functions, procedures, anonymous blocks)
- OCIEnvCreate / OCILogon / OCIStmtPrepare / OCIStmtExecute / OCIBindByName
- Oracle DUAL pseudo-table and SYSDATE

## Historical Context
Published in 2006 for 4D 2004, this note is part of a series of Tech Notes covering the low-level 4D for OCI plug-in that replaced the older, higher-level 4D Oracle plug-in. It predates 4D's own integrated SQL engine (v11, 2007) by over a year, reflecting an era when Oracle integration in 4D required hand-written OCI handle management rather than any built-in SQL layer. The specific plug-in commands are legacy, but the general pattern of invoking server-side stored PL/SQL routines with bound parameters remains conceptually valid in any Oracle integration.

## Status
**Superseded** — 4D for OCI and this style of manual OCI handle programming have been superseded by later 4D connectivity approaches, though the PL/SQL concepts themselves remain valid.
