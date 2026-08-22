# Tech Note: Building Interactive Graphic Interfaces with 4D Draw, Part IV:A Color Palette D (TN 00-02)

**Author:** Tim Tonooka, ACI Technical Support
**Published:** January 1, 2000 | **Product/Version:** 4D Draw v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11941
**Download:** https://kb.4d.com/DLTN/TN/2000/Windows/TN_2000_01-05_(JAN)/00-02_Graphic_Interfaces_4.exe

## Overview
This Tech Note covers Part IV of a series on 4D Draw interactive interfaces, explaining how to programmatically construct and interact with a color-palette display built from individual 4D Draw objects.

## Key Points
- It recaps the series so far: Part I built the underlying 4D Draw vector graphics and BMP-to-vector conversion tooling via the "v65Trace" auto-trace example database; Part II covered rigorously validating that a document is genuinely a well-formed BMP file before processing it; and Part III explained the "Image Data" page, where clicking any pixel in a displayed BMP picture reveals that pixel's color/position details via configured 4D Draw area click detection.
- Building on that, Part IV's proposition is to construct a visual color-palette display — one separate 4D Draw object per color in the BMP's palette — and wire up interactivity so that clicking either a palette object or a pixel in the displayed image cross-highlights the corresponding entry in the other display, with the full color specification for the selected entry shown on the form.
- The note poses (and answers in the body) four specific technical questions: how to programmatically construct the palette diagram as a set of 4D Draw objects, how to detect which specific object was clicked within a 4D Draw area, how to indicate an object's "selected" status without relying on 4D Draw's native selection handles (likely to keep the visual presentation clean), and how to support highlighting multiple objects simultaneously (for example, all palette entries matching a given pixel's color, if it appears more than once in the image).
- Featured technology is 4D Draw's object creation and manipulation API, BMP palette-data extraction carried over from earlier parts, and custom click-detection/highlighting logic implemented without 4D Draw's built-in selection UI.
- At roughly 926 lines including source code, this is one of the most substantial notes in this batch, reflecting the technical depth 4D's Technical Notes series would go into for advanced, fully custom graphic-interface techniques during this period, well before such visualization work would typically be handled by higher-level charting or web-based components.

## Featured Technology
- 4D Draw
- Color palette rendering
- 4D Draw object click detection
- Multi-object selection/highlighting

## Historical Context
This is Part IV of the multi-part 4D Draw interactive-interface series, focused on building a clickable color-palette display (one 4D Draw object per palette color) with cross-highlighting between a BMP image and its rendered palette. Like the rest of this series, it depends entirely on 4D Draw, a vector-graphics technology that has been superseded in 4D's current product line, making the concrete techniques for constructing and click-detecting individual 4D Draw objects obsolete, even though the underlying UI patterns (clickable swatch grids, cross-highlighting between related displays, multi-select without native selection handles) remain recognizable, generally-relevant interface design concepts. Related updates since: 4D Draw has been discontinued/superseded in the current 4D product line; Clickable color-swatch and cross-highlighting UI patterns are now typically built with modern list box, picture, or web-area based components rather than hand-built 4D Draw object grids.
