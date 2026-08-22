# Tech Note 21-20: Intro to 4D View Pro Offscreen Areas

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** November 15, 2021 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78816
**Download:** https://kb.4d.com/DLTN/TN/2021/21-20_VPOffscreenAreas.zip

## Proposition
4D View Pro offscreen areas let developers create, import, process, and export spreadsheet documents entirely in the background without a visible form area, useful for server-side or batch report generation.

## Key Points
- **Offscreen area purpose**: process 4D View Pro documents without any visible UI element, ideal for background/server report generation.
- **Class-based setup**: a class implementing `onEvent` handles VP lifecycle events, instantiated and passed to `VP Run offscreen area`.
- **Formula-based setup**: for non-class code, a project method wrapped in `Formula(...)` is assigned to the area object's onEvent property.
- **Key attributes**: area, onEvent, autoQuit (must be False for async import/export callbacks), timeout (default 60s), result, plus arbitrary custom properties.
- **Lifecycle events**: On VP Ready, On Load, On Unload, On End URL Loading, On URL Loading Error, On VP Range Changed, On Timer.
- **Document operations**: VP NEW DOCUMENT, VP IMPORT DOCUMENT (supports .4vp, .xlsx, .txt/.csv), and VP EXPORT DOCUMENT, with Excel import running asynchronously.
- **Returning results**: This.result set inside the onEvent handler (e.g., in On Unload) becomes the return value of VP Run offscreen area.

## Featured Technology
- 4D View Pro (VP) offscreen areas
- VP Run offscreen area
- VP NEW DOCUMENT / VP IMPORT DOCUMENT / VP EXPORT DOCUMENT
- Class-based and formula-based onEvent handlers

## Best Practices Highlighted
1. Set autoQuit to False whenever using asynchronous import/export callbacks so the area doesn't close prematurely.
2. Use the class-based approach for more complex offscreen workflows and the formula-based approach for simpler, non-class codebases.
3. Set an appropriate timeout (or 0 for none) when long-running imports/exports are expected, to avoid premature area closure.

## Context / Positioning
This note supports 4D's ongoing expansion of 4D View Pro (its modern, HTML/CSS-based spreadsheet component that replaced classic 4D View) into headless/automation scenarios, reflecting the broader industry expectation that reporting/spreadsheet features be scriptable for servers, not just desktop UIs.

## Historical Commentary
**Status:** Current

Fully current: 4D View Pro offscreen areas remain a standard, actively documented 4D feature with the same API surface (VP Run offscreen area, onEvent, autoQuit, VP NEW/IMPORT/EXPORT DOCUMENT) shown here. There is no successor feature — this technique is still exactly how developers do headless spreadsheet processing in 4D today. This note remains directly usable, current reference material rather than historical context.
