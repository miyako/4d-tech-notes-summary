# Tech Note 10-03: Dynamically Creating Tag Clouds with SVG

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** January 25, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75998
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_01-04_(JAN)/10-03_TagCloud.zip

## Proposition
This note shows how to build data-driven tag clouds using 4D v11 SQL's newly introduced SVG support — generating SVG documents dynamically via DOM XML commands and rendering them as clickable images that link back to underlying data.

## Key Points
- **SVG** (Scalable Vector Graphics) is a W3C XML vector-graphics specification newly supported by 4D v11 SQL, rendered via **DOM EXPORT TO PICTURE** or displayed in the new **Web Area** form object.
- SVG elements can respond individually to **mouse click/over events**, unlike standard raster images (JPEG/GIF).
- A **4D SVG component** offers a friendlier way to design SVG graphics than writing raw DOM XML commands.
- Sample **Tag Cloud (TCL) database** sizes and colors sales associate names based on total sales, driven entirely by data.
- Covers **TCL_madeCloud_arrays**, generating SVG from data, wrapping text in SVG, color shading, and the tag-cloud weighting algorithm itself.
- **Click handling** on tag cloud elements displays the underlying selection of records.

## Featured Technology
- 4D v11 SQL SVG support (DOM EXPORT TO PICTURE, XML/DOM commands)
- 4D SVG component for designing SVG graphics
- Web Area for clickable/interactive image display
- Tag cloud data-driven visualization algorithm

## Best Practices Highlighted
1. Use the 4D SVG component rather than hand-writing raw DOM XML commands when non-XML-experts need to build SVG graphics.
2. Drive visual attributes (size, color/brightness) directly from underlying data to make weighted visualizations self-updating.
3. Wire up click handlers on SVG elements to bridge from a visual summary back to the underlying record selection.

## Context / Positioning
Published as 4D v11 SQL's SVG support was new, this note built directly on the general weighted-list algorithms from the companion note "Generating Weighted Lists in 4D" (asset #76053), applying them to an eye-catching SVG visualization.

## Historical Commentary
**Status:** Partially Superseded

This note demonstrates generating data-driven tag clouds by building SVG documents dynamically via 4D v11 SQL's newly introduced XML/DOM commands, rendering them as clickable picture variables or in a classic Web Area form object.

SVG-in-4D via DOM XML commands and the classic Web Area still function today, but 4D has since added more direct, higher-level ways to work with SVG and interactive visualizations, and modern 4D web development increasingly favors HTML/CSS/JS rendered in the (now Chromium-based) Web Area or dedicated charting/visualization components rather than hand-assembling SVG through DOM XML commands. The core tag-cloud/weighted-visualization idea remains valid, but the specific SVG-construction technique is a dated way to achieve it.
