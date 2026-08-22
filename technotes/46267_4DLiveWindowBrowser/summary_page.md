# Tech Note 07-16: Building a Simple Browser with 4D Live Window

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** April 26, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.0 (4D Live Window 1.1 beta) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=46267
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_13-16_(APR)/07-16_4DLW_Browser.zip

## Overview
Presented as a development diary rather than a formal reference, this note documents building a simple embedded web browser interface with the 4D Live Window plug-in, explicitly not intended to replace a real web browser but to build a reusable framework and share lessons learned, particularly around the plug-in's new event system.

## Key Points
- Explicitly warns that 4D Live Window is meant to *extend* 4th Dimension with embedded web content, not to replace the user's actual web browser (4D already has OPEN WEB URL for that).
- Design goals: support a navigable "session" of visited URLs, and correctly enable/disable Back/Forward/Stop buttons based on session position and load state.
- The session is implemented as a simple 4D text array of visited URLs, mimicking standard browser session semantics (new navigation truncates any "forward" history).
- 4D Live Window 1.1 introduced callback-based events (Before, During, After, Error) registered via `WEB_SetPreferences`, which are essential to tracking navigation state.
- A key challenge: reconciling 4D Live Window's own navigation events with separate 4D Form events (e.g., a button's "On Clicked"), since actions like clicking Back generate a Before event that must be handled differently from user-typed navigation.
- Solution: define a custom superset of "browser events" tracked in a process variable (protected by a semaphore), updated by the plug-in callbacks, with `CALL PROCESS` and the "On Outside Call" form event used to notify the form to refresh.
- The included sample database ("4DLW Browser.4DB") uses a time-limited demo version of the plug-in and a documented method-prefix naming convention (LWB_EVENT_, LWB_FORM_, LWB_SESSION_, etc.).
- Notes real-world limitations: complex sites with heavy redirection/JavaScript navigation (e.g., abcnews.com) can break event-based session tracking.

## Featured Technology
- 4D Live Window plug-in (4D Web 2.0 Pack)
- WEB_SetPreferences, WEB_Back/WEB_Forward/WEB_Stop/WEB_Refresh/WEB_SetURL
- 4D Form events ("On Clicked", "On Outside Call")
- CALL PROCESS, process variables, semaphores

## Historical Context
4D Live Window was a Web 2.0 Pack plug-in for embedding a native web browser control inside 4D forms — a capability now provided natively via 4D's built-in Web Area form object, without a separate licensed plug-in. The specific commands and event model described (WEB_SetPreferences, Web_kNavigate/Web_kError selectors) are obsolete, though the general pattern of tracking asynchronous navigation events to drive UI state (enabling/disabling buttons based on position and load status) remains a broadly applicable UI engineering technique for any embedded browser control today.

## Historical Commentary
**Status:** Obsolete

The 4D Live Window plug-in and 4D Web 2.0 Pack have been discontinued; current 4D provides a built-in Web Area object that replaces the need for this plug-in's commands and licensing model entirely, though the event-driven navigation-tracking approach documented here remains conceptually instructive.
