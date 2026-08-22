# Tech Note 10-05: Array Utilities

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** February 12, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76020
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_04-07_(FEB)/10-05_ArrayUtilities.zip

## Proposition
This note documents Array Utilities, a 4D v11 SQL component providing a broad library of ARR_-prefixed methods for validating, sizing, searching, copying, and performing set/statistical operations on classic 4D arrays, so developers don't need to write these routines themselves.

## Key Points
- **Array information/validation**: ARR_IsAnArray, ARR_IsNumericArray, ARR_IsTextArray, ARR_IsNdxValid.
- **Sizing and populating**: ARR_SizeArrays, ARR_InsertRows, ARR_DeleteRows, ARR_DeleteRowsByIndex.
- **Set operations**: ARR_Distinct, ARR_Intersect, ARR_Difference, ARR_Union, ARR_ArrayToSet.
- **Statistical functions**: mean, median, mode, min/max, standard deviation, variance, weighted mean, sum/sum-of-squares, frequency counts, and range.
- **Running calculations**: running average, running difference, running total, running weighted average, and product.
- **Search, copy, and fill utilities**: FindInArray_All, Find_Between_Values/Indexes, ARR_LookUp, ARR_CopyElements/CopySegment, ARR_FillValue variants, ARR_Convert to/from Text, ARR_Shuffle, ARR_Push, ARR_Pop.

## Featured Technology
- Array Utilities 4D v11 SQL component
- Array set operations (ARR_Intersect, ARR_Difference, ARR_Union)
- Array statistics (mean, median, mode, standard deviation, variance)
- Array search/copy/fill utility methods

## Best Practices Highlighted
1. Validate array type/index before operating on it to avoid runtime errors (ARR_IsAnArray, ARR_IsNdxValid).
2. Use set-style operations (intersect/difference/union) instead of hand-rolled loops for comparing arrays.
3. Reuse a tested statistics library rather than re-implementing standard deviation, variance, or weighted mean calculations per project.

## Context / Positioning
Published as a general-purpose utility component for 4D v11 SQL developers, filling a gap in the classic language's built-in array command set with reusable, tested helper methods.

## Historical Commentary
**Status:** Partially Superseded

This note documents a self-contained component library adding dozens of utility methods for classic 4D arrays: information/validation checks, resizing, set operations (intersect/difference/union), statistical functions (mean, median, mode, variance, standard deviation), running calculations, search, and copy/fill helpers.

Classic arrays and these utility methods remain fully functional in current 4D versions, so the component is still technically usable, but 4D has since introduced native Collection objects (with built-in methods like .min(), .max(), .average(), .distinct(), .sort()) that cover much of this same ground with a more modern, object-oriented syntax. Developers starting new projects today would generally reach for Collections rather than this classic-array utility component, though it remains a valid option for maintaining legacy code.
