# Tech Note: Disabling Tab Controls

- **Asset ID:** 12155
- **Tech Note #:** 01-03
- **Published:** January 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Yves Casquel
- **Page URL:** https://kb.4d.com/assetid=12155
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_01-05_(JAN)/01-03_Disable_Tab_Controls.hqx

## Overview

Yves Casquel of 4D S.A. Technical Support demonstrates two complementary techniques for controlling access to pages reached via a form's tab control — an object driven either by an automatic 'go to page' action or a custom method — using a hierarchical list assigned to the tab control: disabling a tab item so it stays visible but inert, and deleting a tab item so the page becomes entirely unreachable.

## Key Points

- The tab control is built from a hierarchical list (via New list / APPEND TO LIST) rather than a static list of values, so that individual tabs can be toggled at runtime.
- SET LIST ITEM PROPERTIES / GET LIST ITEM PROPERTIES toggle a tab item's Active flag; the Appointments tab starts disabled and is re-enabled only after the user enters a code in a Request("Enter code to access appointments...") dialog.
- REDRAW LIST refreshes the tab control's on-screen appearance after its underlying hierarchical list is modified.
- A separate mechanism — checking radio buttons for 'Undetermined Duration' or 'Limited Duration' — appends or removes the Contracts tab entirely via CLEAR LIST, Load list("Tab"), SELECT LIST ITEM, and DELETE LIST ITEM, contrasting deletion with mere disabling.
- GOTO PAGE(Current form page) forces a page reload after list changes, with a guard that redirects off the Appointments page if it has just been disabled while the user was on it.
- Navigation logic can be driven either by an automatic 'go to page' action on the tab control, or by an object/form method reading Selected list item(◊Tab_Control).

## Featured Technology

- Tab control objects driven by hierarchical lists
- GOTO PAGE command
- SET LIST ITEM PROPERTIES / GET LIST ITEM PROPERTIES
- APPEND TO LIST / DELETE LIST ITEM / CLEAR LIST
- Selected list item command
- REDRAW LIST

## Historical Commentary

**Status:** Still Relevant

Written by Yves Casquel of 4D S.A. Technical Support, this note builds a small sample database that shows two complementary ways to restrict form-tab navigation: disabling a tab list item via SET LIST ITEM PROPERTIES so it is visible but inert, or removing it outright with DELETE LIST ITEM/CLEAR LIST so the page becomes unreachable, all driven from a hierarchical list assigned to the tab control object. Tab controls and hierarchical lists remain a completely standard, unchanged part of 4D form design today, so the core enable/disable and list-manipulation commands shown here still work as-is in both binary and Project Mode forms, though many modern UIs increasingly favor object-array-bound tab bars or explicit visibility properties over hierarchical-list-driven tabs.

**References to newer/updated information:**
- SET LIST ITEM PROPERTIES, GET LIST ITEM PROPERTIES, and GOTO PAGE remain part of the current 4D language with unchanged behavior
- Hierarchical lists and tab-control objects are still standard in 4D form design, though newer form/object-array-based UI patterns offer alternatives
