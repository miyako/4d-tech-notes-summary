# Tech Note 06-17: QuickTime Container 1.2 – More Features

**Author:** Thomas Maul, General Manager, 4D Germany; and Louis Thoumin, International Sales Engineer, 4D S.A.
**Published:** April 28, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=42855
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_14-17_(APR)/06-17_QTime_Container_1.2.zip

## Overview
This note documents version 1.2 of the QuickTime Container plug-in for 4D, an update to the plug-in from TN 05-30 that adds offscreen movie/audio handling, metadata tag reading, movie-frame screenshot capture, and Windows redraw optimizations, all built on top of Apple's QuickTime framework.

## Key Points
- **Offscreen areas:** `QTNewOffscreenArea` opens a movie/song invisibly (no on-screen display) so code can query it (e.g., via `QTGetControl` for movie length) or capture a screenshot; `QTDeleteOffscreenArea` must always be called afterward to free memory.
- **Metadata tag reading:** `QTGetTags` returns parallel text arrays of "user data" tags — for MP3s: album, artist, title, comment, track number; for camera pictures: maker, model, software, timestamp, host, comment — using QuickTime's 4-character tag identifiers.
- **Frame screenshot capture:** `QTScreenshot` returns a 4D picture of the movie's current frame at its displayed size, or at native/full size when combined with `QTSetControl(Area; QTSize; 100)`.
- **Other new/changed commands:** `QTSetMovie` now supports paths over 255 characters on both platforms; `QTRemoveMovie` cleanly closes/erases a movie or picture and hides the controller; two new read-only `QTGetControl` selectors expose preferred play rate and preferred volume.
- **Optimizations:** improved Windows redraw behavior (less flicker on resize, especially for growing containers) and a source rebuild against then-current Apple Xcode 2.2 / Microsoft Visual Studio 2005 for OS/4D compatibility.

## Featured Technology
- QuickTime Container plug-in (QTContainer) for 4D
- Apple QuickTime framework (movie/audio/picture handling, metadata, playback control)
- 4D picture type integration for programmatic screenshot capture

## Historical Context
Published in 2006 for 4D v2004, this note is a plug-in reference document from an era when QuickTime was Apple's standard cross-platform media framework and long predates 4D's SQL engine (2007), Project Mode (2018), or ORDA. QuickTime itself has since been deprecated and discontinued by Apple (QuickTime for Windows support ended in 2016; macOS moved to AVFoundation), making the plug-in's entire foundation obsolete.

## Historical Commentary
**Status:** Obsolete

Apple's QuickTime framework, on which this entire plug-in and command set depends, has been deprecated and discontinued (QuickTime for Windows was officially end-of-lifed in 2016, and modern macOS relies on AVFoundation instead). As a result, none of the specific commands documented here (`QTNewOffscreenArea`, `QTGetTags`, `QTScreenshot`, etc.) are usable in a modern development context, and any current 4D media-handling need would require an entirely different, modern API.
