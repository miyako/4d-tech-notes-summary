# Tech Note 96-17: Some Common Problems Encountered When Using 4th Dimension on the Power Macintosh

**Author:** David Adams
**Published:** March 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=11697
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_16-20_(MAR)/96-17_PowerMac_Problems.exe

## Overview
This Tech Note is a troubleshooting roundup addressing several distinct problems 4D developers commonly ran into when using 4th Dimension on Power Macintosh hardware during the mid-1990s transition from 68K to native PowerPC code.

## Key Points
- **Type 11 errors:** usually caused by an application memory partition set too small; resolved by increasing the allocation via the Finder's Get Info dialog.
- **PowerPC vs. 68K memory needs:** native PowerPC (RISC) code generally requires more memory than 68K (CISC) code, so partition sizes tuned for 68K Macs often need to be increased when running natively on Power Macintosh hardware; specific recommended sizes are given.
- **WorldScript bug:** documents an international text-handling bug under WorldScript in certain configurations, with a workaround.
- **CommonGround Shortcut conflict:** flags a known instability-causing conflict between the CommonGround Shortcut system extension and 4th Dimension.
- **General extension conflicts:** describes the classic Mac OS troubleshooting technique of selectively disabling extensions to isolate a conflicting INIT.
- **Compiler memory formula:** provides a formula for correctly estimating the memory 4D's compiler needs when compiling larger applications on Power Macintosh hardware.

## Featured Technology
- Power Macintosh native (PowerPC) vs. 68K emulation
- Macintosh memory allocation (application/partition sizing)
- WorldScript text-handling
- System extension conflict diagnosis
- 4D Compiler memory-sizing formula

## Historical Context
Published March 1996, at the height of the Mac's transition from 68K to PowerPC processors, this note reflects the very real compatibility friction developers faced running an existing 68K-era application like 4th Dimension natively on new PowerPC hardware, within classic Mac OS's cooperative multitasking and manually-sized memory partition model.

## Historical Commentary
**Status:** Obsolete

Every mechanism this note addresses — Type 11 errors, manual memory partition sizing, WorldScript, and INIT/extension conflicts — belongs to classic Mac OS's memory and system architecture, which was completely replaced by Mac OS X's protected virtual memory model and modern macOS. The 68K-to-PowerPC transition itself has been obsolete for decades (having since been followed by transitions to Intel and then Apple Silicon), and 4D's compiler and memory management have been substantially modernized, removing the need for any of the specific fixes or formulas described here.

