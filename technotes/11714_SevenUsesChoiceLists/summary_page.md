# Tech Note 96-35: Seven Powerful Uses of 4D Choice Lists

**Author:** Walt Nelson
**Published:** August 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11714
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_33-36_(AUG)/96-35_Choice_Lists.exe

## Overview
This Tech Note explores seven creative, code-light techniques built on 4th Dimension's Choice List feature, showing how far beyond simple dropdown data entry the feature can be pushed.

## Key Points
1. **Conditional Lists** — a one-line `SET CHOICE LIST` call in a field's script dynamically swaps the list shown in a dependent field (e.g. Auto Brand → Auto Model), paired with `GOTO AREA` to auto-advance the cursor.
2. **Linked Hierarchical Lists** — zero-code drill-down lists (e.g. Platform → Mac → Mac PCI → model), as long as each level's labels repeat the parent level's text.
3. **Rate Chart Lookup Tables** — fixed-width-padded choice list elements act like a mini flat file; a procedure (`LiabRateCalc`) extracts values via string offsets, avoiding extra files/indexes.
4. **Required Values** — the "List Required" field attribute enforces that entered data matches an approved list, useful for clean statistical reporting.
5. **Range of Values** — numeric/date choice lists constrain entries to a valid range; custom alert text requires a hand-written validation routine instead of 4D's default alert.
6. **Storing Demo Data** — text-only choice lists travel with the structure and avoid the overhead of a full demo data file; built/converted via `SELECTION TO ARRAY`, `ARRAY TO LIST`, and string functions.
7. **DBA List Updater Interface** — a "List of Lists" selector plus a scratch "Updater" list let a Database Administrator edit any list, including ones marked not User Modifiable.
- **Strengths recap:** structure-level portability, sorted-list type-ahead, hierarchical linking, dynamic association via `SET CHOICE LIST`, and multi-user list update propagation under 4D Server.
- **Limitations:** a 30-character element limit, and lists shouldn't exceed a few dozen elements — beyond that, use a real 4D file.

## Featured Technology
- 4D Choice Lists (structure-level objects)
- `SET CHOICE LIST`, `LIST TO ARRAY`, `ARRAY TO LIST`
- 4D Search Editor (Required/Range list attributes)

## Historical Context
Choice Lists and the commands demonstrated here (`SET CHOICE LIST`, `LIST TO ARRAY`, `ARRAY TO LIST`) remain part of the modern 4D language, so much of this note's core guidance is still directly usable today. That said, some of the more creative workarounds — using padded-text choice lists as a substitute for real lookup tables or as a demo-data storage mechanism — reflect the constraints of a pre-SQL, pre-ORDA 4D where developers had to improvise with structure-level text objects. Modern 4D developers have far more natural alternatives for these specific use cases (real related tables, JSON structures, or ORDA-based data models), following the introduction of 4D's SQL engine (2007) and ORDA (2018).
