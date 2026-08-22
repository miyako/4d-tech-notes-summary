# Tech Note 96-33: Creating a Program Item with a Custom Icon to Launch Your Executable File on Windows

**Author:** Julie Pearson
**Published:** August 1, 1996 | **Product/Version:** 4D Compiler v3.x | **Platform:** Windows
**Page:** https://kb.4d.com/assetid=11700
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_33-36_(AUG)/96-33_Customized_Icons.exe

## Overview
This Tech Note walks Windows developers through creating a custom-icon shortcut (Program Item / Start Menu entry) for an executable produced by merging a 4D Compiler Pro-compiled structure with 4D Engine, since the Windows merge process generates multiple files with a generic default icon rather than a single polished application as on the Macintosh.

## Key Points
- **The Windows merge output:** Customdb.EXE, Customdb.4DC, and Customdb.RSR are generated together in a Distrib folder — unlike the Mac's single stand-alone application.
- **Windows 95 steps:** add the EXE to the Start/Programs menu via Taskbar Properties → Start Menu Programs → Add/Browse, name it, then customize its icon via the shortcut's Properties → Shortcut tab → Change Icon.
- **Windows NT / 3.1x for Workgroups steps:** create a new Program Item in Program Manager, set its Description and Command Line to the EXE's full path, then use Change Icon (pointing to a custom .ico file or browsing PROGRAM.EXE/MOREICONS.DLL) to assign the icon.
- **Custom icon creation:** covered separately in Appendix B of the 4D Compiler Reference Manual.

## Featured Technology
- 4D Compiler Pro (merge with 4D Engine)
- Windows 95 Start Menu / Taskbar Properties
- Windows NT & Windows 3.1.x for Workgroups Program Manager

## Historical Context
This note is entirely bound to Windows 3.1/95/NT-era shell mechanics — Program Manager groups and the classic Windows 95 Taskbar Properties dialogs — none of which exist in any currently supported version of Windows. The underlying goal, giving a distributed 4D application a polished custom icon, remains a valid concern for developers today, but it is now handled directly within 4D's modern build/packaging tools (e.g. Build Application) rather than requiring manual OS shell configuration after the fact. The 4D Compiler Pro + 4D Engine merge workflow described here also reflects a build/deployment model that has been substantially modernized in current 4D releases.
