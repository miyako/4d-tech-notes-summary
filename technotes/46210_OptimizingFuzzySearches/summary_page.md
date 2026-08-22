# Tech Note 07-15: Optimizing Fuzzy Searches

**Author:** David Adams
**Published:** April 19, 2007 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46210
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_13-16_(APR)/07-15_Fuzzy_Searches.zip

## Overview
This note documents a query optimization for fuzzy string searches implemented via the FuzzyTools component (introduced in Tech Notes 06-18 and 06-19), motivated by growing user expectations — set by search engines like Google — for tolerant, typo-forgiving search behavior that 4D's built-in QUERY tool cannot provide natively.

## Key Points
- Explains the **Edit Distance (Levenshtein) algorithm**: counts the minimum additions/deletions/substitutions to transform one string into another (e.g., "kitten" → "sitting" = distance 3).
- Explains the **Longest Common Subsequence (LCS) algorithm**: finds the longest ordered (non-contiguous) matching character sequence, giving more human-intuitive similarity scores than raw substring matching (e.g., "John Anderson" vs. "Jon Anderssen" scores ~85% via LCS vs. ~54% via longest substring).
- Core optimization insight: a string's **length** mathematically bounds which other strings can possibly match under a given edit-distance or LCS threshold, enabling an indexed pre-filter before the unavoidable sequential fuzzy comparison.
- New optional parameters added to `Fuzzy_FindByEditDistanceCount` and `Fuzzy_FindByLCSLength` accept a pointer to an (ideally indexed) numeric string-length field, triggering an automatic `QUERY SELECTION` to eliminate impossible-length candidates first.
- Also discusses complementary "blocking" strategies to reduce the starting selection: querying a reliable field first, random sampling for very large datasets, or phonetic-encoding pre-filters (acknowledging English phonetic algorithms are imperfect).
- Notes that four other US Census-derived similarity algorithms in FuzzyTools do not get this optimization, since no generalized min/max length formula exists for them.
- Benefit is data-dependent: if all strings in a table cluster around the same length, the length pre-filter provides no benefit, but real-world datasets typically see meaningful gains.
- Ships with a demo database (15,000+ sample surnames) and the updated FuzzyTools component source/component file.

## Featured Technology
- FuzzyTools component (`Fuzzy_FindByEditDistanceCount`, `Fuzzy_FindByLCSLength`, `Fuzzy_GetEditDistanceCount`, `Fuzzy_GetLCSLength`)
- Edit Distance (Levenshtein) and Longest Common Subsequence algorithms
- QUERY SELECTION-based indexed pre-filtering
- SELECTION TO ARRAY (used internally to reduce 4D Server network traffic)

## Historical Context
This note predates 4D v11's native SQL engine (2007) and is written entirely against classic 4D 2004 procedural/set-based query commands. FuzzyTools was a specialized (likely community/third-party) component rather than a core 4D feature. The specific component and its command syntax are now historical, but the core algorithmic technique — using string length as an indexed pre-filter to bound the search space for edit-distance/LCS fuzzy matching before falling back to sequential comparison — remains a generally valid optimization technique in any fuzzy-matching system today, including full-text search engines and dedicated fuzzy-matching libraries.

## Historical Commentary
**Status:** Historical interest only

The FuzzyTools component and its specific 4D 2004-era commands are obsolete curiosities, but the length-based pre-filtering optimization principle for fuzzy string matching remains conceptually sound and applicable regardless of platform or era.
