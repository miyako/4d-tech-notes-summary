# Tech Note 96-04: Removing Win32s

**Author:** Christopher Chapman
**Published:** January 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Win
**Page:** https://kb.4d.com/assetid=11687
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_01-05_(JAN)/96-04_Removing_Win32s.exe

## Overview
4D and 4D Server were Win32 applications that, under 16-bit Windows 3.1(1) and Windows for Workgroups, required a 32-bit compatibility/thunking layer called Win32s to run at all. When another application installed an incompatible or overwritten version of Win32s, 4D-related problems could occur that a simple product reinstall would not fix. This Tech Note documents how to manually and completely remove Win32s so a compatible version can be freshly installed.

## Key Points
1. Remove the `device=<Windows>\<System>\win32s\w32s.386` line from the `[386Enh]` section of `SYSTEM.INI`.
2. Change the `drivers=mmsystem.dll winm16.dll` line in the `[BOOT]` section of `SYSTEM.INI` to just `drivers=mmsystem.dll`.
3. Delete `W32SYS.DLL`, `WIN32S15.DLL`, and `WIN32S.INI` from the `<WINDOWS>\<SYSTEM>` directory.
4. Run `deltree <windows>\<system>\win32s` (e.g. `deltree c:\windows\system\win32s`) from the DOS command line to remove the remaining folder.
5. Reinstall the correct Win32s version simply by running the installer for 4D, 4D Client, or 4D Server.

## Featured Technology
- Win32s (32-bit compatibility/thunking layer for Windows 3.1/Windows for Workgroups)
- Manual `SYSTEM.INI` editing
- DOS `deltree` command

## Historical Context
Published in January 1996, this note documents a routine but necessary piece of Windows 3.1-era systems administration: because 16-bit Windows had no native 32-bit application support, every Win32 program (including 4D) depended on the shared Win32s layer, and conflicts between different applications' bundled Win32s versions were a recurring source of support tickets.

## Historical Commentary
**Status:** Obsolete

Win32s and the 16-bit Windows 3.1/Windows for Workgroups platforms it supported have been completely obsolete since the mid-to-late 1990s, superseded by the native 32-bit Windows 95/NT generation and everything since. No modern version of 4D requires or interacts with Win32s in any way, making this note purely of historical interest as a snapshot of mid-1990s Windows compatibility troubleshooting.

