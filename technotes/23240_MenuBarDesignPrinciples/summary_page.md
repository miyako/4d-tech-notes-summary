# Tech Note 02-23: Basic Principles of Menu Bar Design in 4D

- **Asset ID:** 23240
- **Tech Note #:** 02-23
- **Published:** May 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Gary Brocks
- **Page URL:** https://kb.4d.com/assetid=23240
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_20-24_(MAY)/02-23_Menu_Bar_Design.hqx

## Overview

Gary Brocks (4D Evangelist, 4D, Inc.) presents a "4D RAD" menu-bar design pattern — four menu bars (splash, list, detail, plus one empty) combined with MENU BAR, Associated Menu Bar, and Active Menu Bar — that reduces menu-bar switching throughout an application's lifetime to a single line of code, while honoring Apple's Human Interface Guidelines of consistent, grayed-out (not disappearing) menu items.

## Key Points

- Identifies three basic application "areas" — splash screen, list of records, detail view of a single record — each of which logically enables a different subset of menu operations (e.g., querying/sorting only makes sense at the list view, not the detail view).
- Quantifies the scaling problem of manual enable/disable code: a 6-menu, 36-item menu bar requires managing 108 individual enable/disable operations across just three application areas.
- Distinguishes the "current" menu bar (set with the `MENU BAR` command, only one displayed at a time) from menu bar "activation," which is controlled per-form by the Active Menu Bar checkbox and the Associated Menu Bar combo box; an associated menu bar's menus are automatically appended to the current bar and auto-activated by the form.
- Documents seven concrete test scenarios covering every combination of current menu bar, associated menu bar, and the Active Menu Bar checkbox, to precisely establish which menu items end up active and displayed in each case.
- The "4D RAD" system: create four menu bars (1=splash, 3=list, 4=detail, all carrying the same menus with different items enabled/disabled) plus 2=an intentionally empty menu bar; assign menu bar 2 as every form's Associated Menu Bar and turn Active Menu Bar on everywhere, so any bar set as current via `MENU BAR(n)` becomes activated without appending extra menus.
- Sample code shows the entire transition logic reduced to one line per context change: `MENU BAR(3)` before displaying a list with `MODIFY SELECTION`, and `MENU BAR(4)` in a detail form's `On Load` event; returning to the list uses `MENU BAR(3)` in the `On Close Detail` event.
- Explains 4D's automatic "connected menu" behavior (the File menu is auto-connected to every new menu bar, and Edit is auto-placed on the current bar) which is why the "empty" menu bar 2 still behaves as functionally empty for the purposes of this system, and notes the pattern extends naturally to per-user-role menu sets via 4D's password system.

## Featured Technology

- MENU BAR command (current menu bar switching)
- Associated Menu Bar form property
- Active Menu Bar form property checkbox
- Menu bar activation vs. display distinction
- Empty menu bar pattern for uniform activation
- 4D RAD menu system architecture (splash/list/detail menu bars)

## Historical Commentary

**Status:** Partially superseded

Gary Brocks presents a rapid-application-development menu system architecture for classic 4D: four menu bars (splash screen, list view, detail view, plus one deliberately empty menu bar) combined with the MENU BAR command and the Associated/Active Menu Bar form properties, so that switching which menu items are enabled requires changing exactly one line of code rather than manually enabling/disabling dozens of menu items as users move between application contexts. This is a sound, well-reasoned application of Apple's Human Interface Guidelines (consistency, grayed-out unavailable items) to 4D's specific menu-bar/form-association mechanics of that era. Classic 4D menu bars and this activation model still exist in current 4D, so the mechanics remain technically valid, but most modern 4D development has moved toward web-based (Qodly) or object/list-form-driven UIs where this classic desktop menu-bar RAD pattern is less central, making it now primarily relevant to classic 4D desktop client maintenance.

References to newer/updated information:
- The MENU BAR command and Associated/Active Menu Bar form properties described here remain part of current 4D for classic desktop-client menu bars
- Much modern 4D development (web-based Qodly apps, list-form/object-driven UIs) relies less on classic menu-bar-per-context designs, reducing the centrality of this specific RAD menu pattern
