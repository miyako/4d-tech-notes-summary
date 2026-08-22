# Tech Note 15-12: Creating CSS Image Sprites files in 4D

**Author:** Charles "Charlie" Vass, Technical Services Engineer, 4D Inc.
**Published:** June 23, 2015 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77321
**Download:** https://kb.4d.com/DLTN/TN/2015/15-12_CreatingSpritesImages.zip

## Proposition
CSS image sprites reduce HTTP requests and eliminate hover-state flicker by combining many small web images into one master sheet, addressed via `background-position`. This note shows how to generate such sprite sheets programmatically in 4D using `COMBINE PICTURES` and `TRANSFORM PICTURE`, including a purpose-built sprite-maker tool.

## Key Points
- **Historical framing:** traces sprites from early video-game graphics through Dave Shea's 2004 CSS sprite technique that reduced JavaScript-hover-driven HTTP requests and flicker.
- **4D's picture command evolution:** contrasts the original black-and-white-oriented Picture Operators with the fuller-fidelity `COMBINE PICTURES` and `TRANSFORM PICTURE` commands introduced in 4D v11.
- **Three sprite layout strategies:** vertical, horizontal, and composite (grid) organization of combined images.
- **"4D CSS SPRITES Maker" tool:** a bundled utility automating sprite-sheet generation from a folder of source images.
- **Bonus tools included:** a Gradient Button Maker and a "4D SPRITES Date Widget," built on the same underlying picture-combination approach.
- **Working web examples:** included to show the generated sprites functioning in real HTML/CSS.

## Featured Technology
- `COMBINE PICTURES`
- `TRANSFORM PICTURE`
- 4D Picture Operators (legacy)
- CSS `background-position`
- 4D CSS SPRITES Maker (bundled tool)

## Best Practices Highlighted
1. Combine related small icons/images into a single sprite sheet to reduce page load HTTP requests.
2. Use `COMBINE PICTURES`/`TRANSFORM PICTURE` rather than legacy black-and-white Picture Operators to preserve full-color image fidelity.
3. Automate sprite-sheet generation with a repeatable tool rather than manual image editing, to keep sprites consistent as source assets change.

## Context / Positioning
Published in the classic Design Mode era (v14.x, 2015), this note reflects mid-2010s web performance orthodoxy — a period when CSS sprites were still a widely recommended optimization technique for HTTP/1.1-era websites, well before HTTP/2 changed the performance calculus.

## Historical Commentary
**Status:** Obsolete

CSS image sprites were a legitimate, widely used web performance technique through the mid-2010s, but the arrival of HTTP/2 (and later HTTP/3) multiplexing largely eliminated the per-request overhead problem sprites were designed to solve, and SVG icons, icon fonts, and modern compressed image formats have since taken over most of the use cases sprites once served. The 4D commands used here (`COMBINE PICTURES`, `TRANSFORM PICTURE`) remain valid and functional in current 4D, but the specific web technique this note teaches is now largely a historical curiosity rather than a recommended practice for modern sites.
