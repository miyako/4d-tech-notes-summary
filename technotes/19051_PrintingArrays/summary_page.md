# Tech Note: Printing Arrays

- **Asset ID:** 19051
- **Tech Note #:** 01-52
- **Published:** November 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hussey, Editor and Publisher, Dimensions Journal
- **Page URL:** https://kb.4d.com/assetid=19051
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_51-56_(NOV)/01-52_Printing_Arrays.hqx

## Overview

Steve Hussey demonstrates how to print array-backed dialog data -- something 4D cannot do directly -- using a sample invoice database that builds a grouped, scrollable "Sales by Year" summary in arrays and then prints it via the PRINT FORM command, one array-driven line at a time, through matching process variables on a Detail form.

## Key Points

- The sample Invoice table has Amount, Invoice_Type ("Cash"/"Credit"/"Check"), and Invoice_Year fields; an Invoice Summary dialog shows five parallel arrays (`aint_Year`, `areal_YearTotal`, `areal_Amount_Cash`, `areal_Amount_Credit`, `areal_Amount_Check`) as grouped scrollable areas that scroll in sync.
- The year array is built with `DISTINCT VALUES([Invoice]Invoice_Year;aint_Year)` then `SORT ARRAY(aint_Year;>)`; companion total arrays are sized to match with `ARRAY REAL(...;Size of array(aint_Year))`.
- A loop `For ($Year;1;Size of array(aint_Year))` runs `QUERY([Invoice];[Invoice]Invoice_Year=aint_Year{$Year})`, then a nested loop over `NEXT RECORD` uses a `Case of` on `Invoice_Type` to accumulate Cash/Credit/Check totals into the corresponding array element, followed by a per-year total calculation.
- Grouped scrollable areas are created by placing individually named array-bound objects side by side and using the Group menu item, producing one shared scroll bar for all arrays simultaneously.
- Since only process (or interprocess) variables -- not arrays -- can be printed on a form, printing requires a parallel Detail form with process variables (e.g. `int_Year_frm`, `real_Amount_Cash_frm`) that are set from each array element inside a print loop.
- The print routine `INV_SmryPrt` calls `PRINT SETTINGS` for paper options, then `PRINT FORM([Invoice];"INV_HDR_prt")` for the header (built by dragging the Header marker to 0 and Detail down, since PRINT FORM only ever prints a form's Detail section), loops through the year array setting process variables and calling `PRINT FORM([Invoice];"INV_Dtl_prt")` per row while accumulating grand totals, then prints a footer form and finally issues `PAGE BREAK(*)` to eject the accumulated pages from memory to the printer.
- The technique is presented as general-purpose: any array of data (not just invoice summaries) can be printed this way by mapping array elements to process variables one row at a time.

## Featured Technology

- PRINT FORM command
- DISTINCT VALUES / SORT ARRAY
- Grouped scrollable array display on a dialog
- Process variables mirroring array elements for printing
- PRINT SETTINGS / PAGE BREAK
- QUERY-based accumulation loop

## Historical Commentary

**Status:** Partially superseded

Steve Hussey, Editor and Publisher of Dimensions Journal, explains a workaround for a real limitation in classic 4D: arrays cannot be printed directly, so this note shows how to loop through array elements, copy each one into a process variable placed on a Detail-only print form, and call PRINT FORM repeatedly (header, then one call per data row, then footer) followed by PAGE BREAK to produce a printed report from array-backed dialog data. This process-variable-per-row PRINT FORM looping technique remains technically valid in current 4D and is still occasionally used, but modern 4D reporting increasingly favors List Forms, Quick Reports, or web/PDF-based report generation that can work with arrays, collections, or entity selections more directly, reducing the need for this manual per-row form-printing loop.

References to newer/updated information:
- The PRINT FORM/process-variable-loop technique described here still works in current 4D, but many developers now use List Forms, printable collections, or PDF/report generation tools that handle array or collection data more directly
- Nothing about PRINT FORM's inability to print arrays directly has changed; this note's underlying technique remains a valid, if manual, workaround today
