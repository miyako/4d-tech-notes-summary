# Tech Note: Editing Variables Between 4D Clients

**Author:** Not specified
**Published:** January 1, 1998 | **Product/Version:** 4D Client v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11776

## Overview
This Tech Note demonstrates a 4D V6 feature that allows viewing and modifying variable contents across multiple connected 4D Clients, without using fields, semaphores, or disk-based documents for synchronization.

## Key Points
- **Cross-client variable access:** One 4D Client can view and modify variables held by another client.
- **No traditional sync required:** Bypasses fields, semaphores, and disk files.
- **New in v6:** This inter-client variable sharing was a new capability in 4D V6.
- **Use cases:** Broadcasting notifications, sharing state, lightweight inter-client messaging.

## Featured Technology
- 4D Client inter-process variable sharing
- 4D Server v6 client/server architecture
- Alternative to semaphore and field-based synchronization

## Historical Context
**Status:** Obsolete

The specific cross-client variable access mechanism described here reflects the tightly coupled client/server architecture of 4D v6. Modern 4D approaches inter-process and inter-client communication very differently. Shared objects and shared collections (introduced in v16+) provide thread-safe data sharing between processes. Server-side stored procedures and ORDA entity selections with optimistic locking have replaced the need for direct variable sharing across clients. The underlying concept of lightweight inter-client communication remains relevant, but the mechanism has been entirely redesigned.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
