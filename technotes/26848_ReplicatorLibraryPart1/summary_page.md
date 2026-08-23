# Tech Note: Replicator Library

- **Asset ID:** 26848
- **Tech Note #:** 03-07
- **Published:** February 28, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Simon J Wright
- **Page URL:** https://kb.4d.com/assetid=26848
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_06-10_(FEB)/03-07_Replicator_Library.hqx

## Overview

Simon J Wright of Knowledge Sharing Systems, Inc. presents the first of two Tech Notes on Replicator, a cross-platform 4D code library distributed via 4D Insider that adds automatic, multi-server data replication to an existing 4th Dimension database. This first note covers Replicator's architecture, installation, and configuration, deferring deeper implementation details to the second part. Replicator works in two phases: capturing database events (new, modified, or deleted records) via trigger methods attached to each replicated table, which write queue entries into an rpl_Queue table, and then a background replication process/stored procedure that walks rpl_Queue, creates one target sub-record per configured remote server, opens a connection, and pushes the change — retrying on the next cycle if a target server is unreachable. Conflicts are resolved using a DateTime Stamp field normalized to Greenwich Mean Time ("Zulu time"), so a replicated record is only applied if it is newer than the local one, and per-table/per-server replication rules can be restricted further with a 4D boolean formula evaluated via QUERY SELECTION BY FORMULA. Integration requires adding Key and DateTime Stamp fields to each replicated table, wiring a trigger call (rpl_Trigger), installing the 4D Open for 4D and 4D Pack plug-ins, and configuring site codes, server addresses, and schedules through the rpl_DoConfiguration dialog, with a bundled two-site demo (North Carolina/South Carolina) walking through the whole setup end to end.

## Key Points

- Replicator captures database events (new, modified, deleted records) purely through trigger methods (`rpl_Trigger`) attached to each replicated table, ensuring changes from any source — 4D Client, Web, stored procedures, 4D Open, or ODBC — are captured uniformly into an `rpl_Queue` table.
- Each queued change record tracks a replication type (`M` for modify, `D` for delete), a status progression (`P` pending → `I` in-progress → `C` complete), and a `DateTime Stamp` normalized to Greenwich Mean Time so that a remote record is only overwritten if the incoming change is genuinely newer.
- A background replication process (recommended to run on a workstation, not as a server stored procedure) walks `rpl_Queue`, creates one target sub-record per configured remote server from the `rpl_Configuration` table, and attempts delivery to each, logging and retrying on the next cycle if a server is unreachable.
- Per-table, per-server replication can be further filtered with a developer-supplied 4D boolean rule applied via `QUERY SELECTION BY FORMULA`, so only records matching the rule are replicated to a given remote server.
- Installation is done through 4D Insider's Groups & Components drag-and-drop mechanism, requiring the 4D Open for 4D and 4D Pack plug-ins, a dedicated "Replication" password group, added Key/DateTime Stamp fields on replicated tables, and hooks in the On Startup/On Server Startup/On Server Shutdown/On Exit database methods.

## Featured Technology

- Trigger-based database event capture (new/changed/deleted records)
- rpl_Queue and rpl_Configuration replication tables
- 4D Open for 4D and 4D Pack plug-in dependencies
- TCP/IP-based server-to-server replication process
- DateTime Stamp conflict resolution (Zulu/GMT time)
- QUERY SELECTION BY FORMULA-based per-record replication rules
- 4D Insider component installation (Groups & Components)

## Historical Commentary

**Status:** Superseded

For 2003, Replicator packaged a surprisingly complete peer-to-peer replication system — trigger capture, queued delivery, timestamp-based conflict resolution, and a monitoring UI — built entirely from user-land 4D code plus the 4D Open for 4D and 4D Pack plug-ins. That third-party plug-in dependency chain (4D Open for 4D in particular) is long discontinued, making Replicator itself unusable as shipped on current 4D versions. The core replication concepts it teaches (trigger-based change capture, timestamped conflict resolution, per-target delivery queues) remain foundational to any replication design, but 4D has since built out its own remote access and synchronization capabilities (ORDA remote datastores, REST APIs, and 4D Sync/on-going data exchange tooling) that make a hand-rolled 2003-era replication library unnecessary for new projects.

References to newer/updated information:
- The 4D Open for 4D plug-in that Replicator depends on has long been discontinued, making this specific library non-functional on current 4D versions
- 4D has since introduced ORDA remote datastores and REST APIs, which provide built-in, higher-level alternatives to hand-rolled record replication between servers
