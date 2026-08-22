# Tech Note 01-03: Disabling Tab Controls

**Author:** Not specified in source document
**Published:** January 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12155
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_01-05_(JAN)/01-03_Disable_Tab_Controls.exe

## Overview
A comparison of two techniques — disabling versus deleting — for preventing users from navigating to certain pages via a tab control. This Tech Note addresses a common form-design need: when a form uses tab controls tied to either an automatic action or a custom 'go to page' style method, developers frequently need to prevent users from accessing certain pages under specific conditions.

## Key Points
- In 4D, this can be accomplished in one of two ways — disabling the tab control so it remains visible but inert, or deleting it outright so the page is no longer reachable at all — and this note illustrates both approaches side by side.
- Its featured technology is simply the tab control object and the conditional logic needed to manage its enabled/deleted state at runtime, a small but broadly applicable form-navigation technique useful any time access to specific form pages needs to be conditionally restricted.

## Featured Technology
- Tab controls (form objects)
- Automatic action / 'go to page' method pattern
- Form navigation control

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Still relevant

This note compares two ways to restrict access to certain form pages navigated via tab controls (associated with either an automatic action or a custom 'go to page' method): disabling the tab control outright, or deleting it. Tab controls and the underlying need to conditionally restrict navigation remain a completely standard, still-current 4D form design pattern, so this note's guidance is directly usable by developers building binary or Project Mode forms today with little modification.

**Related updates since:**
- Tab controls and their enable/disable behavior remain unchanged in current 4D form design, in both Design Mode and Project Mode

