# Tech Note 09-05: Optimizing File Parsing with Match regex

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** February 4, 2009 | **Product/Version:** 4D v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75143
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_05-08-(FEB)/09-05_MatchRegexParse.zip

## Proposition
Compares classic 4D file-parsing techniques against a new approach combining Match regex with large Text variables, showing it to be both simpler to write and significantly faster once 4D v11 SQL's Unicode and 2GB Text variable support are leveraged.

## Key Points
- **RECEIVE PACKET + Position:** simple and long-standing, but limited to "contains" matching, involves frequent filesystem access, and locks the file during parsing.
- **BLOB Boyer-Moore search:** abstracts parsing from the file itself but is complex to implement and made significantly harder by Unicode's variable-width byte encoding.
- **Match regex + Text variables:** combines the readability of the packet-based approach with regex pattern-matching power, and sidesteps Unicode complexity entirely since Match regex handles character comparison internally.
- **Critical usage detail:** the optional `start` parameter of Match regex must be passed (and initialized to at least 1) to search beyond the first line of text.
- **Real-world benchmark:** parsing ~85,000 lines of Perforce `p4 fstat` output showed Match regex 1.3x faster than Position and vastly faster than BLOB search.
- **Sample benchmark:** on a synthetic 10,000-line test, Match regex was 1.4x faster than Position and 40x faster than BLOB search.

## Featured Technology
- Match regex command with start/pos_found/length_found parameters for line-by-line parsing
- 2GB Text variables and native Unicode (UTF-16) support in 4D v11 SQL
- Comparison against RECEIVE PACKET/Position and BLOB Boyer-Moore search techniques
- Performance benchmarking of parsing algorithms on real Perforce command output

## Best Practices Highlighted
1. Prefer Match regex over large Text variables for file parsing in v11 SQL rather than legacy BLOB-based byte scanning, especially with Unicode data.
2. Always pass and correctly initialize the `start` parameter to Match regex when parsing beyond a single line.
3. Use the `.*` pattern as a simple, reliable way to extract a full line of text with Match regex.
4. Benchmark parsing techniques against realistic, production-scale data rather than assuming theoretical performance.

## Context / Positioning
Written to help developers re-evaluate long-standing 4D parsing idioms in light of major new v11 SQL string-handling capabilities, backed by concrete performance data rather than assertion alone.

## Historical Commentary
**Status:** Still Relevant

Match regex, 2GB Text variables, and native Unicode support are all still core, fully supported parts of the 4D language, and the parsing technique and performance reasoning presented here remain accurate and directly usable today.

Since this note, 4D has expanded its regular-expression and text-handling tooling further (additional regex-related commands and richer text/object APIs in later versions), giving developers more options than the single Match regex command discussed here — but nothing in this note has been deprecated or superseded.
