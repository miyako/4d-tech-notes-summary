# Tech Note 18-04: Kiosk Mode on Windows 10

**Author:** Guillaume Kotulski, Developer, 4D SAS.
**Published:** March 27, 2018 | **Product/Version:** 4D v16 | **Platform:** Win
**Page:** https://kb.4d.com/assetid=77976
**Download:** https://kb.4d.com/DLTN/TN/2018/18-04_KioskModeOnWindows10.pdf

## Proposition
A step-by-step guide to locking down a Windows 10 machine into kiosk mode running a 4D application, using Microsoft's Windows Configuration Designer, aimed at point-of-sale and other public-facing deployment scenarios.

## Key Points
- **OS requirements:** requires Windows 10 Enterprise or Education, version 1709 or above, to use the Windows Configuration Designer.
- **Windows Configuration Designer walkthrough:** covers building a provisioning package that designates the kiosk account and the 4D application as the assigned-access shell.
- **Advanced settings:** additional kiosk behavior (e.g., restart handling) is configurable within the tool.
- **Export and install:** the provisioning package is exported and applied to the target machine to activate kiosk mode.
- **Recovery procedure:** exiting kiosk mode requires an admin account, disconnecting the kiosk session (e.g., via `tsdiscon`), and either restoring a system restore point or reverting the provisioning package.
- **PowerShell alternative:** the same configuration can be scripted via PowerShell instead of the GUI tool.

## Featured Technology
- Windows Configuration Designer
- Windows 10 Assigned Access / Kiosk Mode
- PowerShell (as scripting alternative)

## Best Practices Highlighted
1. Create a system restore point (or otherwise plan a rollback path) before deploying a kiosk configuration, in case recovery is needed.
2. Clean up any kiosk-specific accounts created during setup once no longer needed.
3. Prefer PowerShell scripting for repeatable/automated kiosk deployments across multiple machines.

## Context / Positioning
This note addresses a deployment/operations concern (locking down client hardware) rather than a 4D language feature, aimed at 4D developers or integrators deploying point-of-sale or public terminal solutions on then-current Windows 10 (1709-era). It reflects the state of Microsoft's kiosk tooling at the time rather than any 4D-specific capability.

## Historical Commentary
**Status:** Partially superseded

This note is fundamentally about Microsoft's Windows kiosk configuration tooling rather than about 4D itself, so its accuracy tracks Windows' own evolution rather than 4D's Design-Mode-to-Project-Mode or ORDA transitions. Since 2018, Microsoft has continued to evolve its recommended approach to kiosk/locked-down device management — particularly for enterprise fleets, where Microsoft Intune and other MDM-based kiosk provisioning are now commonly recommended alongside or instead of the standalone Windows Configuration Designer workflow described here.

The core idea — pointing Windows' assigned-access kiosk shell at a 4D application executable — remains valid regardless of which specific Microsoft tool is used to configure it, so the note's central 4D-relevant guidance still holds even if some Windows Configuration Designer screens/steps have shifted in newer Windows releases.
