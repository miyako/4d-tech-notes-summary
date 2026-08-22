# Tech Note 05-30: QuickTime Container

**Author:** Not specified in available source
**Published:** September 2, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=39063
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_30-33_(SEP)/05-30_QuickTime_Container.exe

## Overview
This Tech Note presents the QuickTime Container plug-in, which allows a 4D developer to open a window and play any QuickTime-supported movie or audio file directly within a 4D application.

## Key Points
- Supports all movie and audio formats that Apple QuickTime itself supported.
- The standard QuickTime controller can be added with minimal coding.
- Optional commands expose full programmatic access to playback, enabling a custom user interface.

## Featured Technology
- QuickTime Container plug-in (4D plug-in wrapping Apple QuickTime)
- QuickTime movie/audio playback and controller UI
- 4D Plug-in API (command-based extension of the 4D language)

## Historical Context
**Status:** Obsolete

This plug-in's entire value proposition depended on Apple's QuickTime framework, which Apple fully discontinued (including QuickTime for Windows) around 2016, making the plug-in itself non-functional on any modern OS. 4D's plug-in architecture has also moved on substantially since 2005 (Unicode support, Universal Binary in v11 SQL, and later 64-bit-only plug-ins), so this specific binary would not load in current 4D regardless of QuickTime's status. Developers today embedding audio/video in a 4D application would instead use HTML5 `<audio>`/`<video>` elements inside a 4D Web area. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and its example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
