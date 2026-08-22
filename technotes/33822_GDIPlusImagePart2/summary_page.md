# Tech Note 04-35: 4D GDIPlus_Image Plug-In that uses Microsoft Windows GDI+: Part II of II

**Author:** Not specified in source (teaser page only; full PDF not recovered)
**Published:** September 2, 2004 | **Product/Version:** 4th Dimension v2004 | **Platform:** Win
**Page:** https://kb.4d.com/assetid=33822
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_31-35_(JUL)/04-35_4D_GDIPlus_Image_2.exe

## Overview
This Tech Note is Part II of a two-part series documenting the GDIPlus_Image plug-in, a third-party (4D Germany-authored) plug-in that wraps Microsoft Windows' GDI+ graphics API to let 4D applications open, display, manipulate, rotate, and save images in formats such as BMP, JPG, GIF, EMF, WMF, TIF, PNG, and ICO. Where Part I (TN 04-25) introduced the plug-in's features and the accompanying sample database, Part II focuses on the practical mechanics: installing the plug-in into a 4D 2004 application and using its exposed commands. Because GDI+ is a Windows-only native API, the plug-in and this note are explicitly platform-limited to Windows, reflecting a period when 4D developers frequently reached for compiled C plug-ins to access OS-native graphics capabilities not yet built into the 4D language itself. The note is part of 4D's regular Technical Note series distributed to registered developers, complete with downloadable Windows and Mac example packages (the Mac package likely containing only documentation given the Windows-specific nature of GDI+). As a plug-in-specific installation and command reference, its value was tightly coupled to the lifespan of the GDIPlus_Image plug-in itself rather than to core 4D language features.

## Key Points
- This summary is derived solely from the on-page teaser paragraph for this Tech Note; the full PDF content could not be recovered.
- The second half of a two-part guide covering installation and command usage of the community-authored GDIPlus_Image Windows plug-in.

## Featured Technology
- GDIPlus_Image plug-in
- Microsoft Windows GDI+
- Third-party 4D plug-in architecture

## Historical Context
**Status:** obsolete

This note documents installation and usage of GDIPlus_Image, a third-party Windows-only plug-in wrapping Microsoft's GDI+ API for image manipulation in 4D 2004; the plug-in itself was a product of its era and is not part of any current 4D distribution. 4D's built-in picture-handling capabilities (native picture variables, list box picture columns, and expanded PICTURE-related commands) have since absorbed most of the format conversion and manipulation needs this plug-in addressed, making the specific installation/plug-in approach obsolete even though the general idea of extending 4D via compiled plug-ins for OS-native graphics remains architecturally valid.

**Note on sourcing:** This Tech Note's content_source is `teaser_only` — only the short on-page teaser paragraph was available in this environment (the original full Tech Note PDF/archive could not be recovered), so this page intentionally does not go beyond what that teaser states.
