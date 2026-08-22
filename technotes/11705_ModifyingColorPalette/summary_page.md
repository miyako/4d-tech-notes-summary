# Tech Note 96-26: Modifying 4th Dimension's Color Palette

**Author:** Julie Pearson
**Published:** May 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11705
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_22-26_(MAY)/96-26_Mod_Color_Palette.exe

## Overview
This Tech Note explains how developers can change the colors displayed in 4D's interface — pictures, procedure editor tokens, layout editor objects — by editing the "pltt" (palette) resource embedded in the 4D or 4D Client application file, either to use non-default colors or to eliminate color-flashing at launch.

## Key Points
- **pltt resource 2000** controls picture field/variable colors, procedure editor token colors, and layout editor object colors.
- **Editing process (Mac):** open the 4D application in ResEdit, open pltt resource 2000, and double-click individual color entries to change them via the color wheel.
- **Critical caveat:** objects store only the palette *index* of a color, not the color itself, so changing an entry can unpredictably recolor every object using that index — caution advised.
- **Windows workaround:** because pltt data lives in the 4D.RSR file (the Windows equivalent of the Mac resource fork), developers had to move the .RSR file to a Mac using 4D Transporter, edit it in ResEdit, and transport it back.
- **Platform difference:** on Mac, 4D's logical color palette overrides the system's absolute palette while frontmost, causing visible flashing when switching apps; on Windows, 4D's colors are simply best-matched to whatever the OS provides, with no flash or override behavior.
- **Best-matching limitation:** if the display hardware/settings can't render a chosen color exactly, 4D substitutes the closest available color on both platforms.

## Featured Technology
- ResEdit (Apple's classic Mac OS resource editor)
- 4D's "pltt" color palette resource
- 4D Transporter (cross-platform resource file transfer utility)

## Historical Context
This entire technique is rooted in classic Mac OS's resource-fork architecture and 8-bit indexed color palettes — both long obsolete. ResEdit was retired with the transition away from classic Mac OS, and modern displays universally use 24/32-bit true color, eliminating both the palette-flash problem and the very concept of a shared, index-based application color palette that this note addresses. 4D Transporter, used here to shuttle a Windows resource file to a Mac for editing, is likewise not part of the modern 4D toolset. This note is now of purely historical interest, illustrating the resource-level customization techniques developers relied on in the mid-1990s.
