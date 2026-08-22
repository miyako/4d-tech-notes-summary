# Tech Note 11-21: Understanding the 4D v12 Cache

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** June 29, 2011 | **Product/Version:** 4D v12.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76368
**Download:** https://kb.4d.com/DLTN/TN/2011/11-21_UnderstandingCache.pdf

## Proposition
This Tech Note explains what the 4D database cache is, how 4D manages it as the sole gateway for all data-file I/O, how it changed across v11 SQL and v12, and what tools exist to observe and troubleshoot it.

## Key Points
- **What the cache is:** a large memory block fully managed by 4D (not the OS), through which all data-file access is routed.
- **v11 SQL redesign:** brought 64-bit support, improved memory management, larger/more efficient caches, and better diagnostic tools.
- **v12 refinements:** continues evolving cache performance and management further.
- **Observability:** GET CACHE STATISTICS lets developers distinguish normal cache usage from a too-small cache or a genuine malfunction.
- **Tuning tips:** FLUSH BUFFERS(*), keeping the cache resident in physical memory, the _USER_IND_COLUMNS parameter, and a v11 SQL-specific 20-second flush interval quirk.

## Featured Technology
- 4D database engine cache management
- GET CACHE STATISTICS command
- FLUSH BUFFERS(*) and cache-tuning parameters

## Context / Positioning
Published in mid-2011 as 4D v12 built on the major v11 SQL cache redesign, this note helped developers and administrators understand and correctly size a critical, but often opaque, part of the database engine's performance profile.

## Historical Commentary
**Status:** Still Relevant

The fundamental role of the 4D cache as the sole gateway between the database engine and disk I/O remains true in current 4D versions, so the conceptual explanation here is still broadly relevant.

However, specific tuning guidance (typical cache sizes, the _USER_IND_COLUMNS parameter, and the 20-second flush interval quirk of 4D v11 SQL) is dated to early-2010s hardware and 4D internals; modern installations run on far larger RAM budgets, and current 4D documentation should be consulted for up-to-date cache-sizing guidance.
