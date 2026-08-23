# Tech Note 02-10: Managing the Setup of 4D Chart Areas

- **Asset ID:** 23256
- **Tech Note #:** 02-10
- **Published:** March 31, 2002
- **Product / Version:** 4D Chart 6.8
- **Platform:** Mac & Win
- **Author:** Tim Tonooka
- **Page URL:** https://kb.4d.com/assetid=23256
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_10-14_(MAR)/03-10_Chart_Setup.hqx

## Overview

Tim Tonooka (4D Solution Partner) surveys every technique for configuring a 4D Chart area's look and behavior — object/form methods, disk templates, the default area, and the CT ON EVENT custom event handler — including the only mechanism available for 4D Chart areas hosted in plug-in (external) windows, where there is no object or form method to hook into.

## Key Points

- Explains 4D Chart's document-oriented model: a 4D Chart area displays one document at a time, which can hold multiple graphs, text, lines, and pictures, and can be up to 3500x3500 pixels, saved to a picture field, disk file, or template.
- Enumerates the seven ways to configure a 4D Chart area's setup and their precise precedence: (1) default-area copy on creation, (2) disk template load, (3) `CT ON EVENT` handler firing on the area-creation event (if enabled via `CT EVENT FILTER`), (4) object method `On Load`, (5) form method `On Load` — noting object/form methods only work for form-based areas, not plug-in windows.
- Documents the `CT ON EVENT`-installed custom event handler as the only way to run setup code for a 4D Chart area in a plug-in window; the demo's `CHT_EventHandler` method uses `CT SET DISPLAY` to show/hide interface elements based on a Preferences palette.
- Shows intercepting 4D Chart's own File > Print menu command with `CT ON MENU` installing a `CHT_MenuHandler` method that checks the menu command code (1009 = Print) and either runs custom print code or falls back to `CT DO COMMAND` for standard behavior.
- Explains `CT NEW DOCUMENT` / File > New clearing behavior: objects and most settings reset from the default area, but settings like `CT EVENT FILTER` and `CT ON MENU` persist across a document clear and are not reapplied from templates.
- Lists the key 4D Chart setup commands: `CT ON ERROR`, `CT ON EVENT`, `CT ON MENU`, `CT EVENT FILTER`, `CT EXPERT COMMAND`/`CT EXPERT MODE`, `CT SET ENTERABLE`, `CT SET DISPLAY`, `CT SET DOCUMENT SIZE`, `CT SET PROPERTIES`, `CT AREA TO AREA`, `CT SET REFNUM`, and the `CT SET TEXT/LINE/FILL ATTRIBUTES` family.
- Notes that "button mode" (small 4D Chart areas under 300x150 pixels rendering as a button instead of an area) can be disabled with `CT SET ENTERABLE`, and that the architecture of 4D Draw closely parallels 4D Chart so the techniques carry over.

## Featured Technology

- CT ON EVENT / CT EVENT FILTER custom event handler
- CT ON MENU custom menu handler
- CT SET DISPLAY / CT SET ENTERABLE / CT SET PROPERTIES
- 4D Chart plug-in windows (external windows)
- CT DO COMMAND
- 4D Chart default area and disk templates
- 4D Chart / 4D Draw shared architecture

## Historical Commentary

**Status:** Obsolete

Tim Tonooka's note is a thorough reference for configuring 4D Chart areas — explaining the precedence order between the default area, disk templates, the CT ON EVENT event handler, and object/form On Load code, plus how to intercept 4D Chart's own menu bar with CT ON MENU. This was essential knowledge in the 4D v6.x/6.8 era when 4D Chart was the only built-in graphing engine, including for plug-in (external) windows that have no object or form method to hook into. 4D Chart itself has since been deprecated in favor of the modern, cross-platform, script-driven chart area / SVG-based charting built into current 4D versions, so this note is now of historical interest only for maintaining legacy 4D Chart-based databases.

References to newer/updated information:
- 4D Chart (the CT_ command family) has been superseded by 4D's modern built-in Chart area / SVG-based charting components in current 4D versions
- Newer 4D charting is form-object based with structured properties rather than requiring CT ON EVENT/CT ON MENU interception tricks for area configuration
