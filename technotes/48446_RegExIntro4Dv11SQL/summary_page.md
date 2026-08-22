# Tech Note 07-47: Introduction to Regular Expressions in 4D v11 SQL

**Author:** Robert Molina, Technical Support Engineer, 4D Inc.
**Published:** December 19, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=48446
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_46-47_(DEC)/07-47_RegEx_Intro.pdf

## Overview
This Tech Note introduces regular expressions (regex) as a newly, natively supported feature of 4D v11 SQL, framing it as evidence of 4D's commitment to industry-wide standards. It covers regex background, syntax basics, and how to use the new `Match regex` command in 4D code.

## Key Points
- Regex background: traces the concept from Kleene/Thompson through Perl and PCRE to ICU (International Components for Unicode), whose regex package 4D adopted as its engine.
- Core syntax: literals (fixed text), metacharacters (e.g. `.` for any character, `$` for end of line), and operators (`*`, `+`, `|` for OR).
- `Match regex` command: supports an optional start position, `pos_found`/`length_found` output parameters (scalar or array), and an optional `*` flag to anchor matching strictly at the given position.
- Capture Groups: parenthesized subpatterns (e.g. `([0-9]{2})/([0-9]{2})/([0-9]{4})`) populate arrays with per-group start positions and lengths, enabling structured extraction (e.g. splitting a date into month/day/year).
- Efficiency argument: a 4-line manual 4D routine using `Position`/`Substring`/`Character code` to do case-sensitive text search is replaced by a single `Match regex` call.
- Escaping: literal operator/metacharacters must be escaped with `\`, and because 4D also treats `\` as its own escape character, patterns in 4D code often require double backslashes (e.g. `"\\+"`).
- Error handling: invalid regex patterns trigger a generic 4D error dialog without pinpointing the specific syntax problem.

## Featured Technology
- `Match regex` command (new in 4D v11 SQL)
- ICU regular expression engine
- Regex literals, metacharacters, operators
- Capture Groups via array parameters

## Historical Context
Published at the close of 2007, alongside the broader rollout of 4D v11 SQL's new SQL engine, this note documents one of the earliest additions of native pattern-matching to the 4D language — a capability many competing platforms and scripting languages had offered for years. The `Match regex` command and ICU-based engine described here remain part of 4D's language today, so the syntax and technique guidance is still largely applicable, though 4D has since added further regex-related commands and capabilities beyond what is covered in this note.

## Historical Commentary
**Status:** Still relevant

The fundamentals taught here — regex syntax, the `Match regex` command, and capture groups — continue to work in current 4D versions largely as described, making this note one of the more durable pieces of 2007-era 4D documentation. The main caveat is that 4D's regex-related command set and capabilities have expanded since 2007, so this note should be read as a foundational introduction rather than a complete modern reference.
