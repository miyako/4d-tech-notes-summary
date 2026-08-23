# Tech Note: Inherited Forms in 4D v6.7

- **Asset ID:** 11990
- **Tech Note #:** 00-60
- **Published:** December 1, 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hussey (CEO, Alto Stratus LLC)
- **Page URL:** https://kb.4d.com/assetid=11990
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_56-60_(DEC)/00-60_Inherited_Forms.hqx

## Overview

Steve Hussey (CEO, Alto Stratus LLC) explains 4D v6.7's inherited forms feature — one master form shared across multiple tables for consistent buttons and layout — and shows how to write table-agnostic form logic for such a shared form using the Current form table command.

## Key Points

- To create an inherited form: open the Property List palette for a form, set its new **Inherited Form Table** and **Inherited Form Name** properties, and its parent's objects appear (read-only) inside the child form's edit window; inherited objects can be hidden via Form > Display > Inherited Form or a contextual menu.
- Forms load and combine objects in a fixed order: Page 0 (master page) of the inherited form, Page 1 of the inherited form, Page 0 (master page) of the open form, then the current page of the open form — only pages 0 and 1 of the inherited form can appear elsewhere.
- Unlike static templates created with the New Form Wizard, the inheritance reference stays live: editing the parent form automatically updates every form that inherits from it, and inheritance can be chained recursively (a form can inherit from a form that itself inherits from a third form).
- The sample database (Util_Preference_Application, Client, Contact tables) shares one Master_Input_Form and one Master_List_Form across the Client and Contact tables, with standard buttons: record navigation, Accept/Save (input forms); Query…, Subset, All, Delete, Sort…, Labels…, Reports… (list forms).
- The `Current form table` command returns a pointer to the table that owns the currently executing form, letting generic button code call `QUERY(Current form table->)`, `ALL RECORDS(Current form table->)`, `ORDER BY(Current form table->)`, `PRINT LABEL(Current form table->; Char(1))`, and `REPORT(Current form table->; Char(1))` without hardcoding a table name.
- A `WND_TableName` project method uses `Table name(Current form table)` in a `Case of` statement to build an appropriate window title (e.g. "Client Records" vs. "Contact Records") combined with `Records in selection`/`Records in table`, and is invoked on each form's `On Load` event.
- The Subset/Delete button logic uses a `UserSet` set of user-highlighted rows (`Records in set`, `USE SET`, `CREATE SET`) to scope query/deletion operations to just the selected rows while preserving the surrounding selection.

## Featured Technology

- Inherited Form Table / Inherited Form Name form properties
- Current form table command
- Table name command
- QUERY / ORDER BY / PRINT LABEL / REPORT invoked generically via a pointer
- USE SET / CREATE SET for list-form record subsets
- SET WINDOW TITLE for dynamic per-table titles

## Historical Commentary

**Status:** Still relevant

This note explains 4D v6.7's then-new inherited forms feature (one master form reused across multiple tables via the Inherited Form Table/Name properties) and shows how to write table-agnostic button code for a shared form using Current form table, so the same Query/Subset/All/Delete/Sort/Labels/Reports buttons work correctly no matter which table's form is open. Inherited forms as a concept, and the Current form table command itself, remain part of current 4D, so this technique is still directly usable; it has not been replaced so much as supplemented by newer form architecture and object-oriented form/class-based patterns that give developers additional ways to structure reusable UI logic.

**References to newer/updated information:**
- Inherited forms and the Current form table command remain part of the current 4D language and are still a valid way to build reusable, table-agnostic list/input forms
- Modern 4D form architecture (including object-oriented forms, form/object classes, and ORDA-based entity selections) offers additional, more structured techniques for writing reusable form logic beyond the pointer-based, Table name-driven Case of statements shown in this note
