# Tech Note 96-27: A Little Set Theory Never Hurt Anybody: Understanding 4D's Search Engine

**Author:** Walt Nelson
**Published:** May 1, 1996 | **Product/Version:** 4th Dimension v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11706
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_25-26-27_(MAY)/96-27_Set_Theory.exe

## Overview
This Tech Note applies basic mathematical Set Theory (union, intersection, complement) to explain how 4D's Search Editor evaluates multi-line queries joined by And, Or, and Except conjunctions, using the 4D Airlines sample database to demonstrate how line order affects results.

## Key Points
- **Set theory primer:** union (Or), intersection (And), and complement/difference (Except) are introduced as the mathematical basis for how search criteria combine.
- **The "Funnel Concept":** each search line progressively narrows (And) or adds to (Or) the running candidate record set, rather than each line being evaluated independently against the whole file.
- **Line order matters:** because each line operates on the accumulated result of the lines above it, reordering And/Or/Except lines with identical criteria can produce different final record sets.
- **Worked examples:** side-by-side queries against the 4D Airlines demo database (flights, employees, pilots) show how reordering and grouping conjunctions changes results.
- **Practical guidance:** recommendations for structuring multi-line searches (grouping Or'd alternatives, correct placement of Except lines) to reliably get the intended result.

## Featured Technology
- 4D Search Editor (QUERY interface)
- And / Or / Except query conjunctions
- 4D Airlines sample database

## Historical Context
The specific Search Editor interface and 4D Airlines demo database featured in this note are long superseded — the Search Editor has been substantially redesigned in modern 4D, and the 4D Airlines database is no longer shipped with current versions. However, the underlying set-theoretic logic explained here — how And/Or/Except conjunctions combine as intersection/union/difference, and why line order and grouping affect query results — still accurately describes how 4D's QUERY command and query editor behave today, making the core conceptual teaching of this note still relevant to writing correct queries in current 4D.
