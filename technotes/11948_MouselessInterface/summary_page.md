# Tech Note: Designing a "Mouseless" Interface

**Author:** Not specified in source document
**Published:** February 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11948
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a guide to building a fully keyboard-driven ("mouseless") interface in the Custom Menus environment using the HIGHLIGHT RECORDS command.

## Key Points
- Its proposition centers on the then-recently-introduced HIGHLIGHT RECORDS command (new in 4D version 6.5), which lets code programmatically highlight records in an output form exactly as if the user had clicked records while holding Shift or Ctrl/Command, giving developers full programmatic control over multi-record selection state without any mouse interaction.
- The note frames keyboard-driven event handling as needing to cover three main categories: selecting items from the menu bar, navigating within selections and subselections of records, and navigating/entering data within a detail form — though it explicitly limits its own scope to the first two categories, noting that detail-form navigation and data entry are already managed internally by 4D itself.
- The accompanying sample database is built for 4D v6.5 and, notably, its code is also provided as a 4D Insider library, reflecting 4D Insider's role at the time as a structure-documentation and code-sharing tool for the developer community.
- Featured technology includes the HIGHLIGHT RECORDS command itself, general keyboard-event handling logic in forms, and menu-bar/selection navigation techniques within the Custom Menus environment specifically (as distinct from the standard menus environment).
- This kind of note reflects both a genuine accessibility concern (supporting users who cannot or prefer not to use a mouse) and a broader theme in classic 4D development of tightly controlling form and selection behavior via code, a pattern seen across several other Tech Notes from this same era covering custom UI behavior.
- It remains a useful historical example of building rigorous, fully keyboard-operable interfaces well before dedicated accessibility APIs and guidelines were as formalized as they are today.

## Featured Technology
- HIGHLIGHT RECORDS command
- Keyboard-driven navigation
- Custom Menus environment
- 4D Insider library

## Historical Context
This note documents building an entirely keyboard-navigable interface in 4D's classic Custom Menus environment, centered on the then-new HIGHLIGHT RECORDS command (introduced in 4D v6.5) for programmatically simulating Shift/Ctrl-click multi-selection. Accessibility-minded, keyboard-only interface design remains a genuinely relevant concern today, but the specific Custom Menus environment and its manual keyboard-event plumbing this note relies on have been superseded by 4D's modern Design environment, form event model, and accessibility support, alongside HIGHLIGHT RECORDS itself remaining a valid but now well-established language command. Related updates since: HIGHLIGHT RECORDS remains part of the current 4D language, now a long-established rather than newly introduced command; 4D's forms and event-handling model has evolved substantially since the Custom Menus environment of this era, offering more built-in support for keyboard navigation and accessibility. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
