# Tech Note: 4D GDIPlus_Image Plug-In that uses Microsoft Windows GDI+: Part I of II

- **Asset ID:** 33063
- **Tech Note #:** 04-25
- **Published:** June 24, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Win
- **Author:** Thang Nguyen (4D Technical Support); plug-in by Thomas Maul, General Manager, 4D Germany
- **Page URL:** https://kb.4d.com/assetid=33063
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_21-25_(MAY)/04-25_4D_GDIPlus_Image.hqx

## Overview

Part I of a two-part note introducing GDIPlus_Image, a Windows-only 4D plug-in built by Thomas Maul (4D Germany) around Microsoft's GDI+ graphics API, letting 4D open, display, convert, and manipulate pictures in BMP/JPG/GIF/EMF/WMF/TIF/PNG/ICO formats without requiring Apple QuickTime on Windows.

## Key Points

- GDI+ is Microsoft's successor to classic Windows GDI, adding gradient brushes, cardinal splines, independent path objects, matrix transformations, scalable regions, alpha blending, and multi-format image support (BMP, GIF, JPEG, Exif, PNG, TIFF, ICON, WMF, EMF).
- The plug-in's core benefit is removing the Windows-side dependency on Apple QuickTime for picture compression/conversion, since GDI+ is built into Windows XP and Windows 2003 Server (and can be added to earlier Windows versions via a redistributable DLL).
- The sample database's "Open Picture Document" screen lets users browse and load image files by type; a "Show Codec" screen lists available encoders/decoders using the same API Windows Explorer itself uses to preview pictures.
- "Picture Display Properties" exposes zoom (with Scale to Fit modes), scroll X/Y offsets, Start/End crop coordinates, interpolation quality (low/high/bicubic/bilinear), rotate/flip, and thumbnail generation, plus a full matrix transform panel (Clear all, Rotate, Scale, Translate, Shear) with append/pre-pend ordering.
- "Save Picture Document" converts and saves pictures into BMP/JPG/GIF/EMF/WMF/TIF/PNG/ICO, supporting rotation without recompression, adjustable JPEG compression rate, and TIFF color depth/compression settings.
- On Mac OS or in cross-platform applications, the note recommends continuing to use Apple QuickTime, since GDI/GDI+ are Windows-specific APIs from Microsoft.
- Part II (not covered in this note) was planned to document the plug-in's method-level API in more depth.

## Featured Technology

- GDIPlus_Image plug-in
- Microsoft Windows GDI+ graphics API
- Multi-format image conversion (BMP/JPG/GIF/EMF/WMF/TIF/PNG/ICO)
- Picture rotate/flip/zoom/crop/scroll display properties
- GDI+ matrix transformations (rotate/scale/translate/shear)
- Codec/decoder enumeration

## Historical Commentary

**Status:** Obsolete

This note (Part I of II) introduces a third-party, Windows-only plug-in built by 4D Germany's Thomas Maul around Microsoft's then-new GDI+ API, primarily to let 4D avoid requiring Apple QuickTime on Windows machines for image conversion and manipulation. The GDIPlus_Image plug-in itself was never part of 4D's core distribution and has not been maintained for modern 4D versions, so it is obsolete as practical guidance today. However, 4D's own native picture-handling commands (and the OS's built-in imaging frameworks) have since expanded to cover most of what this specialized plug-in once uniquely provided.

**References to newer/updated information:**
- 4D's built-in picture/image commands have grown substantially since 2004, reducing dependency on third-party image plug-ins for basic format conversion
- Modern 4D no longer depends on Apple QuickTime for Windows picture handling, which was the core problem this plug-in worked around
- The GDIPlus_Image plug-in was never incorporated into 4D's core product and is not available for current 4D versions
