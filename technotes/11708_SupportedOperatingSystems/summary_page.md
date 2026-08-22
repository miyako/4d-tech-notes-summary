# Tech Note 96-29: Operating Systems Supported by 4D and 4D Server

**Author:** Walt Nelson
**Published:** June 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11708
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_27-30_(JUN)/96-29_Operating_Systems.exe

## Overview
This Tech Note gives developers a broad, comparative overview of the five operating systems 4th Dimension supported in mid-1996 — Mac OS, Windows 3.1x, Windows for Workgroups 3.11, Windows 95, and Windows NT 3.5x — including hardware requirements, stability, and platform recommendations.

## Key Points
- **Mac OS:** ease-of-use and built-in networking leader, but a minority player in corporate America; slowest disk access of the group.
- **Windows 3.1x (with Win32s):** largest installed base but frequent General Protection Faults (GPFs) requiring reboots; no built-in networking.
- **Windows for Workgroups 3.11:** adds faster disk access and peer-to-peer networking over Windows 3.1x.
- **Windows 95:** addresses many Win 3.1x stability/memory issues, positioned as a stepping stone toward Windows NT.
- **Windows NT 3.5x:** most robust option with protected memory (no reboot after app crash); recommended for both 4D development and 4D Server hosting, despite higher cost and somewhat slower relative speed.
- **Comparison table:** RAM/disk requirements and pros/cons tabulated for each OS.
- **Cross-cutting comparisons:** software compatibility, hardware compatibility (Mac's single-vendor standard vs. fragmented Windows/Intel hardware), crash behavior, and disk access speed.
- **Recommendations:** Windows NT Workstation for development/server hosting, minimum 75MHz Pentium / 100MHz PowerMac, and practical 1996-era hard disk sizing/SCSI-vs-IDE guidance.

## Featured Technology
- Mac OS (System 7.5.x)
- Windows 3.1x / Windows for Workgroups 3.11 with Win32s
- Windows 95
- Windows NT 3.5x

## Historical Context
Every operating system discussed in this note — Windows 3.1x, Windows for Workgroups, Windows 95, Windows NT 3.5x, and the referenced classic Mac OS 7.5.x — has been fully discontinued for decades and is unsupported by any current software, including modern 4D. Win32s, the compatibility layer required to run 4D at all on 16-bit Windows 3.1x, is likewise entirely obsolete. The note is now a historical snapshot of PC and Mac computing circa 1996 — informative about the era's tradeoffs (dial-up-adjacent hardware economics, GPF-prone 16-bit Windows, single-vendor Mac hardware) but with no direct applicability to any operating system 4D runs on today.
