# Tech Note: Using Operators on Pictures

**Author:** Not specified in source document
**Published:** May 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11961
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers an explanation of how 4D's logical (Boolean-style) operators behave when applied to Picture-type fields and variables.

## Key Points
- It frames these picture operators as directly analogous to the Boolean logical operators (AND, OR, and similar) used with True/False values, just applied instead to bitmap image data, where the operation is carried out pixel-by-pixel or region-by-region across two pictures.
- The note's core proposition is that once a developer understands standard Boolean logic, picture operators become far less mysterious, since they follow the same underlying logical rules applied to a different data type.
- An example database is included (per the source text) to let readers see the operators in action rather than relying purely on the written explanation.
- Because only the teaser/summary text survives in this archive, the specific list of supported picture operators and their exact bitwise/graphical effects are not preserved here, but the note is squarely about 4D's classic Picture field type and its logical-operation support, part of the broader graphics capabilities available in 4D v6.5 alongside 4D Draw and the Picture Library.
- This kind of note served developers building interfaces or effects that combine or mask images programmatically (for example, highlighting, masking, or overlay effects) without needing a graphics plug-in.
- It reflects the pre-modern-image-API era of 4D, when picture manipulation happened through a small set of built-in logical operators rather than a rich image-processing library.

## Featured Technology
- Picture fields
- Logical/Boolean picture operators
- Bitmap compositing

## Historical Context
This note clarifies how 4D's logical operators apply to Picture data (bitmap compositing operations analogous to AND/OR/XOR on Boolean values), a feature of the classic QuickDraw-era picture-handling engine in 4D v6.5. The specific picture-operator behavior described is tied to 4D's original bitmap-based Picture field implementation predating vector/4D Draw enhancements and later cross-platform picture engine rewrites, so while the Boolean-logic analogy remains conceptually instructive, the concrete operator behaviors may differ from 4D's modern picture-handling internals. Related updates since: 4D's picture field engine and supported picture formats/operations have been substantially rewritten and modernized in the many releases since 4D v6.5; Cross-platform picture handling today relies on modern image formats and APIs rather than the classic QuickDraw/GDI-based operators this note discusses. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
