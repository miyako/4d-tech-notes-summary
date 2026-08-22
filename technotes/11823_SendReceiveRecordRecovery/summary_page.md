# Tech Note: Using Send/Receive Record to Recover, Replace or Update

**Author:** Not specified
**Published:** January 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11823

## Overview
This Tech Note describes using the SEND RECORD and RECEIVE RECORD commands to move data between two 4D databases for recovery, migration, version upgrades, or structural changes.

## Key Points
- Covers multiple scenarios: abandoning obsolete structures, delivering partial data to clients, recovering from corruption, version upgrades, and faster v3-to-v6 migration.
- SEND RECORD and RECEIVE RECORD provide record-level inter-database data transfer.
- Especially useful when standard data file conversion fails or produces errors.
- For very large v3 data files, export/import could be faster than direct v6 conversion.

## Featured Technology
- 4D v6.0
- SEND RECORD / RECEIVE RECORD commands
- Data migration and recovery
- Database version conversion

## Historical Context
**Status:** Obsolete

While SEND RECORD and RECEIVE RECORD remain available in modern 4D, they are rarely used. Modern 4D provides SQL, ORDA, JSON, and XML-based import/export mechanisms that offer more flexible data migration. 4D's data file maintenance and recovery tools have also improved significantly. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
