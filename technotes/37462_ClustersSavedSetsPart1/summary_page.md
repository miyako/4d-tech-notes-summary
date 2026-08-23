# Tech Note: Clusters: Using Saved Sets Effectively - Part I

- **Asset ID:** 37462
- **Tech Note #:** 05-21
- **Published:** June 3, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=37462
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_21-24_(JUN)/05-21_Clusters_Part_I.hqx

## Overview

Kent Wilbur (Manager of Information Systems, 4D, Inc.) opens a two-part series explaining how to build "Clusters" — saved, continuously maintained Boolean-array sets, one per indexed word — to make full-text keyword search over a table dramatically faster than repeated Contains queries, illustrated with a [TextBlocks]/[Words] example database.

## Key Points

- Opens with a report-performance case study: a per-cell multi-criteria query approach taking over 20 minutes was cut to under 2 minutes by precomputing one `CREATE SET` per Genre and per State and combining them per cell with `INTERSECTION`, turning (rows × columns) multi-criteria queries into (rows + columns) single-criteria ones.
- Explains that a Set is a one-bit-per-record bitmap of membership, making it extremely memory-efficient and far faster to apply than re-running a query — but sets go stale the instant underlying data changes, which is the problem "Clusters" solve by keeping saved sets updated as records are saved.
- Credits this exact clustering technique as the real mechanism behind 4D's own online Knowledgebase's widely admired query speed since 2000 — on ordinary hardware, not a specialized SQL/Oracle backend as many assumed.
- Traces the technique's history in the 4D community: originally stored in size-limited (32,000-character) text variables, then in documents via `DOCUMENT TO BLOB` once BLOBs arrived in 4D version 6 (as documented by Steven Willis in 1999 Dimensions magazine articles).
- This note's refinement: move sets directly between the data file and 4D Sets using BLOB storage (rather than writing to a document on disk via SAVE SET/LOAD SET), and add support for exact-phrase matching on top of keyword clusters.
- The example database parses every unique word (excluding a stop-word list) out of the [TextBlocks] table's title/text fields, storing one record per word in [Words], each with a BLOB-encoded Boolean array marking which [TextBlocks] records contain that word — automatically refreshed whenever a record is saved.

## Featured Technology

- 4D Sets (bitmap-style record-membership tracking)
- CREATE SET / INTERSECTION / UNION / DISTINCT VALUES
- BLOB-encoded Boolean arrays for persistent "clusters"
- Per-word inverted index ([Words] table)
- Report-query optimization via precomputed sets

## Historical Commentary

**Status:** Superseded

This note lays out the conceptual foundation for a hand-built inverted-index search technique, grounded in a real, well-explained performance case study and 4D's own KnowledgeBase as a production example. Saved sets remain part of current 4D and the underlying idea — precompute cheap, reusable set memberships rather than re-querying — is still good practice for report-style aggregations. But the specific full-text-search clustering technique has been substantially superseded by decades of query-engine and indexing improvements, and by ORDA's entity selections for large-selection handling, making this manual approach much less necessary for new development.

**References to newer/updated information:**
- 4D's classic query engine and indexing have been substantially optimized in versions since 2005, reducing the performance gap this manual clustering technique aimed to close
- ORDA's entity selections (introduced in 4D v16 R2+) provide lazy-loaded, cursor-like access to large record sets, addressing similar performance concerns with a different, more modern mechanism
