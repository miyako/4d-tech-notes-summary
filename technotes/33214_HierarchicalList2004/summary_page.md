# Tech Note: Working with Hierarchical List in 2004

- **Asset ID:** 33214
- **Tech Note #:** 04-27
- **Published:** July 8, 2004
- **Product / Version:** 4D 2003.3
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=33214
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_26-30_(JUN)/04-27_HierarchicalList_2004.hqx

## Overview

Written by Jamras Komoncharoensiri, this note catalogs the set of enhancements 4D 2004 made to the Hierarchical List object and its associated commands. It walks through each updated command in turn: SET/GET LIST PROPERTIES gained multipleSelections (enabling Shift-click/Ctrl- or Cmd-click multi-selection) and editable parameters (controlling whether users can add/delete/sort choice-list values via a Modify button, requiring SAVE LIST to persist); SET/GET LIST ITEM PROPERTIES gained an itemRef|* parameter (referencing the last-selected item when multiple are selected) and a color parameter (an RGB longint, with -1 resetting to the original color); SET LIST ITEM, GET LIST ITEM, and List item parent all gained an itemRef|* or itemPos|* wildcard parameter referencing the current item; the older SELECT LIST ITEM BY REFERENCE/SELECT LIST ITEM commands were renamed to SELECT LIST ITEMS BY REFERENCE/SELECT LIST ITEMS BY POSITION (plural) and gained an array parameter enabling true multi-item selection by reference or position; and Selected list item was renamed Selected list items, similarly gaining array and '*' parameters to return either item positions or item references for all currently selected items. The note also documents that list items can now be made directly editable in place (via the Enterable form property, or forced with the new EDIT ITEM command), and that three new form events -- On selection change, On expand, and On collapse -- fire on mouse or keyboard-driven selection and sublist expand/collapse actions, referencing the bundled HList_Demo database for worked examples of each numbered feature.

## Key Points

- SET LIST PROPERTIES/GET LIST PROPERTIES gained multipleSelections (0=no/1=yes) and editable parameters; SAVE LIST must be called after changing the editable property for it to take effect.
- SET LIST ITEM PROPERTIES/GET LIST ITEM PROPERTIES gained an itemRef|* parameter (where * targets the last-selected item) and a color parameter, an RGB longint computed as (Red<<16)+(Green<<8)+Blue, with -1 resetting to the default color.
- SET LIST ITEM, GET LIST ITEM, and List item parent all gained a wildcard '*' option for their item-reference/position parameter to directly target the current selected item, reducing calls to Selected list item(s).
- Count list items gained a '*' parameter: omitted it returns only visible (expanded) items, while passing '*' returns the total item count regardless of expand/collapse state.
- SELECT LIST ITEM BY REFERENCE / SELECT LIST ITEM were renamed to the plural SELECT LIST ITEMS BY REFERENCE / SELECT LIST ITEMS BY POSITION and gained an array parameter to select multiple items by reference or position at once.
- Selected list item was renamed Selected list items and gained an array parameter (returning positions by default, or item references when '*' is passed) to support reading multi-item selections.
- Hierarchical List items can now be edited in place (click-to-highlight, then click-and-hold to enter edit mode) when the Enterable form property is set, or forced programmatically with the new EDIT ITEM command; three new events, On selection change, On expand, and On collapse, fire on the corresponding user interactions.

## Featured Technology

- SET LIST PROPERTIES / GET LIST PROPERTIES (new multipleSelections, editable parameters)
- SET LIST ITEM PROPERTIES / GET LIST ITEM PROPERTIES (new itemRef|* and color parameters)
- SET LIST ITEM / GET LIST ITEM / List item parent (new itemRef|* wildcard parameter)
- SELECT LIST ITEMS BY REFERENCE / SELECT LIST ITEMS BY POSITION (renamed, multi-selection array parameter)
- New On selection change / On expand / On collapse form events

## Historical Commentary

**Status:** Partially Superseded

This note documents a meaningful round of 4D 2004 usability upgrades to the Hierarchical List object -- native multi-selection, per-item coloring, in-place editing, and new expand/collapse/selection-change events -- that made building tree-style UI significantly more capable than in prior 4D versions. Most of the specific commands and constants described (SET/GET LIST PROPERTIES, SELECT LIST ITEMS BY REFERENCE/POSITION, the On expand/On collapse/On selection change events) remain part of the current 4D classic language and function largely as documented, though 4D's List Box object and, in Project mode, other modern hierarchical/tree form controls now offer overlapping or more capable alternatives for many tree-display use cases that a developer today might reach for instead of the plain Hierarchical List object.

**References to newer/updated information:**
- SET/GET LIST PROPERTIES, SET/GET LIST ITEM PROPERTIES, SELECT LIST ITEMS BY REFERENCE/POSITION, and the On expand/On collapse/On selection change events remain part of the current 4D language, largely unchanged from what this note describes
- 4D's List Box form object and other modern tree/hierarchical UI controls now provide additional, often more capable, alternatives to the plain Hierarchical List object for many use cases
- EDIT ITEM remains available for programmatically forcing a Hierarchical List item into edit mode regardless of its Enterable property
