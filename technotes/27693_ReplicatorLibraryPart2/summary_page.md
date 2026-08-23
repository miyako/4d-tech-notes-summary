# Tech Note: Replicator Library (Part II)

- **Asset ID:** 27693
- **Tech Note #:** 03-19
- **Published:** April 16, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac OS X
- **Author:** Simon J Wright, Chief Systems Architect, Knowledge Sharing Systems, Inc.
- **Page URL:** https://kb.4d.com/assetid=27693
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_16-20_(APR)/03-19_Replicator_Library_2.hqx

## Overview

Simon J Wright continues his two-part exploration of the Replicator code library, a third-party add-on for near-real-time database replication between 4D Server installations built on top of the 4D Open for 4D plug-in. This second installment focuses on architectural trade-offs -- push vs. pull, ownership and key design, trigger usage, collision handling, and topology -- rather than basic setup, which was covered in Part I.

## Key Points

- Motivates replication with concrete scenarios: WAN performance for remote 4D Client access, security-driven data subsetting, spreading load across servers, and merging data from multiple physical locations (illustrated with a North Carolina/South Carolina example).
- Surveys 4D Open for 4D's capabilities (simultaneous multi-server connections, cross-platform, record/array/variable binding) and idiosyncrasies (no direct Create Record equivalent, no automatic locked-record signaling, no subtable support, per-five-connections license consumption).
- Explains push (Replicator's approach) vs. pull replication, and how Replicator tracks local changes to push using the `rpl_Queue` table rather than diffing entire databases.
- Solves the multi-server ownership problem -- avoiding duplicate primary keys created independently on different servers -- via site-prefixed alpha keys (e.g., `ABC0001` vs. `DEF0001`).
- Argues triggers (via Database Events: Save New/Existing Record, Delete Record) are the right place to *capture* changes but the wrong place to *transmit* them, since a hung remote connection in a trigger would stall the entire local server.
- Describes near-real-time (not real-time) replication as the practical target, with a throttleable process delay trading off replication lag against local server performance.
- Details the "most recent" collision-resolution rule used when the same record is changed on two servers within the replication delay window, and Replicator's use of a dedicated "Replication" user group so trigger code can distinguish locally-originated changes from incoming replicated ones (avoiding "replication ping-pong" in two-way/peer topologies).
- Surveys replication topologies -- one-way two-node, two-way two-node, hierarchical, and full peer -- and their differing resilience/complexity trade-offs.
- Documents the library's two tables (`rpl_Configuration`, a single-record BLOB config store; `rpl_Queue`, with Seq/TableNum/KeyValue/ReplicationType/Status/DateTimeStamp/Targets fields) and key project methods: `rpl_Initialize`, `rpl_Trigger`, `rpl_ReplicationService`, `rpl_RS_Replicate`, and `rpl_RS_ReplicateToServer`.
- Notes Replicator augments rather than replaces 4D Backup, recommending Backup always remain in use even where replication is deployed.

## Featured Technology

- Replicator code library (rpl_Queue / rpl_Configuration tables)
- 4D Open for 4D plug-in (remote-server connectivity)
- Push-based, trigger-captured near-real-time replication
- Ownership fields and site-prefixed keys for multi-server uniqueness
- Most-recent-wins replication collision resolution
- Replication topology design (one-way, two-way, hierarchical, peer)

## Historical Commentary

**Status:** Superseded

Simon J Wright, in this second of two Tech Notes, digs into the design trade-offs behind the third-party Replicator code library: push-vs-pull replication, record ownership and site-prefixed keys to avoid duplicate primary keys across servers, why triggers are a good place to capture changes but a bad place to transmit them, near-real-time (not real-time) replication via a queue table, and a "most recent wins" rule to resolve replication collisions using a dedicated Replication user group to avoid replication ping-pong. Replicator itself is a bespoke, 4D Open-dependent library from a third party and has certainly been superseded as a product; 4D Open has itself been superseded by 4D's built-in remote/ORDA connectivity for talking between 4D databases, and modern distributed 4D architectures increasingly rely on ORDA and REST-based datastore access rather than 4D Open point-to-point connections. That said, the conceptual material on replication design (ownership, collision resolution, topology trade-offs, why triggers shouldn't do slow work) remains a solid, still-applicable primer for anyone designing a multi-server synchronization system in any technology.

References to newer/updated information:
- The specific Replicator library and its dependency on the 4D Open for 4D plug-in are obsolete; 4D Open has been superseded by 4D's built-in remote datastore/ORDA access for connecting to other 4D databases
- Modern 4D applications needing data synchronization between servers typically build on ORDA remote datastores and REST APIs rather than a bespoke trigger-plus-queue-table replication library like this one
- The general replication-design concepts discussed (ownership fields, site-prefixed keys, push vs. pull, collision resolution, avoiding heavy work in triggers) remain valid, technology-agnostic distributed-systems knowledge
