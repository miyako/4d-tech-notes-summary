# Tech Note 04-33: Taking Advantage of Execute on Server

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** August 19, 2004 | **Product/Version:** 4D v2003.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=33643
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_31-35_(JUL)/04-33_Execute_on_Server.exe

## Overview
This Tech Note addresses a core 4D Client/Server performance concern: certain operations — notably large queries and applying formulas across large selections — can generate heavy network traffic if executed on a client machine that must repeatedly communicate with the server for each record. It explains how to use a single method to make the server itself perform the operation and return only the final result, drastically cutting the amount of client-server network chatter compared to a naive client-side implementation. The accompanying worked example updates one thousand records, run once on the client and once on the server, to concretely illustrate the performance difference this technique produces. This reflects 4D 2003/2004-era Client/Server architecture, where developers needed to consciously choose where code executed (client vs. server) to avoid needless network round-trips, since the platform did not yet have modern client-side caching or entity-based lazy loading. The note is a practical optimization guide aimed at developers building multi-user 4D Client/Server applications who need to keep network operations efficient at scale.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- A guide to using EXECUTE ON SERVER to offload network-intensive client/server operations, such as large queries or bulk formula updates, onto the server.

## Featured Technology
- EXECUTE ON SERVER
- 4D Client/Server architecture
- Network-intensive operation optimization

## Historical Context
**Status:** still relevant

The core problem this note solves — minimizing network chatter in Client/Server 4D applications by running bulk operations on the server rather than the client — remains a foundational performance consideration in 4D applications today, and the EXECUTE ON SERVER command (and its language successors) is still part of the current 4D classic language. The specific 1990s/2000s Client/Server networking constraints described are less severe on modern hardware and networks, but the architectural principle of minimizing client-server round trips for bulk data operations is timeless and still taught to 4D developers.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
