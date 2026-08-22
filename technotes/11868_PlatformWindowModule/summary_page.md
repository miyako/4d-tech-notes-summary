# Tech Note 95-21: A Platform Independent Window Management Module

**Author:** Jeff Browning
**Published:** April 1, 1996 | **Product/Version:** 4D v3.x (3.5) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11868
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_16-21_(APR)/96-21_Window_Module.exe

## Overview
This note documents a fully reusable procedure module that lets developers open and position windows consistently across Macintosh and Windows, at a time when 4D 3.5's OPEN WINDOW command behaved differently per platform (positioning relative to the screen on Mac, but to the application/MDI frame on Windows) and layouts often needed platform-specific scaling for differing monitor resolutions.

## Key Points
- Solves platform-dependent window positioning: supports center, upper/lower center, all four corners, stacked ("cascaded"), fill-screen, and offscreen positions, transparently adapted per platform.
- Handles all standard 4D window types: standard modal, 1-pixel modal, shadow border modal, movable modal, DA style, floating with/without scroll bar, and modeless variants (with size box, zoom box, or neither).
- Manages window resizing and loads the platform/look-appropriate scaled layout automatically, based on the current "look" (Automatic, Macintosh, Windows 3.1, Windows 95).
- Implements transparent cross-process window stacking/cascading — closed bottom-most stacked windows free their position for the next new stacked window, working across multiple 4D processes.
- Includes an interactive WinMod example database with a Test Windows dialog to exercise every position/type/size/title/look combination, which also generates a ready-to-paste line of 4D code.
- Core procedures: `Startup_WI` (initializes constants), `WI_OpenStd`/`WI_CloseStd` (open/close windows), a `WI_Layout` helper, and a small generic `ER_ErrorProc` error-reporting helper.

## Featured Technology
- OPEN WINDOW command and 4D 3.5 layout scaling
- Companion "Platform and Look Detection Module" (TN 96-20, also by Jeff Browning) — a required dependency
- ACI_PACK extension package (bundled with 4D/4D Server of that era)
- Interprocess variables and parameter indirection for a reusable procedure library

## Historical Context
This is a classic mid-1990s cross-platform engineering note, addressing Mac/Windows UI inconsistencies (window positioning semantics, resolution-driven layout scaling) that predate any of 4D's modern form/window architecture. The module's dependence on a separate platform-detection tech note and the ACI_PACK extension reflects the procedure-library and plugin conventions of that era. The underlying platform inconsistencies it works around have long since been resolved or become irrelevant as Mac/Windows display and windowing conventions converged and 4D's own window/form handling evolved; the specific code and dependencies here are of historical interest only, though the general discipline of encapsulating platform quirks behind one reusable interface remains a sound engineering principle.
