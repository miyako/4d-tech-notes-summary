# Tech Note: How to quit 4D Server while running stored procedures

**Author:** Not specified
**Published:** February 1, 1998 | **Product/Version:** 4D Server v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11795

## Overview
This Tech Note describes the correct procedure for shutting down 4D Server v6 when stored procedures are actively executing. Stored procedures — 4D methods running on the server machine in their own processes — were a new feature in v6, and their asynchronous nature required careful handling during server shutdown.

## Key Points
- **Stored procedures** are 4D methods executed on the server within dedicated 4D processes, independent of any connected client.
- **Graceful shutdown** requires waiting for stored procedure execution to complete before stopping the server.
- **Client disconnection** must be handled properly prior to server shutdown to avoid data loss or corruption.
- **Operational guidance** for multi-user 4D Server deployments.

## Featured Technology
- 4D Server v6 stored procedures
- Server-side process execution
- Client/server disconnect and shutdown coordination

## Historical Context
**Status:** Superseded

Stored procedures remain a core feature of 4D Server, but the process management and shutdown APIs have been significantly modernized since v6. Modern 4D Server provides the ON SERVER SHUTDOWN database method for structured cleanup, and preemptive processes (introduced in v15) changed the concurrency model fundamentally. The specific shutdown technique described in this 1998 note is outdated, though the underlying concern — graceful server shutdown with active background processes — remains a valid operational requirement.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
