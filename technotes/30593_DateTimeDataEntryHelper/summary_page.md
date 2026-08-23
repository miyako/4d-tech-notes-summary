# Tech Note: Helping Date and Time Data Entry

- **Asset ID:** 30593
- **Tech Note #:** 03-49
- **Published:** November 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Melinda Gallo; Thierry Ozil
- **Page URL:** https://kb.4d.com/assetid=30593
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_48-51_(NOV)/03-49_Date_and_Time_Entry.hqx

## Overview

Melinda Gallo (4D Today) and Thierry Ozil (4D S.A.) present a small calendar/clock pop-up widget, adapted from the 4D Web Calendar and 4D Calendar sample databases (by Steve Hussey and Dave Batton), that lets users pick a date or time by clicking a small icon next to a field rather than typing it. Clicking the icon opens a modal dialog positioned at the mouse location showing a month grid (and a similar dialog for time), and the selected value is written directly back into the target field through a pointer parameter.

## Key Points

- CLND_Init detects the OS's short date format (US MM/DD/YY vs. European DD/MM/YY) by testing whether Day of(Date('02/01/02')) equals 2
- CLND_DlgDay_open computes screen position from GET MOUSE/SCREEN COORDINATES and opens a modal 176x206 popup window positioned at the click, passing the target field by pointer ($1->)
- CLND_Prefs_Set lets the host application configure the calendar's first day of week (Sunday/Monday), selection color, and font style
- CLND_Calendar_Set computes the first/last day of the displayed month with Add to date and Day of, then fills 42 day-slot buttons (btn_Day1..42), hiding unused ones with SET VISIBLE
- Month and year pop-up menus (clnd_Month, clnd_Year) re-run CLND_Calendar_Set when changed, using Add to date to shift the displayed month/year
- Clicking a day button runs CLND_Select, which resets the previous selection's font/color, computes the day delta with Add to date, and calls ACCEPT to close the dialog and return the chosen date via the pointer
- Month names and weekday labels are pulled from choice lists ('mois', 'Jours_Abrégés') specifically to keep localization simple

## Featured Technology

- Custom calendar popup dialog (CLND_ methods)
- DIALOG command (modal popup positioned at click)
- Add to date / Day of / Month of / Year of
- Localized US vs. European date-format detection
- Choice lists for month/day names (localization)
- Pointer-based field assignment ($1-> field target)

## Historical Commentary

**Status:** Historical Interest Only

This hand-built, click-driven date/time popup was a reasonable way to speed up data entry in 2003, when native OS or 4D form date/time pickers were far less capable. Modern 4D form objects and current operating systems (and browsers, for 4D web/QODA apps) now ship with built-in date/time picker controls that cover this exact use case out of the box, making the specific CLND_ method set unnecessary to hand-roll today. It remains an interesting, well-commented example of pointer-based dialog return values and OS locale detection in classic 4D.

**References to newer/updated information:**
- Current 4D form objects provide native date/time picker controls, removing the need for a hand-built calendar popup like this one
- Modern operating systems and browsers also provide native date/time pickers for web-based 4D applications
