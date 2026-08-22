# Tech Note 25-02: Cache information and management

**Author:** Thomas SCHLUMBERGER, Technical Support Engineer, 4D France.
**Published:** February 24, 2025 | **Product/Version:** 4D v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79645
**Download:** https://kb.4d.com/DLTN/TN/2025/25-02_CacheInfoAndManagement.pdf

## Proposition
The 4D cache is central to server performance, buffering structural data, records, indexes, and more to avoid slow disk access — yet its internal organization is deliberately not exposed for confidentiality and future-proofing reasons. This note explains what settings and commands ARE available to observe and influence cache behavior, and traces how cache management has evolved from 4D v6.0 to today.

## Key Points
- **Historical evolution of cache settings:** From the simple Maximum Cache in v6.0, to Flush Data frequency in 2003, to fully adaptive/live-adjustable cache sizing starting with 4D Server v16 (64-bit) via SET CACHE SIZE or the interface.
- **What's stored in cache vs. memory:** Structural definitions, records, indexes, BLOBs, selections, sets, and temporary sort/write buffers live in cache; Web Server cache, Storage content, and logs live in general memory instead.
- **Default sizing risk:** New projects default to a 400MB maximum cache (50% of available RAM cap), which must be manually enlarged as data grows or the database is deployed — an easy-to-miss production gotcha.
- **Deployment-specific settings via User Settings:** Enabling "User Settings" lets Cache values be customized per data file, stored in a settings.4DSettings JSON file distinct from the main structure.
- **Multiple introspection commands, different scopes:** GET MEMORY STATISTICS (general memory/cache sizing), Get database measures (disk/cache read-write byte and access counts, since v14.3), and Cache info (loaded cache objects snapshot, since v16, local mode only).
- **DataStoreClass.flushAndLock():** Flushes the local datastore cache and freezes it for consistent-state operations such as application snapshots.
- **4D_Info_Report component for historical monitoring:** A maintained GitHub component that generates human-readable or logged snapshots of Server cache/memory evolution, useful even when the server runs headless or as a service.
- **Distinct ORDA remote cache:** A separate, dataclass-organized client-side cache with a 30-second expiration, controllable via setRemoteCacheSettings/getRemoteCache/clearRemoteCache, independent from the classic engine cache.

## Featured Technology
- **GET MEMORY STATISTICS** — general memory/cache usage command (renamed from GET CACHE STATISTICS in v13, MEMORY STATISTICS naming from 20 R7).
- **Get database measures** — detailed disk/cache read-write metrics (since 4D v14.3).
- **Cache info** — snapshot of current cache contents (since 4D v16, local mode only).
- **Priority in Cache (Set/Get)** — fine-tuning commands for cache content retention.
- **DataStoreClass.flushAndLock()** — freezes datastore cache to a consistent state.
- **4D_Info_Report (GitHub component)** — historical cache/memory usage reporting tool.
- **ORDA remote cache** — dataclass-scoped, 30-second-expiring client cache for ORDA remote access.

## Best Practices Highlighted
1. Increase the default 400MB maximum cache size as data files grow or when deploying to production.
2. Close the Administration window (or reduce its refresh frequency) when not actively monitoring, to avoid unnecessary CPU load on the Server.
3. Use 4D_Info_Report for ongoing/historical cache monitoring, especially on headless or service-mode servers where the Administration window graphs aren't naturally visible.
4. Reflect realistic CRUD operation ratios when load-testing with large datasets to get representative cache usage patterns.

## Context / Positioning
As an update-style reference note, this Tech Note consolidates decades of cache-related evolution into a single current guide, reflecting 4D's continued emphasis on performance tuning and observability for Client-Server deployments — including newer ORDA-specific caching behavior — as applications scale and increasingly run in headless/service or remote/cloud-adjacent configurations.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
