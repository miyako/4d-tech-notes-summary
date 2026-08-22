# Tech Note 06-35: Plug-in support with Print Form

**Author:** Thomas Maul, General Manager, 4D
**Published:** September 8, 2006 | **Product/Version:** 4D v2004.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44120
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_35-37_(SEP)/06-35_Print_Form_w_Plug-ins.zip

## Overview
4D version 2004.5 introduced support for printing plug-in content — specifically 4D Write — within Print Form-based reports. This note extends an earlier invoice-printing Tech Note (TN 06-27, which used plain 4D text fields) to instead use 4D Write for styled, richly formatted invoice item descriptions including embedded pictures, with automatic splitting of overflow content across page breaks.

## Key Points
- Builds on the "Invoice" sample database from the 4D 2004 Evaluation installer, adding a 4D Write field to the product table for item descriptions; requires the 4D Write plug-in to run.
- Retains the prior note's multi-page print behaviors: distinct first-page vs. subsequent-page headers, and distinct subtotal vs. final-page footers.
- New capability: when a 4D Write item description is too large to fit remaining page space, the content is automatically measured, resized, and split — printing the remainder on the following page via a break area.
- Core method `PrSF_WriteBreakCalculation` handles this: it adjusts the 4D Write object's width to the form, computes remaining vertical space, and decides whether to print the whole item in the Detail area or split it across Detail + Break0.
- Integration steps: use 4D Insider to copy the "PrintSmartForm" method group (four `PrSF_`-prefixed methods) into a target app; design a print form with exactly two headers and three breaks; add a specific `On Printing Detail` form-method snippet; write a driving print method calling `PrSF_Print` with pointers to the main/item tables and footer text/font parameters.
- `PrSF_ItemCalculation`, run once per printed item, can be customized to maintain running subtotals or support multiple document types (invoices, shipping papers, orders) via a `Case of` template method.
- Using a different plug-in (e.g., 4D View) instead of 4D Write would require writing an analogous break-calculation method.

## Featured Technology
- Print Form (4D's multi-page report printing engine, with Detail/Break/Header/Footer areas)
- 4D Write (plug-in for styled text and embedded pictures)
- 4D Insider (tool for copying reusable method groups between 4D databases)

## Historical Context
Written for 4D 2004.5, this note documents an early solution to a persistent reporting challenge: printing variable-length rich content that must paginate cleanly. It predates 4D's own SQL engine (v11, 2007), Project Mode (v17, 2018), and especially 4D Write Pro, the modern rich-text engine introduced in 4D v15 (2016) that eventually replaced the classic 4D Write plug-in referenced here.

## Historical Commentary
**Status:** Superseded

The general challenge this note solves — printing variable-length rich content (text with embedded pictures) that must split cleanly across page boundaries in a paginated report — remains a real and relevant reporting problem today. However, the specific tools used are dated: the classic 4D Write plug-in was superseded by 4D Write Pro starting in 4D v15 (2016), and 4D Insider's role of copying method groups between separate Design Mode structure files reflects a pre-Project-Mode (pre-v17) workflow that modern 4D component/project-based development has moved beyond.
