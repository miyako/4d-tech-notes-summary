# Tech Note 04-14: Operations on Arrays and Selections

**Author:** Not specified in source teaser
**Published:** April 8, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32122
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_10-15_(MAR)/04-14_Operations_on_Arrays.exe

## Overview
This Tech Note provides custom methods that let developers apply set-style operations (union, intersection, difference) to named selections, bridging a gap between 4D's original "sets" mechanism and the newer (v6+) named selections.

## Key Points
- Contrasts **sets** (available since early 4D versions) with **named selections** (introduced in v6), noting their similarities and key differences.
- Sets support union, intersection, and difference, allowing complex queries to be built up in sequential, maintainable steps.
- The note supplies custom methods so named selections can be manipulated the same way as sets.
- Positioned partly as a broader lesson in writing custom commands to extend 4D's language for specific developer needs.

## Featured Technology
- 4D Sets and set operations (union, intersection, difference)
- Named selections
- Custom method/command design patterns

## Historical Context
Only the on-page teaser paragraph for this asset could be recovered (the full archived PDF was not accessible in this environment), so this summary reflects the note's stated scope rather than its exact method code. The core sets/named-selections model described here predates both 4D's native SQL engine (v11 SQL, ~2007) and ORDA's entity selections (v16, 2018), both of which now offer more built-in ways to combine and manipulate record subsets. The general concept of composable record-set operations remains relevant, but the specific custom-method workaround is superseded by later, more integrated language features.
