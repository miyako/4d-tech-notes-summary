# Tech Note 96-44: Manipulating Arrays, Strings, and Dates in 4th Dimension

**Author:** Walt Nelson
**Published:** October 31, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11722
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_42-44_(OCT)/96-44_ArraysStringsDates.exe

## Overview
This Technical Note is a practical library of reusable array, string, and date manipulation routines for 4D developers, built around the "parameter indirection" (pointer-based) technique for writing generic procedures that work across many named arrays or variables without hard-coding their names.

## Key Points
- **Array routines:** `ArrayDelete`/`ArrayInsert` (indirection-based, up to 23 arrays per call; performance note favors bulk resizing over loop-based insert/delete), `ArrayUp`/`ArrayDown` (wraparound highlight navigation for arrow-key buttons), `ArraySum`, and `Arr_Find_in_List`/`ArrFindMeaning` (choice-list code-to-meaning lookups).
- **Date routines:** `Date1stofMonth`/`DateLastOfMonth`, `DateBlank` (indirection-based, up to 25 dates), `DateDayofWeek`, `DateFormatCalc` (locale/date-format detection at startup), `DateGet` (month-offset calculation), and `DateParse`/`DateValidate`.
- **String routines:** `StringBlank`/`StringNmbrZero` (indirection-based, up to 25 fields/variables), `StringConcat`, `StringFmDollars` (dollar-to-words, requires ACI PACK plugin + string resource), and `StringPadSpaces`/`StringPadZeros`/`StringUpprLower`.
- Example database provides interactive test dialogs for each category (Array, Date, String Manipulation menu items).
- Appendix supplies commented source code for the array routines as representative examples.

## Featured Technology
- 4D array manipulation routines
- 4D date manipulation routines
- 4D string manipulation routines
- Parameter indirection (pointer-based array/variable passing)
- 4D Insider

## Historical Context
**Status:** Still relevant

This note reflects the utility-library philosophy that has always been part of 4D development, and much of its content — the parameter-indirection technique and the individual algorithms for array, date, and string handling — remains conceptually applicable today. What has changed: 4D has since added many built-in language commands and object/collection-based methods that can replace several of these hand-rolled routines, and 4D Insider, the standalone tool referenced for moving code between structures, was long ago superseded by the built-in project and methods management of the modern 4D IDE.
