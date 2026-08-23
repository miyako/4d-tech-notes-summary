# Tech Note: Moving Objects

- **Asset ID:** 23220
- **Tech Note #:** 02-1
- **Published:** January 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel, 4D Developer, 4D S.A.
- **Page URL:** https://kb.4d.com/assetid=23220
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_01-04_(JAN)/02-01_Moving_Objects.hqx

## Overview

Roland Lannuzel demonstrates the MOVE OBJECT and GET OBJECT RECT commands together with the On Load, On Timer, and On Resize form events, using an animated analog clock -- whose window randomly relocates and resizes every ten seconds -- as the primary worked example, plus a simpler line-repositioning demo.

## Key Points

- MOVE OBJECT works on both static objects (text, pictures, circles, lines) and dynamic objects (fields, variables, buttons), using relative or absolute coordinates, and can alter proportions via horizontal, vertical, or combined homotheties.
- A key conceptual point: every object's coordinates are those of its smallest bounding rectangle, so to invert a line's slope you must swap the rectangle's x1/x2 (or y1/y2) coordinates rather than manipulating the line's endpoints directly.
- `On Load` calls `SET TIMER(60)` to arm a one-second timer and `DrawClockSpots` to place the twelve dial dots; `On Timer` checks `If (Current time%10=0)` and, every ten seconds, randomizes the clock window's position/size and calls `SET WINDOW RECT` to move/resize it.
- Calling `SET WINDOW RECT` triggers the `On Resize` event, which recalculates and redraws the twelve dial dots via `DrawClockSpots` since the object's Sizing options are set to "Grow" to track the new window size.
- The appendix method `DrawAnalogClock` uses `GET OBJECT RECT` to read the dial's bounding rectangle, computes the center and max radius, then uses `Sine`/`Cosine` on the current hour/minute/second (each scaled by 5/6-degree increments) to reposition the `HoursPin`, `MinutsPin`, and `SecondsPin` hand objects via `MOVE OBJECT`.
- `DrawClockSpots` similarly computes twelve evenly spaced angles (`($i-1)/12*2*Pi`) around the dial center to reposition twelve small 8x8-pixel "Spot" objects.
- A secondary demo shows fixed-coordinate line movement via buttons ("Move Line1 to 20-20-120-120", etc.) and a Reset button, illustrating the simpler, non-animated use of MOVE OBJECT.

## Featured Technology

- MOVE OBJECT command
- GET OBJECT RECT command
- On Timer / On Load / On Resize form events
- SET TIMER / SET WINDOW RECT
- Sine/Cosine trigonometry for clock-hand rotation
- REDRAW WINDOW

## Historical Commentary

**Status:** Still relevant

Roland Lannuzel's note teaches how to reposition and reshape both static and dynamic 4D form objects using MOVE OBJECT and GET OBJECT RECT, driven by the On Load, On Timer, and On Resize form events, using an animated analog clock whose window randomly moves and resizes every ten seconds as the demonstration vehicle. MOVE OBJECT, GET OBJECT RECT, and the On Timer/On Load/On Resize events remain part of the current 4D language and this technique is still directly usable for classic form-based object animation, though today's 4D developers building rich, animated, or web-facing interfaces are just as likely to reach for CSS/JavaScript-based Qodly/web forms, which offer more modern and flexible animation and layout tools than manipulating object rectangles by hand.

References to newer/updated information:
- MOVE OBJECT, GET OBJECT RECT, and the On Timer/On Load/On Resize events remain valid, supported 4D language features today
- Modern 4D UI work increasingly happens in web-based Qodly/form contexts where CSS/JavaScript animation techniques are used instead of manually recalculating object rectangles, though the classic form technique shown here still works for traditional 4D forms
