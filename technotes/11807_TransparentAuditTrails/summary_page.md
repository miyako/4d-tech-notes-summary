# Tech Note 98-24: Transparent Audit Trails

**Author:** Not specified in source document
**Published:** July 1, 1998 | **Product/Version:** 4D v6.0.x | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11807
**Download:** Not available

## Proposition
This Tech Note presents a transparent audit trail system for 4D V6 that uses triggers and BLOBs to automatically archive record changes with minimal code modifications to existing databases.

## Key Points
- Transparent change tracking via triggers — trivial to add to existing databases
- Archives record copies as BLOBs in an [Archive] table
- Timestamps and date-stamps all changes
- Can recover earlier versions of any changed field or record
- Supports BLOB compression and user change tracking variants
- Subtable fields are the only unsupported type
- Leverages 4D V6's trigger and BLOB capabilities

## Featured Technology
- Audit Trail
- Triggers
- BLOBs
- 4th Dimension V6
- Record Archiving

## Context / Positioning
Triggers were a powerful new feature in 4D V6, and this audit trail system showcased their potential for non-intrusive database automation. The BLOB-based archiving approach was creative for its era.

## Historical Commentary
**Status:** Historical Interest Only

Audit trails remain a fundamental requirement in database applications, and this note's transparent trigger-based approach was remarkably forward-thinking. While the specific V6 trigger and BLOB mechanisms are outdated, the architectural pattern of non-intrusive change tracking via triggers is still conceptually sound and reflects modern audit trail design principles.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
