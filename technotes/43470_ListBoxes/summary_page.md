# Tech Note 06-25: List Boxes

**Author:** Jean-Yves Fock-Hoon, Quality Assurance Manager, 4D Inc.
**Published:** June 23, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43470
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_22-26_(JUN)/06-25_List_Boxes.zip

## Overview
Part I of a two-part Tech Note introducing the List Box object, a major new form control added in 4D 2004 that replaces the older approach of manually grouping several basic scrollable areas to display multi-column data. Part I covers how to create and configure a list box via the Design-mode Form editor; Part II (a separate note) covers the same object via the 4D language.

## Key Points
- List Box is a new 4D 2004 object superseding older grouped-scrollable-area techniques, offering more control over data display and entry.
- Created by drawing from the Form editor toolbar; clicking once selects the whole object, clicking again selects a specific column or header — a UI subtlety developers must watch for.
- Number of columns: the count of visible columns, driven by underlying arrays (typically Boolean/array-backed); increasing the count auto-inserts new default columns.
- Number of Static columns: the count of leading columns that cannot be reordered via drag.
- Show Column Header: toggles header title visibility; controllable at runtime with `SET VISIBLE`, independent of whether header variables are otherwise in use.
- Multiple Selections: a Design-mode-only checkbox enabling multi-row selection (no language equivalent).
- Row Style Array, Font Color Array, Background Font Color Array: properties allowing per-row visual styling via 4D arrays.

## Featured Technology
- 4D List Box object (Design mode configuration)
- 4D Form editor
- Array-driven column/row display and styling

## Historical Context
Published in June 2006, this is foundational documentation for the List Box object in its first year of existence in 4D 2004 — a form control that went on to become a cornerstone of 4D UI development for the next two decades. It predates 4D v11's 2007 SQL engine, Project Mode (2018), and ORDA.

## Historical Commentary
**Status:** Still relevant

The core List Box concepts explained here — array-backed columns, static (non-movable) columns, header visibility, multiple-row selection, and per-row style arrays — remain fundamental to how List Box works in 4D today, even though the object's feature set, styling options, and Design/Project Mode tooling have been substantially expanded since 2004. This note is a useful historical baseline for understanding the object's original design.
