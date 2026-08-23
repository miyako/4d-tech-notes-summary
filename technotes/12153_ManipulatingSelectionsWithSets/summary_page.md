# Tech Note: Mainipulating Selections with Sets

- **Asset ID:** 12153
- **Tech Note #:** 01-02
- **Published:** January 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=12153
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_01-05_(JAN)/01-02_Manipulate_Using_Sets.hqx

## Overview

Jamras Komoncharoensiri of 4D, Inc. Technical Support explains the performance rationale for using 4D Sets to cache and instantly restore record selections instead of repeatedly querying, then demonstrates a specific technique for partitioning one selection into several non-overlapping sub-selections using REDUCE SELECTION and the DIFFERENCE set operation.

## Key Points

- Compares switching time between a non-set approach (S*T, always requerying) and a set approach (N*(T+F), querying once then instantly restoring via USE SET), showing sets win once switching happens more often than there are distinct selections.
- CREATE SET([Table 1];$Setname) saves the current selection under a name; USE SET($SetName) instantly restores it as the current selection with no new query.
- The Make_Initial_Set method builds progressively smaller sets (e.g., Set3, Set2, Set1) by repeatedly calling REDUCE SELECTION($pos) to shrink the current selection and CREATE SET at each step, working from the largest set to the smallest so no records are cut off.
- The Start_Partitioning method computes true partitions by comparing consecutive sets with DIFFERENCE($SetName1;$SetName2;$SetDestination), excluding the smaller set's records from the larger one and storing the result in a destination set (e.g., dSet3, dSet2, dSet1), then CLEAR SET to free the intermediate sets.
- Frames the partitioning technique as an alternative to running REDUCE SELECTION multiple times per query, explicitly for scenarios needing multiple independent sub-selections (e.g., top/middle/bottom 30 out of 90 records).
- Cross-references related documents: Technical Note 97-37 'Sets in 4D V6', two Tech Tips on Union/Difference/Intersect with the Userset and correct Set usage, and 4D Language Reference 6.7 entries for Sets, UNION, INTERSECTION, DIFFERENCE, and REDUCE SELECTION.

## Featured Technology

- Sets (CREATE SET / USE SET / CLEAR SET)
- REDUCE SELECTION
- DIFFERENCE (set operation)
- Selection partitioning algorithm
- Records in selection

## Historical Commentary

**Status:** Partially Superseded

Written by Jamras Komoncharoensiri of 4D, Inc. Technical Support, this note formalizes the time-savings math behind using 4D Sets to cache and switch between record selections instead of re-querying, and then demonstrates a specific partitioning technique — using REDUCE SELECTION plus the DIFFERENCE set operation across successive iterations — to carve one selection into several equal-sized sub-selections (e.g., top/middle/bottom thirds) without repeated queries. Sets remain a core, unchanged part of 4D's classic language and this performance rationale is still valid today, though modern applications increasingly also have ORDA entity selections available as an alternative, object-oriented mechanism for persisting and manipulating selection state.

**References to newer/updated information:**
- CREATE SET, USE SET, CLEAR SET, and DIFFERENCE remain fully supported in current 4D versions with unchanged core behavior
- ORDA entity selections (2018+) offer an additional, more modern, object-oriented way to manage and persist selection state alongside classic sets
