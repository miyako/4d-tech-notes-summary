# Tech Note 11-12: PHPExcel Library with 4D v12

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** April 15, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76312
**Download:** https://kb.4d.com/DLTN/TN/2011/11-12_PHPExcel_Library_and_4D.zip

## Proposition
This note demonstrates how to leverage 4D v12's newly embedded PHP interpreter to call the open-source PHPExcel library for reading Microsoft Excel files from within a 4D application. It documents the relevant PHPExcel API functions (getting sheet names, active sheet index, sheet count, row/column counts, and cell data/styles), then builds a layer of PHP class wrappers and corresponding 4D project methods that bridge PHP calls into 4D-callable functions. A capstone example shows importing Excel data directly into a 4D list box. The note is aimed at developers who need to import or process Excel spreadsheet data without relying on OS-level automation or manual CSV conversion.

## Key Points
- Explains 4D v12's newly embedded PHP interpreter as the enabling technology for calling PHP libraries directly from 4D code.
- Documents core PHPExcel API functions for sheet enumeration, row/column counts, and cell data/style retrieval.
- Builds PHP class wrapper functions (excel_GetSheetNames, excel_GetDataFromCell, etc.) around the PHPExcel API.
- Builds corresponding 4D project methods (Excel_GetFileFormat, Excel_NumSheets, Excel_GetDataFromRow, etc.) that call the PHP wrappers from 4D.
- Provides a working example importing Excel data into a 4D list box.
- Includes a general-purpose PHP diagnostic utility method (UTIL_phpMoreInfo).

## Featured Technology
- 4D's embedded PHP interpreter (v12)
- PHPExcel open-source library
- 4D-to-PHP wrapper methods for reading Excel data into list boxes

## Best Practices Highlighted
- Wrap third-party PHP library calls in dedicated 4D project methods to isolate integration complexity
- Layer PHP class wrappers between the raw library API and 4D-callable methods for cleaner interfaces

## Context / Positioning
Published shortly after 4D v12 introduced its embedded PHP interpreter, this note showcased a flagship use case (reading Excel files without native Excel automation) to help developers adopt the new PHP integration capability.

## Historical Commentary
**Status:** Partially Superseded

4D's embedded PHP interpreter and the PHPExcel-based approach shown here still function, but this integration path is now a niche, legacy technique — 4D has since added native spreadsheet capabilities via 4D View Pro, which can read/write true Excel (.xlsx) files directly without a PHP bridge, and PHPExcel itself was deprecated years ago in favor of its successor library PhpSpreadsheet. For new development, native 4D tooling is the more idiomatic choice.
