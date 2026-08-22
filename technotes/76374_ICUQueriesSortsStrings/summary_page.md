# Tech Note 11-22: ICU in 4D: Impact on Queries, Sorts and String Comparisons

**Author:** Djompolo TANDJIGORA, Quality Control Engineer, 4D SAS.
**Published:** July 11, 2011 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76374
**Download:** https://kb.4d.com/DLTN/TN/2011/11-22_ICUin4D.pdf

## Proposition
This Tech Note explains what ICU (International Components for Unicode) is and how 4D has used the ICU collation algorithm since v11.2 Unicode for all sorts, queries, and string comparisons, detailing the practical impact on developers.

## Key Points
- **What ICU is:** an open-source library providing consistent Unicode handling — character/word/line boundaries, collation, transliteration — across C/C++/Java and platforms.
- **Unicode fundamentals:** covers the ASCII/Unicode relationship as background for understanding comparison behavior.
- **"Ignorable" characters:** codes below 9, between 14-31, and unbreakable spaces can be silently treated as equivalent or ignored during comparisons.
- **Workaround:** the "*" parameter forces character-code-based (non-ICU) comparison on commands that support it.
- **Commands affected:** documents specific impact on C_STRING/C_TEXT equivalence, Position, Replace string, Uppercase/Lowercase, and Char.
- **Japanese-language databases:** notes a specific behavior change starting in v11.5.
- **Practical tips:** XLIFF file saving, forbidden characters, 4D Menu Unicode support, and keyboard-layout-based database conversion, plus a summary table of behavioral differences.

## Featured Technology
- ICU (International Components for Unicode) collation algorithm
- 4D v11 Unicode string/text handling (C_STRING vs C_TEXT equivalence)
- Position, Replace string, Uppercase/Lowercase, Char commands under ICU

## Context / Positioning
Published in mid-2011 following 4D's transition to Unicode text handling in v11.2, this note addressed real developer confusion about unexpected sort, query, and comparison results caused by the newly adopted ICU collation algorithm.

## Historical Commentary
**Status:** Still Relevant

4D's adoption of ICU-based collation for Unicode sorts, queries, and comparisons described here remains the foundation of how 4D handles text comparison today, making this note's core explanation still directly applicable and largely timeless as a reference for understanding string-comparison edge cases like ignorable characters and unbreakable spaces.

The specific command list and Japanese-language-database caveats are dated to the v11.x timeframe, but the underlying ICU behavior model has persisted essentially unchanged through subsequent 4D versions.
