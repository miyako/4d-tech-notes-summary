# Tech Note 09-43: The 4D v11 SQL Data File Cache

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** November 19, 2009 | **Product/Version:** 4D v11.4 SQL | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75945
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_41-45_(NOV)/09-43_4Dv11SQLCache.pdf

## Proposition
Explains what 4D's data file cache is, why it fluctuates the way it does, how it was redesigned and enlarged in 4D v11 SQL, and what new diagnostic tools are available to observe and troubleshoot it.

## Key Points
- **The cache is 4D-managed memory**, not OS-managed, holding far more than records/indexes: structural definitions, selections, sets, transactions, sort buffers, and more.
- **Purge algorithm**: 4D first purges non-dirty (unmodified) objects, then flushes and purges again, then spills other engine objects to a "temporary files" folder next to the data file if still short on space.
- **Used-cache fluctuation is normal** — it is not a hardware cache and dropping to a low value simply means old objects were purged to make room for new ones.
- **v11 SQL cache is much larger**: up to ~4GB (vs. 2GB in 4D 2004) thanks to improved memory management; getting the largest cache requires a 64-bit OS and at least 8GB of RAM.
- **New 3-way associative addressing** eliminates sequential search for cached objects, and records now load/flush in blocks for efficiency.
- **BLOBs/Pictures are now cached** (previously stored outside the cache in 4D 2004), which can significantly increase cache usage.
- **Diagnostic charts** illustrate normal usage, "cache too small" (repeatedly plunging to 0), and "cache malfunction" (narrowing usage range) patterns.
- **New commands**: `FLUSH BUFFERS(*)` (flush + purge for diagnostics), `GET CACHE STATISTICS` (detailed memory/cache metrics), a "Keep Cache in Physical Memory" preference, and the `_USER_IND_COLUMNS` SQL system table to pre-load indexes.

## Featured Technology
- 4D data file cache (in-memory object manager)
- FLUSH BUFFERS(*)
- GET CACHE STATISTICS
- _USER_IND_COLUMNS system table (4D SQL engine)
- Keep Cache in Physical Memory preference

## Best Practices Highlighted
1. Understand your own database's access patterns before assuming a fluctuation chart indicates a problem — "normal" varies by application.
2. Use a 64-bit OS with at least 8GB RAM to reach the largest possible cache under 4D v11 SQL's still-32-bit process model.
3. Use `GET CACHE STATISTICS` at regular intervals to build empirical usage charts rather than guessing at cache size.
4. Pre-warm important indexes via `_USER_IND_COLUMNS` for predictable startup performance.

## Context / Positioning
Published as 4D v11 SQL matured, this note explained a major but largely invisible architectural improvement (a redesigned, larger, BLOB-aware cache) and gave administrators concrete tools and heuristics to size and diagnose it — important groundwork as databases and hardware were both scaling up in this era.

## Historical Commentary
**Status:** Partially Superseded

The note documents a genuine, then-important architectural improvement — 3-way associative cache addressing, larger caches, and in-cache BLOB storage — and its diagnostic tooling (`GET CACHE STATISTICS`, `FLUSH BUFFERS(*)`) remains valid in current 4D versions. The general reasoning about purge/flush behavior and interpreting used-cache fluctuation charts is still conceptually sound.

However, the specific numeric guidance is entirely a product of its era: 4D was still a 32-bit process bound by ~4GB address space limits at the time, hence the emphasis on 64-bit OSes and 8GB of RAM. 4D has been a native 64-bit application since v13 (2012), removing those addressing ceilings altogether, so a developer today would size the cache very differently and should consult current 4D documentation rather than this note's specific memory recommendations.
