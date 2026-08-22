# Tech Note 96-56: Launching Multiple Instances of 4D Server Automatically on Macintosh and Windows

**Author:** Fred Johnson
**Published:** December 1, 1996 | **Product/Version:** 4D Server v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11727
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_51-56_(DEC)/96-56_Multiple.exe

## Overview
This Technical Note explains how to configure multiple instances of 4D Server, each paired to its own database, so they launch automatically when a Macintosh or Windows machine boots — a "turnkey" solution for database administrators. It assumes the reader already knows how to set up multiple 4D Server instances using TCP/IP and/or IPX (with an appendix provided for that background).

## Key Points
- **Macintosh:** Use ResEdit to assign a unique Creator code (4D>A, 4D>B, 4D>C, etc.) to each instance's Server application, Structure file, and Datafile so they pair correctly; place aliases of each structure file in the Startup Items folder to auto-launch on boot.
- **Macintosh troubleshooting:** "File not found" errors are resolved by re-checking Creator code consistency and alias targets (must alias the Structure file, not the Datafile).
- **Windows:** Rename each 4D Server executable (e.g., 4dServ1.exe, 4dServ2.exe), write a dedicated .bat file per instance pointing to its executable and structure file, and add shortcuts to those .bat files in the Startup folder (Windows NT via Program Manager Startup group; Windows 95 via Start Menu Programs/Taskbar Properties).
- **Appendix — TCP/IP and IPX multi-instance addressing:** AppleTalk's ADSP could broadcast multiple simultaneous server instances natively, but TCP/IP and IPX/SPX addresses identify only the machine, not individual server processes; 4D Server 1.5.x added a Port Number parameter (set via 4D Customizer Plus editing the TCP.OPT/IPX.OPT file) to distinguish instances.
- **Client connection:** Because multiple TCP/IP or IPX instances aren't auto-discoverable via the connection Browser, 4D Client users must "hard code" the server address plus port number to reach a specific instance.
- **Troubleshooting instance visibility:** Seeing only one instance over TCP/IP or IPX is expected (not a misconfiguration), since only ADSP supports multi-instance broadcast.

## Featured Technology
- 4D Server
- ResEdit
- TCP/IP and IPX/SPX multi-instance addressing (port numbers)
- Windows Startup folder / .bat launch scripts
- AppleTalk (ADSP) multi-server broadcast

## Historical Context
**Status:** Obsolete

This note is a system-administration guide entirely tied to classic Mac OS tooling and mid-1990s networking protocols. ResEdit and Creator-code-based file association vanished along with classic Mac OS when Mac OS X arrived in 2001. IPX/SPX networking was phased out industry-wide well over two decades ago in favor of universal TCP/IP, and AppleTalk itself was discontinued by Apple in the 2000s. Startup Items aliases (Mac) and .bat files placed in a Startup folder (Windows) have likewise been replaced by dedicated OS service-management facilities (e.g., launchd on macOS, Windows Services) for auto-launching background server processes. The underlying administrative goal — running multiple independently addressable server instances on a single host — remains a standard and relevant concept in IT operations today, just solved with entirely different, more robust tooling.
