# Tech Note 02-17: 4D Banner

- **Asset ID:** 23250
- **Tech Note #:** 02-17
- **Published:** April 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri
- **Page URL:** https://kb.4d.com/assetid=23250
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_15-19_(APR)/02-17_4D_Banner.hqx

## Overview

Jamras Komoncharoensiri (4D Inc. Technical Support) builds "4D Banner," a scrolling announcement marquee that broadcasts administrator messages to all connected 4D Client users, animated with MOVE OBJECT and sized using a clever 4D Chart offscreen-area text-measurement trick.

## Key Points

- The Banner form has three objects: `vMovingText` (a non-enterable text variable, initially 1 pixel wide), `BackGround` (a rectangle defining the visible scroll boundary), and a hidden button `bHidden` to suppress 4D's default button on the form.
- The Composer form's Send/Save-and-Send buttons call `mLaunchBannerProcess`, which checks `Application type` to either open a local process directly (standalone apps) or broadcast via `EXECUTE ON CLIENT("@";"mOpenBannerLocal";$1)` to every connected 4D Client.
- `mOpenBannerLocal` checks for an existing `"4DBannerProcess"` via `Process number`; if none exists it creates one with `New process`, otherwise it updates the running process's message via `SET PROCESS VARIABLE`.
- `mSetTextBoundary` measures the pixel width a message needs by drawing it into a 4D Chart offscreen area (`CT New offscreen area`, `CT Draw text`, `CT SET TEXT ATTRIBUTES` for Arial 12pt Bold) and widening the text object by 5 points at a time via `CT SIZE` until `CT GET BOUNDARY` shows it no longer wraps to a second line — then applies that measured width to the real `vMovingText` object with `MOVE OBJECT`.
- The `On Load` form event captures `BackGround`'s coordinates with `GET OBJECT RECT` and starts a `SET TIMER(5)` (5-tick interval); the `On Timer` event then calls `MOVE OBJECT` to slide `vMovingText` five pixels left each tick until its right edge passes the left boundary, at which point `mUpdateMessage` swaps in a new queued message or loops the current text back to the right to scroll again.
- The banner window itself is opened as a small floating palette via `Open window(50;50;471;88;-(Palette window);"4D Banner";"mCloseBanner")`, keeping it visible but non-intrusive across the 4D Client desktop.

## Featured Technology

- MOVE OBJECT (animating a floating text banner)
- GET OBJECT RECT
- EXECUTE ON CLIENT (broadcasting to 4D Client machines)
- SET TIMER / On Timer form event
- 4D Chart offscreen area for text-width measurement (CT New offscreen area, CT Draw text, CT GET BOUNDARY)
- New process / SET PROCESS VARIABLE for interprocess messaging
- Open window (palette window) for a floating banner

## Historical Commentary

**Status:** Superseded

This note builds a scrolling marquee-style announcement banner for 4D Client environments, using MOVE OBJECT in a timer loop to slide a text variable across a small palette window, and cleverly repurposes 4D Chart's offscreen-area text metrics (CT Draw text / CT GET BOUNDARY) purely to measure how wide a message needs to be rendered at a given font/size before resizing the on-screen text object to match. It broadcasts the banner to connected 4D Clients via EXECUTE ON CLIENT, a solid pattern for its era of internal company-wide announcements inside a 4D Client/Server deployment. The specific animated-marquee UI style is now dated (most modern apps use toast/snackbar notifications or in-app banners instead of scrolling marquee text), and using 4D Chart purely as a text-metrics engine is an unusual workaround; 4D's current text/object APIs and richer client notification mechanisms make this specific implementation largely obsolete, though EXECUTE ON CLIENT remains a valid 4D Client/Server broadcast mechanism.

References to newer/updated information:
- The animated scrolling-marquee banner UI pattern has been largely superseded by modern toast/snackbar/in-app notification patterns
- EXECUTE ON CLIENT remains a supported 4D command for broadcasting execution to connected 4D Clients in current 4D Client/Server versions
- 4D Chart, used here only as a workaround for measuring text pixel width, has been superseded by other charting/graphics features in current 4D; modern 4D offers more direct text-measurement approaches without needing an offscreen chart area
