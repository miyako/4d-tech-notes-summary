# Tech Note: 4D GDIPlus_Image Plug-In that uses Microsoft Windows GDI+: Part II of II

- **Asset ID:** 33822
- **Tech Note #:** 04-35
- **Published:** September 2, 2004
- **Product / Version:** 4th Dimension 2004
- **Platform:** Win
- **Author:** Thang Nguyen (Technical Support, 4D Inc.); plug-in and content provided by Thomas Maul, 4D Germany
- **Page URL:** https://kb.4d.com/assetid=33822
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_31-35_(JUL)/04-35_4D_GDIPlus_Image_2.hqx

## Overview

Written by Thang Nguyen with plug-in and content contributed by Thomas Maul (4D Germany), this is Part II of a two-part note (following #33063) covering the Windows-only GDIPlus_Image plug-in, which wraps Microsoft's GDI+ API to give 4D advanced image-manipulation features such as gradient brushes, alpha blending, and multi-format image support. Part II focuses on plug-in installation -- placing the plug-in in the WIN4DX folder next to the structure file or application, and, on older Windows systems lacking GDI+, downloading and installing Microsoft's separate GDI+ DLL redistributable -- and then documents each of the plug-in's 14 commands with parameter specs and sample code drawn from the demo database. Covered commands include GDI_LoadPictureFile and GDI_SavePictureFile (with JPEG/TIFF-specific transform, compression, and color-depth options), GDI_GetPictureProperties/GDI_SetDisplayProperties/GDI_GetDisplayProperties for reading and controlling resolution, size, zoom, scroll offset, and crop bounds, GDI_SetDisplayMode for interpolation quality and rotate/flip transforms, and GDI_SetActiveFrame paired with an ON TIMER-driven loop to play back animated GIF frames.

## Key Points

- Installation requires placing the plug-in in the WIN4DX folder next to the structure file/application; pre-XP/2003 systems additionally need Microsoft's separate GDI+ DLL redistributable.
- GDI_LoadPictureFile(Area;Path) loads an image into a plug-in area and returns 0 on success or a GDI+ error code otherwise.
- GDI_SavePictureFile(Area;Path;Format;{Option1;Option2}) saves in multiple formats, with Option1/Option2 controlling JPEG rotate/flip-during-save and compression level, or TIFF compression scheme and color depth.
- GDI_GetPictureProperties returns resolution, pixel dimensions, format GUID, and (for animated GIFs) frame count and per-frame delay time in milliseconds.
- GDI_SetDisplayProperties/GDI_GetDisplayProperties control zoom percentage, scroll offset, and crop start/end coordinates, with named constants like GDI_ScaledToFit and GDI_ReduceToFitPropCentered for common scaling behaviors.
- GDI_SetDisplayMode(Area;Interpolation;Rotate) applies interpolation quality (nearest-neighbor through high-quality bicubic) and rotate/flip transforms via documented numeric constants.
- GDI_SetActiveFrame combined with GDI_GetPictureProperties' frame count/delay output and an ON TIMER form event drives animated GIF playback frame by frame.

## Featured Technology

- GDIPlus_Image third-party plug-in
- Microsoft Windows GDI+ API
- GDI_LoadPictureFile / GDI_SavePictureFile commands
- GDI_GetPictureProperties / GDI_SetDisplayProperties / GDI_GetDisplayProperties
- GDI_SetDisplayMode (interpolation and rotate/flip constants)
- GDI_SetActiveFrame for animated GIF playback

## Historical Commentary

**Status:** Obsolete

This note documents a third-party, Windows-only plug-in that wrapped Microsoft GDI+ to give 4D 2004 image manipulation capabilities -- gradient brushes, JPEG/TIFF encoder options, animated GIF playback -- well beyond 4D's native picture handling of the time. The GDIPlus_Image plug-in itself is not part of any current 4D distribution, and 4D's built-in picture-handling commands and list box picture support have since absorbed most everyday format-conversion and manipulation needs, making this specific plug-in and its GDI_-prefixed commands obsolete, though the general pattern of extending 4D via a compiled plug-in for OS-native graphics APIs remains architecturally valid.

**References to newer/updated information:**
- The GDIPlus_Image plug-in and its GDI_-prefixed commands are not part of current 4D distributions
- 4D's native picture-handling commands and supported formats have expanded substantially since 2004, reducing reliance on third-party image plug-ins
- 4D's compiled plug-in API itself has since evolved (Unicode, universal binary, 64-bit support) since 4D v11 SQL, changing how any equivalent plug-in would be built today
