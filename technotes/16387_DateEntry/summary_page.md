# Tech Note: Date Entry

- **Asset ID:** 16387
- **Tech Note #:** 01-31
- **Published:** July 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Elaine Smith
- **Page URL:** https://kb.4d.com/assetid=16387
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_31-35_(JUL)/01-31_Date_Entry.hqx

## Overview

Elaine Smith (Technical Support Engineer) presents the Date Entry example database, which uses a set of routines and special function keys to make date-field entry more flexible: by tabbing into a field, users can set the date using shortcuts instead of typing a full date string.

## Key Points

- Reviews 4D's Form event inheritance rules: Form-method-oriented events (e.g., `On Load`) require the Form-level event checkbox to be enabled or no object receives them, while Object-method-oriented events (e.g., `On Clicked`) are independent — disabling an event at the Form level doesn't stop Object-level handlers, and vice versa.
- `On Before Keystroke` fires before a typed character is applied to the field's display value; `On After Keystroke` fires after, letting code react to (or look ahead based on) what was typed.
- `FILTER KEYSTROKE` (called during `On Before Keystroke`) replaces the entered character with the first character of a supplied string, or cancels the keystroke entirely if passed an empty string (`FILTER KEYSTROKE("")`); `Keystroke` returns the actual character typed.
- Tom Dillon's (DataCraft) `HandleDate`/`StringToDate` example methods implement single-letter shortcuts: `T` (today), `M` (first of month), `H` (last of month), `Y` (first of year), `R` (last of year), `+`/`-` (add/subtract a day), triggered from a date field's `On Before Keystroke` event and finalized on `On Data Change`.
- `StringToDate` also parses delimiter-free date strings (e.g., "070476" → 07/04/76, "07041976" → 07/04/1976, "0704" → 07/04 current year), with two-digit years resolved according to the `SET DEFAULT CENTURY` command, and supports both MM/DD/YY and DD/MM/YY formats.
- Usage is simply calling `HandleDate(Self)` from a date field's object method, with the field's `On Before Keystroke` and `On Data Change` events enabled.

## Featured Technology

- On Before Keystroke / On After Keystroke form events
- FILTER KEYSTROKE command
- Keystroke command
- HandleDate / StringToDate example methods (Tom Dillon, DataCraft)
- SET DEFAULT CENTURY for two-digit year resolution
- Form/Object event inheritance rules

## Historical Commentary

**Status:** Obsolete

The underlying commands (`On Before Keystroke`, `FILTER KEYSTROKE`, `Keystroke`) still work exactly as described in current 4D versions, and keystroke-trapping techniques remain valid for building custom data-entry behaviors. However, the specific UI pattern demonstrated — hidden, undocumented single-letter shortcuts for setting a date — reflects period UI conventions; modern 4D form design overwhelmingly favors discoverable calendar/date-picker widgets over memorized function keys, so the technique itself, while technically functional, is no longer a recommended approach.

**References to newer/updated information:**
- 4D form objects now commonly use built-in date/calendar picker controls rather than custom function-key-driven entry routines
- The On Before Keystroke/On After Keystroke events and FILTER KEYSTROKE/Keystroke commands described remain part of the current 4D language, unchanged in behavior
- Modern UI/UX conventions favor discoverable calendar widgets over hidden function-key shortcuts
