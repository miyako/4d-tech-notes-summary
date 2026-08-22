# Tech Note 98-16: Simulating the DISPLAY RECORD command

**Author:** Not specified in source document
**Published:** May 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11799
**Download:** Not available

## Proposition
This Tech Note provides an alternative to the DISPLAY RECORD command that allows browsing records one by one with navigation buttons, without locking records — particularly useful in client/server and read-only data contexts.

## Key Points
- Simulates DISPLAY RECORD without record locking
- Provides Next, Previous, First, and Last navigation buttons
- No requirement for users to double-click in a list
- Ideal for client/server environments to avoid record contention
- Also suitable for read-only data delivery (e.g., CD-ROM)

## Featured Technology
- DISPLAY RECORD
- 4th Dimension
- Client/Server
- Record Navigation

## Context / Positioning
Record locking was a significant concern in 4D client/server environments. CD-ROM data distribution was a common deployment model in the late 1990s.

## Historical Commentary
**Status:** Historical Interest Only

The record navigation pattern described here addresses a fundamental UI concern that persists conceptually in 4D development, though the specific implementation details have evolved with modern list box and entity selection approaches. The concern about record locking in client/server remains relevant in principle.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
