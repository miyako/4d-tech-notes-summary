# Tech Note: Colors, Palettes, 4D 3.x.x and 4D V6

**Author:** Not specified
**Published:** October 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11784
**Download:** Not available (no working download link archived — teaser only)

## Overview
This note documents the conversion of 4th Dimension 3.x.x databases with customized color palettes to version 6.0, explaining a fundamental change in how 4D handled color on Macintosh starting with V6: dropping the 256-color 'pltt' palette resource restriction in favor of full 24-bit color.

## Key Points
- Aimed at developers writing 4D extensions/plugins that deal with customized colors and palettes.
- Starting with 4D 6.0, Macintosh colors are no longer restricted to the 256 simultaneous colors of a 'pltt' resource.
- Pictures pasted from other graphical applications with custom color tables now display with their actual colors instead of the nearest 'pltt' approximation.
- 4th Dimension no longer installs the 'pltt' resource or calls the Mac OS `SetPalette` routine.
- All objects now store colors as 24-bit `$RRGGBB` values instead of indexes into a 'pltt' resource.
- The 'pltt' resource (still present for color menus) can now be freely customized since it only affects UI, not stored object colors.
- Caveat: colors are still approximated if the monitor/video card is limited to 256 colors or less, or if a 4D extension itself sets a palette on a window.

## Featured Technology
- Macintosh 'pltt' color palette resource
- 24-bit `$RRGGBB` color storage model
- Mac OS `SetPalette` routine
- 4D extension/plugin color handling

## Historical Context
Published October 1997 alongside 4D V6, this note is entirely tied to classic Mac OS's resource-based, indexed-color display model (System 7/8 era), which was rendered obsolete once Mac OS X introduced a modern, universally 24-bit+ graphics and color model. The specific 'pltt' resource mechanics, SetPalette calls, and 256-color limitations described here have no bearing on current 4D or modern operating systems, making this note of purely historical interest for understanding how far back 4D's cross-platform color handling had to accommodate legacy hardware and OS limitations.
