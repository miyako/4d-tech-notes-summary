# Tech Note 96-38: Developing with 4D Server Part 1: Advantages of 4D Server Multi-User Development

**Author:** Walt Nelson
**Published:** September 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11717
**Download:** https://kb.4d.com/DLTN/TN/1996/MacOS/TN_1996_37-41_(SEP)/96-38_Server_Pt_1.hqx

## Overview
Part 1 of a three-part series, this note argues for centralized, server-based 4D development (4D Client connected to 4D Server) over traditional single-user local development, weighing disadvantages against advantages.

## Key Points
- **Pain points of single-user dev:** version-mismatch confusion between home/office copies, Mac/Windows font rendering differences, manual code-merge headaches, and inconsistent cross-platform documentation screenshots.
- **Disadvantages of Server development:** need for a server machine and licenses (modest hardware suffices); ~10x slower sign-on over remote connections (though local-speed once objects are copied down); distracting Structure Window refresh flashing; compiling requires remote-control software (Timbuktu Remote recommended) to run 4D Compiler at full speed on the server.
- **Simplicity:** one "Current Development Version" folder on the Server eliminates version confusion across locations.
- **Hard drive space:** avoids redundant large data files across multiple local machines.
- **Realistic performance measurement:** testing over a remote connection approximates real-world customer conditions better than testing on a fast local developer machine.
- **Multi-platform testing:** immediate cross-platform verification via connected Mac and Windows clients, without manual structure transport.
- **Multi-programmer development:** the biggest advantage — one shared code base, with object locking, code-respect discipline, and a keyboard/mouse trick for recovering off-screen window title bars across platforms.
- **Shared documentation:** using 4D Write lets developers combine Mac and Windows screenshots in one shared document.
- Previews Part 2 (multi-developer password system) and Part 3 (naming conventions).

## Featured Technology
- 4D Server / 4D Client multi-developer workflow
- 4D Compiler
- Timbuktu Remote (remote control software)
- 4D Write

## Historical Context
**Status:** Still relevant

The core argument for centralized, server-based multi-developer workflows over local single-user development remains broadly sound: eliminating version confusion, enabling realistic performance testing, and supporting concurrent multi-programmer and multi-platform development are all still valid engineering goals. What has changed: Timbuktu Remote, the remote-control tool recommended for compiling on a remote server, was discontinued years ago in favor of modern remote administration tools; centralized version control systems like Git have since become the dominant solution to the "which copy is current" problem this note addresses via a shared 4D Server folder; and 4D Write, the documentation vehicle mentioned, was replaced by 4D Write Pro in 2016.
