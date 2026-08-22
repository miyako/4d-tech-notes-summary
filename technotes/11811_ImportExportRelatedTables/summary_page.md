# Tech Note 98-28: Import and Export Data From Related Tables

**Author:** Not specified in source document
**Published:** August 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11811
**Download:** Not available

## Proposition
This Tech Note provides two solutions for importing and exporting data from related tables in 4D — using Quick Reports and using 4D's Communication programming commands — since the built-in import/export menus only support the current table.

## Key Points
- Built-in Export/Import Data menus only work with the current table
- Solution 1: Quick Report to generate a text/ASCII document with related data
- Solution 2: Programming with SET CHANNEL, SEND PACKET, RECEIVE PACKET, SEND RECORD
- Quick Report output can be imported into other applications
- Programming approach works in both Runtime and User mode

## Featured Technology
- Import/Export
- Related Tables
- Quick Report
- SET CHANNEL
- SEND PACKET
- RECEIVE PACKET

## Context / Positioning
The inability to import/export related table data through 4D's standard menus was a frequently encountered limitation that drove developers to find programmatic workarounds.

## Historical Commentary
**Status:** Superseded

Importing and exporting data from related tables remains a common requirement, though modern 4D provides much more sophisticated data exchange capabilities through ORDA, JSON/XML support, and built-in import/export enhancements. The workarounds described here reflect the limitations of 4D v6's built-in import/export menus.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
