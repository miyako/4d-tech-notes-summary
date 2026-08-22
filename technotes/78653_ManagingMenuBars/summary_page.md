# Tech Note 21-03: Managing Menu Bars Across Forms and Processes

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** February 22, 2021 | **Product/Version:** 4D v18 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78653
**Download:** https://kb.4d.com/DLTN/TN/2021/21-03_ManagingMenuBars.zip

## Proposition
Menu bar item states (enabled/disabled) often need to differ between forms — a mail client's Compose vs. Inbox screens, for example. This note shows how to use independent menu bar references to keep each form's menu state isolated and correctly restored on navigation.

## Key Points
- **Three assignment methods compared:** Toolbox menu bar via form property, `SET MENU BAR` by number, and `Create menu` for an independent runtime reference — only the last avoids shared global state across forms/processes.
- **Per-form menu bar references:** call `Create menu(n)` and `SET MENU BAR` in each form's `On Load`, so state changes (`DISABLE MENU ITEM`, etc.) are remembered independently per reference.
- **Restoring state on return:** re-assign the previous form's reference with `SET MENU BAR` after a `DIALOG` or `CLOSE WINDOW` call to restore its menu state when navigating back.
- **Memory management:** `RELEASE MENU` must be called in `On Unload` for any menu created with `Create menu`.
- **Keeping UI in sync:** buttons that mirror menu actions must be manually kept in sync (`OBJECT SET ENABLED`) alongside menu item state changes.
- **Generic handlers via parameters:** `SET MENU ITEM PARAMETER`/`Get selected menu item parameter` let one shared method branch its behavior per calling form/demo.
- **Cross-process communication:** `SET/GET MENU ITEM PROPERTY` lets one process flag state (e.g. "record saved") on another process's referenced menu bar without manual reassignment, since each process already owns its own bar.
- **Active Menu Bar form property** is automatically enabled on Project mode forms, allowing Toolbox and `SET MENU BAR`-assigned bars to combine.

## Featured Technology
- `SET MENU BAR`, `Create menu`, `RELEASE MENU`
- `DISABLE MENU ITEM` / `ENABLE MENU ITEM`
- `SET MENU ITEM PARAMETER` / `GET MENU ITEM PROPERTY` / `SET MENU ITEM PROPERTY`
- `New process`, `Open form window`, `DIALOG`

## Best Practices Highlighted
1. Use `Create menu` references (not raw Toolbox/number-based assignment) whenever different forms need independent menu states.
2. Always pair menu bar creation with `RELEASE MENU` in `On Unload` to avoid memory leaks.
3. Keep any on-screen buttons mirroring menu actions manually synchronized with the corresponding menu item state.
4. Use menu item parameters/properties to build reusable, generic menu-handling methods across multiple forms.

## Context / Positioning
This is a classic desktop-UI craftsmanship tech note, addressing a longstanding pain point in building multi-form 4D desktop applications with process-aware menu bars — a topic orthogonal to (and unaffected by) 4D's parallel ORDA/web/Project-mode evolution, since menu bars are specific to the classic desktop client UI.

## Historical Commentary
**Status:** Still relevant

Every command used here (`SET MENU BAR`, `Create menu`, `RELEASE MENU`, menu item parameters/properties) remains current and unchanged in modern 4D versions — there is no successor mechanism, since classic desktop menu bars are still managed exactly this way. The one dated detail is contextual rather than technical: the note notes that "Active Menu Bar" is automatically enabled on Project mode forms, reflecting Project mode's rise to become the default project format, which remains true today. This technique is directly applicable to any current 4D desktop (4D/4D Server + 4D Remote client) application with multi-form menu requirements.
