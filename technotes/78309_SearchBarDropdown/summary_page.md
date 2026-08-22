# Tech Note 19-14: Creating a Search Bar with Dropdown List

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** August 30, 2019 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78309
**Download:** https://kb.4d.com/DLTN/TN/2019/19-14_SearchBar.zip

## Proposition
A search bar with a live dropdown of suggestions saves users a step compared to plain search fields, and this note provides a complete, reusable implementation pattern for it in classic 4D forms.

## Key Points
- **Basic search:** `Get edited text` on `On After Edit` feeds a `QUERY` against the target table (e.g., `first_name=$input+"@"`).
- **Compound field search:** `Split string` splits user input on spaces to query first name then refine with `QUERY SELECTION` on last name.
- **Dropdown visibility:** `OBJECT SET VISIBLE` shows/hides a selection-based list box depending on whether there's input or matches.
- **Dynamic dropdown height:** computed from `Records in selection`, `LISTBOX Get rows height`, and `OBJECT GET/SET COORDINATES`, capped at a max row count.
- **Keyboard navigation:** invisible up-arrow/down-arrow/enter buttons drive `LISTBOX SELECT ROW` and `Selected record number` to change and display the selection.
- **Cursor and scroll polish:** `HIGHLIGHT TEXT` keeps the text cursor at the end of inserted text; `OBJECT SET SCROLL POSITION` keeps the highlighted suggestion visible when scrolling.
- Built entirely on classic table selections and array/selection-based list boxes rather than ORDA.

## Featured Technology
- `QUERY`, `QUERY SELECTION`, `Split string`
- Selection-based list box, `LISTBOX SELECT ROW`, `OBJECT SET SCROLL POSITION`
- `HIGHLIGHT TEXT`, `Selected record number`, `LOAD RECORD`

## Best Practices Highlighted
1. Cap the dropdown's visible row count and let it shrink for fewer suggestions to keep the UI compact.
2. Track first-vs-subsequent arrow-key presses (`Form.searched`) to avoid skipping the first suggestion.
3. Keep the cursor and scroll position synchronized with the currently highlighted suggestion for a polished feel.

## Context / Positioning
Part of 4D's 2019 series of practical UI-recipe tech notes, this document captures a request commonly needed in business applications (autocomplete search), built at a time when 4D was transitioning many features toward ORDA/object notation but still supporting classic selection-based forms extensively.

## Historical Commentary
**Status:** Partially superseded

The dropdown-as-you-type UX pattern itself remains completely valid and common in 4D applications today. However, the underlying implementation — classic `QUERY`/`QUERY SELECTION` against table selections and a selection-based (rather than collection/entity-based) list box — reflects 4D's pre-ORDA programming style. A developer building this today would more likely use ORDA entity selections (`.query()`) and a collection- or entity-selection-based list box, consistent with 4D's post-v16/17 shift toward object notation; the classic technique shown here still works but is not the modern idiomatic approach.
