# Tech Note 96-30: Tips and Techniques for Optimizing the Memory Allocated to 4th Dimension

**Author:** Julie Pearson
**Published:** June 1, 1996 | **Product/Version:** 4D Server v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11709
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_27-30_(JUN)/96-30_Optimizing_Memory.exe

## Overview
This Tech Note explains how to allocate and fine-tune the memory used by 4th Dimension, 4D Server, and 4D Client on both Windows and Macintosh, plus PowerMac-specific performance tips and a precise MacsBug-based technique for measuring 4D Server's actual kernel memory consumption.

## Key Points
- **Windows configuration:** all memory settings (Stack size, Permanent off-screen buffer, Cache memory, kernel block count/size) are configured via 4D Customizer Plus's Preferences resource dialog, since Windows has no Finder-level memory partition concept.
- **Macintosh configuration:** total memory is set at the Finder via Get Info; the cache-vs-kernel percentage split is then configured separately via Customizer Plus's Memory resource. 4D Server can typically afford a higher cache percentage than 4th Dimension since it lacks UI-management overhead.
- **PowerMac/PCI Mac tuning tips:** add a Level II cache card, enable the native PowerPC ("Modern") Memory Manager, prefer real RAM over virtual memory, set disk cache to 1/16th of physical RAM, and consider Speed Doubler for I/O performance.
- **MacsBug load-testing technique:** simulate maximum production load (max clients, max named selections, max processes, ~90% of records selected per file), then compare "Heap Totaling" (HT) reports taken via MacsBug before and after to precisely measure kernel memory consumption and tune the cache/kernel split accordingly.

## Featured Technology
- 4D Customizer Plus (memory/preferences resource editing)
- Classic Mac OS Finder-level memory partitioning (Get Info)
- MacsBug (low-level Macintosh debugger)

## Historical Context
This note documents 4D's mid-1990s manual, fixed-partition memory model — a world where developers had to hand-configure a specific memory allocation for the application and manually balance cache vs. kernel memory splits. That entire model is obsolete: modern operating systems (including current macOS) use dynamic virtual memory management, and current 4D versions handle memory allocation automatically without requiring Finder-level partition sizing or manual kernel/cache tuning. 4D Customizer Plus and MacsBug, the two tools central to this note, are no longer part of the 4D or Macintosh development toolchain, and the PowerPC-specific hardware advice (Level II cache cards, Speed Doubler) has no bearing on any current hardware architecture.
