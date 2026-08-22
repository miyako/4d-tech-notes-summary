# Tech Note 11-24: SVG Coordinate System – Part 2

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** August 1, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76385
**Download:** https://kb.4d.com/DLTN/TN/2011/11-24_SVG_Coordinate_System_P2.zip

## Proposition
This Tech Note is the second in a two-part series on the SVG coordinate system used by 4D's SVG component, focusing on the "rotate" and "skew" values of the SVG transform attribute after Part 1 covered "translate" and "scale".

## Key Points
- **Foundational recap:** re-establishes the infinite default user coordinate system, the viewport, and the viewBox concepts underpinning all SVG transformations.
- **Transform - rotate:** detailed walkthrough of how the rotate transform value repositions and reorients SVG objects.
- **Transform - skew:** detailed walkthrough of how the skew transform value distorts SVG object shapes.
- **Mechanics over black-box usage:** stresses understanding the underlying transform mechanics rather than trial-and-error, since results are often unintuitive.
- **Demo database:** provided so developers can directly experiment with rotate and skew values.
- **Series continuity:** explicitly builds on the earlier "SVG Coordinate System" note covering translate and scale.

## Featured Technology
- 4D SVG rendering engine
- SVG transform attribute: rotate and skew
- SVG viewport / viewBox coordinate system

## Context / Positioning
Published mid-2011 for 4D v12 as a direct follow-up to an earlier Tech Note, this note completed 4D's documentation of SVG transform mechanics at a time when the 4D SVG component was actively promoted as the modern path to rich, custom vector graphics inside 4D applications.

## Historical Commentary
**Status:** Partially Superseded

The SVG standard itself (viewport, viewBox, transform rotate/skew) is timeless web knowledge that remains accurate today, but the specific delivery mechanism — 4D's proprietary SVG rendering engine used to draw picture objects in classic Design Mode forms — has fallen out of favor as 4D applications increasingly embed standard web content via web areas instead.

Developers wanting rotated/skewed vector graphics in a 4D app today would more likely use an HTML5/SVG web area or a JS charting library than 4D's native SVG picture-object engine described here.
