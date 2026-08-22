# Tech Note: New Operators and Method Editor

**Author:** Not specified in source document
**Published:** July 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11768
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note documents a tokenization ambiguity introduced in the 4D v6 Method editor when new v6 operators were added to the language, and how it could cause the interprocess variable symbol (<>) to be misread as a bitwise operator in certain expressions.

## Key Points

- New operators added in 4D v6 created situations where an expression could be parsed more than one way.
- The v6 Method editor's tokenizer could, in one such situation, convert the interprocess variable symbol (<>) into a bitwise operator.
- This differed from how the v3 Procedure editor handled the same source text, making it a migration hazard for method code carried over from v3.
- The note provides a specific workaround to avoid the misinterpretation.

## Featured Technology

- 4D V6 Method editor (successor to the V3 Procedure editor)
- New V6 language operators
- Interprocess variable symbol (<>) tokenization

## Historical Context

Written for developers migrating code from 4D v3 to the newly released v6, at a time when the Method editor still worked against the classic binary .4DB structure file with no Project Mode equivalent. The tokenizer behavior described here is tied entirely to that era's editor implementation.

## Historical Commentary
**Status:** Historical interest only

This note documents a narrow tokenization edge case in the V6 Method editor (a symbol/operator ambiguity around the interprocess variable prefix) that only matters to anyone still hand-editing legacy V3/V6-era binary-structure method code; the underlying V6 Method editor and its tokenizer were themselves superseded long ago by later-generation code editors. The specific workaround is of historical interest only for modern development.
