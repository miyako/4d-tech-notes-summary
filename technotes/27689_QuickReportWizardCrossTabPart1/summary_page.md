# Tech Note: Creating a quick Report Wizard

- **Asset ID:** 27689
- **Tech Note #:** 03-16
- **Published:** April 16, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon, 4D Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=27689
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_16-20_(APR)/03-16_Creating_a_QR_Wizard.hqx

## Overview

Jean-Yves Fock-Hoon explains 4D 2003's reworking of the Quick Report editor as a "Report" plug-in area -- not a removable external file but one that behaves like the once-external, later-integrated 4D Chart -- and shows how to build a custom List-report wizard around it, using a sample `[Interface]Wizard` form and the `[Cities]` table as the working example. A second part of the Tech Note extends the same wizard to cross-tab reports.

## Key Points

- The Report plug-in is embedded via a plug-in area (`QRBuilder`) placed on page 0 of a form, invoked in the demo with `DIALOG` from a dedicated interface table rather than directly on an entry form.
- Wizard navigation logic lives in `Wizard_Changepage` (enables/disables menu, toolbar, and contextual-menu items for the current step) and `Wizard_OnCommand` (detects and dispatches user actions).
- First page selects report type -- List or Cross-tab, via `QR SET REPORT KIND` -- and target table via `QR SET TABLE`; this note covers only the List-report path in depth.
- Fields can be added via the contextual menu (opens the 4D Formula dialog for typing a formula or picking fields) or via drag-and-drop, decoded with `DRAG AND DROP PROPERTIES` and `QR Get drop column` -- a positive return value means insert a new column (`QR INSERT COLUMN`), a negative value means replace an existing column's contents (`QR GET/SET INFO COLUMN`).
- `QR ON COMMAND` intercepts menu/toolbar/contextual-menu selections so custom logic can run `QR EXECUTE COMMAND` or cancel the action; the `OK` variable reports whether a dialog was validated (1) or canceled (0).
- Sorting uses `QR SET SORT` with an array of column IDs (developer must avoid letting users sort on non-sortable types like pictures); `QR GET SORT` reads current sort configuration, and break levels are auto-added/removed as sort criteria change.
- Break-level cells support calculation tags: `#S` (sum), `#N` (min), `#X` (max), `#A` (average), `#C` (count), and `##N` to insert the current value of another column N (not usable for pictures); multiple tags can combine in one cell.
- Break-level actions -- no action, page break, or extra spacing (percentage or fixed points) -- are set via the "Total spacing" dialog or programmatically with `QR GET TOTAL SPACING`/`QR SET TOTAL SPACING` (0 = none, positive = points, negative = percentage, 32000 = force a page break).
- Column display formats use `#`, `0`, `*`, `^` characters (own format per column; the `##Z` tag lets one column reuse another's format), and per-cell style attributes are independently configurable.
- The Report plug-in automatically runs a report on the "deepest" related Many table it detects among the inserted fields (via an internal `RELATE MANY SELECTION`), which can mean a report defined on a One table like `[Countries]` silently omits parent records with no matching child records (e.g., no invoices).

## Featured Technology

- Report plug-in area (4D 2003 Quick Report editor as internal plug-in)
- QR SET REPORT KIND / QR SET TABLE commands
- QR ON COMMAND / QR EXECUTE COMMAND (menu, toolbar, contextual menu handling)
- Drag-and-drop field insertion via DRAG AND DROP PROPERTIES / QR Get drop column
- Break-level calculation tags (#S, #N, #X, #A, #C, ##N)
- QR SET TOTAL SPACING (page breaks / extra spacing at break levels)

## Historical Commentary

**Status:** Partially superseded

Jean-Yves Fock-Hoon explains 4D 2003's reimagining of the Quick Report editor as a "Report" plug-in area -- comparable in spirit to how 4D Chart was once an external plug-in later folded into the product -- and builds a custom List-report wizard around it, covering drag-and-drop field insertion, break-level calculation tags, sorting, display formats, and page-break/spacing control at break levels. The Report plug-in area concept and the specific QR commands shown (QR SET REPORT KIND, QR ON COMMAND, QR SET TOTAL SPACING, etc.) remain part of current 4D, so a wizard built this way would still function largely as described. However, 4D Write Pro has since become the more commonly used tool for building modern, richly formatted reports and report-building interfaces, so this classic Quick-Report-plug-in wizard approach, while still valid, is now a less frequently chosen path for new report UI work.

References to newer/updated information:
- The Report plug-in area and its QR command set (QR SET REPORT KIND, QR ON COMMAND, QR SET TOTAL SPACING, drag-and-drop column insertion) remain part of current 4D and continue to work as described
- 4D Write Pro has since become the more commonly used tool for building modern, richly formatted reports and custom report wizards, though the classic Quick Report plug-in engine described here is still available for list-style tabular reporting
