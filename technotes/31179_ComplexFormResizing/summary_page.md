# Tech Note: Complex Form Resizing

- **Asset ID:** 31179
- **Tech Note #:** 04-03
- **Published:** January 31, 2004
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel, 4D S.A.
- **Page URL:** https://kb.4d.com/assetid=31179
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_01-04_(JAN)/04-03_Complex_Form_Resizing.hqx

## Overview

Roland Lannuzel presents a language-based method for computing coordinated object placement and size when a 4D form is resized, going beyond 4D's basic default Grow/Move object behaviors, illustrated end-to-end with a resizable calculator form containing 17 buttons of varying sizes and margins.

## Key Points

- Explains why naive Grow settings fail: identical adjacent objects set to Grow will overlap on resize rather than moving apart, so each object needs both a resize ratio and a move ratio computed from the window's size delta.
- Establishes the design rule that resize/move ratios across all objects (and the spaces/margins between them) should sum to 100% of the window's width or height change, worked through examples with equal-size objects, unequal-size objects, and margins/inter-object spacing ("the perfect zoom").
- For the calculator example, breaks down concrete ratios per button (e.g. button 7: 20% resize / 4% move; button 8: 20% resize / 28% move; the wide "C" button: 44% resize ratio) derived from each object's position and width relative to the row.
- Each of the 17+ form objects is described by eight tracked values — initial X/Y, width, height, move-X%, grow-X%, move-Y%, grow-Y% — stored in parallel long integer/real arrays plus an object-name array, loaded from an `Elements` table via `SELECTION TO ARRAY`.
- The `On Load` form event initializes the arrays and places objects with `MOVE OBJECT`; the `On Resize` event computes `$DeltaX`/`$DeltaY` from `GET WINDOW RECT` against reference dimensions (`RefWinX`/`RefWinY`) and reapplies `MOVE OBJECT` to every object using its stored percentages, then recalculates font sizes for the display and buttons proportionally via `GET OBJECT RECT` and `FONT SIZE`.
- Window resizing itself is driven by an invisible object (a repurposed thermometer) at the bottom-right corner that continuously calls a `ResizeWindow` method while the mouse is held down, enforcing the window's aspect ratio and manually resizing the window (which then fires `On Resize`).
- Suggests broader applications: building object "skins," or showing/hiding form objects based on user login, using the same array-driven approach.

## Featured Technology

- On Load and On Resize form events
- Per-object move/resize percentage ratios stored in arrays
- MOVE OBJECT command for programmatic placement
- GET WINDOW RECT / GET OBJECT RECT for delta computation
- ARRAY LONGINT / ARRAY REAL and SELECTION TO ARRAY for loading layout data
- Invisible thermometer object hijacked for live window-resize dragging

## Historical Commentary

**Status:** Partially superseded

This note by Roland Lannuzel of 4D S.A. presents a language-based technique, illustrated with a resizable calculator form, for proportionally resizing and repositioning multiple form objects together during a window resize — going beyond 4D's basic per-object Grow/Move behaviors by computing per-object move and grow percentages stored in parallel arrays and applying them on the On Resize form event via MOVE OBJECT. The core problem of coordinated, proportional object layout on resize is still relevant, but 4D's form object model has since gained more built-in anchoring and responsive-layout capabilities, reducing how often developers need to hand-roll this exact array-driven percentage math today; the technique remains a valid, understandable reference for cases requiring fully custom resize logic.

References to newer/updated information:
- Later 4D versions added more built-in form object anchoring/auto-resize options (percentage-based positioning in the Form editor), covering many cases that previously required fully custom On Resize code like this
- 4D's form and object model has continued to evolve, but the general On Load/On Resize event pattern and language-based MOVE OBJECT approach described here remains structurally valid in current 4D forms
