# Tech Note: Assigning a Menu Bar

- **Asset ID:** 23224
- **Tech Note #:** 02-06
- **Published:** February 28, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri, 4D, Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=23224
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_05-09_(FEB)/02-06_Menu_Example.hqx

## Overview

Jamras Komoncharoensiri explains the mechanics of menu bar management in a single-process 4D application: the two ways to assign a menu bar (form-associated vs. process-loaded via MENU BAR), how 4D combines them, how system menus like Edit and Help become available, and how to add, insert, and delete menu items programmatically at runtime.

## Key Points

- A menu bar can be assigned directly to a form through Form Properties' General page "Associated Menu Bar" drop-down, combined with the "Active Menu Bar" checkbox; 4D automatically swaps in the correct menu bar when switching between forms (illustrated with Output form using menu bar #2 and Input form using menu bar #3).
- Alternatively, a menu bar can be loaded procedurally into the current process with the `MENU BAR` command, which persists as long as the process runs, but this only works if the form's Active Menu Bar option is already enabled -- a blank associated menu bar can be used to avoid unwanted duplicate items.
- A conditional example checks `Current user` to load menu bar #5 for "Administrator" or #3 otherwise via `MENU BAR(5)` / `MENU BAR(3)`.
- New processes need an explicit `MENU BAR` call to make the Edit menu accessible (since no default process menu bar is loaded for them, unlike the initial custom process which gets menu bar #1); the Help menu remains accessible to all processes regardless.
- A worked `New_Form_Process`/`mExample4c` example shows creating a new process with `New process` and calling `MENU BAR(3)` before displaying `OUTPUT FORM`/`INPUT FORM`/`ALL RECORDS`/`MODIFY SELECTION`.
- Menu items can be added at runtime with `APPEND MENU ITEM` (adds at end) or `INSERT MENU ITEM` (adds at a specific position), handled via the `On Menu Selected` form event and `Get menu item` to identify which item was chosen.
- A reusable `Delete_Menu_Item` project method searches every menu and item using `Count menus`/`Count menu items`/`Get menu item` to find and remove a named item with `DELETE MENU ITEM`; the note warns that inserting items shifts subsequent item numbers, which can break their associated methods if item numbers were hard-coded.

## Featured Technology

- Form Properties Associated Menu Bar setting
- MENU BAR command
- APPEND MENU ITEM / INSERT MENU ITEM / DELETE MENU ITEM
- Get menu item / Count menus / Count menu items
- On Menu Selected form event
- New process for per-process menu bars

## Historical Commentary

**Status:** Still relevant

Jamras Komoncharoensiri's note explains how classic 4D single-process menu bars work: assigning an Associated Menu Bar to a form versus loading one procedurally into a process with MENU BAR, how 4D combines process and form-associated menu bars, and how to add, insert, and delete menu items programmatically with APPEND MENU ITEM/INSERT MENU ITEM/DELETE MENU ITEM. These native menu bar commands are still part of current 4D and the note's guidance on associated-versus-process menu bars remains broadly accurate, though its explicit single-process scope means it does not address today's more common multi-process/multi-window custom applications, and many modern 4D UIs supplement or replace native menu bars with web-based or ribbon-style navigation.

References to newer/updated information:
- 4D's native menu bar commands (MENU BAR, APPEND/INSERT/DELETE MENU ITEM) remain part of the current product largely unchanged from this description
- Many modern 4D applications supplement or replace native OS menu bars with web-based or custom on-screen navigation, and this note does not address multi-process menu bar coordination
