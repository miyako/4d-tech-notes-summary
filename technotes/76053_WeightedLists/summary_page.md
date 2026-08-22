# Tech Note 10-08: Generating Weighted Lists in 4D

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** March 15, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76053
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_07-11_(MAR)/10-08_WeightedLists.zip

## Proposition
This note explains the general concept of weighted (relevance-ranked) lists — as used by search engines, Spotlight, and tag clouds — and demonstrates two concrete 4D algorithms for computing and displaying such rankings, backed by a sample database.

## Key Points
- A weighted list pairs a **data array** with a parallel **weights array**; sorting both by the weights array orders the data by relevance.
- Surveys real-world examples: **tag clouds**, the **4D Doc Center**, and **Google search results**, each using different display strategies for the same underlying concept.
- Sample database implements **two search algorithms**: one searching multiple fields across a table and related records (weighting by match location), another suited to large single-text-field searches.
- Covers practical steps: **getting search terms, keyword filtering, keyword frequency counting, and finding distinct keyword values**.
- The weighting factors are entirely developer-defined — any criteria relevant to the application can drive the weight calculation.

## Featured Technology
- Weighted list / relevance-ranking algorithms
- Parallel data + weight array sorting
- Keyword frequency and distinct-value search techniques

## Best Practices Highlighted
1. Separate "what is relevant" (weight calculation) from "how it's displayed," letting the same ranking data drive different presentation styles (tag cloud, list, etc.).
2. Choose the search algorithm to match the data model — multi-field/related-record scoring versus single large-text-field scoring require different approaches.
3. Sort parallel data/weight arrays together to keep relevance rankings correctly aligned with their source data.

## Context / Positioning
Published alongside the companion note "Dynamically Creating Tag Clouds with SVG" (asset #75998), which builds a visual weighted-list presentation on top of the algorithms introduced here.

## Historical Commentary
**Status:** Still Relevant

This note presents a general algorithmic technique for building relevance-ranked (weighted) lists in 4D — pairing a data array with a parallel weights array and sorting both together — illustrated through search-term frequency and multi-field relevance scoring.

The underlying algorithm is a timeless, database-agnostic concept unrelated to any deprecated 4D mechanism, and the classic array-sorting commands used remain fully functional today. It is still a perfectly valid approach, though modern 4D developers working with ORDA-based entity selections might instead compute and sort relevance using collection classes or SQL ORDER BY expressions rather than parallel classic arrays; the core idea, however, has not been superseded.
