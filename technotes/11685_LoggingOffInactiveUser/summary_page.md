# Tech Note 96-02: Logging Off an Inactive User

**Author:** Kent Wilbur
**Published:** January 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11685
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_01-05_(JAN)/96-02_Logging_Off_Users.exe

## Overview
This Tech Note presents a technique for automatically logging off 4D Server users after a period of inactivity — important because 4D Server was licensed on concurrent usage (an idle user occupies a license slot) and for security (an unattended session shouldn't stay open indefinitely). It also covers a companion "controlled shutdown" pattern that saves in-progress work before a database quits.

## Key Points
- **Fixed-timer approach (rejected):** logging off strictly after N minutes regardless of recent activity unfairly penalizes users who were just active (e.g., mid-coffee-break).
- **Continuous event-checking approach (rejected):** turning on `ON EVENT CALL` permanently gives perfect activity credit but imposes a noticeable performance overhead intercepting every keystroke/click.
- **Blended solution:** a `LogoffChecker` background process sleeps for roughly a third of the timeout period, briefly enables event checking to sample for activity, resets a presence flag if the user is active, and otherwise displays a one-minute warning before calling `QUIT 4D`.
- The core building blocks are `DELAY PROCESS`, `ON EVENT CALL`, `PAUSE PROCESS`/`RESUME PROCESS`, and a shared presence flag (`àfUsrPresent`) toggled by an `OnCallQuit` procedure.
- A **controlled shutdown** technique is also presented: a global `àfQuit` flag checked at the top of every global procedure, combined with custom per-window processes that respond to the `OUTSIDE CALL` layout execution phase to save/cancel modified records before the process ends.
- Background or long-running processes should disable the logoff checker (`PAUSE PROCESS`) for their duration so they aren't logged off while still working.
- An example "Auto Shop" database with users Moe, Larry, and Curly demonstrates the system; per-user logoff preferences could be added via a `[User]` file.

## Featured Technology
- 4D Server concurrent-usage licensing model
- `ON EVENT CALL`, custom processes, `DELAY PROCESS`/`PAUSE PROCESS`/`RESUME PROCESS`
- Controlled shutdown via `OUTSIDE CALL` layout execution phase

## Historical Context
Published in January 1996 for 4D Server 3.x, this note reflects an era when 4D's concurrent-usage licensing made freeing idle seats a direct financial/practical concern, and when there was no built-in session-timeout feature — developers had to hand-build the entire polling/event mechanism using low-level process-scheduling primitives.

## Historical Commentary
**Status:** Superseded

The underlying business need — timing out idle sessions to free licenses and improve security, and saving in-progress work before quitting — remains entirely relevant today, but 4D has since introduced more built-in session and user-management capabilities that reduce the need to hand-roll this exact polling/event-flag technique from scratch. 4D's licensing model, client/server architecture, and terminology (Events/Methods replacing Phases/Procedures starting in 4D V6, 1997) have also evolved substantially since this 1996-era 4D Server 3.x note was written.

