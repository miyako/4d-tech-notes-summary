# Tech Note 96-52: Configuring Your System for 4D and 4D Server/Client on the Macintosh Platform

**Author:** Jay H. Burgherr
**Published:** December 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=11726
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_51-56_(DEC)/96-52_SysConfig.exe

## Overview
This Technical Note addresses how to configure and maintain a stable Macintosh system for running 4D, 4D Server, and 4D Client as Apple's newer, faster PCI-based Power Macintosh hardware became common, focusing heavily on Apple's Open Transport networking stack and a notorious class of "Type 11" crashes.

## Key Points
- **What is Open Transport:** Apple's modern (for the time) networking stack replacing MacTCP/"Classic Networking," enabling simultaneous multi-protocol communication (e.g., AppleTalk + TCP/IP), switchable saved configurations, support on Power PC/68030/68040 Macs, and mandatory use on PCI-bus Macs; faster than MacTCP.
- **Type 11 errors:** The single most frequent Technical Support complaint after PCI Mac upgrades or Open Transport adoption; 4D, Server, and Client were among the first commercial apps built Open Transport-native, and ACI worked with Apple to resolve early compatibility issues.
- **Recommended tested configuration:** 4th Dimension 3.5.3+, 4D Server/Client 1.5.3+, 4D Network components 1.5.3+, Mac OS 7.5.3 Revision 2+, Open Transport 1.1.1+; caution against jumping to "the latest" OS version without similar vetting.
- **System install options:** (1) full hard-drive reformat and fresh System 7.5.3+ install, or (2) lower-risk "Verify and Repair" using Disk First Aid and Apple Drive Setup, both followed by installing Open Transport.
- **Open Transport 1.1.1 install procedure:** back up data, read the ReadMe, record existing MacTCP settings, run the installer, use the Network Software Selector to pick Open Transport on non-PCI Macs, then reconfigure AppleTalk, TCP/IP, and MacIPX control panels.

## Featured Technology
- Open Transport (Apple networking stack)
- MacTCP
- 4D / 4D Server / 4D Client version compatibility
- Classic Mac OS System 7.5.3 installation
- AppleTalk networking

## Historical Context
**Status:** Obsolete

This note is a hardware/OS compatibility and networking-stack configuration guide entirely specific to classic Mac OS, 1996-era PCI Power Macintosh hardware, and Apple's now-defunct Open Transport/MacTCP networking stacks. Classic Mac OS and Open Transport were fully superseded by Mac OS X starting in 2001, which uses a completely different, POSIX-based networking architecture with no equivalent "Type 11" error class. AppleTalk itself was discontinued by Apple in the 2000s. None of the specific version-compatibility guidance or installation steps in this note apply to any current 4D or macOS setup, though the note's broader caution about verifying compatibility before adopting new OS releases remains generally sound advice for any software environment.
