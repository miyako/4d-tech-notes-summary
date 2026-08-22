# Tech Note 06-34: Optimization and new cache management for 4D 2004

**Author:** 4D S.A.
**Published:** August 25, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44012
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_31-34_(AUG)/06-34_Cache_Management.pdf

## Overview
This note explains how 4D's in-memory cache stores address allocation tables, index pages, and records on top of the OS's own virtual memory and disk caching, and documents specific cache/memory management optimizations shipped in 4D 2004: reduced fragmentation at large cache sizes, significantly faster cache-flush write throughput, and faster record loading via better use of the OS system cache.

## Key Points
- Background on OS virtual memory (Windows 2000/XP, Mac OS X) and disk caching sets the stage for 4D's own application-level cache.
- 4D's cache stores address/allocation tables, index pages, and records, evicting lower-priority objects (mainly records) first when space runs low.
- Cache "flushing" (writing dirty data to disk) happens on a timed interval (5–30 min recommended), via `FLUSH BUFFER`, or manually — mainly to protect against crashes/power loss.
- Sizing guidance: always try to keep address/index data cached (nearly every operation needs it); cache records only if they're reused (single-use records don't benefit, and an undersized cache under heavy reuse can thrash worse than no cache at all).
- 4D 2004 improvements: (1) cache fragmentation at large sizes (up to 1 Gb) is resolved; (2) a rewritten flush algorithm dramatically improves throughput (benchmarked ~10-15 Mb/s → 40-45 Mb/s on a PowerMac G5), making the old 4D 2003 `SET DATABASE PARAMETER` cache-write-optimization selector largely unnecessary or even counterproductive; (3) record loading is up to 50% faster on higher-end machines by leveraging the OS-level system cache, with no code changes required.
- Practical tuning guidance uses the 4D Runtime Explorer's cache statistics (index page hit ratio, record hit ratio, transaction/selection hit ratios) to validate cache sizing, and recommends flushing after large deletes (100,000+ records) or big transactions.
- Ultimately, database performance is bounded by available OS-level RAM.

## Featured Technology
- 4D's internal cache/memory management (address tables, index pages, records)
- FLUSH BUFFER command
- 4D Runtime Explorer (activity/cache monitoring)
- SET DATABASE PARAMETER (legacy cache-write optimization selector)

## Historical Context
Written for 4D 2004, comparing directly against 4D 2003-era cache behavior, and benchmarked on period hardware (PowerMac G5, disks at ~50-60 Mb/s). This predates 4D's own SQL engine (v11, 2007), Project Mode (v17, 2018), and modern 64-bit memory management with vastly larger typical RAM sizes.

## Historical Commentary
**Status:** Historical interest only

The specific comparisons (4D 2003 vs. 2004 cache behavior), hardware benchmarks (PowerMac G5 throughput figures), and cache-size ceilings discussed (up to 1 Gb) are firmly tied to mid-2000s 32-bit-era systems and are no longer directly applicable to modern hardware or current 4D internals, which have continued to evolve substantially since. That said, the general cache-tuning philosophy — keep index/address data cached, size record caching to actual reuse patterns, watch hit ratios, avoid thrashing — remains conceptually sound database performance guidance applicable in spirit to any caching system, including current 4D.
