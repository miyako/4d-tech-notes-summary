# Tech Note 10-30: Compacting Address Tables

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** October 5, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76195
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_30-33_(OCT)/10-30_Compacting_Address_Tables.zip

## Proposition
Josh Fletcher's Tech Note addresses a subtle but consequential change introduced in 4D v11 SQL: address tables (the internal structures mapping record numbers to disk locations) are no longer compacted automatically as part of a database Compact via the Maintenance and Security Center, a deliberate change made to preserve record numbers across compacts.

## Key Points
- 4D v11 SQL stopped auto-compacting address tables during database Compact to preserve record numbers
- Large, sparsely-populated address tables can still waste memory and hurt performance
- TRUNCATE TABLE is presented as the manual solution to reclaim address table space
- Compacting must carefully account for triggers, integrity constraints, indexes, and sequence numbers
- Includes a ready-to-use AddressTableCompactor component with documented usage and enhancement ideas

## Featured Technology
- Address Table internals
- TRUNCATE TABLE SQL command
- AddressTableCompactor component
- Maintenance and Security Center
- record number preservation

## Best Practices Highlighted
- Back up indexes and sequence numbers before compacting so they can be restored afterward
- Only compact address tables when genuinely needed — evaluate space/performance impact first

## Context/Positioning
Published to help developers deal with an unintended side-effect of a 4D v11 SQL change (address tables no longer auto-compacted) that could silently degrade performance over time in high-churn tables.

## Historical Commentary
**Status:** Partially Superseded

This note explains a low-level 4D data-engine concern — reclaiming space from bloated internal address tables after 4D v11 SQL stopped compacting them automatically during a database Compact, to preserve record numbers. The core mechanics (address tables, TRUNCATE TABLE, record numbering) are internals of 4D's classic data engine that persist today for compatibility, but this is a niche/legacy performance-tuning topic that is largely superseded by 4D's modern data engine improvements and by ORDA, where entity-based access patterns reduce direct exposure to address-table-level concerns for most developers.
