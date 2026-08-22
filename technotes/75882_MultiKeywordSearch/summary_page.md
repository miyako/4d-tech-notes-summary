# Tech Note 09-34: Multi-Keyword Search

**Author:** Joe Resuello, Tech Marketing Engineer, 4D Inc.
**Published:** August 27, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75882
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_31-35_(AUG)/09-34_MultiKeywordSearch.zip

## Proposition
This Tech Note proposes a way to handle multi-word keyword searches in 4D v11 SQL by letting 4D's own keyword-indexing algorithm define what constitutes a "word," rather than the developer manually parsing the user's search string on spaces, apostrophes, and hyphens.

## Key Points
- Builds on and contrasts with the earlier TN 09-09 "Advanced Keyword Search," which explicitly used whitespace as a delimiter.
- Uses the `%` "contains keyword" operator (introduced in 4D v11 SQL) for single-keyword searches on Alpha/Text fields.
- For multi-keyword phrases, chains multiple `QUERY` calls with the `*` (AND) continuation flag.
- Core technique: save the user's raw search string into a separate keyword-indexed field (`[Saved_Searches]Data`), then run `DISTINCT VALUES` on it to get an array of exactly the tokens 4D's own keyword engine would extract.
- Documents 4D v11.2's new ICU-based keyword algorithm, which treats decimal numbers and apostrophe/hyphen-containing words as single tokens (an improvement over the older algorithm).
- Because word-boundary logic is delegated to 4D itself, the technique automatically adapts if 4D's keyword algorithm changes in the future.
- Demonstrated against a sample Wikipedia-article database with searches like "Jim Henson's muppets," "Mac OS X v10.5," "pv-sd4090," and "$616,667."

## Featured Technology
- 4D v11 SQL keyword indexing (Alpha/Text fields)
- `%` (contains keyword) operator
- `QUERY` command with compound `*` (AND) syntax
- `DISTINCT VALUES` command
- ICU-based keyword definition algorithm (4D v11.2+)

## Best Practices Highlighted
1. Don't reinvent word-boundary/tokenization logic — delegate to the same engine that built the index you're searching.
2. Keyword-index an auxiliary "saved search" field purely to reuse 4D's tokenizer, rather than parsing strings manually.
3. Build procedural (loop-driven) compound queries so the same code path handles both single- and multi-keyword searches.

## Context/Positioning
Published as a direct follow-up/refinement of TN 09-09, this note showcases the practical implications of 4D v11.2's ICU-based keyword algorithm change and offers a more future-proof searching pattern for the then-new 4D v11 SQL keyword-index feature.

## Historical Commentary
**Status:** Partially Superseded

This note is a clever classic-language technique built entirely on 4D v11 SQL's keyword-index feature and imperative QUERY/DISTINCT VALUES commands operating on selections and arrays — the kind of imperative, selection-based data access that ORDA's entity selections and fluent query methods were designed to replace starting in 4D v16 R5/R6 (2017). The keyword-index engine and `%` operator still exist in current 4D and this classic code will still run unmodified, but a modern implementation would more likely express the same logic via ORDA's `.query()` against an entity selection rather than chaining QUERY calls with wildcard continuation syntax. The core insight — delegate word-boundary decisions to 4D's own algorithm instead of reinventing tokenization — remains a genuinely good, timeless idea independent of the access-layer used.
