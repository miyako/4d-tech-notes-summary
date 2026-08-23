# Tech Note 02-15: Event Manager

- **Asset ID:** 23252
- **Tech Note #:** 02-15
- **Published:** April 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Stephanie Robineau
- **Page URL:** https://kb.4d.com/assetid=23252
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_15-19_(APR)/02-15_Event_Manager.hqx

## Overview

Stephanie Robineau (4D Technical Note Department) presents a small diagnostic database that traces the real-world execution order of 4D form events, using a generic event-logging method applied to forms and objects, so developers can observe and control event execution order across Add/Modify Records, Dialog, and Print record scenarios.

## Key Points

- The sample database's "Test" window (opened via File > Test) lets the user choose object types to test on one tab, and specific events to monitor on a second tab, with Shift+click to select/deselect all events at once.
- A "test mode" pop-up offers three scenarios — Add/Modify Records, Dialog, and Print record — because the sequence of events that fire depends heavily on how the form is actually being used.
- Clicking Test opens two windows: a floating palette that logs each executed event (new entries appended to the top of the list) and a window containing the objects selected for testing.
- Events logged differ noticeably between Add/Modify Records mode and Dialog mode, illustrating that the same objects can produce a different event sequence depending on context.
- In Print record test mode, choosing print preview updates the palette live with the events fired during printing; the palette's logged contents can themselves be printed via a Print button.
- "Display record" mode was deliberately not implemented in the demo because On Load is the only event it fires, and only for the main form — there was nothing further to trace.
- The author notes the same generic event-trapping method can be reused to trap and log trigger execution, not just form/object events.

## Featured Technology

- 4D form event tracing (generic event-logging method)
- Add/Modify Records vs Dialog vs Print record test modes
- Form event execution order
- On Load form event
- Trigger event trapping (same technique)

## Historical Commentary

**Status:** Partially superseded

This note demonstrates a diagnostic tool — a generic event-trapping method installed on forms and objects that logs each form event as it fires to a floating palette, letting a developer observe the actual order in which 4D executes form events under different scenarios (data entry/modify, dialog, and print). This kind of empirical event-order investigation was valuable in the 4D v6.8 era when form event documentation was sparse and behavior could vary by mode; the underlying event set and firing order have evolved somewhat in later 4D versions (and modern object notation/forms), so the specific event list here is dated, but the general debugging technique of instrumenting event handlers to trace execution order remains a valid and still-used approach today.

References to newer/updated information:
- 4D's form/object event model has evolved since v6.8 (e.g. additional events, changes with 4D's object notation and modern form editor), so the exact event list and behaviors demonstrated are dated
- The general technique of tracing form events with a shared logging method remains valid and is comparable to using 4D's built-in debugger or trace/log statements today
