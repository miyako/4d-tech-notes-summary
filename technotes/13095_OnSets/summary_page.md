# Tech Note: On Sets

- **Asset ID:** 13095
- **Tech Note #:** 01-13
- **Published:** March 30, 2001
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=13095
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_11-15_(MAR)/01-13_On_Sets.hqx

## Overview

Jean-Yves Fock-Hoon (Quality Assurance Manager, 4D, Inc.) explains 4D's Set data structure and how it compares to the ordinary current selection, showing why sets can be faster and more memory-efficient for saving, combining, and testing complex query results, illustrated with a 50,000-record People/RPG-player example database.

## Key Points

- A current selection is an in-memory, sortable list of record pointers requiring 4 bytes per record; a set instead uses just 1 bit per record to mark membership, cannot be sorted, but can be saved to disk and reloaded faster than rebuilding a selection.
- `COPY NAMED SELECTION`/`CUT NAMED SELECTION` let a developer stash the current selection into a temporary selection to build a different one without losing it; sets go further, supporting `UNION`, `INTERSECTION`, and `DIFFERENCE` between two saved sets.
- 4D provides three set scopes: inter-process sets (prefixed `<>`, usable by all processes), process sets (no prefix, usable only by the creating process), and local sets (prefixed `$`, existing only on the 4D Client machine that created them) — set names can be up to 80 characters including any prefix.
- 4D automatically maintains two special sets: "Lockedset" (records locked by other processes during `ARRAY TO SELECTION`, `APPLY TO SELECTION`, or `DELETE SELECTION`) and "Userset" (records the user has highlighted in a displayed selection).
- The example database's "How does it work" screen lets users build sets ("SetF"/"SetG"/"SetH") from highlighted records via `COPY SET`, then combine them with `INTERSECTION`/`UNION` into further named sets, and test membership per-record with `Is in set` to draw bullets.
- Benchmarking shows non-indexed-field queries taking ~118-152 ticks on repeat runs versus 0-3 ticks when simulated via pre-built sets and `USE SET`/`INTERSECTION`/`UNION`/`DIFFERENCE`; in Client/Server, using sets requires extra synchronization methods (`ROBOT_Rec_has_been_Created`, etc.) since sets must be kept current as records are added, modified, or deleted.

## Featured Technology

- Sets (inter-process, process, and local sets)
- COPY NAMED SELECTION / CUT NAMED SELECTION
- COPY SET / UNION / INTERSECTION / DIFFERENCE / USE SET
- Is in set command
- Lockedset and Userset automatic sets
- 4D Server set synchronization in Client/Server

## Historical Commentary

**Status:** Still relevant

Jean-Yves Fock-Hoon's note explains 4D's Set data structure as a memory-efficient (1 bit per record), unordered alternative to selections, useful for saving/reloading searches, combining results with UNION/INTERSECTION/DIFFERENCE, and quickly testing membership with Is in set, while also covering the automatic Lockedset/Userset sets and the synchronization challenges of using sets in Client/Server. Sets and the described commands remain part of 4D's classic language essentially unchanged today and the memory/speed tradeoffs described are still accurate, so this note's core content is still directly applicable, though ORDA-based development on data classes now offers query and entity-selection patterns that reduce how often developers reach for low-level sets.

**References to newer/updated information:**
- 4D's Set commands (UNION, INTERSECTION, DIFFERENCE, USE SET, Is in set, etc.) remain unchanged in the current classic language
- ORDA-based entity selections and today's query optimizer reduce some scenarios where developers previously needed to hand-manage sets for performance, though sets remain available and useful for classic-language code
