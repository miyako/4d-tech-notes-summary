# Tech Note: Inside the Report Demo Database

- **Asset ID:** 19056
- **Tech Note #:** 01-57
- **Published:** December 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar, Inside Sales Representative, 4D, Inc. (example database created by Tad Michael Wheeler, DataCraft)
- **Page URL:** https://kb.4d.com/assetid=19056
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_57-61_(DEC)/01-57_Inside_the_Report_Demo.hqx

## Overview

Jonathan Baltazar tours the "Report Demo" sample database (originally created by Tad Michael Wheeler of DataCraft), a three-table hierarchical example built around Departments, Employees, and Donations, to explain how it demonstrates 4D's classic grouped/subtotaled reporting commands and a reusable name-formatting utility.

## Key Points

- The database uses `On Startup` -> `Shell_Startup` to bootstrap a shared "Simple Shell" UI framework common to many 4D example databases of the era.
- The `ReportDemo_SpecialReport` project method sets `SET PRINT PREVIEW(True)`, selects `ALL RECORDS([DONATIONS])`, then applies a three-key `ORDER BY` (Department Name, Quarter of Date, Donation Date) to sort the report data.
- `BREAK LEVEL(2;1)` inserts a break after the second sort key (Quarter of Date), and `ACCUMULATE([DONATIONS]Donation Amount)` computes a running subtotal for each quarter within a department.
- The report is rendered by switching `OUTPUT FORM` to `"R.Quarter"`, calling `PRINT SELECTION([DONATIONS])`, then switching back to the `"Output"` form, with `SET PRINT PREVIEW(False)` closing the preview session.
- On the Employee input form, the `pSal` (salutation), First Name, Middle Initial, and Last Name object methods all call a shared `ReportDemo_FormatName` project method to keep `[EMPLOYEES]Emp Formal Name` in sync as fields are entered.
- `ReportDemo_FormatName` uses a `Case of` block to abbreviate the middle initial (blank if empty or ".", otherwise `Substring` to the first character plus "."), then nested `If`/`Case of` logic to assemble Salutation + First + Middle + Last, First + Last, or just Last depending on which fields are populated.
- The example illustrates practical, still-valid patterns for grouped reports (department -> quarter subtotal) and for keeping a derived display field synchronized across several form-level object methods.

## Featured Technology

- ORDER BY multi-field sorting
- BREAK LEVEL
- ACCUMULATE
- SET PRINT PREVIEW
- PRINT SELECTION / OUTPUT FORM
- Substring-based name formatting

## Historical Commentary

**Status:** Still relevant

Jonathan Baltazar walks through the 'Report Demo' sample database (created by Tad Michael Wheeler of DataCraft) to teach 4D's classic reporting building blocks -- ORDER BY, BREAK LEVEL, and ACCUMULATE -- for producing a subtotaled donations report grouped by department and quarter, plus a small name-formatting utility method. These reporting commands are still part of current 4D and the break-level/accumulate pattern remains a valid, still-used technique for simple grouped reports, though modern 4D applications more often use the more flexible List Form / collection-and-ORDA-based reporting or dedicated reporting tools for anything beyond a basic printed report.

References to newer/updated information:
- ORDER BY, BREAK LEVEL, ACCUMULATE, SET PRINT PREVIEW, and PRINT SELECTION remain valid, supported 4D commands for this exact type of grouped report
- Modern 4D reporting for richer or web-facing needs increasingly uses collection/ORDA-based approaches or dedicated reporting components rather than classic break-level printed reports
