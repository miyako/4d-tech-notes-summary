# Tech Note 08-31: Picture Management in 4D v11 SQL

**Author:** Luis Pineiros (Technical Services Team Member, 4D Inc.)  
**Published:** August 27, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=50901  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_28-31_(AUG)/08-31_Picture_Mgmnt.zip

## Overview

This Technical Note documents major enhancements to picture management in 4D v11.2, introducing native support for current picture formats available on Mac OS X and Windows. The release prioritizes preserving original image characteristics (transparency, gradients, color depth, etc.) without lossy conversion, and adds sophisticated picture transformation commands for scaling, cropping, flipping, and combining images. It also enhances the user interface with drag-and-drop picture import and contextual menu support.

## Key Points

**Native Format Support (Primary Innovation)**
- Previous versions of 4D converted all pictures to an intermediate format, losing transparency, gradients, antialiasing, and other native characteristics
- 4D v11.2 introduces native codec support for the picture formats currently available on Mac OS X and Windows
- Pictures retain their original format characteristics through all operations (storage, retrieval, transformation)
- Identical interface and behavior for picture fields and picture variables

**Supported Picture Formats & Codecs**
- **4D Picture (.4pct)** – 4D's native format
- **JPEG (.jpg, .jif, .jpeg, .jpe)** – Lossy compression
- **PNG (.png)** – Lossless with transparency
- **BMP/Paint Brush (.bmp, .dib, .rle)** – Windows bitmap
- **GIF (.gif)** – Limited color depth with transparency
- **Radiance** – High dynamic range imaging (Mac OS X only)
- **PDF (.pdf)** – Portable document format (Mac OS X only)
- **TIFF (.tif, .tiff)** – Tagged image format
- **EMF (.emf)** – Windows metafile (Windows only)
- **PICT (.pic, .pct, .pict)** – Legacy Macintosh format
- **SVG (.svg)** – Scalable vector graphics
- **Silicon Graphics (.sgi, .rgb)** – SGI format
- **Photoshop (.psd)** – Adobe format (limited support)
- **Mac Paint (.pntg, .pnt, .mac)** – Legacy Mac format
- **TGA (.targa, .tga)** – Truevision format
- **JPEG 2000 (.jp2)** – Next-generation JPEG
- **QuickTime (.qtif, .qti)** – Apple QuickTime format

**Codec ID Forms**
The PICTURE CODEC LIST command returns codec identifiers in three forms:
- Extension (e.g., `.gif`)
- MIME type (e.g., `image/jpeg`)
- 4-character QuickTime code (e.g., `PNTG`)

**Picture Transformation Commands**

- **SCALE:** Resize picture to specified width/height; handles aspect ratio preservation
- **CROP:** Extract rectangular region from picture; define left, top, width, height coordinates
- **FLIP HORIZONTALLY:** Mirror image left-to-right
- **FLIP VERTICALLY:** Mirror image top-to-bottom
- **FADE TO GREY SCALE:** Desaturate image to grayscale
- **COMBINE PICTURES:** Composite two pictures with positioning and opacity control; performs pixel-blending for overlays

**User Interface Enhancements**

- **Drag and Drop:** Users can drag picture files directly onto picture fields or variables to import; native 4D picture management used
- **Contextual Menus:** Right-click (Windows) or Control-click (Mac) on picture fields/variables to access: Cut, Copy, Paste, Clear, Import from file, Save to file, and display format options
- **Display Format Options:** Truncated (non-centered), Scaled to fit, Scaled to fit centered proportional
- **Scrollbars:** Optional horizontal and vertical scrollbars for truncated pictures; three settings: Yes (always visible), No (never visible), Automatic (visible when needed)

**Picture Storage Locations**
1. **Picture Fields:** Table fields with picture data type
2. **Picture Variables:** In-memory picture container variables
3. **Resources Folder:** External picture files referenced by application
4. **Static Image Objects:** Embedded pictures in form layouts
5. **Pictures Library:** Centralized picture repository

All storage locations benefit from native codec support and format preservation.

**Local Coordinates & Click Detection**
Picture fields and variables can track local coordinates of clicks, enabling precise control and interactive image-based UIs (e.g., clickable image maps).

## Featured Technology

- Native picture codec support (Mac OS X and Windows)
- Picture transformation commands (SCALE, CROP, FLIP, FADE, COMBINE)
- Picture CODEC LIST command
- Drag-and-drop picture import
- Contextual menu support for pictures
- Picture scrollbars
- Format preservation through operations
- Multi-location picture storage

## Historical Context

Published in August 2008, this note represents 4D's commitment to eliminating lossy intermediate format conversion and providing developers with powerful, native image manipulation capabilities. At the time, JPEG 2000 support, PDF picture support (Mac), and SVG support represented cutting-edge image format handling. The release coincided with increasing need for rich media in business applications and growing complexity of image-based UIs.

## Historical Commentary

**Status:** Still Relevant

The foundational concepts documented in this note—native format preservation, non-destructive transformations, and flexible picture storage—remain core to 4D's picture handling in all modern versions. The specific command names and codec list have evolved (modern 4D supports additional formats like WebP), but the architectural approach has proven durable. Web-based image processing (HTML5 canvas, SVG manipulation via JavaScript) provides additional options in modern applications, but 4D's native picture commands continue to be the primary tool for server-side image processing and database-resident picture management. 4D Write Pro (introduced 2016) and 4D View Pro (introduced 2018) provide enhanced document and spreadsheet capabilities that work alongside these core picture commands.
