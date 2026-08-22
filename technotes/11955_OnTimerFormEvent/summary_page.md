# Tech Note: The On Timer Form Event

**Author:** Not specified in source document
**Published:** March 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11955
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a tour of practical uses for the On Timer form event, including simulating menus, moving objects, and building a custom resize box.

## Key Points
- It covers using On Timer to simulate menus within a window (useful in the Custom Menus environment, where 4D's standard menu bar behavior could be restricted or customized), to animate or move objects on a form over time, and to simulate a window resize box — a draggable corner control that lets users resize a window even when the platform or environment doesn't provide one natively.
- The note's proposition is that On Timer, a periodic form event that fires at a developer-defined interval, is a flexible building block applicable to multiple distinct UI problems rather than a single narrow use case.
- Featured technology centers on this one language-level event and the surrounding form-object techniques needed to use it effectively: tracking elapsed time, redrawing or repositioning objects on each timer tick, and coordinating mouse-tracking logic for the simulated resize box example.
- This kind of note was valuable to developers building custom, non-standard interfaces in the Custom Menus environment of 4D v6.5, where achieving behaviors taken for granted in native OS windows (like resizing) required manual implementation.
- Because only the brief teaser text survives in this archive, the specific example code for each of the three use cases is not preserved here, but the scope is clear from the introduction.
- On Timer remains part of 4D's language to this day, making the general technique-survey approach of this note more durable than many of its era's more narrowly platform-specific companions.

## Featured Technology
- On Timer form event
- Simulated menus
- Custom Menus environment
- Simulated resize box

## Historical Context
This note surveys the On Timer form event, a classic 4D language feature that still exists in the current 4D language largely unchanged in concept, used here to build several period-specific custom UI tricks (simulated menus, object animation, and a hand-built resize box) that were necessary before 4D added richer native UI features. The On Timer event itself remains a valid, still-used 4D language feature today, so this note is conceptually still relevant, even though the specific UI problems it solves (simulated resize boxes, simulated menus in the Custom Menus environment) are largely obsolete now that 4D forms support native window resizing and standard menu bars more flexibly. Related updates since: The On Timer form event remains part of the current 4D language and is still commonly used for periodic UI updates and polling; Native window resizing and standard menu-bar support in modern 4D forms have removed the need for many of the specific simulated-UI tricks this note demonstrates. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
