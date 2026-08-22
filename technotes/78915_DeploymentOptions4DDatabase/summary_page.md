# Tech Note 22-08: Deployment Options for a 4D Database

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 26, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78915
**Download:** https://kb.4d.com/DLTN/TN/2022/22-08_DeploymentOptions.pdf

## Proposition
4D databases can be deployed in multiple ways depending on availability, security, and administration needs; this note catalogs the tradeoffs of GUI, Windows Service, and headless deployment for developers choosing a production deployment strategy.

## Key Points
- **Three deployment models**: user-executed application (double-click, full GUI), Windows Service (Session 0, no GUI, auto-restart), and headless mode (CLI-launched, cross-platform, no GUI).
- **CLI flags for headless mode**: `--args`, `--structure`, `--data`, and `--headless` control structure/data selection and headless behavior.
- **Output streaming**: LOG EVENT with the 'Into system standard outputs' selector routes messages to stdout/stderr, redirectable to log files with shell operators.
- **Windows Service Startup Types**: Automatic, Automatic (Delayed Start), Manual, and Disabled each have different reboot/dependency behavior.
- **Remote Administration window access**: still available via a connected 4D Remote client's Help menu even when the server has no local GUI.
- **Two-way vs. one-way admin interactions**: toggling servers/processes vs. read-only monitoring (memory, uptime, logs, email alerts).
- **Headless mode auto-handles GUI-dependent events** (e.g., cancels debugger prompts, auto-restarts after merged-app updates) by logging and taking default actions.

## Featured Technology
- 4D Server
- Windows Services
- Headless mode
- LOG EVENT (stdout/stderr)
- Administration window

## Best Practices Highlighted
1. Use headless mode for CI/automated/server environments needing cross-platform behavior without a GUI.
2. Use Windows Services when native OS-level auto-restart-on-boot is the priority and the platform is Windows-only.
3. Route headless-mode stdout/stderr to log files for later troubleshooting since there is no interactive console.

## Context / Positioning
This note reflects 4D's continued investment in server-grade, DevOps-friendly deployment (headless mode, CLI control, log streaming) alongside its traditional desktop-app roots, aligning with the broader industry shift toward containerized/scripted application deployment.

## Historical Commentary
**Status:** Still Relevant

Headless mode has only become more emphasized in subsequent 4D releases and is the standard approach for Docker/CI deployments of 4D Server today; nothing in this note is deprecated. The Windows Service option remains valid but headless mode is now generally preferred for new deployments due to its cross-platform nature. This is a durable operations reference with no significant API changes since publication.
