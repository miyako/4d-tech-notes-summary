# Tech Note 04-25: 4D GDIPlus_Image Plug-In that uses Microsoft Windows GDI+: Part I of II

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** June 24, 2004 | **Product/Version:** 4th Dimension v2003.3 | **Platform:** Win
**Page:** https://kb.4d.com/assetid=33063
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_21-25_(MAY)/04-25_4D_GDIPlus_Image.exe

## Overview
This Tech Note introduces GDIPlus_Image, a 4D plug-in created by Thomas Maul, General Manager of 4D Germany, that wraps Microsoft Windows' native GDI+ graphics API to give 4D applications the ability to open, display, and manipulate picture files in BMP, JPG, GIF, EMF, WMF, TIF, PNG, and ICO formats, plus rotate and re-save manipulated images in BMP, JPEG, GIF, TIF, and PNG without recompression loss. As Part I of a two-part series, it covers the new capabilities GDI+ itself brought to the table, explains the practical benefits of adopting the GDIPlus_Image plug-in over other approaches, and walks through the accompanying 4D GDIPlus_Image sample database, leaving installation and detailed command usage to Part II (TN 04-35). Because GDI+ is a Windows-native technology, both the plug-in and this note are explicitly scoped to the Windows platform, illustrating how 4D developers of this era relied on compiled, OS-specific plug-ins to reach native platform capabilities not yet built into 4D's cross-platform language. This note is aimed at Windows-focused 4D developers who need richer image manipulation (especially format conversion and lossless rotation) than 4D's native picture-handling commands offered at the time.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- The first half of a two-part guide introducing the GDIPlus_Image plug-in, created by 4D Germany, which uses Microsoft Windows' GDI+ to open, display, manipulate, rotate, and save images across many formats.

## Featured Technology
- GDIPlus_Image plug-in
- Microsoft Windows GDI+
- Image format conversion (BMP/JPG/GIF/EMF/WMF/TIF/PNG/ICO)

## Historical Context
**Status:** obsolete

This note introduces a third-party, Windows-only plug-in (GDIPlus_Image) built around Microsoft's GDI+ API for image format conversion and manipulation in 4D applications circa 2004; the plug-in itself is not part of any current 4D distribution and has not been maintained for modern 4D versions. 4D's own native picture-handling commands and supported formats have since expanded considerably, covering much of what this specialized plug-in once uniquely provided, which renders the plug-in and this introduction obsolete as practical guidance even though the plug-in architecture concept it demonstrates remains valid.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
