# Tech Note 96-31: Breaking the Rules to Improve Performance, Part 1—Expanding the Concept of a Keywords Subfile

**Author:** Walt Nelson
**Published:** July 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11710
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_31-32_(JUL)/96-31_Performance_1.exe

## Overview
Part 1 of a two-part series, this Tech Note shows how to expand 4D's traditional "Keywords subfile" pattern into a fast, forgiving, single-field free-text search across many underlying fields — deliberately breaking the "don't use subfiles" and "normalize your data" rules to solve real search-performance pain over WAN/dial-up connections.

## Key Points
- **Problem:** traditional Quick Search UIs require users to know the data's structure, use the mouse to pick fields, and tolerate no misspellings — all of which become far more costly as search round-trips slow down over a WAN or modem (a 7-second local search could become 70+ seconds remotely).
- **Solution:** a single-field, indexed Keywords subfile that stores every searchable word from multiple target fields (contact name, company, case number, product, etc.), built via:
  1. A word-parsing routine (`KeywordParse`).
  2. A subrecord-creation routine that adds a keyword subrecord per unique word if missing.
  3. Data-entry scripts on each searchable field that call the parse/create routines.
  4. An Included Output Layout with a single enterable `vFind` variable for free-text search.
- **Power-user syntax:** `&` prefix for AND-matching across all typed keywords; `_` for phrase matching.
- **Nine advantages** enumerated, including no need to know the schema, tolerance for spelling variation, no growing UI/code per additional searchable field, and consistently fast performance because the single keyword index stays cached in memory.
- **Cautions:** limit the subfile to one field (~30 chars), and to roughly 25–30 keyword subrecords per parent record, since 4D transmits full records with subrecords to the client.

## Featured Technology
- 4D subfiles (used here as a search index rather than a hierarchical data structure)
- 4D array and string-parsing commands (`TextParseWords`, `LIST TO ARRAY`/`ARRAY TO LIST` family)
- 4D Included Output Layouts with enterable variables

## Historical Context
The core UX idea here — one free-text box that searches across many fields without the user needing to know the schema — is a genuinely modern, still-relevant pattern (mirrored today by full-text/search-index features). However, the specific mechanism (a hand-built subfile of parsed keyword tokens) and its motivating constraint (WAN/dial-up latency) are firmly rooted in 1990s network conditions and 4D's pre-SQL, pre-ORDA procedural language. 4D subfiles as a general data-modeling construct have long since fallen out of favor relative to standard related tables, and 4D's introduction of a true SQL engine (v11 SQL, ~2007) and later ORDA (2018) gave developers standard, indexed multi-field query capabilities that make this manual keyword-subfile workaround unnecessary today.
