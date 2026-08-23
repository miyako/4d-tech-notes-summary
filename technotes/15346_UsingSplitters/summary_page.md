# Tech Note: Using Splitters

- **Asset ID:** 15346
- **Tech Note #:** 01-27
- **Published:** June 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Gilles Mellot
- **Page URL:** https://kb.4d.com/assetid=15346
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_26-30_(JUN)/01-27_Using_Splitters.hqx

## Overview

Gilles Mellot (4D S.A.) sets out to popularize the Splitter object (introduced in 4D v6.5), which he notes remains underused because developers aren't aware of its full range of capabilities, covering everything from basic resize/move interactions with neighboring form objects to advanced programmatic animation and a drag-out-to-floating-palette technique.

## Key Points

- A splitter divides a form area into regions (area 1/area 2 for a single splitter); dragging it affects only the neighboring objects, based on each object's individual "Move horizontally/vertically" and "Grow horizontally/vertically" resize properties — walked through via a progression of examples, Test_1 through Test_8, covering fixed, growing, and moving object combinations on each side, including cases needing a second splitter.
- A splitter's position is bound to a longint variable that updates live as the user drags it, and — conversely — can be set programmatically to move the splitter under code control.
- Demonstrates an `On Timer`-driven "animation" (`SET TIMER` in `On Load`, splitter position updated each `On Timer` tick: `Splitter_V:=Splitter_V-4`, `Splitter_H:=Splitter_H+1`) that shrinks and slides pictures, interruptible by holding the Shift key.
- A more advanced example lets users drag an "Anchor" handle for a group of splitter-managed array columns outside the window to spawn a separate floating "Palette" process, created via `New process`, that mirrors and continues to independently control the same column widths.
- Cross-process synchronization between the main window and the detached palette uses `CALL PROCESS` combined with the `On Outside Call` form event, reading interprocess variables (`◊Message`, `◊Pos_1`, `◊Pos_2`) to relay splitter position changes.
- Notes that invisible objects are not moved or resized by a splitter's action; they must be explicitly repositioned with `MOVE OBJECT` once made visible again to match the splitter's current position.

## Featured Technology

- Splitter form objects (introduced in 4D v6.5)
- Move horizontally / grow horizontally object resize properties
- SET TIMER / On Timer event for programmatic splitter animation
- GET OBJECT RECT / MOVE OBJECT for reading and setting splitter position
- CALL PROCESS / On Outside Call for cross-process splitter synchronization (drag-to-palette)
- Longint variable binding to splitter position

## Historical Commentary

**Status:** Still relevant

Splitters remain a supported 4D form object today, and the fundamentals covered here — variable-bound splitter position, interaction with neighboring objects' move/grow properties, and reading/setting that position programmatically — are unchanged and still directly useful for building resizable classic-language forms. The more elaborate On Timer animation and cross-process drag-to-palette techniques are less commonly needed now that list boxes, group objects, and richer form APIs handle much of this territory, but nothing about splitters themselves has been deprecated.

**References to newer/updated information:**
- Splitter objects remain a supported 4D form object type in current versions, with the same variable-binding behavior described here
- Modern 4D form layout increasingly relies on list boxes, group objects, and object properties for adaptive resizing, reducing (but not eliminating) reliance on manual splitter-based layouts
- CALL PROCESS and On Outside Call remain valid current 4D mechanisms for inter-process communication, though newer patterns (e.g., worker processes, shared interprocess variables) are also commonly used today
