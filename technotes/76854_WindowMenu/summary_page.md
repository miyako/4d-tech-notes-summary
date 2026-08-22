# Tech Note 13-09: How to Build a Window Menu

**Author:** Tim Penner, Technical Services Engineer, 4D Inc.
**Published:** July 22, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76854
**Download:** https://kb.4d.com/DLTN/TN/2013/13-09_BuildWindowMenu.zip

## Proposition
This Tech Note explains how to implement a classic "Window" menu — a dynamic menu that lists all open windows and lets users switch between them, ticking the active one — using a set of provided example 4D methods (WM_OnStartup, WM_HandleClick, WM_SetMenuBar, WM_UntickWindows, etc.).

## Key Points
- Defines what a Window menu is and why users expect one for switching between open windows.
- Provides a full set of example methods (WM_DeleteMenuItem, WM_FormMethod, WM_GetItemPosition, WM_HandleClick, WM_OnStartup, WM_Reset, WM_SetMenuBar, WM_SetWindowTitle, WM_UntickWindows).
- Describes dynamically building/updating menu bar items as windows open, close, or come to the front.
- Covers ticking the menu item corresponding to the currently active window.
- Includes an example database and step-by-step installation instructions for reuse in other projects.

## Featured Technology
- Window menu (dynamic menu bar item)
- MENU BAR command family
- Custom menus
- Window management methods (WM_*)

## Best Practices Highlighted
1. Centralize window-menu bookkeeping in dedicated WM_ prefixed methods for maintainability.
2. Reset/rebuild the menu on relevant window events rather than assuming state.

## Context/Positioning
Published for 4D v13.3, at a time when 4D applications were still built as classic multi-window desktop apps with hand-rolled native-style menu bars, a common request from "savvy" desktop users.

## Historical Commentary
**Status:** Still Relevant

The technique of maintaining a dynamic Window menu via classic 4D language methods and MENU BAR commands still works today in Design Mode/Project Mode desktop applications, since 4D remains backward compatible with this classic UI programming style. Its relevance has waned somewhat as user expectations shifted toward tabbed or single-window applications and as document-based desktop metaphors became less central, but for classic-style multi-window 4D desktop apps the approach remains valid with no vendor-provided modern replacement.
