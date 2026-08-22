# Tech Note 10-19: Running 4D Server as a Mac OS X "Faux" Service

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** June 24, 2010 | **Product/Version:** 4D Server v11.6 | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=76121
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_17-20_(JUN)/10-19_OSXFauxService.zip

## Proposition
Because Mac OS X of the era had no equivalent to Windows' "Register as a Service" for 4D Server, this note presents a workaround using Login Items and a paired AppleScript application to auto-launch 4D Server at startup and cleanly shut it down at system shutdown/restart, approximating true service behavior.

## Key Points
- **The problem:** 4D Server can be registered as a Windows Service (auto-launch at boot, persistent across user logouts, clean shutdown without the "Delay" dialog) but Mac OS X had no equivalent registration mechanism.
- **The technique:** a Login Item launches a small paired AppleScript application, which starts 4D Server (with a specific database) and later intercepts the system "quit" event to signal 4D Server to shut down without delay.
- **Multiple pairing scenarios** are handled: built/OEM/VAR servers, self-contained `.4dbase` bundles, and structure/data pairs requiring a `.4DLink` file.
- **PairingsMaker utility database** (included) automates generation of the AppleScript and Terminal scripts so developers don't need AppleScript expertise.
- **Optional hide-and-lockout** options are covered for restricting end-user interference with the running server process.

## Featured Technology
- Mac OS X User Accounts Login Items
- AppleScript application launching and shutdown handling
- 4DLink files for pairing 4D Server with a database
- .4dbase self-contained bundles
- PairingsMaker utility database (included with the note)

## Best Practices Highlighted
1. Use a self-contained `.4dbase` bundle or explicit `.4DLink` pairing depending on where structure and data files live.
2. Automate script generation (via PairingsMaker) rather than hand-writing AppleScript for each deployment.
3. Handle the shutdown "quit" event explicitly to avoid presenting the "Delay" dialog during unattended restarts.

## Context / Positioning
Published for 4D v11.6/early v12 era, this note filled a real operational gap for Mac-based 4D Server administrators who needed Windows-service-like reliability without a native macOS service registration feature.

## Historical Commentary
**Status:** Obsolete

This note addresses a genuine historical gap: older Mac OS X versions had no built-in mechanism to register 4D Server as a true background service, so this workaround used Login Items plus a paired AppleScript application to launch and quit the server.

Modern macOS has since gained first-class facilities for this — launchd daemons/agents configured via `launchctl` and LaunchDaemon/LaunchAgent `.plist` files — which are far more robust (surviving without a logged-in user session, integrated with system logging, etc.) and are what current 4D Server deployment guidance and most administrators use instead of this AppleScript/Login-Items workaround.
