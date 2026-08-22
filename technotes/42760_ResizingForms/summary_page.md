# Tech Note 06-16: Resizing Forms

**Author:** Jean-Yves Fock-Hoon, Technical Support Engineer, 4D Inc.
**Published:** April 21, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42760
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_14-17_(APR)/06-16_Resizing_Forms.zip

## Overview
This note explains a breaking change to window/form resizing behavior introduced in 4D 2004: code that worked fine in 4D 6.8 using SET WINDOW RECT to resize both a window and its contents together no longer works, because 4D 2004 split that behavior into two distinct commands and added a new object "pusher" system.

## Key Points
- **The break:** in 4D 6.8, SET WINDOW RECT resized both the window frame and its contents; in 4D 2004, SET WINDOW RECT only changes the window's outer bounds and no longer resizes contents.
- **The fix:** a new RESIZE FORM WINDOW command reproduces the old "drag the corner" behavior (resizing/moving objects per their form properties); migrating 6.8-era code requires computing a size delta via GET WINDOW RECT, applying it with RESIZE FORM WINDOW, then repositioning with SET WINDOW RECT.
- **Fine-grained resizing control:** SET FORM HORIZONTAL RESIZING / SET FORM VERTICAL RESIZING let code programmatically enable, disable, or bound (min/max) a form's resizability, overriding the form's own static settings.
- **Object properties matter:** each object's Move/Grow settings, combined with the form's Automatic Size vs. fixed size setting and min/max width/height, jointly determine whether a resize leaves the interface usable or breaks it (objects can slide off-screen or overlap).
- **Critical warning:** never leave a form's min/max width/height at the 0–32000 defaults if the form is resizable — always define sensible real bounds.
- **Design-time aid:** the form editor's "Display Limits" contextual-menu option visualizes a form's real displayable area relative to the window's current size, helping catch these issues before runtime.
- **Seven worked examples:** the note demonstrates fixed-size dialogs revealing off-screen objects, resizable dialogs with growing scrollable areas, programmatic min/max width overrides, and objects becoming unusable when resizing rules are misconfigured.

## Featured Technology
- SET WINDOW RECT / GET WINDOW RECT (window boundary manipulation)
- RESIZE FORM WINDOW (drag-corner-style resize simulation)
- SET FORM HORIZONTAL RESIZING / SET FORM VERTICAL RESIZING
- Form object Move/Grow properties and the 4D 2004 "pusher" system
- Form editor "Display Limits" visualization

## Historical Context
Published in 2006 for 4D v2004, this note documents classic Design Mode form and window behavior from well before 4D's SQL engine (2007), Project Mode (2018), or ORDA. It's essentially a migration guide for a breaking API change between 4D 6.8 and 4D 2004's form-resizing commands.

## Historical Commentary
**Status:** Superseded

The specific migration problem this note solves (porting 6.8-era SET WINDOW RECT code to 4D 2004) is long resolved and only relevant to databases still carrying two-decade-old legacy code. The broader concepts — resizable forms with Move/Grow object properties, min/max window bounds, and programmatic resizing control — remain part of classic 4D Design Mode forms, but this note's framing as a version-migration guide, and its exact command set, is tied to a specific historical transition rather than current 4D form/UI development, which increasingly also includes web-based and Qodly Studio-driven UI paradigms.
