# Tech Note 06-18: Fuzzy Matching in 4th Dimension

**Author:** David Adams
**Published:** May 5, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42939
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_18-21_(MAY)/06-18_Fuzzy_Matching.zip

## Overview
This is the internals/theory-focused final part of a three-note FuzzyTools series, covering why approximate string matching matters, the general theory behind it, and the actual source-code architecture of the FuzzyTools component (companion notes TN 06-19 documents its public API and TN 06-20 applies it to deduplication).

## Key Points
- **Why fuzzy matching matters:** opens with real-world scenarios — a help desk failing to match customer records, a government consolidating decades of voter/land/waste data, and an ER intake team racing to match patients to medical history — to motivate the need for phonetic and distance-based fuzzy matching.
- **Sources of matching error:** typos, phonetic misspellings, legitimately variable spellings/abbreviations, inconsistent date formats, OCR errors, low-quality web-form submissions, and names that drift over time or geography.
- **Gateway/contract architecture:** public routines (e.g., `Fuzzy_GetPhoneticKey`) validate all inputs and then dispatch to private worker routines (`FuzzyP_GetMetaphoneCode`, `FuzzyP_GetSoundexKnuthCode`, etc.) under a simple "contract": the public routine guarantees clean inputs, the private routine guarantees a return value, and errors are always set — letting internal algorithm code skip defensive checks entirely.
- **Built-in self-testing:** routines like `FuzzyP_TestSoundexKnuth` run each algorithm against known-correct test strings and report any mismatches in a tab-delimited format; two dedicated Runtime-mode test screens are included in the sample database.
- **Guidance for extenders:** preserve the gateway/contract structure when modifying the code, always re-run the test suites after changes, and consult the inline "Read Me Public/Private" documentation routines.
- **Known limitation:** the component's algorithms are built for short strings (up to 80 characters); extending them to BLOBs or long text is referred to the related note "Scanning Text and BLOBs Efficiently" (TN 05-42).

## Featured Technology
- FuzzyTools component full source code
- Phonetic algorithms: Metaphone4/6, Skeleton_Key, four Soundex variants
- Distance algorithms: edit distance (Levenshtein), Longest Common Subsequence (LCS)
- Gateway/contract component-design pattern with self-testing routines

## Historical Context
Published in 2006 for 4D v2004, this note predates 4D's own SQL engine (introduced in v11, 2007), Project Mode (v17, 2018), and ORDA — it is firmly a classic procedural-language, Design Mode-era artifact, describing a third-party component rather than a built-in 4D capability.

## Historical Commentary
**Status:** Historical interest only

The approximate-string-matching theory and the gateway/contract software architecture pattern described here are both timeless and could inform component design in any modern language, including current 4D. However, the FuzzyTools component itself, and its specific method names and source code, are a 2006-era third-party artifact with no direct counterpart in current 4D distributions — a developer today would need to source the original component or reimplement the algorithms from scratch (or use a modern library) rather than follow this note as a literal how-to.
