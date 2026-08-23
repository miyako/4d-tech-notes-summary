# Tech Note: Addendum GDIPlus PlugIn Version 1.1

- **Asset ID:** 36094
- **Tech Note #:** 05-06
- **Published:** February 10, 2005
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Thomas Maul
- **Page URL:** https://kb.4d.com/assetid=36094
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_05-11_(FEB)/05-06_GDIPlus_Addendum_1.1.hqx

## Overview

Thomas Maul (General Manager, 4D Germany) documents version 1.1 of the GDIPlus plug-in — a Windows-focused plug-in exposing Microsoft's GDI+ picture engine to 4D — covering its adoption of 4D 2004's new bundle-based plug-in architecture, new scrollbar and mouse-wheel support, and a new GDI_GetPictureBlob command for efficient thumbnail generation.

## Key Points

- GDIPlus 1.1 adopts 4D 2004's new bundle-format Plug-In Architecture while remaining compatible with 4D 2003; ships with a Mac OS X stub so the plug-in is visible cross-platform, though GDI+ features remain Windows-only.
- Installation: place the bundle in 4D 2004's new PlugIns folder; for 4D 2003, copy GDIPlus.bundle/Contents/Windows into Win4DX (and the full bundle into Mac4DX for the OS X stub).
- The plug-in area now automatically shows scrollbars when a picture is larger than the visible area (4D 2003+ only); two new optional GDI_SetDisplayMode(Area; Interpolation; Rotate; HorScrollbar; VerScrollbar) parameters (1=show, 2=hide, -1=leave unchanged) control this explicitly.
- Mouse wheel scrolling is now automatically supported in both the plug-in area and external GDI+ windows.
- New command GDI_GetPictureBlob(Area; Format) → theBlob retrieves the currently displayed picture as a blob in a specified format, intended for efficiently building thumbnail grids (e.g. in a List Box) without keeping large source pictures fully loaded in 4D memory.
- Recommended thumbnail workflow: GDI_LoadPictureFile → GDI_ConvertToThumbnail → GDI_GetPictureBlob, then convert the blob to a 4D picture with 4D Pack's AP Read Picture Blob (BMP format avoids needing QuickTime).
- Also includes faster redraw performance for very large pictures and general bug fixes addressing bad redraws and scrollbar-calculation issues.

## Featured Technology

- GDIPlus plug-in (Windows GDI+ picture rendering for 4D)
- 4D 2004 Plug-In Architecture (bundle format) with 4D 2003 compatibility
- GDI_SetDisplayMode with new scrollbar-control parameters
- GDI_GetPictureBlob command
- 4D Pack AP Read Picture Blob for blob-to-4D-picture conversion
- Mouse wheel support in plug-in areas and external windows

## Historical Commentary

**Status:** Obsolete

Thomas Maul (General Manager, 4D Germany) documents version 1.1 of the GDIPlus plug-in, a Windows-only plug-in exposing Microsoft's GDI+ picture-rendering engine to 4D, adding scrollbar and mouse-wheel support, a new GDI_GetPictureBlob command for building thumbnail grids without keeping full pictures in memory, and adoption of 4D 2004's new bundle-based plug-in architecture while staying 4D 2003-compatible. As a third-party Windows-specific plug-in addendum for a very old 4D plug-in architecture, this note is squarely of historical interest: GDI+ itself, the specific plug-in, and its bundle-installation instructions for 4D 2003/2004 are all long superseded by native 4D picture handling and cross-platform picture commands introduced in later 4D versions.

References to newer/updated information:

- The GDIPlus plug-in was tied to the Windows-only GDI+ engine and the 4D 2003/2004-era plug-in architecture; it is not part of current 4D
- Modern 4D includes far more extensive native, cross-platform picture-handling commands (scaling, thumbnails, blob conversion), reducing reliance on a third-party GDI+ plug-in like this one
