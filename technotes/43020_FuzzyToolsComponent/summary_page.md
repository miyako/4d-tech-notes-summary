# Tech Note 06-19: Fuzzy Tools Component

**Author:** David Adams
**Published:** May 12, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43020
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_18-21_(MAY)/06-19_Fuzzy_Tools_Component.zip

## Overview
This note documents the FuzzyTools component's public API — a suite of phonetic and string-distance fuzzy matching tools for 4th Dimension, packaged as a compiled component to reduce complexity (roughly 20 exposed methods versus 70+ internal ones) and simplify distribution/updating across projects.

## Key Points
- **Why a component:** packaging as a component reduces the developer-facing surface area, simplifies keeping the code up to date across multiple databases, and centralizes error/parameter checking through a "gateway" routine pattern.
- **Compiled by design:** the component is meant to run compiled (not interpreted), with full parameter/variable typing supported.
- **Sample database demos:** "Show Words" (phonetic/distance experiments against ~15,000 surnames and ~5,000 place names), "Show People" (duplicate-hunting report over 500 records with 50 known duplicates), "Compare Strings" (interactive two-string comparison), and "WordList Utilities" (shared-word-percentage text comparison).
- **Phonetic key generation:** `Fuzzy_GetPhoneticKey` supports seven algorithms — Metaphone4, Metaphone6, Skeleton_Key, and four Soundex variants (Knuth, Miracode, Simplified, SQLServer) — with Metaphone4/6 recommended as the best general-purpose choice; Soundex is included mainly for legacy compatibility since it produces many false positives.
- **Runtime introspection:** `Fuzzy_GetPhoneticMethodTypes` lets code retrieve the list of valid algorithm names to pass to `Fuzzy_GetPhoneticKey`, supporting either string or text arrays as output.
- **Series context:** this note is the practical/API-reference middle piece of a three-note series — TN 06-18 covers the algorithmic internals and source code, TN 06-20 applies the tools to a full deduplication workflow.

## Featured Technology
- FuzzyTools 4D component (gateway/private-routine architecture)
- Phonetic algorithms: Metaphone4, Metaphone6, Skeleton_Key, Soundex (Knuth/Miracode/Simplified/SQLServer)
- Distance algorithms: edit distance (Levenshtein), Longest Common Subsequence (LCS)
- WordList shared-word text comparison utilities

## Historical Context
Published in 2006 for 4D v2004, a year before 4D v11 introduced 4D's native SQL engine (2007) and over a decade before Project Mode (v17, 2018) or ORDA. FuzzyTools was a third-party/community component of that era, not a built-in 4D feature, distributed alongside this technical note series.

## Historical Commentary
**Status:** Historical interest only

The phonetic and string-distance algorithms documented (Soundex variants, Metaphone, edit distance, LCS) are timeless computer science and the gateway/private-routine API design pattern remains a reasonable approach to component design in any language, including modern 4D. However, the FuzzyTools component itself is a period 4D 2004-era third-party artifact that is not part of current 4D distributions, so a developer today would need to locate the original component, reimplement the algorithms, or find a modern equivalent rather than use this note as a direct how-to.
