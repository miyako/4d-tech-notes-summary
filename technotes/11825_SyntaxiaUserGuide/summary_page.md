# Tech Note 99-03: Syntaxia - A Database of 4D Language Components

**Author:** Bart Scott, Manager of Analysis
**Published:** January 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11825
**Download:** https://kb.4d.com/DLTN/TN/2017/Windows/TN_1999_01-03_(JAN)/99-03_Syntaxia_User_Guide.exe

## Overview
Syntaxia is a 4D database serving as a comprehensive reference tool for all language elements in 4D v6, cataloging commands, constants, and plug-in commands with their syntax, shortcuts, chapter references, and command numbers.

## Key Points
- Contains five fields per entry: command name, syntax, chapter reference, wildcard shortcut, and command number/constant value.
- Covers 500+ 4D commands, plus constants and plug-in commands (4D Calc, 4D Chart, 4D Draw, 4D Write) — approximately 1,500 total entries.
- Interface uses five tab controls for filtering by alphabet letter, source selection, form switching (with/without syntax), and sort order/direction.
- Full keyboard equivalent support: letters for alphabet tabs, numbers 1-7 for sources, +/- for form switching, arrows for sort control.
- Documents the wildcard shortcut system (e.g., typing `C_L@` to tokenize to `C_Longint`).
- Explains the value of command numbers for future-proofing code against command renames (e.g., SEARCH → QUERY).
- Designed to run in minimal memory as a background desk accessory.

## Featured Technology
- 4D v6.0
- Tab control objects
- 4D language command reference
- Wildcard/shortcut tokenization system
- 4D Calc, 4D Chart, 4D Draw, 4D Write plug-ins

## Historical Context
**Status:** Historical interest only

The Syntaxia database is a charming artifact of the 4D v6 era, when developers needed creative solutions to navigate a rapidly growing command set. Today, 4D's built-in Explorer, online documentation, and code completion in the Method Editor provide far superior language reference capabilities. The 4D language has grown from the ~500 commands documented here to well over 1,500 built-in commands. Several plug-ins referenced in this note (4D Calc, 4D Chart, 4D Draw) have been discontinued entirely. The wildcard shortcut system described (typing abbreviated commands with @) is still supported in 4D's Method Editor, though modern type-ahead/autocomplete has largely superseded it. The download is a Windows .exe self-extracting archive that cannot be opened in this environment.
