# Tech Note 06-27: Complex Invoice Printing Using Print Form

**Author:** Thomas Maul, General Manager, 4D
**Published:** July 7, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43584
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_27-30_(JUL)/06-27_Complex_Invoice.zip

## Overview
This note demonstrates the power of 4D 2004's enhanced Print Form command through the example of printing a complex, multi-page invoice — with distinct first-page/continuation headers, subtotal vs. final footers, and automatic wrapping of long item text across page breaks — using a reusable "PrintSmartForm" method group.

## Key Points
- Built on the standard "Invoice" example database, extended with a product-description text field and the PrintSmartForm form/methods.
- The 4D form is laid out into named header, detail, break, filler, and footer zones that Print Form triggers appropriately per page.
- Long article descriptions that span multiple lines/pages require calculating word-break positions via a plug-in rather than printing as a single text object.
- Uses "LineStarts," a plug-in first published in September 1992 as 4D's very first Tech Note (from 4D US), recompiled as a cross-platform Mac/Windows bundle for this note.
- LineStarts usage: pass a text field, font, size, style, and width; returns an array of break positions.
- Integrating the reusable PrintSmartForm code: copy the "PrintSmartForm" group via 4D Insider, or manually copy the four "PrSF_" methods.
- Requires wiring the form's `On Printing Detail` event to call `PrSF_PrintFormMethod`, and calling `PrSF_Print` with pointers to the invoice/line-item tables and text formatting parameters.
- `PrSF_ItemCalculation` is a customizable per-item hook (using a Case statement) for accumulating subtotals or supporting multiple document types (invoices, shipping papers, orders).

## Featured Technology
- 4D Print Form command (enhanced in 4D 2004)
- PrintSmartForm reusable method group
- LineStarts plug-in (text break/word-wrap calculation)
- 4D Insider (for copying reusable components)

## Historical Context
Published in 2006 for 4D 2004, this note showcases classic 4D form-based printing techniques predating 4D Write Pro (2016) and any modern document-generation tooling. It references LineStarts as originating from 4D's very first published Tech Note in 1992, giving it a notable lineage within 4D's technical documentation history.

## Historical Commentary
**Status:** Still relevant

The specific LineStarts plug-in binary and 4D Insider-based component-copying workflow are outdated, but the core Print Form layout technique — dividing a form into header/detail/break/footer zones to produce complex multi-page documents — remains conceptually how 4D's classic form-based printing works today. Developers using 4D's traditional printing approach (rather than 4D Write Pro) would still recognize and could still apply this pattern.
