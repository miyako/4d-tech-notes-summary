# Tech Note: 4D Quick Report Editor Source Code - Part III

- **Asset ID:** 36923
- **Tech Note #:** 05-15
- **Published:** April 15, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=36923
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-15_QR_Editor_Source_III.hqx

## Overview

Kent Wilbur (4D, Inc.) concludes his three-part Quick Report editor source-code series by dissecting the wizard: its page-based navigation system, the distinct page flows for list-style versus cross-tab reports, and the complex graphics that give the editor its visual polish. The note positions the underlying project methods as reusable building blocks for developers who want to construct their own, simpler report editor UI rather than use the stock wizard as-is.

## Key Points

- The wizard is structured as a sequence of form pages, one per wizard step; the first page selects report type (list vs. cross-tab) and determines which subsequent pages are shown.
- A shared navigation system lives on form page 0 so its Next/Back controls overlay every wizard step consistently.
- 'The list style Wizard pages' is the longest section, walking through the pages used to configure a list-style report (fields, sorting, and related settings), reusing the hierarchical-list and synchronization code from Parts 1 and 2.
- 'The cross-tab style Wizard pages' covers the shorter, distinct page flow for cross-tab reports.
- 'The graphics behind the editor' section catalogs over a hundred images used across the form — some simple pictures, some resource-referenced, some that grow/move/stay fixed on resize — and explicitly advises against trying to modify them due to their complexity.
- Recommends that developers wanting their own report editor take the active objects (Views 1–2) and project methods from the source and build a fresh, simpler form/interface around them rather than editing the existing graphics.
- Closes the trilogy by highlighting reusable general concepts demonstrated across all three parts: virtual in-memory structure building, BLOB-based settings retrieval, packing multiple values into a longint, and hierarchical list manipulation/synchronization.

## Featured Technology

- 4D Quick Report wizard multi-page form navigation
- List-style wizard pages (report type selection through field/sort configuration)
- Cross-tab-style wizard pages
- Shared page-0 navigation system for a multi-page wizard form
- Complex form graphics (resource-based images, resizing/growing objects)

## Historical Commentary

**Status:** Historical Interest Only

This final installment of the three-part Quick Report editor series covers the wizard itself: the multi-page form navigation system and the distinct sets of pages used for list-style versus cross-tab reports, plus a closing note on the editor's elaborate graphics (which the author explicitly advises against trying to modify). Read together, the trilogy is a rare, unusually thorough piece of internal 4D UI source documentation for its time, but it documents a specific classic Quick Report form that has since been superseded by more modern reporting approaches; the wizard-navigation and multi-page-form techniques it demonstrates remain conceptually valid for classic-language multi-step form wizards but are not how new 4D UI wizards are typically built today (dialog boxes, forms with page controls, or web-based front ends are more common now).

References to newer/updated information:

- 4D Write Pro and List Box-based reporting have superseded the classic Quick Report wizard whose full source is documented across this three-part series
- No known follow-up 'Variations on the Quick Report editor' series was published; the invitation in this note appears not to have been picked up in later official Tech Notes
