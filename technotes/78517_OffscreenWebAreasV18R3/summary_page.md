# Tech Note 20-12: Offscreen Web Areas in v18 R3

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** July 27, 2020 | **Product/Version:** 4D v18 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78517
**Download:** https://kb.4d.com/DLTN/TN/2020/20-12_OffscreenWebAreas18R3.zip

## Proposition
Loading and processing web content previously required a visible Web Area on a form. This Tech Note introduces `WA Run offscreen area`, a new v18 R3 command that spins up a Web Area entirely in memory — with no form or window needed — enabling web scraping, metadata extraction, and screenshot generation even on a headless server.

## Key Points
- **New command**: `WA Run offscreen area` accepts an object parameter with `url`, `area`, `onEvent`, `autoQuit`, `timeout`, `result`, and arbitrary custom properties.
- **Lifecycle callback events**: `On Load`, `On End URL Loading`, `On URL Loading Error`, `On Unload` — invoked via a Formula object or class `onEvent` function.
- **JavaScript bridge**: `WA Evaluate JavaScript`, `WA EXECUTE JAVASCRIPT FUNCTION`, and related commands are usable inside the callback to interact with the loaded page.
- **Timeout tracking**: a `timeoutReached` boolean property is automatically added post-execution if the timeout elapsed.
- **Structured error handling**: `WA GET LAST URL ERROR` inside `On URL Loading Error` captures URL, description, and code into a custom `error` object property, checkable afterward with `OB Is defined`.
- **autoQuit control**: when true (default), the command auto-stops on load-finish/error; when false, the callback or `$4d` object must explicitly call `CANCEL`/`ACCEPT`.
- **Demo examples**: three sample scenarios, including scraping the latest 4D blog post title from blog.4d.com and timing each lifecycle phase with `Milliseconds`.

## Featured Technology
- WA Run offscreen area (new in v18 R3)
- Formula-based onEvent callback pattern
- WA Evaluate JavaScript
- WA GET LAST URL ERROR
- Headless web page scraping/automation

## Best Practices Highlighted
1. Use `autoQuit:=False` combined with explicit `CANCEL`/`ACCEPT` when finer control over when the offscreen area terminates is needed.
2. Always check `OB Is defined($params;"error")` after the command returns to detect and handle load failures.
3. Set a sensible `timeout` value and check `timeoutReached` to avoid offscreen areas hanging indefinitely on unresponsive pages.

## Context / Positioning
This note documents a genuinely new v18 R3 capability that extended 4D's long-standing Web Area feature into headless/background use cases — web scraping, metadata extraction, server-side rendering tasks — that previously required either a visible window or an external tool, reinforcing 4D's positioning as capable of both interactive UI and backend automation work within a single platform.

## Historical Commentary
**Status:** Current

`WA Run offscreen area` remains a current, supported 4D command, and the overall pattern — object-based parameters, Formula-based `onEvent` callback, `WA Evaluate JavaScript` for page interaction, and `WA GET LAST URL ERROR` for error handling — is still how headless web automation is done in 4D today; nothing here has been deprecated. If anything, this feature has become more useful over time: 4D's Web Area engine was later rebuilt on a bundled Chromium engine, giving offscreen areas more modern, consistent JavaScript/DOM behavior than was available when this note was written, without requiring any change to the API surface documented here.
