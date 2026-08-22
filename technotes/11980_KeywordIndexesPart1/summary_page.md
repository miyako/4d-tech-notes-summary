# Tech Note: Keyword Indexes, Part 1

## Overview
- **Technical Note 00-37**
- **Author:** Steve Hussey, CEO, Alto Stratus LLC
- **Published:** August 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note opens a three-part series by Steve Hussey on building keyword indexes in 4D as a faster alternative to slow, sequential 'contains' wildcard queries against long text fields. The proposition is illustrated with an example of importing 4D Networked User Group (NUG) email messages into fields for date, sender, subject, and message contents: searching the subject field directly with a wildcard '@4D@' pattern works, but becomes slow as the table grows, because 4D must scan every record sequentially. Instead, the note shows how to parse a text field into its individual constituent words and store each one as its own record in a related many-table, so a keyword search becomes a fast, indexed lookup on the many-table followed by a relation traversal back to the matching parent record(s), rather than a full-table scan. It also introduces the idea of maintaining an exclusion list of common words (such as prepositions) that should not be indexed, to keep the keyword table lean and the search results meaningful. This first part is deliberately scoped to a single table; the series goes on (in parts not necessarily archived here, plus the multi-table Part 3 covered separately) to add synonym support and cross-table indexing. The featured technology is 4D's core many-to-one relational query architecture, used as a hand-built search index.

## Featured Technology
- Keyword Indexes
- Related many-tables
- 4D query/set system

## Historical Context
This is the first of Steve Hussey's three-part series (Part 3 is also archived here as asset 11985) on building keyword indexes by decomposing text fields into individual keyword records in a related many-table, with a stop-word exclusion list to skip indexing common prepositions and the like. This manual pattern for fast text search predates any native full-text or keyword indexing 4D later introduced, so the specific mechanics are superseded, though the underlying relational data-modeling technique it teaches remains sound and broadly instructive.

## What's Changed Since
- 4D has since introduced more capable native indexing options that reduce the need to hand-build a many-table keyword index of this kind for basic text search
- The many-to-one relational data modeling pattern taught in this note remains valid, general database design knowledge

