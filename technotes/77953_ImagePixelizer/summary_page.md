# Tech Note 18-03: Image Pixelizer

**Author:** Kristopher Merolla, Technical Services Engineer, 4D Inc.
**Published:** February 22, 2018 | **Product/Version:** 4D v16R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77953
**Download:** https://kb.4d.com/DLTN/TN/2018/18-03_Image_Pixelizer.zip

## Proposition
Shows how to pixelate an image — reducing its quality into blocky, low-resolution chunks — by combining native 4D image handling with a hidden Web Area running JavaScript (for per-chunk color averaging via Canvas image data) and SVG drawing to reconstruct the pixelated output.

## Key Points
- **Hidden Web Area as a JavaScript sandbox:** used purely to execute JavaScript calculations (color averaging) that weren't available through native 4D commands at the time, with the area inspectable for console errors during development.
- **Chunking the image:** the picture is divided into a grid of cells whose dimensions are computed in 4D before being handed off for processing.
- **Base64 round-trip:** image chunks are Base64-encoded to pass into the JavaScript context and decoded back on return.
- **color_avg.js:** a JavaScript function using HTML5 Canvas image data to compute the average color of each image chunk.
- **SVG reconstruction:** `SVG_New` and `SVG_New_rect` draw solid-colored rectangles representing each averaged chunk, rebuilding the pixelated image as vector rectangles.
- **DOM Export to VAR / DOM CLOSE / XML Decode / BLOB TO PICTURE:** the pipeline used to extract the SVG from the Web Area, decode it, and convert it into a usable 4D picture.
- **Bonus selective pixelation:** a "Pixelizer_Area" form lets users pixelate just a selected rectangular region of an image, combining it back with the untouched remainder.

## Featured Technology
- Web Area (hidden, for JS execution)
- SVG drawing commands (SVG_New, SVG_New_rect)
- JavaScript / HTML5 Canvas (color_avg.js)
- Base64 encoding
- DOM Export to VAR, DOM CLOSE, XML Decode, BLOB TO PICTURE

## Best Practices Highlighted
1. Use a hidden Web Area as a general-purpose JavaScript execution engine when 4D lacks a native command for a specific calculation.
2. Inspect the Web Area during development to catch JavaScript errors/console logs.
3. Reduce full-resolution images to protect assets (e.g., watermarking/protecting paid content) or obscure identities selectively rather than uniformly.

## Context / Positioning
This note exemplifies the "extend 4D via Web Area + JavaScript" pattern common in the pre-ORDA, pre-Project-Mode 4D era (v16), where native commands for advanced image/graphics manipulation were more limited and developers often bridged the gap using an embedded browser engine for calculations, then round-tripped results back into 4D's native picture format.

## Historical Commentary
**Status:** Still relevant

The Web Area, SVG drawing commands, DOM Export to VAR, and BLOB TO PICTURE are all still current 4D commands, so this technique remains directly reproducible today. The overall workaround pattern — using a hidden Web Area as a JavaScript compute engine for tasks not natively supported — also remains a valid and still-used technique in modern 4D development, not something ORDA or Project Mode rendered obsolete.

That said, 4D has continued to expand its native picture and image-manipulation command set since 2018, so some simpler pixelation or image-processing needs might now be achievable with fewer native commands rather than requiring the full JS/SVG round-trip shown here; developers should check current native picture commands before assuming this workaround is still the only path.
