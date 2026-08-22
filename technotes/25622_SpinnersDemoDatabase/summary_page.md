# Tech Note 03-5: Inside the Spinners Demo Database

**Author:** Gou Yang, 4D Inc. Technical Support
**Published:** January 31, 2003 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25622
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_01-05_(JAN)/03-05_inside_spinners.exe

## Overview
TN 03-5 is a code-walkthrough Tech Note explaining the mechanics of the "Spinners" demo database, a small example showing spinner (increment/decrement) controls for numeric, date, and time fields built entirely from classic 4D language primitives — On Timer, GET MOUSE, and SET TIMER — with no dedicated spinner widget in the toolkit.

## Key Points
- Demonstrates the On Timer event combined with GET MOUSE to detect a held-down mouse button and drive continuous increment/decrement.
- Uses a pointer (Spin_ObjectPtr) so the same generic method can spin any Time, Date, or numeric field.
- Implements acceleration: after a configurable delay (0/1/3 seconds), the timer interval shortens for faster spinning.
- Handles Date fields with US (M/D/Y) vs. non-US (D/M/Y) ordering when deciding which date component to adjust.
- Platform detection via PLATFORM PROPERTIES toggles Mac vs. Windows-specific button visibility.
- Originally written by Tom Dillon (DataCraft), revised by Raymond Manley for 4D, Inc.

## Featured Technology
- On Timer event
- 4D Compiler
- Form/object methods
- Date & Time field types

## Historical Context
Written for 4D 6.8 in January 2003, this note predates 4D's later native stepper/spinner form objects and shows how such UI conveniences had to be hand-built from timer events and pointers in the classic 4D language and Design Mode environment.

## Historical Commentary
**Status:** Historical Interest Only

The On Timer/GET MOUSE technique shown here is a period-accurate workaround for a UI affordance (a numeric/date/time spinner) that modern versions of 4D and most other platforms now provide as a built-in widget or via native OS controls, so the specific plumbing is of mostly historical/educational interest today. The underlying concepts — pointers to typed variables, event-driven form methods, and timer-based polling — remain valid 4D language fundamentals still used in current versions.
