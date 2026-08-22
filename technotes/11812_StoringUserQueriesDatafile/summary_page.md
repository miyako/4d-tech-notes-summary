# Tech Note 98-29: Storing User Created Queries in the Datafile

**Author:** Not specified in source document
**Published:** August 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11812
**Download:** Not available

## Proposition
This Tech Note implements a system for storing user-created queries in the data file, enabling query reuse, sharing in client/server environments, and programmatic execution without user intervention.

## Key Points
- Stores queries in the data file for persistence and reuse
- Enables query sharing among multiple users in client/server mode
- Eliminates the need to recreate complex queries each time
- Allows developers to execute stored queries programmatically
- Includes 'SearchReport' example database with forms and methods
- Elements can be copied to other databases using 4D Insider

## Featured Technology
- Query Editor Alternative
- Stored Queries
- Client/Server
- 4D Insider

## Context / Positioning
4D Insider was a companion tool for copying design elements between databases. The concept of stored/saved queries was a practical solution to the limitations of the built-in query editor's lack of persistence.

## Historical Commentary
**Status:** Historical Interest Only

The concept of stored queries that can be shared and reused remains highly relevant in database applications. Modern 4D provides more sophisticated query capabilities through ORDA's query strings and entity selections, as well as stored procedures and preemptive processes, but the fundamental idea of saving and sharing queries persists.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
