# Tech Note: 4D Quick Report Editor Source Code - Part II

- **Asset ID:** 36838
- **Tech Note #:** 05-14
- **Published:** April 7, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=36838
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-14_QR_Editor_Source_II.hqx

## Overview

Kent Wilbur (4D, Inc.) continues his Quick Report editor source-code series with Part 2, covering the manual-mode form page used when an end user builds a report without the wizard. The note walks through handling drag-and-drop and double-click interactions between the hierarchical field lists and the plug-in report area, and the more subtle mechanics of keeping multiple visible sort-order indicators synchronized for both list-style and cross-tab reports.

## Key Points

- Describes the manual-mode form page layout: Table/select-from popups and a primary hierarchical field list in one view; a static table-name label, related-table field list, and cross-tab sort options in a second overlapping view.
- NQR_MP_CALL acts as the central dispatch method handling user actions directed at the plug-in report area.
- Documents the code for handling drag-and-drop of fields from the hierarchical lists into the plug-in area, plus double-click handling as an alternative interaction path.
- Covers 'Sorting the list style report' — the logic for keeping the sort-order hierarchical list synchronized as the user adds/removes/reorders sort fields.
- Explains 'Synchronizing the visible sorting hierarchical lists' — a technique for making a single underlying list appear consistently in more than one on-screen location, described as the series' key trick.
- Covers a parallel 'Synchronizing the cross tab sorting indicators' section for cross-tab report sort behavior, distinct from the list-style logic.
- Assumes and builds directly on the virtual-structure and hierarchical-list-building code introduced in Part 1; sets up Part 3's coverage of the wizard.

## Featured Technology

- 4D Quick Report editor manual mode form page
- NQR_MP_CALL dispatch method
- Drag and drop handling in the plug-in area
- Double-click handling for hierarchical field lists
- List-style and cross-tab sort-order synchronization
- Hierarchical list synchronization across multiple visible copies

## Historical Commentary

**Status:** Historical Interest Only

The second installment of Kent Wilbur's Quick Report editor source-code series dissects the manual-mode form page: the popups, hierarchical lists, drag-and-drop handling into the plug-in report area, and the logic that keeps multiple on-screen sort-order indicators synchronized for both list-style and cross-tab reports. It is a detailed, code-level tour of a specific classic-4D form implementation rather than a general-purpose technique, so its direct applicability faded once 4D moved reporting toward List Box objects and 4D Write Pro; the drag-and-drop and multi-list-synchronization patterns it documents, however, illustrate general classic-4D form-event programming that developers maintaining legacy databases may still encounter.

References to newer/updated information:

- List Box-based reporting and 4D Write Pro have superseded the classic Quick Report editor's manual mode described here
- The drag-and-drop and multi-list-synchronization form-event patterns documented are general classic-4D techniques, still valid for legacy code but not the primary approach in current object/List Box-driven development
