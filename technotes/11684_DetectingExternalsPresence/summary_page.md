# Tech Note 96-01R: Detecting the Presence of Externals in a 4D Database

**Author:** Julie Pearson (Revised by Jeff Browning)
**Published:** January 1, 1996 (Revised April 1996) | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11684
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_01-05_(JAN)/96-01_Detecting_Externals.exe

## Overview
Prior to 4D v1.5, external testing routines checked whether a 4D external (plugin) was installed, but these no longer worked reliably once 4D introduced the platform-independent extension architecture using Mac4DX/Win4DX folders. This Tech Note provides a portable, code-only solution that works with both the old and new external architectures to detect whether any given 4D external — including 4D's own productivity/connectivity modules or third-party packages — is present.

## Key Points
- The core trick: call one of the external's commands inside an `ON ERR CALL`-trapped procedure; if the external isn't installed, 4D raises a syntax error that the trap catches.
- The example uses a minimal 4D Write call (`WR Error text`) to test for 4D Write's availability, recording the trapped error code in a global `LError` variable.
- An `OnErrCall` procedure sets `LError := Error` and is registered via `ON ERR CALL ("OnErrCall")` before making the test call.
- A crucial detail: an `IDLE` call must immediately follow the command that may trigger the error, so the error is carried out — this is required in compiled databases for the error-handling callback to the 4D kernel to run.
- The pattern generalizes into a `WriteAvail` function returning a boolean, which a `Startup` procedure can call to alert the user and quit if a needed external (like 4D Write) isn't installed.
- Rule of thumb: use a command in the test call that does very little, since the goal is only to probe availability, not to change data.

## Featured Technology
- 4D's old and new (Mac4DX/Win4DX) external/plugin architecture
- `ON ERR CALL` error trapping
- 4D Write (used as the worked example)

## Historical Context
Published in the same January 1996 batch of Tech Notes, this note addresses a real transitional pain point as 4D moved from its original external architecture to the platform-independent Mac4DX/Win4DX folder-based system. Detecting plugin availability by deliberately triggering and trapping an error was the standard workaround at a time when 4D had no direct "is this plugin installed" command.

## Historical Commentary
**Status:** Obsolete

4D's plugin and component architecture has evolved substantially since 1996 (later 4D Plugin SDK generations, and eventually Components and ORDA-era extension mechanisms), reducing or eliminating the need for this deliberately-trigger-an-error detection trick. The specific example external, 4D Write, was itself superseded by 4D Write Pro starting in 4D v14 (2016). The general concept of trapping errors to probe optional functionality remains a recognizable pattern, but it is now largely unnecessary given more direct modern mechanisms for querying installed plugins and components.

