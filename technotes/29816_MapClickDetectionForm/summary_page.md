# Tech Note 03-42: Using a Map in a Form

**Author:** Not specified in source document
**Published:** September 30, 2003 | **Product/Version:** 4D v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=29816
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_40-43_(SEP)/03-42_Using_a_Map_in_a_Form.exe

## Overview
A Tech Note demonstrating how to detect a mouse click on a non-rectangular region of a picture placed on a 4D form, using a clickable map of US states as the example.

## Key Points
- Solves the problem of detecting clicks on non-rectangular regions of an image-based form object.
- Uses a US states map as the concrete worked example.

## Featured Technology
- Non-rectangular hit detection
- Form picture objects

## Historical Context
Written in the classic 4D Design Mode / binary form era, before image maps and modern client-side web frameworks made such click-region detection trivial via HTML/CSS/JS; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

The specific 4D form-object hit-detection technique this note describes has been made largely unnecessary by modern web-based UI (where HTML image maps or SVG regions handle this natively), and even within 4D, web areas embedding modern JS/HTML now make this kind of interactive map far simpler to build than in the classic client-only 4D era.
