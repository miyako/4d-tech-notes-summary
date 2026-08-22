# Tech Note 05-42: Scanning Text and BLOBs Efficiently or Testing Performance Meaningfully

**Author:** David Adams
**Published:** December 22, 2005 | **Product/Version:** 4D (2004.2) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41106
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-42_Scanning_Text_BLOBs.zip

## Overview
Using the concrete problem of scanning text/BLOB data character-by-character or byte-by-byte, this note teaches how to design, run, and correctly interpret meaningful performance benchmarks in 4th Dimension — as much a lesson in testing methodology as in raw optimization.

## Key Points
- Headline finding: scanning text through a pointer is ~710x slower (normalized) than scanning it directly, versus only ~4x for the equivalent BLOB case — illustrating how dramatically small implementation choices can matter.
- All benchmarks run compiled under 4th Dimension 2004.2, with results normalized to the fastest case rather than reported in absolute milliseconds.
- Reviews syntax differences: text is 1-based (`[[n]]` or `≤n≥` on Mac), BLOBs are 0-based (`{n}`).
- Explains why passing BLOBs by value costs contiguous memory allocation, while passing text by pointer triggers a severe, non-obvious performance cliff.
- Central lesson: ratio-based results ("4x slower") can be misleading without absolute-time context — a 2-second difference on a 1MB BLOB may be irrelevant for a background process but significant for a waiting user.
- Personal rule of thumb offered: pass text by value, pass BLOBs by pointer, as a sensible (not absolute) default.

## Featured Technology
- Text/BLOB character-by-character scanning
- Pass-by-value vs. pass-by-pointer parameter performance
- 4D compiled-mode benchmarking methodology

## Historical Context
The specific benchmark ratios are tied to the 4D 2004.2 compiler/runtime and are now obsolete after two decades of engine, memory-management, and hardware evolution — they should not be treated as accurate for current 4D versions. The methodological lesson, however — that raw performance ratios need real-world calibration before driving design decisions — remains genuinely useful and still-relevant advice for any performance engineering work today.
