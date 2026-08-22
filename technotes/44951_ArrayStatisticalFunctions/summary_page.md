# Tech Note 06-45: Statistical Functions for Arrays

**Author:** David Adams
**Published:** December 13, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44951
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_44-45_(DEC)/06-45_Array_Statisitics.zip

## Overview
This note provides a full library of statistical functions for numeric arrays (ArrayStats_*), extending well beyond 4D's built-in field-only, PRINT SELECTION-scoped statistical functions of the 2004/2006 era.

## Key Points
- Native 4D statistics (Sum, Average, Min, Max, Std deviation, Variance, Sum squares) only work on fields and are often restricted to PRINT SELECTION report phases — this note's routines work directly on Real/Integer/LongInt arrays via pointer parameters.
- Full function list: `ArrayStats_GetMean`, `GetMedian`, `GetMin`, `GetMax`, `GetMode`, `GetFrequencyCounts`, `GetRange`, `GetStandardDeviation`, `GetSum`, `GetSumSquares`, `GetSumSquaresAlt`, `GetVariance`, `GetWeightedMean`.
- Adds capabilities not in the native set: weighted averages, mode detection with frequency counts, range, and variance/standard deviation computed either from a sample or a full population.
- Each routine validates its pointer parameter first (nil check, numeric-array-type check, empty-array check) before running its core math, using a shared `ArrayStatsError_Set/Get/GetDefinition` system with 14 documented error codes.
- Explains the statistical reasoning behind sum-of-squares (why raw sum of deviations always equals zero, requiring squared deviations instead) and documents both the standard and an alternate "computational method" formula for sum squares.
- `GetMode`/`GetFrequencyCounts` work together to find all modal values (there can be zero, one, or several) with matching frequency counts, sorted by value.
- Recommends compiling with the "All variables are typed" preference for compatibility with the compiler.

## Featured Technology
- 4th Dimension array commands (`SORT ARRAY`, `COPY ARRAY`, `Find in array`, `INSERT ELEMENT`, `DELETE ELEMENT`)
- Pointer-based generic array parameters
- Custom `ArrayStats_*` statistical routine library and error-code management system

## Historical Context
Published in December 2006, just months before 4D v11 introduced native SQL, this note exemplifies the classic pre-collection, pre-ORDA 4D programming style: generic operations on arrays are built using untyped pointers and manual type-checking rather than typed collection objects or built-in generic methods.

## Historical Commentary
**Status:** Superseded

The array-pointer-based generic programming style used throughout this note (and its hand-rolled error-code system) has been superseded by 4D's later collection objects and object notation, which provide built-in methods like `.average()`, `.min()`, `.max()`, and `.sum()` directly on collections with far less boilerplate. That said, 4D still doesn't offer single built-in commands for some of what this note implements (weighted mean, mode detection), so the underlying algorithms remain directly useful reference material even if a modern implementation would use collections rather than array pointers.
