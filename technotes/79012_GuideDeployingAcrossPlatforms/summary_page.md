# Tech Note 22-18: Guide to Deploying Across Platforms

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** September 26, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79012
**Download:** https://kb.4d.com/DLTN/TN/2022/22-18_DeplyingAcrossPlatforms.pdf

## Proposition
Deploying 4D client-server apps across mixed OS/CPU combinations (Windows/macOS, Intel/Apple Silicon) requires specific build and automatic-update handling per scenario. This note documents four concrete deployment scenarios with step-by-step build, transfer, and update instructions for each.

## Key Points
- **A client-server app must be built at least once on each targeted platform** — you cannot deploy a Mac-built client to run against a Windows-built server without building each side natively.
- **Apple Silicon Macs need Rosetta to run Intel-compiled apps**, toggled via Get Info > Open using Rosetta, unless the app was built from a project-mode database with an 'All processors' compilation target.
- **Project mode on Mac can natively compile universal (Intel + Apple Silicon) binaries**; Windows hosts can only ever compile for Intel.
- **Automatic client updates require incrementing 'Current version'** (or the CurrentVers key in buildApp.4DSettings) and enabling the platform-specific 'Allow automatic update' checkbox.
- **Cross-platform updates require transferring platform-specific build artifacts** — the opposite platform's 4D Volume Desktop folder, or a .4darchive file plus a Compiled Database folder.
- **Windows server → Mac clients is the most involved scenario**, requiring 4D 19 R3+'s 'Allow connection of Silicon macOS clients' option and a Compiled Database folder generated on an actual M1 Mac, since Windows can't natively produce Apple Silicon code.

## Featured Technology
- 4D Server / 4D Volume Desktop merged deployment
- Automatic client update (.4darchive)
- Apple Silicon (M1) vs Intel builds & Rosetta
- Project mode compilation targets (All processors)
- BUILD APPLICATION / buildApp.4DSettings

## Best Practices Highlighted
1. Always build and test the client-server app on every target platform at least once before relying on automatic updates for subsequent releases.
2. Convert to project mode with an 'All processors' compilation target to avoid needing Rosetta at all on Apple Silicon Macs going forward.

## Context / Positioning
Published under 4D v19 (September 2022), during the industry-wide Intel-to-Apple-Silicon transition, this note captures a specific, time-bound engineering challenge: keeping 4D's cross-platform client-server deployment and automatic-update model working smoothly across two CPU architectures at once.

## Historical Commentary
**Status:** partially superseded

The cross-OS deployment mechanics (build-per-platform, .4darchive-based automatic updates) remain current 4D practice, but the Apple Silicon/Rosetta-specific guidance is a transitional-era concern that is steadily becoming less relevant: Intel Macs are increasingly rare in the field, 4D's project-mode 'All processors' universal builds have matured, and the industry-wide Intel-to-Apple-Silicon migration that motivated much of this note is now largely complete. Developers deploying today are far more likely to be dealing purely with Apple Silicon Macs and can often skip the Rosetta-specific steps entirely, though the Windows-server-to-Mac-client Compiled Database folder requirement may still apply for organizations building exclusively on Windows.
