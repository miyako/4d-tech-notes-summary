# Tech Note: Keyword Indexes (Part 3)

## Overview
- **Technical Note 00-45**
- **Author:** Steve Hussey, CEO, Alto Stratus LLC
- **Published:** September 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note completes a three-part series by Steve Hussey on building keyword indexes in 4D by decomposing text fields into individual word records stored in a related many-table, then using that many-table to power fast, word-based queries rather than slow 'contains' wildcard searches across every record. Part 1 covered single-table keyword indexing with a stop-word exclusion list, and Part 2 added synonym support so that searching for one term (like 'folder') could also surface related terms (like 'directory'). This third installment extends the pattern to index keywords across multiple, unrelated tables simultaneously by adding a table-number column to the keyword-link table, so a single keyword search can return matches drawn from commands, error codes, plug-ins, and technical notes all at once — illustrated through Alto Stratus's own in-house 4D knowledge-base application. The note walks through launching the sample 'Keyword_Part_3' database, indexing preloaded 4D command records, and importing/indexing additional notes to see the cross-table search in action. The featured technology is 4D's classic many-to-one/many-to-many relational query architecture used as a hand-built search index, a foundational pattern for developers who needed fast text search well before native full-text indexing existed in 4D.

## Featured Technology
- Keyword Indexes
- Many-to-many relations
- 4D query/set system

## Historical Context
This is the third of a three-part series (with 11980 also archived here) on building keyword indexes by hand using related many-tables in classic 4D, extending the technique to index across multiple tables in one shared keyword store. The manual related-table pattern shown here reflects the query capabilities available before 4D introduced more advanced native full-text/keyword indexing options, so while the specific implementation is now largely superseded, the underlying many-to-many relational data-modeling concept it teaches remains a durable idea in database design generally.

## What's Changed Since
- 4D has since added more capable built-in indexing options that reduce the need to hand-build many-to-many keyword tables for this kind of text search
- The general many-to-many relational modeling technique taught here remains valid database design knowledge independent of 4D-specific indexing improvements

