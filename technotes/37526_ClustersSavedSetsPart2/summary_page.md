# Tech Note: Clusters: Using Saved Sets Effectively - Part II

- **Asset ID:** 37526
- **Tech Note #:** 05-22
- **Published:** June 12, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=37526
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_21-24_(JUN)/05-22_Clusters_Part_II.hqx

## Overview

Kent Wilbur (Manager of Information Systems, 4D, Inc.) completes his two-part Clusters series by showing how to query the per-word Boolean cluster arrays built in Part I, using set operations to turn second-long full-text Contains searches into millisecond-scale keyword and exact-phrase lookups, including a working web front end.

## Key Points

- Benchmark on a ~6,000-record table: uncached Contains query 1219 ms (1 record found) vs. cluster Contains query 4 ms (1 record) — over 99% faster, with cluster AND/OR queries returning in 3 ms.
- `CLUSTER_DoQuery(pTable; queryText; queryType)` parses the query text into words via `CLUSTER_Text2Array`, then calls `CLUSTER_ProcessWordFinds` for AND/OR searches, or runs it in AND mode first and narrows with a traditional `QUERY SELECTION` "Contains" pass for exact-phrase matches.
- `CLUSTER_ProcessWordFinds` loads each word's Boolean array from the [Words] table and combines them using `INTERSECTION` (AND) or `UNION` (OR); for a single keyword it skips set creation entirely and directly changes the current selection for speed.
- `CLUSTER_LoadFromBLOB` converts a stored Boolean array (`BLOB TO VARIABLE`) into either a named 4D Set (`CREATE SET FROM ARRAY`) or the current selection (`CREATE SELECTION FROM ARRAY`), depending on whether a set name is passed.
- A working web interface reuses the exact same `CLUSTER_DoQuery` logic: an HTML form posts And/Or/Contains radio values to a `WEB_ClusterQuery` method invoked via 4DACTION, with `COMPILER_WEB` declaring the mapped form variables.
- Results are rendered with `.shtml` pages using `#4dloop`/`#4dif`/`#4dvar` tags, generating per-record detail links keyed by record number (since the example table has no key field) and handling three distinct "no results" error conditions.
- The note stresses turning on the 4DACTION security setting only for methods meant to be called from the web, since these are otherwise a security exposure — especially in databases converted from pre-4D-2003 versions.

## Featured Technology

- Boolean-array "cluster" set operations (UNION / INTERSECTION)
- CREATE SET FROM ARRAY / CREATE SELECTION FROM ARRAY
- BLOB-stored per-word Boolean arrays ([Words] table)
- 4DACTION-driven web query methods
- COMPILER_WEB automatic form-variable mapping
- .shtml templates with #4dloop / #4dif tags

## Historical Commentary

**Status:** Superseded

This note demonstrates a well-engineered, hand-built full-text search index using 4D's classic Sets and BLOB storage, achieving dramatic (>99%) query-time reductions that were genuinely hard to get any other way in 2005. The specific manual clustering technique has largely been superseded by decades of improvements to 4D's own query engine and indexing, and by ORDA's lazy-loaded entity selections, which address large-selection performance with a fundamentally different (and far less code-intensive) mechanism. For genuine full-text search needs today, most 4D developers would reach for a dedicated full-text index or external search engine rather than reimplementing an inverted-index-by-BLOB scheme.

**References to newer/updated information:**
- 4D's classic query engine and indexing have been substantially optimized in versions since 2005, reducing the performance gap this manual clustering technique aimed to close
- ORDA's entity selections (introduced in 4D v16 R2+) provide lazy-loaded, cursor-like access to large record sets, addressing similar performance concerns with a different, more modern mechanism
