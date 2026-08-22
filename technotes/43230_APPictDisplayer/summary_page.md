# Tech Note 06-22: The AP PICT Displayer Plug-in Area

**Author:** Jean-Yves Fock-Hoon, Quality Assurance Manager, 4D Inc.
**Published:** June 2, 2006 | **Product/Version:** 4D Pack v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43230
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_22-26_(JUN)/06-22_AP_Pict_Displayer.zip

## Overview
4D 2004 does not redraw its GUI while a form method is executing — a progress-bar picture might update, but a text variable counter next to it will appear frozen until the method finishes. This note demonstrates a workaround built on the "AP PICT displayer" plug-in area, part of the 4D Pack plug-in, and its companion `AP PICT UPDATER` command, which forces an immediate on-screen redraw of a picture even mid-method.

## Key Points
- **The problem:** 4D's normal event-driven redraw model means text/variable updates inside a loop are invisible to the user until the method ends.
- **The solution:** `AP PICT UPDATER` bypasses normal redraw timing, immediately painting a new picture into an "AP PICT displayer" area — enabling animation, progress bars, or status updates from inside a running method.
- **Setup rules/restrictions:** the plug-in area must be visible (not marked invisible), must have already been drawn once, and cannot be updated during the `On Load` form event; a common trick is preloading a 1-pixel placeholder picture to avoid an ugly initial resource image.
- **Demonstrated use cases:** an "Installation" slideshow simulating an installer, an "Initialization" dialog driven by the `On Timer` event with dynamically generated text baked into pictures via 4D Chart offscreen areas, an embedded progress bar in a real record input form (no extra process needed), ten simultaneous per-process progress dialogs, and a fun "4D Derby" horse-race animation.
- **Picture composition tricks:** uses 4D's picture operators — `/` to stack pictures vertically (e.g., title above progress bar), `+` to overlay/append pictures (e.g., horse onto track), and `*+` to scale a picture's width/height (e.g., building a partial-fill progress bar or resizing to fit the plug-in area).
- **4D Chart integration:** since text objects also can't redraw mid-method, the note shows compositing live text onto pictures using `CT New offscreen area`, `CT Draw text`, and `CT Area to picture`, including a "blinking text" effect via toggling a space character.
- **Design rationale:** this single-process picture-swapping approach avoids the overhead, synchronization issues, and redraw side effects of spawning a dedicated "progress" process.

## Featured Technology
- 4D Pack plug-in ("AP PICT displayer" plug-in area, `AP PICT UPDATER` command)
- 4D Chart offscreen area commands for compositing text into pictures
- 4D's built-in picture arithmetic operators (`+`, `/`, `*+`)
- Picture library / resource-based picture loading

## Historical Context
This is a 2006-era, pre-multithreading UI engineering technique tied entirely to the long-discontinued 4D Pack plug-in bundle and its proprietary plug-in area type. The underlying problem — a form method blocking normal GUI redraw — has since been addressed through evolutions in 4D's process model and native progress-bar/UI update support, making this specific workaround obsolete. The picture-compositing tricks (using `+`, `/`, `*+` operators and 4D Chart offscreen rendering) are a clever period-appropriate hack rather than a technique any current 4D developer would reach for.

## Historical Commentary
**Status:** Obsolete

The specific plug-in ("AP PICT displayer" from 4D Pack) no longer exists in any supported 4D product, and the redraw limitation it worked around has since been resolved through improvements in 4D's process and event handling. The conceptual pattern — compositing images to represent live progress without a second process — remains a mildly interesting historical example of pre-modern UI engineering in 4D, but has no direct practical application today.
