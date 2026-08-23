# Tech Note: Optimizing Writing to the Cache with 4th Dimension

- **Asset ID:** 33353
- **Tech Note #:** 04-29
- **Published:** July 22, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Mac & Win
- **Author:** Not stated in document
- **Page URL:** https://kb.4d.com/assetid=33353
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_26-30_(JUN)/04-29_Writing_to_Cache.hqx

## Overview

This note (no individual author credited in the document) explains the internal design of 4D's cache memory and a specific write-performance optimization introduced in 4th Dimension 2003. It first describes what the cache holds -- records in transit to/from disk, the bit table, record and index address tables, index pages, current selections, and other objects -- and how 4D flushes cache contents to disk either when the cache fills or on a scheduled interval (15 minutes by default), noting the resulting risk of data loss on power failure and the resulting recommendation to use a UPS. It then contrasts the pre-2003 behavior (4D v6.8), where cache objects were written to disk in the order they were originally copied into the cache -- causing the disk head to seek back and forth unpredictably -- against the 2003 optimization, where 4D first sorts pending writes into the same order as their addresses on disk, so the disk head moves consistently in one direction during a flush, yielding a significant, especially Mac-OS-and-slow-disk performance improvement. The note documents that this ordered-write behavior is enabled by default but can be toggled off via SET DATABASE PARAMETER (selector 26, value 0=enabled/1=disabled) for comparison testing, clarifies that the optimization only affects the order of the disk write itself (not the data file's structure), and closes with general guidance on sizing the cache via Database preferences or Customizer Plus and monitoring cache/record hit ratios in the Runtime Explorer.

## Key Points

- The 4D cache holds records in transit to/from disk plus the bit table, record and index address tables, index pages, current selections, and related objects.
- Cache contents are flushed to disk when the cache fills or at a scheduled interval (15 minutes by default), meaning unsaved cache contents can be lost on power failure -- hence the recommendation to use a UPS.
- Prior to 4D 2003 (i.e. in 6.8), cache objects were written to disk in the order they were copied into the cache, which could force the disk head to seek back and forth non-sequentially during a flush.
- 4D 2003 sorts pending cache writes into disk-address order before flushing, so the disk head moves consistently in one direction, yielding a significant performance gain especially on slow disks / Mac OS.
- The ordered-write optimization is controlled via SET DATABASE PARAMETER with selector 26 (0 = enabled, the default; 1 = disabled), allowing developers to compare both behaviors.
- The optimization affects only the order of writing cache data to disk, not the structure or architecture of the data file itself.
- Cache size can be configured via Database preferences or Customizer Plus, and should be tuned by monitoring cache hit ratio / record hit ratio in the Runtime Explorer until they approach 100%.

## Featured Technology

- 4D cache memory architecture (records, bit table, record/index address tables, index pages)
- Disk-address-ordered cache flushing (introduced in 4D 2003)
- SET DATABASE PARAMETER selector 26 (enable/disable ordered cache writing)
- Cache size configuration via Database preferences / Customizer Plus
- Runtime Explorer cache hit ratio / record hit ratio monitoring

## Historical Commentary

**Status:** Historical Interest Only

This note documents an internal storage-engine optimization -- ordering cache-to-disk writes by physical disk address rather than insertion order -- introduced in 4D 2003, a genuinely meaningful improvement on the spinning-disk hardware of that era, especially on Mac OS. As a low-level engine behavior rather than a developer-facing API, this optimization (and the SET DATABASE PARAMETER selector 26 toggle to control it) reflects 4D's classic cache/data-file architecture, and 4D's storage engine and cache management have continued to evolve significantly since 2003; on modern SSD-based storage, disk-seek-order optimizations of this kind are far less consequential than they were on the mechanical hard disks this note targeted, so the note is now chiefly of historical interest.

**References to newer/updated information:**
- 4D's cache and data-file storage engine has continued to evolve across two decades of releases since this 2003-era optimization was introduced
- Solid-state storage (SSDs), now the norm, has no mechanical seek time, substantially reducing the real-world benefit of disk-address-ordered cache writes on modern hardware
- Cache sizing and monitoring guidance (Database preferences, Runtime Explorer hit ratios) remains broadly applicable, though specific tuning recommendations should be revisited for current hardware and 4D versions
