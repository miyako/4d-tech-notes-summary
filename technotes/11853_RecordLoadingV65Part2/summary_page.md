# Tech Note 99-33: Record Loading in 4th Dimension v6.5, Part 2

**Author:** Not specified in source document
**Published:** September 1, 1999 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11853
**Download:** Not available

## Overview
Part 2 of a series examining how 4D v6.5 loads records internally, with a focus on large records containing BLOBs and the impact on memory usage and network traffic.

## Key Points
- BLOB fields (introduced in 4D v6) made it possible for individual records to be very large (up to 2 GB)
- Record loading behavior in 4D v6.5 deserved closer scrutiny due to these larger record sizes
- Understanding loading mechanics helps optimize network traffic, especially over WANs
- This is Part 2 of a multi-part series on record loading

## Featured Technology
- 4D v6.5
- BLOBs
- Record Loading
- Wide Area Networks

## Historical Context
**Status:** Historical Interest Only

This note addresses record loading mechanics in 4D v6.5, an era when BLOB fields were new and memory/network optimization was critical. The concepts of understanding record loading behavior for performance tuning remain relevant in principle, though modern 4D handles memory management and network traffic very differently with ORDA and optimized entity loading.

### Related Updates
- ORDA entity loading in 4D v17+ replaced procedural record loading patterns
- Modern 4D handles BLOB/object fields with lazy loading automatically

**Note:** The full PDF/archive for this Tech Note could not be recovered — the original download link was either missing or pointed to an obsolete format (e.g., a Windows self-extracting .exe installer). The summary above is based solely on the on-page teaser text preserved from kb.4d.com.
