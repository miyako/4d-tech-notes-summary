# Tech Note 12-18: Synchronizing an HTTP client with 4D Server v12

**Author:** Christophe Keromen, CKTI Consulting Firm
**Published:** October 4, 2012 | **Product/Version:** 4D v12.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76669
**Download:** https://kb.4d.com/DLTN/TN/2012/12-18_SyncHTTPClientAndServer.zip

## Proposition
This Tech Note explains 4D v12's new table-by-table data synchronization feature and demonstrates using it to synchronize a 4D Server over the Internet with an Adobe AIR-based client application, producing a multi-platform (Mac/Windows/Linux, and via AIR mobile ports) standalone app that stays in sync with 4D data.

## Key Points
- Introduces 4D v12's built-in data replication feature enabling any HTTP client to synchronize with a 4D Server.
- Explains that synchronization works on a table-by-table basis, with a per-table checkbox enabling change logging.
- Shows how an SQL command with parameters triggers data replication from the 4D Server side.
- Implements a concrete Adobe AIR client to consume and apply the synchronized data, targeting Mac/Win/Linux and mobile via AIR.
- Positions this as a way to build offline-capable, multi-platform companion clients for a 4D Server backend.

## Featured Technology
- 4D v12 data replication/synchronization
- Table-level change logging
- SQL-triggered replication
- Adobe AIR client (cross-platform)

## Best Practices Highlighted
1. Enable change logging only on the tables that actually need to be synchronized to limit overhead.
2. Use parameterized SQL replication calls rather than bespoke polling logic for consistency.

## Context/Positioning
Published for 4D v12.4 shortly after 4D introduced native data replication in v12, and while Adobe AIR was still a viable path to cross-platform desktop/mobile clients, before native mobile app frameworks (including 4D's own 4D Mobile) existed.

## Historical Commentary
**Status:** Obsolete

Adobe AIR has been effectively abandoned as a client platform for years (Adobe stopped its own investment and it never gained broad mobile traction), so the specific AIR-based client in this note is no longer a realistic implementation choice. 4D's own v12 table-level replication mechanism has also been superseded conceptually by later synchronization/offline strategies and by REST/ORDA-based data access, which modern clients (web, native mobile, or Qodly-built apps) use instead of a custom AIR client talking to a proprietary sync protocol.
