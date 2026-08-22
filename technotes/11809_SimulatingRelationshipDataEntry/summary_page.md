# Tech Note 98-26: Simulating a 4D Relationship During Data Entry

**Author:** Not specified in source document
**Published:** June 1, 1999 | **Product/Version:** 4D v6.5 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11809
**Download:** Not available

## Proposition
This Tech Note provides a method to simulate Related One relationship behavior during data entry, allowing record selection from related lists and creation of new records while maintaining standard relationship properties.

## Key Points
- Simulates Related One relationship behavior programmatically
- Allows choosing from a list when multiple related records match
- Supports creating new records when no match exists
- Preserves standard 4D relationship properties
- Provides more flexibility than built-in automatic relationship resolution

## Featured Technology
- Related One
- Relationships
- Data Entry
- 4th Dimension

## Context / Positioning
Managing relationships during data entry was a fundamental concern in 4D development. The classic Related One/Related Many model was central to 4D's data architecture before ORDA introduced entity-based relations.

## Historical Commentary
**Status:** Obsolete

Relationship simulation during data entry was a common concern in early 4D development. The Related One relationship behavior described here has evolved significantly through 4D's history, and ORDA's entity-based data model (v17+) provides a fundamentally different approach to managing related data during entry.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the original page has no working download link. This summary is based solely on the on-page teaser paragraph.*
