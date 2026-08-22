# Tech Note 11-03: Menus in 4D v12

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** February 10, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76261
**Download:** https://kb.4d.com/DLTN/TN/2011/11-03_Menus_in_4D_v12.zip

## Proposition
This note surveys the full range of ways to build and deploy menus in 4D v12, covering two menu-creation paradigms and how each connects to the rest of an application. It explains creating menus via the visual Tool Box interface as well as entirely programmatically, including building hierarchical (nested) menus and specializing individual menu items (icons, shortcuts, states). It then covers how to assign a completed menu bar to an application — by process or by form — and finishes with instructions for building fully dynamic pop-up menus at runtime. A sample database demonstrates every technique discussed, giving developers a single reference for the whole menu-building lifecycle in 4D v12.

## Key Points
- Explains the two menu paradigms in 4D v12 and when each applies.
- Covers menu creation via the Tool Box interface (visual editor).
- Covers fully programmatic menu creation, including hierarchical (nested submenu) structures.
- Explains specializing menu items (e.g., custom behavior/appearance per item).
- Covers assigning menu bars to specific processes and to specific forms.
- Covers building dynamic pop-up (contextual) menus at runtime.
- Includes a full sample database illustrating all techniques.

## Featured Technology
- 4D Tool Box menu editor
- Programmatic menu bar creation and hierarchical/specialized menu items
- Menu assignment by process and by form; dynamic pop-up menus

## Best Practices Highlighted
- Choose Tool Box-based menu creation for static menus and programmatic creation for menus that must adapt at runtime
- Assign menu bars per form or per process deliberately, matching the application's UI architecture

## Context / Positioning
Published for 4D v12.1 in 2011 as a consolidated reference on menu construction, an area with several overlapping techniques that developers commonly found confusing without a unified guide.

## Historical Commentary
**Status:** Still Relevant

4D's classic menu bar editor and programmatic menu commands described here are still fully supported and remain the standard way to build native application menus in 4D today, so this note is still directly usable. The core menu architecture (Tool Box editor, process/form assignment, dynamic pop-ups) has not been replaced by any newer paradigm, making it one of the more durable UI-related notes from this era.
