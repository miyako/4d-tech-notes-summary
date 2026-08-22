# Tech Note 21-19: Automatic Output and Input Forms

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** October 28, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78807
**Download:** https://kb.4d.com/DLTN/TN/2021/21-19_AutoForms.zip

## Proposition
Project mode dropped binary mode's automatic input/output form generation for tables with no defined form; this component restores that convenience via dynamically built listbox-based Output/Input forms, while also demonstrating modern var-based, project-mode component packaging conventions.

## Key Points
- **Regression addressed**: binary mode auto-generated input/output forms for tables lacking defined forms; project mode removed this due to ORDA's paradigm shift and preference for listboxes over classic list forms.
- **Single exposed method**: `openTableSelection([tableName])` opens the auto-generated Output form for a given table (or the first table alphabetically if omitted).
- **Output form**: dynamic listbox (one column per non-BLOB field), buttons for add/delete/show all/show subselection/query/sort/Quick Report/Label editor, and a table-switching dropdown.
- **Input form**: dynamically generated input objects per field, navigation buttons (first/previous/next/last), and delete/cancel/validate controls.
- **Modern coding style**: uses `var $x : Type` declarations instead of classic `C_TEXT`/`C_LONGINT` compiler directives, plus ORDA/object notation.
- **Project-mode component packaging**: Components folder sits beside the Project folder (not beside a .4DB/.4DC); compiled components use .4DZ (zipped Project folder); uncompiled components need an alias/shortcut trick to be droppable.

## Featured Technology
- Project-mode component architecture (.4dbase/.4DZ)
- var declarations (vs. C_TEXT/C_LONGINT compiler directives)
- ORDA object notation
- Dynamic listbox-based input/output forms

## Best Practices Highlighted
1. Use var-style declarations and ORDA notation in new project-mode code to match current best practice, as demonstrated by this component.
2. Exclude BLOB fields from auto-generated listbox/input forms since their variable content isn't suited to generic display.
3. Provide a single, minimal exposed entry point (like openTableSelection) when packaging developer-utility components for reuse across hosts.

## Context / Positioning
This note documents both a genuine developer-experience gap opened up by 4D's move to project mode/ORDA and 4D's response — community/support-provided tooling to fill it — while also modeling the coding-style shift (var declarations, ORDA) that 4D was encouraging developers to adopt going forward.

## Historical Commentary
**Status:** Still Relevant

Still useful today: project mode still lacks a built-in equivalent to binary mode's automatic input/output forms, so a utility component like this remains relevant for quick table inspection/editing during development. Its coding conventions (var declarations, ORDA notation) have if anything become more standard and recommended in current 4D, so nothing here reads as outdated practice — only the underlying 'problem' (project mode's lost convenience) is itself a historical artifact of the v17-18 project-mode transition that developers have long since adapted to.
