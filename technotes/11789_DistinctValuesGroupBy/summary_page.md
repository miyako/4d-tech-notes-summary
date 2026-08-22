# Tech Note: Distinct Values, Replacing SQL Group By, and Counting Instances

**Author:** Not specified
**Published:** May 1, 1999 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11789

## Overview
This Tech Note explains how to use 4D's procedural language to list unique values in a table, count their instances, and replicate the behavior of SQL's GROUP BY clause — all without a SQL engine, which 4D did not yet have.

## Key Points
- **DISTINCT VALUES command:** Populates an array with unique values from a field across the current selection.
- **GROUP BY equivalent:** Shows how to replicate SQL GROUP BY behavior using 4D's procedural set-based and array-based commands.
- **Instance counting:** Demonstrates counting how many records match each distinct value.
- **Pre-SQL era:** Written when 4D had no SQL engine; all data aggregation was done procedurally.

## Featured Technology
- DISTINCT VALUES command
- 4D set-based and array-based data processing
- Procedural equivalents of SQL aggregation
- Selection and query commands for data analysis

## Historical Context
**Status:** Superseded

This note is a vivid example of the pre-SQL era of 4D development. When it was written in 1999, 4D had no SQL engine — that arrived with 4D v11 SQL around 2007, which provided native GROUP BY, COUNT, and other aggregate functions. Further still, ORDA (introduced in v17, 2018) brought collection methods like `.distinct()` and entity selection-based aggregation, making the procedural workarounds described here entirely unnecessary. The DISTINCT VALUES command itself still exists in modern 4D but is now rarely needed given the richer query and aggregation options available.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
