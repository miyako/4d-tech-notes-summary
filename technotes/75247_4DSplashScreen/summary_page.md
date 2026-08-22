# Tech Note 09-14: 4D Splash Screen

**Author:** Thomas Fitch, Technical Services Team Member, 4D Inc.
**Published:** April 9, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75247
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_13-17_(APR)/09-14_4DSplashScreen.zip

## Proposition
Introduces 4DSplash, a reusable component database that lets any 4D application display a custom, configurable splash screen on startup, installable and configurable via a wizard, programmatically, or by editing an XML preferences file.

## Key Points
- **Drop-in installation:** copy `4DSplash.4dbase` into the host database's Components folder and call `4DSP_SplashScreen` from On Startup Database Method.
- **Three configuration paths:** the 4DSplash Chooser Wizard form (with live preview), programmatic call with nine parameters, or manually editing `demoinfo.xml`.
- **Two visual templates:** a square icon layout and a banner layout, each with suggested image dimensions and configurable header/sub-header/description text and colors.
- **Auto-dismiss behavior:** the splash window uses `SET TIMER(60*10)` to auto-close after ten seconds, and an invisible top button lets users click to dismiss early.
- **XML persistence:** settings are stored under a `/demo/...` XML node tree and read/written using 4D's DOM XML commands, creating the file on first save if it doesn't exist.
- Component works in both interpreted and compiled component modes.

## Featured Technology
- 4DSplash reusable component database (design-mode / .4dbase component)
- XML preferences file (demoinfo.xml) read/written via DOM XML commands
- SET COLOR / GOTO PAGE / SET TIMER classic form commands
- New Process for displaying a modal splash screen window

## Best Practices Highlighted
1. Use transparent-background logo images so the splash screen looks correct against any chosen background color.
2. Keep the component's configuration self-contained in an XML preferences file so the same component can be reused across many customer databases with only a config change.
3. Build wizard-style UI (with live preview) to reduce trial-and-error for less technical developers configuring appearance.

## Context / Positioning
Published shortly after 4D v11 SQL's component-architecture improvements made distributing developer add-ons far easier, this note demonstrates a practical, real-world component developers can adopt as-is or use as a template for building their own.

## Historical Commentary
**Status:** Partially Superseded

This note showcases a classic pattern: a compiled component database (binary .4dbase), installed by copying it into a Design-Mode database's Components folder, and configured through hand-rolled DOM XML preference files with numeric SET COLOR constants.

The underlying idea — a reusable startup splash screen component — is still a reasonable pattern today, but the specific implementation predates Project Mode's text-based, git-friendly component packaging (4D v17+, 2018) and predates JSON as the preferred settings-storage format over manual DOM XML trees. A modern equivalent would likely use a project-mode component/class, JSON preferences, and 4D's current object styling rather than legacy numeric color constants.
