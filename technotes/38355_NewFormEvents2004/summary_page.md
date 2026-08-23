# Tech Note: New Form Events in 4D 2004

- **Asset ID:** 38355
- **Tech Note #:** 05-27
- **Published:** July 31, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=38355
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_25-27_(JUL)/05-27_New_Form_Events.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D, Inc.) documents the form events 4D 2004 added for 3D buttons and picture buttons — On Mouse Enter, On Mouse Move, On Mouse Leave, On Long Click, and On Arrow Click — using an interactive US map dialog to demonstrate rollover highlighting, state/capital lookup, and pop-up menus without the manual polling code these effects previously required.

## Key Points

- On Mouse Enter/On Mouse Leave fire once each as the cursor enters/exits an object's area — used in Example 1 to toggle visibility of state/capital text fields via `SET VISIBLE`.
- On Mouse Move fires on every pixel of mouse movement within an object and is used together with a precomputed pixel-to-state mask (built by a Create_Mask method) to look up the state and capital under the cursor via `GET MOUSE` and array lookups.
- On Long Click, timed to the system's configured double-click interval, is distinguished from On Double Clicked: a single long click opens a new process (M_DisplayFlag) showing the state's flag, while a double-click opens a different process (M_DisplayState) with full state details.
- On Arrow Click fires when the user clicks the small arrow automatically added to a 3D button — no longer requiring a hand-drawn second picture-button object as in older 4D versions — and is used to display a `Pop up menu` of all states for direct navigation.
- Events are generated per-process for the frontmost window, except that floating windows in different processes can each receive events independently — superimposed objects only report the event for the frontmost object.
- Example forms use `New process` with `<>ProcessStack` to launch detail/flag display dialogs, and `BRING TO FRONT` to surface them.

## Featured Technology

- On Mouse Enter / On Mouse Move / On Mouse Leave form events
- On Long Click vs. On Double Clicked form events
- On Arrow Click event for 3D buttons
- 3D button and picture button objects
- Pixel-mask based hit-testing (GET MOUSE, pixel arrays)
- Pop up menu command

## Historical Commentary

**Status:** Historical interest only

This note documents a genuine usability improvement in 4D 2004 — built-in rollover and long-click events that eliminated hand-rolled polling code for hover/rollover effects. The specific subject matter, however, is tied to 3D buttons and picture buttons, a skeuomorphic control style that has fallen out of use in modern 4D form design, which favors flat, natively styled objects. The general form-event architecture these events belong to has continued to expand in later 4D versions (including Project Mode forms) and remains central to classic-language form programming, even though this particular button style is largely of historical interest today.

**References to newer/updated information:**
- 3D-style buttons are a legacy desktop GUI aesthetic no longer emphasized in modern 4D form design, which favors flat/native OS-styled controls
- 4D's form event model has continued to expand in later versions (and functions the same way in Project Mode forms), independent of this specific 3D-button-era addition
