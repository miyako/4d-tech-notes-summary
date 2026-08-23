# Tech Note: Exploring 4D Portal's Reminder Portlet

- **Asset ID:** 19050
- **Tech Note #:** 01-53
- **Published:** November 30, 2001
- **Product / Version:** 4D 6.7.1
- **Platform:** Mac & Win
- **Author:** Cha Yang, 4D, Inc. Technical Support Engineer
- **Page URL:** https://kb.4d.com/assetid=19050
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_51-56_(NOV)/01-53_4D_Portal_Reminder_Portlet.hqx

## Overview

Cha Yang dissects the internals of 4D Portal's Reminder Portlet, which supports monthly, weekly, daily, and one-time reminders with optional ten- or five-minute advance warnings, explaining both how each reminder type's due date is calculated and how a background process periodically scans for and fires due reminders.

## Key Points

- Monthly reminders compute their date by combining a stored day-of-month with the current month/year (`CGI4D_ReminderChangeMonthly`), rolling the date forward a month if the computed date/time has already passed relative to now.
- Weekly reminders use `GEN4D_FindWeeklyDay`, a `Repeat` loop using `Add to date` and `Day number` to find the day-count gap between today and the next occurrence of a chosen weekday, then add that gap to the current date.
- Daily reminders simply add 1 day if today's reminder time has already passed; "once" reminders take a user-specified month/day/year directly.
- Firing logic centers on `$cgi4d_l_delay`, a Longint computed as `(([Reminder]Rem_Date-$CGI4D_CurrentDate)*?24:00:00?)+[Reminder]Rem_Time-$CGI4D_CurrentTime`, giving seconds remaining until due; this is compared against 600 (ten minutes), 300 (five minutes), or 0 to decide whether to send a Ten-minute, Five-minute, or None (exact-time) reminder.
- A `Rem_Ten_Five` field tracks reminder tier state, stepping "Ten" -> "Five" -> "None" as each threshold is crossed and a reminder is sent via `GEN4D_SendReminder`.
- After a "None" reminder fires, `GEN4D_ReassignDate` advances the reminder per its type: Daily +1 day, Weekly +7 days, Monthly +1 month, or marks a one-time reminder as Done.
- The whole system runs via a background process, `Gen4D_UtilityProcess`, launched at startup through `Gen4D_Startup` -> `Shell_DoProcess`, looping with `DELAY PROCESS(<>CGI4D_l_utilityProcess;60*60*1)` (~1 minute) and calling `GEN4D_FindDue` on each wake-up to scan the Reminder table and dispatch due reminders.

## Featured Technology

- 4D Portal Reminder Portlet
- Background process with DELAY PROCESS polling loop
- Monthly/Weekly/Daily/Once reminder date calculation
- Longint delay-seconds formula for Ten/Five/None reminder tiers
- New process / Shell_DoProcess process launching pattern
- Interprocess variables for cross-process process ID tracking

## Historical Commentary

**Status:** Obsolete

Cha Yang, a 4D, Inc. Technical Support Engineer, dissects the 4D Portal Reminder Portlet's internals: a background process that wakes every minute via a DELAY PROCESS loop to scan a Reminder table, computing due dates differently for Monthly/Weekly/Daily/Once reminder types and using a Longint seconds-until-due formula to decide whether to fire a Ten-minute, Five-minute, or exact-time reminder, then reassigning the next due date afterward. 4D Portal itself has long been discontinued as a product, making the specific portlet obsolete, but the general background-process pattern (New process plus a DELAY PROCESS polling loop to periodically scan a table for due items) remains a standard, still-valid 4D technique, and would today likely be built with 4D's more modern scheduling/timer capabilities rather than manually replicated from this specific example.

References to newer/updated information:
- 4D Portal (the product this portlet was built for) has been discontinued, making this specific reminder implementation historical rather than directly reusable
- The general background-process-with-DELAY-PROCESS polling pattern shown here remains valid in 4D today, though modern applications may prefer more structured scheduling/timer mechanisms
