# Tech Note: 4D Quick Report Editor Source Code - Part 1

- **Asset ID:** 36757
- **Tech Note #:** 05-13
- **Published:** March 31, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Kent Wilbur
- **Page URL:** https://kb.4d.com/assetid=36757
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-13_QR_Editor_Source_I.hqx

## Overview

Kent Wilbur (4D, Inc.) begins a three-part technical series unpacking the source code behind the rebuilt 4D 2003/2004 Quick Report editor and wizard. Part 1 covers the code that runs when the editor form is first opened and prepared: loading the database structure into memory as a set of arrays (a "virtual structure"), and building the hierarchical lists of fields the wizard presents to the user. The note is aimed at developers who want to fork, simplify, or borrow pieces of the stock editor for their own report-building UI rather than use the full wizard as shipped.

## Key Points

- Entry point __Open_dialog opens the NQR_Dialog form and exposes three controlling Boolean-like variables — nqr_wizard, nqr_allowsearches, nqr_allowautomatic — matching the QR Report command's last three parameters.
- NQR_Init_Struct_Description builds an in-memory "virtual structure": parallel arrays of table names/IDs (GET TABLE TITLES) and, per table, field names/IDs (GET FIELD TITLES), plus arrays tracking relationship parent/child roles and whether a relation is automatic.
- NQR_MP_Get_Fields (covered in detail) uses that virtual structure to construct the hierarchical list of fields shown to the end user for building a report.
- Demonstrates the SET FORMAT picture-resource trick — e.g. "1;4;:14934;64" (1 column, 4 rows, picture resource #14934, transparent background) — for programmatically swapping form images without touching the form itself, noted as valuable for 4D 2004's new editable user forms.
- Explains QR SET AREA PROPERTY as the only supported way to affect the licensed plug-in area's appearance (menus, toolbar sections); the plug-in area's internal code itself is off-limits.
- Documents the form's layering convention: View 1 (active/programmed objects), View 2 (second layer), View 3 (buttons), View 4 (static objects), View 5 (appearance-only decoration) — used throughout the series.
- Sets up Parts 2 (manual-mode code) and 3 (wizard code) as direct continuations assuming familiarity with this installment.

## Featured Technology

- 4D Quick Report built-in editor form
- NQR_Init_Struct_Description virtual structure builder
- GET TABLE TITLES / GET FIELD TITLES
- Hierarchical list construction (NQR_MP_Get_Fields)
- SET FORMAT picture-resource technique (e.g. "1;4;:14934;64")
- QR SET AREA PROPERTY / QR Get report kind

## Historical Commentary

**Status:** Historical Interest Only

This first installment of a three-part series walks through the source code of 4D 2003/2004's built-in Quick Report editor form, focusing on how it reads the database structure into memory (via GET TABLE TITLES/GET FIELD TITLES) and builds the hierarchical field-picker lists used by the wizard. It's a deep, form-object-level dissection aimed at developers who wanted to fork or slim down the stock editor rather than build reporting from scratch — a very of-its-era approach since 4D forms and their object methods were the only UI layer available. The specific Quick Report editor internals are long obsolete, but the underlying techniques (virtual in-memory structure description, hierarchical list building, and packing multiple values into a single longint via SET FORMAT's picture-resource trick) remain conceptually interesting even though modern 4D favors List Box/ORDA and 4D Write Pro for reporting.

References to newer/updated information:

- 4D Write Pro (introduced 2016) and List Box-based reporting are the modern approaches for building report UIs, superseding the classic Quick Report editor form dissected here
- GET TABLE TITLES and GET FIELD TITLES remain valid 4D commands today, though ORDA-based data model introspection is now the more common technique in modern 4D code
