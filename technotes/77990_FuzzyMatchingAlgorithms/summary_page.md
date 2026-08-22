# Tech Note 18-07: [3rd Party Tech Note] Fuzzy Matching Algorithms for Sets and Binary Properties

**Author:** David Adams
**Published:** April 24, 2018 | **Product/Version:** 4D v16R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77990
**Download:** https://kb.4d.com/DLTN/TN/2018/18-07_Fuzzy_Sets.zip

## Proposition
A math-first, algorithm-focused technical note explaining how to quantify similarity between records using the Jaccard coefficient, Simple Matching Coefficient (SMC), and Sørensen–Dice coefficient, implemented against 4D Sets and binary property vectors, rather than relying only on exact-match queries.

## Key Points
- **Jaccard = intersection over union:** derived through a worked example of overlapping team memberships, showing why simply counting shared members is misleading.
- **Jaccard score vs. Jaccard distance:** both are introduced as complementary ways to express the same similarity measure.
- **Binary properties generalize sets:** any record can be represented as a vector of true/false attributes for comparison, not just literal set membership.
- **Simple Matching Coefficient (SMC):** unlike Jaccard, SMC also credits matching "false" values (shared absences), useful when absence-of-a-property is meaningful.
- **Sørensen–Dice coefficient:** an alternative that weights shared presence differently than Jaccard, useful depending on the semantics of the data.
- **Dichotomization techniques:** practical guidance for converting discrete, categorical, and continuous values into binary properties, including handling fuzzy/threshold values and clustering.
- **Performance/optimization advice:** aggressively narrow the candidate pool before running fuzzy comparisons — pre-filter by simple properties (e.g., item count) or sample 1–2% of a very large dataset rather than scanning everything.
- **4D Sets as the implementation vehicle:** sample code demonstrates applying these coefficients using classic 4D Sets, including a "properties count" parameter.

## Featured Technology
- Jaccard coefficient / Jaccard distance
- Simple Matching Coefficient (SMC)
- Sørensen–Dice coefficient
- Binary property vectors / dichotomization
- Classic 4D Sets

## Best Practices Highlighted
1. Choose the right coefficient (Jaccard vs. SMC vs. Sørensen–Dice) based on whether shared absences should count toward similarity.
2. Dichotomize continuous/categorical data thoughtfully rather than naively, since the choice of thresholds materially affects results.
3. Pre-filter or sample large datasets before running full pairwise fuzzy comparisons to avoid exponential blow-up.
4. Validate any fuzzy-matching approach empirically against your actual data ("you have to try with your data") rather than assuming one metric universally wins.

## Context / Positioning
As an author-contributed ("3rd Party") Tech Note rather than an official 4D Inc. technical-services piece, this document is unusually algorithm-centric and largely 4D-syntax-agnostic; its 4D-specific hook is implementing these coefficients against classic 4D Sets, which were the standard record-grouping mechanism before ORDA entity selections and collections matured.

## Historical Commentary
**Status:** Still relevant

The mathematical content — Jaccard, Simple Matching Coefficient, and Sørensen–Dice similarity scoring, plus the dichotomization and sampling/optimization advice — is timeless and completely unaffected by 4D's later Project Mode or ORDA transitions; these are standard, widely used similarity metrics in data science and record-linkage work generally, not 4D-specific inventions.

The only dated element is the implementation vehicle: the sample code works with classic 4D Sets, which are a legacy mechanism today largely superseded in new development by ORDA entity selections and 4D collections. A developer applying these algorithms today would likely re-implement the set/vector operations using collections or entity selections rather than classic Sets, but the underlying formulas and matching strategy transfer directly with no conceptual changes needed.
