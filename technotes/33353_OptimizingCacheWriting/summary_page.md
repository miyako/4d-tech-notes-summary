# Tech Note 04-29: Optimizing Writing to the Cache with 4th Dimension

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** July 22, 2004 | **Product/Version:** 4th Dimension v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=33353
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_26-30_(JUN)/04-29_Writing_to_Cache.exe

## Overview
This Tech Note explains that writing the cache to disk — covering index pages, records, and deletion markers — was optimized starting with 4th Dimension 2003, producing significant performance improvements that were especially noticeable on Mac OS systems with slower disks or in databases holding large amounts of data. It structures its coverage around four themes: what the cache is, what it contains, how writing to the cache was optimized in 4D 2003, and how to properly configure cache memory size in 4D 2003. This reflects the deeply disk- and memory-bound nature of 4D's classic data engine architecture in the mid-2000s, where the cache sat between application logic and the physical data/index files on disk, and correctly sizing and managing that cache was one of the most direct levers a developer had over application responsiveness, especially before solid-state storage became common. As a performance-tuning guide, the note targets 4D developers and administrators responsible for keeping data-intensive 4D 2003/2004 applications running efficiently on the hardware of the era.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- An explanation of how 4th Dimension's data cache works and how writing the cache (index pages, records, deletion markers) to disk was optimized in 4th Dimension 2003, with guidance on setting cache memory.

## Featured Technology
- 4D data cache
- Cache-to-disk write optimization
- Cache memory sizing

## Historical Context
**Status:** historical interest only

This note's specific advice — tuned around Mac OS-era mechanical disk latency and 4D 2003's particular cache-flushing optimizations — reflects hardware and software conditions that have since been overtaken by SSD storage, vastly larger available RAM, and successive internal improvements to 4D's data engine and cache management across many subsequent versions. The general principle that cache sizing and disk write behavior affect 4D performance remains conceptually true, but the concrete recommendations here are dated enough to be of historical interest only rather than directly actionable guidance for current 4D deployments.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
