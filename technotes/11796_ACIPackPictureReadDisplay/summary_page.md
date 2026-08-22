# Tech Note: Using ACI_PACK to read and display pictures

**Author:** Not specified
**Published:** March 1, 1998 | **Product/Version:** ACI Pack v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11796

## Overview
This Tech Note explains how to use ACI_PACK plug-in commands in combination with native 4D routines to read, display, and export pictures in multiple image formats. The routines discussed are extracted from the Pixys example database that accompanied the note.

## Key Points
- **ACI_PACK picture commands covered:** AP Get Picture Type, AP Read Picture Blob, AP Set Picture Mode, AP Read Picture File, AP Save BMP 8 Bits, AP Save GIF.
- **Native 4D routines covered:** SAVE PICTURE TO FILE, COMPRESS PICTURE.
- **Export formats supported:** PICT, BMP, JPEG, GIF.
- **Read formats supported:** PICT, JPEG, GIF, BMP, and (Windows only) WMF, EMF.
- **Bonus:** .snd and .wav file types are also interpreted on Windows.
- **Includes:** Pixys example database demonstrating all routines.

## Featured Technology
- ACI_PACK plug-in (AP-prefixed picture commands)
- 4D v6 picture and blob handling
- Cross-platform image format support (Mac PICT, Windows BMP/WMF/EMF, JPEG, GIF)

## Historical Context
**Status:** Obsolete

ACI_PACK was a key productivity plug-in in the 4D v6 era, extending 4D's built-in capabilities for picture manipulation, file I/O, and other utility tasks. The specific AP-prefixed commands documented here have been entirely superseded by native 4D picture commands (READ PICTURE FILE, WRITE PICTURE FILE, CONVERT PICTURE, PICTURE CODEC LIST, etc.) introduced and expanded through 4D v11 and later. The PICT format itself was deprecated by Apple and is no longer supported. Modern 4D handles PNG, JPEG, SVG, and other contemporary formats natively without any plug-in.

The full PDF and accompanying Pixys example database could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
