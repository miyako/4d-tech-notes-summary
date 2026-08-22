# Tech Note 06-24: PictContainer Plug-in

**Author:** Thomas Maul, General Manager, 4D Germany
**Published:** June 16, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43420
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_22-26_(JUN)/06-24_PictContainer.zip

## Overview
This note introduces the PictContainer plug-in, which gives 4D 2004 developers an enhanced picture-display area supporting reading, writing, zooming, scroll bars, and drag-and-drop, built on native OS imaging APIs and shipped with full C source code plus a demo database.

## Key Points
- Uses Apple's QuickTime API on Mac OS (preinstalled, Apple's preferred image library at the time) and Microsoft's GDI+ API on Windows (preinstalled on XP/2003, DLL shippable for older systems).
- GDI+ was chosen over QuickTime on Windows partly for better handling of damaged pictures.
- Automatically shows/hides scroll bars based on picture size, available area, and zoom level.
- Supports drag-and-drop of pictures between the PictContainer area, 4D picture variables, fields, and 4D list boxes.
- Format support differs by platform: Mac OS reads all QuickTime formats (PICT, BMP, GIF, JPG, PNG, TIFF, Photoshop, etc.) but writes only to BMP/JPG/PNG/uncompressed TIFF (or Mac pictures); Windows reads BMP, GIF, JPG, PNG, TIFF, EMF, WMF, ICO and writes BMP, GIF, JPG, PNG, TIFF.
- Ships with full C source code and a demonstration database ("PictContainer.4DB") showing loading, zooming (100%/400%), and drag-and-drop between controls.
- Requires the 4D Pack plug-in to be installed for PictContainer to work on Windows.

## Featured Technology
- PictContainer plug-in
- QuickTime API (Mac OS picture handling)
- GDI+ API (Windows picture handling)
- Drag & Drop between 4D picture controls (fields, variables, list boxes)

## Historical Context
Published in June 2006 for 4D 2004, this note reflects an era when 4D's native picture-handling capability was limited enough to warrant a dedicated OS-native plug-in for interactive display features like zoom and drag-and-drop. It predates 4D v11's 2007 SQL engine, Project Mode (2018), and ORDA.

## Historical Commentary
**Status:** Obsolete

QuickTime has been discontinued by Apple for years, and GDI+ is a legacy Windows graphics API long since superseded by newer imaging frameworks, so this plug-in's core native dependencies are no longer viable as described. The general concept of a rich, interactive picture-container control with zoom, scrolling, and drag-and-drop remains relevant, but 4D's own native picture commands and objects have since been considerably expanded, reducing the need for a plug-in like this one.
