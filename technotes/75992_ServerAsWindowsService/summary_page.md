# Tech Note 10-02: Running 4D Server as a Service on Windows

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** January 15, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75992
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_01-04_(JAN)/10-02_Running_4D_Server_as_a_Service.pdf

## Proposition
This note explains why and how to run 4D Server as a Windows service — an unattended, auto-starting/stopping background process — including registration steps, OS-specific caveats, maintenance procedures, and handling of intermediate software/structure updates.

## Key Points
- A **Windows service** automatically starts/stops with the OS and requires no logged-in user, similar to a Unix daemon.
- Benefits include automatic startup/shutdown and configurable **recovery actions on failure**.
- Covers **registration** of 4D Server as a service, with specific caveats for **Windows XP, Server 2003, Vista/7, and Server 2008**.
- Explains maintenance via both the **Services Control Panel** and the **command line** (starting, stopping, unregistering).
- Addresses **intermediate updates**: upgrading the 4D Server software itself and updating the database structure while service-registered.
- Troubleshooting section covers unavailable 4D Service menu items and inability to interact with a running service.

## Featured Technology
- Windows Service registration for 4D Server
- Services Control Panel / command-line service management (sc.exe)
- OS-specific caveats (Windows XP, Server 2003, Vista/7, Server 2008)

## Best Practices Highlighted
1. Register 4D Server as a Windows service for unattended, always-on deployments rather than requiring a logged-in interactive session.
2. Plan carefully for intermediate 4D software or structure updates, since a running service complicates in-place upgrades.
3. Configure service failure-recovery actions so 4D Server restarts automatically after an unexpected crash.

## Context / Positioning
Published as a practical deployment guide for 4D Server administrators, addressing the operational reality of running 4D unattended on a range of Windows OS versions current at the time.

## Historical Commentary
**Status:** Partially Superseded

This note explains why and how to register 4D Server as a Windows service so it starts/stops automatically with the OS and runs without a logged-in user session, including per-OS caveats for Windows XP through Server 2008 and Vista/7, plus maintenance and intermediate-update guidance.

Running a database server as a Windows service is still standard practice today, and 4D still supports service-mode deployment, but the specific OS-version caveats (XP, Server 2003, early Vista) are obsolete since those operating systems are long past end-of-life; current 4D documentation targets modern Windows Server releases with updated service-registration guidance.
