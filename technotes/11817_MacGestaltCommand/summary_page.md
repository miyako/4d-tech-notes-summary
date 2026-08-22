# Tech Note 98-15: The Macintosh Gestalt Command

**Author:** Not specified
**Published:** October 1, 1998 | **Product/Version:** 4D | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11817

## Overview
This Tech Note documents 4th Dimension's support for the Mac OS Gestalt Manager, which enables runtime detection of installed hardware features and system services.

## Key Points
- The Gestalt Manager was created by Apple for standardized runtime feature detection.
- Allows 4D applications to determine available hardware features and system services.
- Essential for adapting application behavior to varying Mac OS configurations.
- Detects capabilities like processors, memory, QuickTime versions, networking features.
- Gives 4D developers direct access to system-level information.

## Featured Technology
- 4D
- Mac OS Gestalt Manager
- System feature/hardware detection
- Runtime environment querying

## Historical Context
**Status:** Obsolete

Apple deprecated and eventually removed the Gestalt Manager in modern macOS. Modern system feature detection uses entirely different Apple frameworks, and 4D provides its own platform detection mechanisms such as GET SYSTEM INFO. The full archive/PDF for this note could not be recovered (NO_DOWNLOAD_LINK_TEASER_ONLY).
