# Tech Note: Keyword Indexes, Part 2 (TN 00-38)

**Author:** Steve Hussey, CEO, Alto Stratus LLC
**Published:** August 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11963
**Download:** https://kb.4d.com/DLTN/TN/2000/Windows/TN_2000_36-40_%28AUG%29/00-38_Keyword_Indexes_Pt_2.exe

## Overview
This Tech Note covers the second installment of a three-part series on building keyword indexes, this one adding synonym-based querying so alternate word forms and abbreviations are found automatically.

## Key Points
- It sets up the problem clearly: keyword indexing (splitting text fields into individual word records in a related Many table) is powerful for querying, but users often miss results because they don't think to search every tense, spelling variant, or abbreviation of a term — for example, searching "transaction" won't find records indexed under "transactions" or "transactional," and "4D" won't match records tagged "4th Dimension" or "ACI US." The note's solution is a Synonym table related Many-to-One to the existing Keyword table, so any keyword can have zero, one, or many associated synonyms, letting a single query for "Directory" also retrieve records indexed under "Folder," "Directories," or "Path." It walks through a hands-on sample database exercise: viewing a mail record's keywords, adding synonyms via a subform (using the "Auto assign related value in subform" relation property), and then demonstrating that a "Find by Keyword" search with "Use synonyms" enabled returns matches that a synonym-disabled search misses.
- The featured technology centers on classic 4D relational modeling and querying: One-to-Many/Many-to-One relations, subform-based data entry with auto-assigned related values, and the underlying KWRD_Find method architecture that powers the keyword search.
- Authored by Steve Hussey of Alto Stratus LLC, the note builds directly on "Keyword Indexes, Part 1" (simple single-table indexing with stop words) and sets up for Part 3 (multi-table keyword indexing), forming a coherent instructional arc.
- The example's narrative device — indexing archived 4D Networked User Group mail messages — grounds the abstract synonym-matching problem in a concrete, relatable scenario for 4D developers of the time.
- This remains a solid illustration of relational database design applied to a practical search-quality problem, independent of any specific 4D version's other features.

## Featured Technology
- Keyword indexing
- One-to-Many relations
- Synonym queries
- 4D query/find system

## Historical Context
This is Part 2 of a three-part classic-4D keyword indexing series, building a synonym table (a Many-to-One relation to the keyword table) so that queries for one term (e.g., "transaction") also surface related forms and synonyms (e.g., "transactions", "folder"/"directory"). The relational, One-to-Many indexing pattern it teaches is a timeless database design technique still valid in any 4D era, though the specific implementation predates 4D's full-text search and later language enhancements. Modern 4D applications would likely still use a comparable relational keyword/synonym schema for this kind of requirement, or lean on external full-text search services for large-scale needs, but the conceptual design remains sound and instructive. Related updates since: 4D has since added more advanced text-search capabilities (e.g., improved QUERY/full-text options) that can complement or replace hand-built keyword/synonym tables for some use cases; The core relational modeling technique (One-to-Many keyword/synonym tables) remains a valid, commonly used pattern in current 4D applications.
