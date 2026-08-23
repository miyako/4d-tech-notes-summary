# Tech Note: Creating a 6.0-style Pop-up in 6.7 using Layered Objects

- **Asset ID:** 15347
- **Tech Note #:** 01-28
- **Published:** June 30, 2001
- **Product / Version:** 4D 6.5
- **Platform:** Mac & Win
- **Author:** Eric Saltzen
- **Page URL:** https://kb.4d.com/assetid=15347
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_26-30_(JUN)/01-28_Popups_6.0_in_6.7.hqx

## Overview

Eric Saltzen (4D, Inc. Technical Support) shows how to restore 4D v6.0's Pop-up menu/Drop-down list behavior — where the object method fired only on an actual user selection — after v6.5 changed it to more closely follow Macintosh interface guidelines and fire the object method even when the user merely browsed and dismissed the menu without changing its value.

## Key Points

- In v6.0, a Pop-up menu/Drop-down list's object method ran only when the user made a selection; starting in v6.5, it fires (`On Clicked`) even if the user just activates and dismisses the menu, re-returning the previously selected value — this note shows how to detect a "real" selection versus mere browsing.
- Technique: place a placeholder value (e.g., "Please make a choice...") as the first item of the associated choice list, and always reset the control back to that placeholder after processing a real selection, so any future `On Clicked` event landing on the placeholder can be treated as "no new selection."
- A second, display-only text object (`displayValue`) is layered directly on top of the Pop-up menu/Drop-down list to visually show the true current value while hiding the underlying placeholder text.
- The `myPopDropList` object method's `On Load` handler uses `PLATFORM PROPERTIES` to detect Windows and adjust the overlay's position/colors, loads choices via `LIST TO ARRAY`, and uses `Find in array` against the associated field to restore the correct displayed value (or the placeholder if none matches).
- The `displayValue` object method calls `POST CLICK(popTargetX;popTargetY)` on `On Clicked` to forward clicks through to the underlying Pop-up/Drop-down control, preserving the illusion of a single combined interface object.
- `On Getting Focus`/`On Losing Focus` handlers (Windows only) use `SET RGB COLORS` to mimic native Drop-down list focus highlighting (white-on-blue when focused).
- Notes that easier alternatives exist for related but different goals: the "Mac OS 7" Platform Interface property preserves the old visual appearance exactly, and the `Pop up menu` command is better suited for context/action menus not tied to a specific form control.

## Featured Technology

- Layered form objects (overlaying a display-only object on a Pop-up menu/Drop-down list)
- PLATFORM PROPERTIES command
- POST CLICK command to forward clicks between layered objects
- LIST TO ARRAY / Find in array for placeholder-based selection detection
- On Load / On Clicked / On Getting Focus / On Losing Focus form events
- SET RGB COLORS for Windows-style focus highlighting

## Historical Commentary

**Status:** Obsolete

This note solves a narrow, version-specific compatibility problem — restoring 4D v6.0's Pop-up/Drop-down list firing behavior after it changed in v6.5 — that has no bearing on any current 4D version; the underlying behavior difference between v6.0 and v6.5+ is not something modern developers ever encounter. The general technique demonstrated, however — layering form objects and using POST CLICK to forward interaction between them to build composite custom controls — remains a legitimate and still-functional 4D pattern, even though it is now rarely needed given richer built-in list box and control options.

**References to newer/updated information:**
- The specific 4D v6.0-vs-6.5+ Pop-up/Drop-down list firing-behavior difference this note addresses is irrelevant to all current 4D versions
- The general technique of layering form objects and using POST CLICK to forward clicks remains valid in current 4D versions for building custom composite controls
- Modern 4D UI development (list boxes, plug-ins, or web-based front ends) rarely relies on hand-layered classic-language pop-up/drop-down workarounds
