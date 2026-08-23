# Tech Note: Operations on Arrays and Selections

- **Asset ID:** 32122
- **Tech Note #:** 04-14
- **Published:** April 8, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel, 4D S.A.
- **Page URL:** https://kb.4d.com/assetid=32122
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_11-15_(APR)/04-14_Operations_on_Arrays_and_Selections.hqx

## Overview

Roland Lannuzel (4D S.A.) closes a gap between 4th Dimension's Sets (which natively support union/intersection/difference) and named selections (which don't), by providing generic, pointer-based array-operation methods and a thin wrapper layer that gives named selections the same set-style combination capabilities.

## Key Points

- Sets are non-sorted, bitmap-style selections using one bit per record in the table (e.g. 12,500 bytes for any set size in a 100,000-record table); named selections use four bytes per record actually selected (e.g. 200 bytes for a 50-record selection) -- more memory-efficient for small selections but with no native union/intersection/difference support.
- Named selections are, internally, arrays of record numbers (the same numbers returned by `Record Number` and consumed by `GOTO RECORD`); `LONGINT ARRAY FROM SELECTION` extracts these numbers into an array, and `CREATE SELECTION FROM ARRAY` rebuilds a selection from a modified array.
- Generic methods `4DARR_Union`, `4DARR_Intersection`, `4DARR_Difference` (and similar) operate on any two same-typed arrays (String/Text/Real/Integer/LongInt/Date/Boolean/Picture) passed by pointer, with an optional `"*"` argument controlling whether element 0 is included.
- `4DARR_CheckParam` validates that all three arguments are pointers to arrays of the identical type; `4DARR_BuildArraysCheck` efficiently finds common elements between the two source arrays using `Find in array` with an incrementing search-start position, populating parallel Boolean "found" arrays.
- The specific `4DARR_Union` implementation optimizes by copying the larger source array into the destination first, then appending only the "not found" elements from the smaller array, using `4DARR_AddLines` to pre-allocate space and trimming any excess afterward.
- A wrapper layer (`4DSEL_UNION` etc., built on `4DSEL__Build`) converts two named selections to longint arrays via `LONGINT ARRAY FROM SELECTION`, applies the requested array operation, removes duplicates with `4DARR_DistinctValues`, and creates the resulting named selection via `CREATE SELECTION FROM ARRAY`.

## Featured Technology

- LONGINT ARRAY FROM SELECTION / CREATE SELECTION FROM ARRAY
- 4DARR_Union / 4DARR_Intersection / 4DARR_Difference generic array-set-operation methods
- Pointer-based generic array methods (works across array types via Type())
- Find in array with a search-start-position argument
- 4DSEL_UNION-style wrapper methods for named selections
- Record-number-based selection manipulation

## Historical Commentary

**Status:** Partially superseded

This note by Roland Lannuzel (4D S.A.) addresses a real gap in classic 4D: while 4D's Sets support union/intersection/difference operations natively, named selections do not, despite often being more memory-efficient for small selections within large tables. The note explains that named selections are really just arrays of record numbers under the hood, and provides generic, pointer-based utility methods (`4DARR_Union`, `4DARR_Intersection`, `4DARR_Difference`, etc.) that operate on any array type by converting selections to longint arrays via `LONGINT ARRAY FROM SELECTION` and back via `CREATE SELECTION FROM ARRAY`. The underlying commands (`LONGINT ARRAY FROM SELECTION`, `CREATE SELECTION FROM ARRAY`, `Find in array`, array operations) all remain part of current 4D and this technique still works as described, though 4D has since added its own native selection set-operation commands, making the hand-rolled `4DARR_*` methods less necessary for straightforward union/intersection/difference needs on selections.

**References to newer/updated information:**
- 4D has since added native commands for combining/comparing selections and sets directly, reducing the need to hand-roll union/intersection/difference via record-number arrays
- The core LONGINT ARRAY FROM SELECTION and CREATE SELECTION FROM ARRAY commands, and generic pointer-based array techniques shown here, remain valid and functional in current 4D
