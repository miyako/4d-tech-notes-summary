# Tech Note 01-22: Sending Sets

**Author:** Not specified in source document
**Published:** June 4, 2001 | **Product/Version:** 4D Client v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=14005
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_21-25_(MAY)/01-22_Sending_Sets.exe

## Overview
A technique for sending a Set from one 4D Client to other connected clients in v6.7.x without writing and reloading a temporary document. This short Tech Note addresses a client/server pain point: sending a Set (4D's lightweight structure for holding a group of record references) from one connected 4D Client to other clients.

## Key Points
- Prior to 4D v6.7.x, doing this typically required writing the set to a temporary document on disk that the receiving clients would then load — an approach with obvious overhead and cleanup concerns in a multi-user environment.
- The note shows how, starting with v6.7.x, this can be accomplished more directly, without the temporary-document round trip.
- Its featured technology is 4D's classic client/server architecture and the Sets data structure, aimed at developers building multi-user 4D applications who need to synchronize a record selection across several connected clients efficiently.

## Featured Technology
- 4D Client/Server
- Sets
- SEND SET / inter-client communication

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Partially_superseded

This note documents a v6.7.x-era improvement in 4D Client/Server for propagating a Set (a lightweight record-selection structure) from one connected client to others, avoiding the older pattern of writing a temporary document that other clients then load. Sets remain a core part of 4D's classic language today and this general mechanism is still technically usable, but 4D's client/server and multi-user synchronization story has since expanded considerably (including newer client/server messaging and, more recently, ORDA-based REST access from multiple front-ends), so the specific inter-client Set-sending pattern here is a superseded approach for most modern multi-client designs.

**Related updates since:**
- 4D's classic client/server architecture has been supplemented by ORDA and REST-based access, offering different patterns for sharing selections/state across clients
- 4D Server has gained additional built-in interprocess/network communication commands since 2001 that reduce the need for this specific workaround

