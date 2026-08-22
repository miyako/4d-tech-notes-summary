# Tech Note 06-15: Comparison Operators

**Author:** Robert Molina, Technical Support Engineer, 4D Inc.
**Published:** April 14, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42647
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_14-17_(APR)/06-15_Comparison_Operators.pdf

## Overview
A tutorial-style refresher on 4th Dimension's six comparison operators (=, #, <, >, <=, >=) and how they behave across String, Numeric, Date, Time, and Pointer data types — a foundational language reference rather than a product-feature note.

## Key Points
- **"=" is not assignment:** unlike C++ and similar languages, 4D's "=" is purely comparative; assignment always uses ":=", eliminating a common source of bugs in other languages.
- **Conditional statements drive control flow:** comparison operators combine with operands to produce a Boolean result used by If/Case (branching) and While/For/Repeat (looping) structures.
- **String comparisons are case- and diacritic-insensitive by default:** "A"="a" and "n"="Ñ" both evaluate TRUE; use the `Ascii()` command to force exact code-point comparison when case/accent sensitivity is required. The "@" wildcard character (only valid in the right-hand operand) matches any number of trailing characters.
- **Numeric comparisons and floating-point precision:** real-number equality can silently fail due to floating-point imprecision (e.g., 32.000001 = 32.000002 can evaluate TRUE); use `Round()` to normalize precision before comparing.
- **Date comparisons:** dates range from 1/1/100 to 12/31/32,767; two-digit years ≥30 are assumed 1900s, <30 assumed 2000s; mismatched date formats (mm/dd/yyyy vs dd/mm/yyyy) from external data sources can silently invert comparison logic.
- **Time comparisons:** times range 00:00:00 to 596,000:00:00 in 24-hour format and can be compared directly against an equivalent integer number of seconds.
- **Pointer comparisons:** only equality/inequality are supported (no <, >), since pointer values carry no ordering semantics; attempting ordered comparison on pointers raises a runtime error.

## Featured Technology
- 4th Dimension core comparison/relational operators (=, #, <, >, <=, >=)
- Boolean conditional expressions and control-flow structures (If/Case/While/For/Repeat)
- `Ascii()` command for case/diacritic-sensitive string comparison
- `Round()` command for real-number comparison precision
- Wildcard (@) string matching

## Historical Context
Published in 2006 for 4D v2004, well before 4D's SQL engine (v11, 2007), Project Mode (v17, 2018), or ORDA existed. Unlike many technical notes tied to specific products or plug-ins, this one documents core 4th Dimension language semantics that have carried through essentially unchanged across 4D's history.

## Historical Commentary
**Status:** Still relevant

Because this note covers fundamental language operators rather than a specific product feature or plug-in, nearly all of its content remains directly applicable in current 4D development, including in classic 4D code alongside the SQL engine 4D introduced later. The floating-point precision caution, date-format warning, string case/diacritic-insensitivity behavior, and pointer-comparison rules are all still true today. Only the specific documentation URLs cited (the old 4d.com/docs/CMU/ structure) are outdated and would need updating to current 4D documentation links.
