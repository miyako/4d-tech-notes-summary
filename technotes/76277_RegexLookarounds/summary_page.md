# Tech Note 11-07: Using RegEx “Lookarounds” with 4D Match regex

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** March 14, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76277
**Download:** https://kb.4d.com/DLTN/TN/2011/11-07_Lookarounds.zip

## Proposition
This note is a detailed tutorial on regex 'lookarounds' — lookahead and lookbehind assertions — as usable within 4D's Match regex command. It explains how the regex engine evaluates lookahead and lookbehind internally, then systematically covers positive and negative variants of both, along with important caveats about lookbehind support. It then applies these constructs to a series of realistic scenarios: validating passwords containing special characters of a specific length, extracting the integer portion of a decimal number only if a fractional part exists, finding a word not preceded by a certain phrase, handling case sensitivity in lookarounds, combining positive/negative lookaround with conditionals, nesting lookaround patterns, and testing password content with lookaround patterns. Each scenario includes the pattern, an explanation of how it works, and relevant caveats.

## Key Points
- Explains the internal mechanics of how a regex engine initializes and evaluates lookahead/lookbehind assertions.
- Covers both positive and negative lookahead and lookbehind, with caveats specific to lookbehind support.
- Applies lookarounds to password validation (special characters, specific length) as a worked scenario.
- Applies lookarounds to conditional numeric extraction (integer part only if a fractional part exists).
- Covers finding words not preceded by a given phrase, and handling case sensitivity in lookaround patterns.
- Demonstrates combining positive/negative lookaround with conditionals and nesting lookaround patterns for advanced validation.

## Featured Technology
- Match regex command (4D's regular expression engine)
- Regex lookahead and lookbehind (positive/negative) constructs
- Nested and combined lookaround patterns with conditionals

## Best Practices Highlighted
- Use lookarounds to enforce complex validation rules without capturing/consuming the matched text
- Test lookbehind constructs carefully given engine-specific limitations noted in the Tech Note

## Context / Positioning
Published in 2011 for 4D v12, at a time when 4D's Match regex command had matured enough to support advanced regex features, and developers needed practical guidance applying lookarounds to real validation problems like password rules.

## Historical Commentary
**Status:** Current

Regular expression syntax and lookaround semantics are a language-level standard that has not changed, so this note's core content (how lookaround assertions work and how to write them) is genuinely timeless and remains directly usable with 4D's Match regex command today.
