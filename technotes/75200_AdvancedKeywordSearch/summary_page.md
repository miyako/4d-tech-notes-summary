# Tech Note 09-09: Advanced Keyword Search

**Author:** Luis Pineiros, Technical Services Team Member, 4D Inc.
**Published:** March 4, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75200
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_09-12_(MAR)/09-09_Advanced_Keyword_Search.zip

## Proposition
Builds on 4D v11 SQL's new Keyword Index and `%` (Contains Keyword) operator to implement fast, precise multi-word search, using a 5,000-article Wikipedia sample database to illustrate word-boundary rules and a chained-query technique for multi-keyword AND searches.

## Key Points
- **Keyword Index:** an Alpha/Text field option indexing data word-by-word (even single characters), usable alongside a regular index, that 4D auto-selects for optimization.
- **% operator vs. @text@/text@:** demonstrates via a comparison table how `%"system"` matches only the whole word "system," unlike `@system@`/`system@` which also match "systematic" or "ecosystem."
- **ICU word-boundary rules:** numbers (with commas/decimals/currency), apostrophes, and hyphens stay attached to words; punctuation and spaces are split out as separate boundaries.
- **Single-keyword limitation:** `%` matches only one keyword per call, so phrase/multi-word searches require chaining multiple `QUERY` calls with `&` (AND).
- **Case/diacritic insensitivity:** the `%` operator ignores case and diacritics by design.
- **Custom tokenizer:** `Util_GetStringToken` splits free-text user input on a configurable delimiter (default space) into a text array for iterative query-building.
- **Three match modes:** the sample UI lets users choose Word, Begins With, or Contains matching per search.

## Featured Technology
- 4D v11 SQL Keyword Index for Alpha/Text fields
- % (Contains Keyword) query operator
- QUERY command with compound (&) statements for multi-keyword search
- Custom word-tokenizing utility (Util_GetStringToken) for splitting multi-word search input

## Best Practices Highlighted
1. Use a Keyword Index plus `%` instead of `@text@` when searching for whole words, for both better precision and better performance.
2. For multi-word searches, tokenize user input yourself and chain one `%` query per word with `&`, since `%` only matches one keyword at a time.
3. Use `DESCRIBE QUERY EXECUTION` to inspect and verify the query plan/index usage of keyword searches.

## Context / Positioning
A direct follow-up to an earlier note introducing keyword indexing, this Tech Note addresses the practical gap of multi-word searching and demonstrates it at meaningful scale (5,000 real-world text articles) rather than with a toy dataset.

## Historical Commentary
**Status:** Still Relevant

Keyword indexing and the `%` operator remain fully supported, standard 4D features for fast word-based search, and the chained-compound-query technique for multi-word AND search shown here is still a valid, commonly used pattern today.

The main development since is ORDA (4D v16 R5+, 2017), which offers an alternative entity-based query syntax (`dataClass.query()`) for expressing the same underlying searches, but it does not replace or deprecate the keyword index/`%` operator mechanics this note explains — those concepts remain directly applicable in both classic and ORDA-based code.
