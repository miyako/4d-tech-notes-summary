# Tech Note 13-01: Advanced List Box Printing

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** January 29, 2013 | **Product/Version:** 4D v13.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76764
**Download:** https://kb.4d.com/DLTN/TN/2013/13-01_ListBoxPrinting.zip

## Proposition
This Tech Note documents advanced printing techniques for 4D v13 List Boxes, covering printing both selection-based and array-based list boxes, producing multi-page printouts with distinct first-page vs. subsequent-page headers, and contextual printing of multiple list boxes or other objects on the same page.

## Key Points
- Confirms list boxes became printable objects starting in 4D v12, inheriting the same programmatic configuration available on-screen.
- Demonstrates printing selection-based list boxes.
- Demonstrates printing array-based list boxes, including subtotal rows.
- Covers multi-page print jobs with different header content on the first page versus subsequent pages.
- Covers contextual/combined printing of multiple list boxes or other form objects together on a single page.

## Featured Technology
- 4D v13 List Box (selection-based and array-based)
- Multi-page printing / page headers
- Subtotals in array-based list boxes
- Contextual printing of multiple objects per page

## Best Practices Highlighted
1. Reuse the same dynamic list box configuration logic for both screen display and print output.
2. Design distinct first-page/continuation-page headers for long multi-page reports for readability.

## Context/Positioning
Published for 4D v13.2 to help developers exploit the then-recent (v12) addition of list box printing support for building sophisticated printed reports directly from forms.

## Historical Commentary
**Status:** Still Relevant

Classic list box printing techniques described here still function in current 4D versions since printable list boxes and their configuration commands remain part of the language. The main shift since this note is that list boxes can now also be built on collections/entity selections rather than only arrays or record selections, so a modern report might source its data via ORDA while reusing the same printing/pagination techniques shown here.
