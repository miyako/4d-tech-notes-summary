# Tech Note 99-31: Building Interactive Graphic Interfaces with 4D Draw, Part 1

**Author:** Tim Tonooka, ACI Technical Support
**Published:** July 1, 1999 | **Product/Version:** 4D Draw v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11876
**Download:** https://kb.4d.com/DLTN/TN/1999/Windows/TN_1999_27-31_(JUL)/99-31_Graphic_Interfaces_1.exe

## Overview
This is an extensive first installment in a multi-part series on creating interactive graphic interfaces using 4D Draw. It explains how to convert bitmap images into 4D Draw vector graphics and use those graphics as interactive UI elements—clickable shapes that can trigger database lookups, change colors programmatically, and serve as sophisticated data visualization tools.

## Key Points
- **Interactive graphic concept:** 4D Draw areas can function as interactive interfaces where irregularly-shaped vector objects act as buttons (e.g., states on a USA map)
- **v65Trace example database:** Features four main functions—Convert Picture to BMP, BMP Picture Properties (with pixel-level inspection), Trace BMP Picture (bitmap-to-vector conversion), and 4D Draw Window
- **BMP format choice:** BMP was selected for its simplicity and consistency; ACI_Pack's `AP Save BMP 8 bits` command ensures a specific, predictable format
- **Graphics format primer:** Detailed review of TIFF, PICT, WMF, EPS, JPEG, GIF, and BMP formats with pros/cons for each
- **4D Draw vs. 4D Chart:** Extensive comparison documenting 15+ advantages of 4D Draw for interactive interfaces, including object locking (DR LOCK), background layers, named objects (DR SET NAME), zoom control, handle suppression, and binding to fields
- **Multiple vector creation approaches:** Manual drawing, programmatic creation, importing existing documents, file conversion utilities, commercial tracing software (ArtLine, Adobe Streamline, CorelTrace, ScanVec Tracer), and 4D-native tracing
- **Bézier curve handling:** Explains how PICT-to-4D Draw conversion handles Bézier curves as smoothed polygons, and why 4D-native tracing avoids this issue

## Featured Technology
- 4D Draw (vector graphics plug-in with extensive programmatic control)
- ACI_Pack plug-in (`AP Read Picture File`, `AP Save BMP 8 bits`, `AP Save GIF`)
- BMP file format (Version 3, 8-bit color, no compression)
- PICT/QuickDraw graphics format
- 4D Chart (compared unfavorably for interactive use)
- BLOB operations for low-level file parsing
- 4D v6 resizable forms

## Historical Context
**Status:** Obsolete

This note is a fascinating artifact of 1999-era 4D development. 4D Draw, 4D Chart, and the ACI_Pack plug-in have all been discontinued. The PICT format and QuickDraw (referenced extensively) are deprecated Apple technologies. The commercial tracing software mentioned (ArtLine, Adobe Streamline, CorelTrace, ScanVec Tracer) are mostly discontinued or absorbed into other products. Modern 4D developers would use SVG support (built into 4D since v14), Web Areas with JavaScript/Canvas/SVG for interactive graphics, or external front-end frameworks. Despite its obsolescence, the note demonstrates remarkable ingenuity in building sophisticated interactive UIs within the constraints of late-1990s database tooling.
