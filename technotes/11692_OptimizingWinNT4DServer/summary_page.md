# Tech Note 96-10: Optimizing Windows NT for High-Performance with 4D Server

**Author:** Christopher Chapman
**Published:** February 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Win
**Page:** https://kb.4d.com/assetid=11692
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_06-10_(FEB)/96-10_Optimizing_NT.exe

## Overview
This Tech Note provides Windows NT tuning techniques for maximizing 4D Server performance, based on Microsoft's recommendations and ACI's own testing, with explicit disclaimers that results may vary and that changes should be tested carefully before use in production.

## Key Points
- **Use NTFS:** the NT File System is faster, more reliable, and supports NT's built-in security model compared to FAT or HPFS; running 4D Server, structure files, and data files on NTFS is one of the single most significant performance improvements available.
- **Pagefile sizing:** optimal pagefile size = physical RAM + 12 MB; with multiple physical hard drives, distribute pagefiles evenly across all drives **except** the one containing `/WINNT` (worked example: 24 MB RAM, 3 drives → 18 MB pagefile per non-system drive).
- **Compress the data file's directory** on an NTFS volume (roughly halves physical disk reads due to ~2:1 compression, at the cost of extra CPU/decompression overhead — the note suggests adding ~12 MHz CPU and 8 MB RAM headroom to compensate).
- **Launch 4D Server with REALTIME priority** via a batch file (`start /REALTIME 4DSERVER.EXE`) so NT gives it priority CPU time slices over other applications; no other application should run on the server machine concurrently for best results.
- **Minimize display overhead:** set the server's display to 640x480x256 colors to reduce rendering memory/CPU overhead (with the RAM-per-pixel-depth math spelled out).
- **Minimize desktop overhead:** use a blank/None screen saver, or simply turn the monitor off.

## Featured Technology
- Windows NT File System (NTFS)
- Windows NT pagefile/virtual memory configuration
- NTFS directory/file compression
- `REALTIME` process priority via batch file
- Windows NT display and desktop control panel configuration

## Historical Context
Published February 1996, this note reflects Windows NT server tuning practices from an era of megabyte-scale RAM (the worked pagefile example uses 24 MB total physical memory) and early NTFS adoption, when database administrators had to manually balance pagefiles across physical drives and hand-tune display settings to squeeze maximum throughput from comparatively modest server hardware.

## Historical Commentary
**Status:** Obsolete

The specific numeric guidance here (megabyte-scale pagefile formulas, 640x480 display recommendations, manual REALTIME batch launching) is entirely tied to 1996-era hardware and Windows NT's memory/process management, both of which have been superseded many times over by modern gigabyte-to-terabyte-scale systems, vastly more sophisticated automatic OS memory management, and current NT/Windows Server versions. NTFS itself has long since become the unquestioned default Windows filesystem, so the note's advocacy for it over FAT/HPFS no longer represents a live choice. The general instinct behind these tips — use a fast filesystem, prioritize the database server process, and avoid wasting resources on unnecessary display/desktop overhead — remains conceptually familiar, but none of the specific techniques are applicable to modern server deployments.

