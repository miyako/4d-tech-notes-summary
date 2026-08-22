# Tech Note 11-26: List Boxes in 4D v12: Hierarchy and Printing

**Author:** Bertrand Soubeyrand, Soubeyrand Consultant.
**Published:** August 18, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76393
**Download:** https://kb.4d.com/DLTN/TN/2011/11-26_ListBoxExtendedFeatures.zip

## Proposition
This Tech Note covers the two major list box enhancements introduced in 4D v12 — printing list boxes and building hierarchical (collapsible/expandable) list boxes using arrays — with a demo database illustrating both.

## Key Points
- **History of the list box object:** from 4D 2004 (array-only) through 4D v11 SQL (table/named-selection support) to v12's fully programmable, dynamically retitlable columns and headers.
- **New/modified commands:** LISTBOX COLLAPSE, LISTBOX EXPAND, LISTBOX SET HIERARCHY, LISTBOX GET HIERARCHY, LISTBOX GET PRINT INFORMATION, LISTBOX SELECT BREAK, and updated LISTBOX Get column width.
- **Hierarchy building:** constructing a hierarchical list box object from boolean arrays and exporting/importing its format via XML.
- **Printing support:** shows how OPEN PRINTING JOB, OPEN PRINTING FORM, and Print object make a previously-unprintable array-based list box printable.
- **Worked example:** an interface with buttons driving the print_lb_process method, plus a full example database.

## Featured Technology
- Array-type list boxes (LISTBOX SET HIERARCHY / LISTBOX GET HIERARCHY / LISTBOX COLLAPSE / LISTBOX EXPAND)
- List box printing (OPEN PRINTING JOB, OPEN PRINTING FORM, LISTBOX GET PRINT INFORMATION)
- XML export of list box configuration

## Context / Positioning
Published in mid-2011 for 4D v12, this note addressed two long-standing list box limitations (no printing, no hierarchy) that had frustrated developers building reporting-style grid interfaces since list boxes were introduced in 4D 2004.

## Historical Commentary
**Status:** Still Relevant

Array-based hierarchical list boxes and the LISTBOX printing commands documented here still exist and function in current 4D, so the technique remains usable as described.

That said, 4D has since added collection/entity-selection-based list boxes that are generally preferred for new development because they integrate directly with ORDA data sources rather than requiring manual array population and synchronization, so new projects would likely start from that newer approach instead of the pure-array technique shown here.
