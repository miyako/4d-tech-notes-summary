# Tech Note 07-38: New List Box Features in 4D v11 SQL

**Author:** Larry Sharpe, 4D Developer, InfoService
**Published:** September 26, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47598
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_35-38_(SEP)/07-38_4D_v11_SQL_Listbox.zip

## Overview
This note covers new List Box capabilities in 4D v11 SQL — Current Selection and Named Selection as data sources, alongside the pre-existing array-based approach — plus the new Project Forms concept, illustrated with a [People]/[Companies] sample database.

## Key Points
- Three List Box Data Sources documented: **Arrays** (as in 4D 2004), **Current Selection** (fields/expressions from the records currently selected), and **Named Selection** (similar, but based on a persisted ordered set).
- **Project Forms**, new in v11 SQL, allow building forms not bound to any specific table — well suited to dialogs — and are used for all example forms in this note.
- Sample database: [People] and [Companies] tables linked via a company reference, each with trigger-generated auto-increment IDs, usable in "List of Tables" mode (v11 SQL's renamed "User Mode").
- All three List Box examples support Add/Modify (double-click) and Delete on [People] records, configurable for single or multi-row selection via List Box Properties plus matching button-script changes.
- A shared Project Method (`ListBox_xxx_Functions`) centralizes logic reused by the List Box and its Add/Delete buttons.
- Arrays example: manual `Selection To Array` population plus a hidden ID array for record identification; cannot use in-column Expressions (unlike the newer data sources).
- Current Selection example: fields/columns configured directly in List Box Properties/Column Properties, with a simple `All Records` call (a Query or related-table selection could substitute).
- Developers can still fall back to List Box/Object Properties commands in code for the ~5% of cases the form editor doesn't cover.

## Featured Technology
- List Box form object with Current Selection / Named Selection data sources
- Project Forms (table-independent forms)
- List Box Properties / List Box Column Properties
- `Selection To Array`, `All Records` commands

## Historical Context
Published in September 2007 as 4D v11 SQL approached release, this note documents a genuinely lasting improvement to 4D's form-building toolkit — selection-bound List Boxes and Project Forms — delivered at a time when all 4D development still occurred in binary Design Mode, roughly a decade before Project Mode (2018) formalized project-based form/file organization.

## Historical Commentary
**Status:** Still relevant

List Boxes bound to a Current Selection or Named Selection (rather than manually managed arrays) became, and remain, standard practice in 4D development, so the core techniques in this note are still directly applicable. Project Forms, introduced around this time, went on to become foundational to 4D's later Project Mode (4D v17, 2018), making this note a good historical marker of where that concept began, even though the specific "List of Tables" mode terminology and screenshots reflect the pre-Project-Mode design environment.
