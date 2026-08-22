# Tech Note 16-11: Stemming Algorithm for Query Expansion

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** August 26, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77610
**Download:** https://kb.4d.com/DLTN/TN/2016/16-11_StemmingAlgorithm.zip

## Proposition
This note explains and implements the Porter 2 (Snowball) English stemming algorithm in 4D, so that search queries can be automatically expanded to match related word forms (e.g., matching "assess" against "assessing", "assessment", "assessed").

## Key Points
- **Porter 2 Stemmer background:** an improved, faster successor to the original Porter Stemmer algorithm by Martin Porter.
- **Formal linguistic definitions:** suffix, vowels, doubles, R1/R2 regions, short syllable, and short word are all defined precisely before the algorithm steps.
- **Multi-step transformation:** Steps 0 through 5 progressively strip and normalize suffixes to reach a word's stem.
- **Exceptional forms handling:** two groups of irregular words are special-cased outside the regular step logic.
- **Reusable component API:** P2S_Stem($word) stems a single word; P2S_Stem_Words($words) stems a list/collection of words.
- **Demo database included** to illustrate usage and expected stemmed output.
- **Use case: query expansion,** improving search recall by matching on word stems rather than exact strings.

## Featured Technology
- 4D v15.x component architecture
- Porter 2 / Snowball stemming algorithm
- 4D text-processing commands
- Query expansion for search

## Best Practices Highlighted
1. Apply stemming to both indexed content and user search terms consistently for accurate matching.
2. Special-case known exceptional word forms rather than relying solely on the general algorithm steps.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

The Porter 2 stemming algorithm is language theory, not 4D-version-specific technology, so this Tech Note remains technically accurate and directly usable in current 4D versions with only minor syntax modernization (e.g., typed variables vs. C_TEXT declarations). It predates ORDA-based full-text search features, and if this were rewritten today it would likely use collection/ORDA idioms, but the algorithm and component design are unaffected by the 4D Design Mode-to-Project Mode transition.
