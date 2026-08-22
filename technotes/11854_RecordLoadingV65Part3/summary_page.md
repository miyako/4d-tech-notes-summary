# Tech Note: Record Loading in 4th Dimension v6.5, Part 3

**Author:** Not specified
**Published:** October 1, 1999 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11854

## Overview
Part 3 of a series examining record loading mechanics in 4D v6.5, with particular attention to large records containing BLOBs, memory limitations, and optimizing network traffic for wide area networks.

## Key Points
- Record loading mechanics were previously taken for granted in older 4D versions
- BLOB data type introduction created scenarios with very large records
- Understanding loading behavior helps optimize performance
- Minimizing network traffic is especially important over WANs
- Covers memory limitations and their impact on record loading

## Featured Technology
- 4D v6.5 record loading engine
- BLOB (Binary Large Objects) data type
- Memory management in client-server environments
- Network traffic optimization for WAN deployments

## Historical Context
**Status:** Superseded

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). The specific v6.5 record loading mechanics described here have been extensively rewritten in subsequent 4D versions. ORDA (introduced in v17) provides entity selections with lazy loading, and modern 4D allows field-level data retrieval control through attribute selection. The 4D Server networking stack has been rewritten multiple times. However, the conceptual concerns—efficient data retrieval, BLOB handling, memory management, and WAN optimization—remain relevant for modern 4D developers.
