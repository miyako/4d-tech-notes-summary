# Tech Note: Using the 4D API Query Commands

- **Asset ID:** 19055
- **Tech Note #:** 01-56
- **Published:** December 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Christian Cypert, 4D & WebSTAR Plug-in Evangelist
- **Page URL:** https://kb.4d.com/assetid=19055
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_57-61_(DEC)/01-56_4D_API_Query_Commands.hqx

## Overview

Christian Cypert explains how a 4D plug-in written in C/C++ can construct and execute database queries using the classic 4D Plug-in API, covering both the quick "show the native Query Editor" route (PA_QueryDialog) and the full programmatic three-stage query-building sequence (PA_OpenQuery / PA_QueryXxx / PA_CloseQuery).

## Key Points

- `PA_QueryDialog` displays 4D's built-in Query Editor directly from a plug-in, pre-populated with a specified default table (e.g. `PA_Query(1)` for Table One).
- Building a query without the dialog is a three-stage process: `PA_OpenQuery(TableNumber)` initializes the query, one or more `PA_QueryXxx` calls (String, Date, Integer, Longint, Real, Boolean, Time) define the search criteria, and `PA_CloseQuery` triggers execution.
- Query Operators mirror 4D's AND/OR/EXCEPT: `eQO_LogicalAND`, `eQO_LogicalOR`, `eQO_Except`, plus `eQO_NoOperator`, which is mandatory for the first query line since there is nothing yet to combine it with.
- Comparison Operators map to 4D's Equal/Greater/Contains style operators: `eQC_IsEqual`, `eQC_IsDifferent`, `eQC_IsGreater`, `eQC_IsGreaterOrEqual`, `eQC_IsLess`, `eQC_IsLessOrEqual`, `eQC_Contains`, `eQC_NotContains`.
- Example 1 (`TN_QueryString`) builds a single-criterion query equivalent to `QUERY([People];[People]LastName="Smith")` using `PA_QueryString` with `eQO_NoOperator`/`eQC_IsEqual`.
- Example 2 (`TN_QueryMultipleStrings`) adds a second `PA_QueryString` call joined with `eQO_LogicalAND` to also match a first name, mirroring `QUERY([People];&;[People]FirstName="John")`.
- Example 3 (`TN_QueryComplex`) combines a string, a longint (`PA_QueryLongint`), and a date (`PA_QueryDate`) criterion, introducing the `PA_Date` structure (accessed via `.fDay`/`.fMonth`/`.fYear`) populated by `PA_GetDateParameter`.

## Featured Technology

- PA_QueryDialog (native Query Editor from a plug-in)
- PA_OpenQuery / PA_CloseQuery
- PA_QueryString / PA_QueryLongint / PA_QueryDate (PA_QueryXxx family)
- eQO_LogicalAND / eQO_LogicalOR / eQO_Except / eQO_NoOperator query operators
- eQC_IsEqual and related comparison operators
- PA_Date data structure

## Historical Commentary

**Status:** Superseded

Christian Cypert shows plug-in developers how to build 4D queries programmatically from compiled C/C++ code using the classic 4D Plug-in API's PA_OpenQuery/PA_QueryXxx/PA_CloseQuery sequence, as an alternative to displaying 4D's built-in Query Editor via PA_QueryDialog, progressing from a single-field query up to a three-criteria query mirroring 4D's own QUERY command syntax. This entire technique is tied to the classic, compiled 4D Plug-in API, which has been superseded by 4D's modern plug-in/component and 4D language capabilities; a modern 4D developer would simply use the QUERY command (or ORDA entity selection queries) directly in 4D code rather than building queries from a C plug-in.

References to newer/updated information:
- The classic 4D Plug-in API (PA_* functions) shown here has been superseded by 4D's modern component/plug-in architecture and the 4D language's native QUERY and ORDA querying capabilities
- Building queries programmatically from a compiled plug-in is now rarely necessary since equivalent and more flexible querying is available directly in 4D code
