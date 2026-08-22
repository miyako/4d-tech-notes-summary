# Tech Note 07-31: 4D Live Window JavaScript Part 1 – Offscreen Areas

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** August 8, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Windows only
**Page:** https://kb.4d.com/assetid=47211
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_30-34_(AUG)/07-31_4DLW_Offscreen_Area.zip

## Overview
Part 1 of a two-part series, this note shows a workaround for creating an "offscreen" 4D Live Window (4DLW) plug-in area — which 4DLW could not natively support — by hiding a Palette window containing the plug-in area off-screen, enabling JavaScript functions loaded there to be treated as callable 4D "code libraries."

## Key Points
- `Web_JavaScriptReturn(Area; Function; Result; Parameter1...5)` executes a named, existing JavaScript function with up to 5 text parameters and returns a text result (distinct from `Web_JavaScriptExecute`, covered in Part 2).
- Since 4DLW cannot create a true offscreen area, the demo opens a "Palette window" containing the 4DLW area and moves it beyond `Screen width` bounds — the hosting process must remain unhidden (not `HIDE PROCESS`) or the plug-in stops working.
- A custom "event model" (an interprocess variable plus `CALL PROCESS`) lets other processes trigger and await results from JavaScript calls handled by the hidden window's `OnOutsideCall` handler.
- Three example JavaScript-as-4D-method functions are implemented: get browser user agent, calculate day-of-week of birth via Zeller's algorithm, and get OS from `navigator.appVersion`.
- JavaScript execution in 4DLW is Windows-only; Mac OS's WebKit layer was too unstable and could crash the database. The demo uses a time-limited 4DLW 1.1.2 license.

## Featured Technology
- 4D Live Window (4DLW) plug-in
- 4D Web 2.0 Pack
- `Web_JavaScriptReturn` command
- Palette windows, `CALL PROCESS`, custom interprocess event model

## Historical Context
Published August 2007, in the active but ultimately short-lived 4D Web 2.0 Pack era, ahead of 4D v11's native SQL engine later that year, and roughly a decade before Project Mode and ORDA arrived.

## Historical Commentary
**Status:** Obsolete

4D Live Window and the entire 4D Web 2.0 Pack have been discontinued, so the specific plug-in, its `Web_JavaScriptReturn` API, and the hidden-Palette-window trick described here no longer apply to any current 4D product. The broader goal — calling JavaScript logic from 4D code as a reusable library — is a reasonable historical curiosity, but would be solved very differently today (e.g., an external Node.js service or HTTP call) rather than by hiding a browser plug-in window off-screen.
