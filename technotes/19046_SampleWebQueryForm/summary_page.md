# Tech Note: Sample Web Query Form

- **Asset ID:** 19046
- **Tech Note #:** 01-48
- **Published:** October 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Eric Saltzen, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=19046
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_46-49_(OCT)/01-48_Web_Query_Form.hqx

## Overview

Eric Saltzen (4D, Inc.) walks through building simple and advanced web-based search forms for a stock-symbol database using 4D 6.7's new semi-dynamic HTML tag set (4DSCRIPT, 4DLOOP, 4DVAR), including dynamically building and executing multi-criteria QUERY strings based on user-selected fields, comparators, and conjunctions.

## Key Points

- Database Properties are set to Start without Context (non-contextual/semi-dynamic mode) with Use 4DVAR Comments instead of Brackets enabled, and pages use the .shtm extension so 4D parses them for embedded tags before serving.
- findStockSymbol.shtm (simple form) and findStockGeneral.shtm (advanced form) are populated by a 4DSCRIPT call to WEB_QueryFormFill, which fills parallel aField/aValue arrays based on which form's name is passed as a parameter, then a 4DLOOP tag renders one HTML table row per array element.
- The advanced form additionally offers per-row AND/OR/Except conjunction and Equal-to/Not-equal-to/Less-than/etc. comparator pop-ups (hidden on the first row via a 4DIF test), with option values set to 4D's internal comparator representations for direct reuse server-side.
- On submit, WEB_QueryFormHandle calls the 6.7 command GET WEB FORM VARIABLES, builds a text array of QUERY(...) command strings conditioned on which fields were filled in (using a $includeConjunction flag and string multiplication to conditionally insert the "|" OR operator), and runs them with EXECUTE.
- Zero-match and >1000-match result sets are caught and redisplay the form with an explanatory tErrorMessage; otherwise results.shtm renders the [Stock] selection, using a 4DSCRIPT call to WEB_GetLookupURL to substitute the ticker symbol into an exchange-specific external stock-quote URL.
- WEB_FormVariable is a small convenience wrapper around Find in array(nameArray;...) that must be called only after GET WEB FORM VARIABLES has populated the name/value arrays in the same process.

## Featured Technology

- 4D 6.7 semi-dynamic (.shtm) HTML tags: 4DSCRIPT, 4DLOOP, 4DVAR, 4DIF
- GET WEB FORM VARIABLES
- EXECUTE for building/running dynamic QUERY strings
- Non-contextual (Start without Context) web publishing mode
- Dynamic query construction with AND/OR/Except conjunctions and comparator pop-ups
- 4D array-driven HTML table generation

## Historical Commentary

**Status:** Partially Superseded

This note builds a stock-symbol search form against a 4D database using 4D 6.7's new semi-dynamic HTML tag set (4DSCRIPT, 4DLOOP, 4DVAR), offering both a single-field simple form and a multi-field advanced form that emulates 4D's built-in Query Editor by letting the user pick field, comparator, and conjunction per row, then dynamically builds and EXECUTEs a QUERY string. The core idea -- a web search form against 4D data with dynamically constructed queries -- remains a bread-and-butter task today, but the specific 4D-Tags/.shtm implementation shown has been superseded by REST/ORDA-based query APIs consumed by modern JavaScript front ends. The technique of building a query string and running it with EXECUTE is also now more commonly done with ORDA's dynamic query() method rather than string-built classic QUERY/EXECUTE.

References to newer/updated information:
- 4D Tags/HTML-embedded (.shtm) web publishing has been superseded by REST/ORDA APIs consumed by client-side JavaScript applications
- ORDA's entity selection query() method now offers a safer, more structured way to build dynamic multi-criteria queries than concatenating QUERY command strings for EXECUTE
