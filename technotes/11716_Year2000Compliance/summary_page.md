# Tech Note 96-37: 4th Dimension, the Year 2000 and Everything

**Author:** ACI US Technical Support
**Published:** July 1, 1996 | **Product/Version:** 4th Dimension v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11716
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_35-37_(JUL)/96-37_Year_2000.exe

## Overview
Written in 1996 amid growing industry concern about the Year 2000 problem, this Tech Note confirms that 4th Dimension's internal Date data type is fundamentally Y2K-safe, then addresses the real practical risk: correctly interpreting user-entered two-digit years across the century boundary.

## Key Points
- **4D's Date type is Y2K-safe:** dates are stored internally with a full four-digit year, so no engine-level rollover bug exists.
- **The real risk is UI-level:** applications commonly let users type only a two-digit year, which can be misinterpreted once the year 2000 arrives.
- **Pivot-year algorithm:** a configurable threshold year below which two-digit input resolves to the 2000s and above which it resolves to the 1900s (e.g., pivot 30: "29" → 2029, "30" → 1930).
- **`Sys date format` command:** returns the OS's locale-specific date format string (separators, field order), enabling locale-aware date parsing.
- **`SET DATE FORMAT` command:** documented for overriding 4D's own date display format when needed.

## Featured Technology
- 4D Date data type
- Sys date format command
- SET DATE FORMAT command
- Pivot-year (century detection) algorithm

## Historical Context
The Year 2000 rollover this note prepared developers for occurred uneventfully in 2000 and is now purely a historical software-engineering milestone, making the note's central motivation a matter of historical interest only. Modern interfaces overwhelmingly default to four-digit year entry, largely eliminating the two-digit ambiguity problem this note solves. That said, the `Sys date format` and `SET DATE FORMAT` commands remain part of modern 4D for locale-aware date formatting, and the pivot-year technique itself remains a conceptually valid, general-purpose pattern for interpreting ambiguous abbreviated date input in any system today.
