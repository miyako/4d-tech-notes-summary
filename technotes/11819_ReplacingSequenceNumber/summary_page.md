# Tech Note 98-17: Replacing the Sequence Number Command

**Author:** Not specified
**Published:** December 17, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11819

## Overview
This Tech Note explores limitations of 4D's built-in Sequence number command and presents two alternative approaches for generating sequential record numbers, including a transaction-safe method.

## Key Points
- The built-in Sequence number command is easy to use but has limitations.
- Presents two alternative methods with discussion of pros and cons.
- Extends one method to handle multiple sequence numbers within a transaction.
- Addresses concurrency and reliability concerns in multi-user environments.
- Important for business applications requiring gap-free sequential numbering.

## Featured Technology
- 4D v6.0
- Sequence number command
- Transaction management
- Multi-user concurrency handling

## Historical Context
**Status:** Historical interest only

The Sequence number command remains available in modern 4D, but auto-increment field attributes now handle most simple numbering needs automatically. ORDA's entity-level locking provides better concurrency control for record creation. The conceptual challenge of reliable sequential numbering in concurrent environments remains relevant. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
