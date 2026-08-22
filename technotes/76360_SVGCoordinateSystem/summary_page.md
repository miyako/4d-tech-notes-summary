# Tech Note 11-19: SVG Coordinate System

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** June 9, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76360
**Download:** https://kb.4d.com/DLTN/TN/2011/11-19_SVG_Coordinate_System.zip

## Proposition
This Tech Note introduces the SVG coordinate system as it applies to 4D's SVG component — the user coordinate system, viewport, and viewBox — and covers the "translate" and "scale" values of the SVG transform attribute, as Part 1 of a series.

## Key Points
- **User coordinate system:** the theoretically infinite default 2D canvas SVG objects are drawn on.
- **Viewport:** constrains SVG drawing to a finite rectangle suited to screens, 4D forms, and picture objects.
- **viewBox:** maps user-space coordinates onto the defined viewport.
- **Tying concepts together:** shows how the user coordinate system, viewport, and viewBox interrelate before transformations are applied.
- **Transform - translate:** how the translate value repositions SVG objects.
- **Transform - scale:** how the scale value resizes SVG objects.
- **Series setup:** explicitly defers "rotate" and "skew" transform values to a follow-up Tech Note.

## Featured Technology
- 4D SVG rendering engine
- SVG viewport and viewBox
- SVG transform attribute: translate and scale

## Context / Positioning
Published mid-2011 for 4D v12, this note laid the conceptual groundwork for 4D's push toward the SVG component as a modern, flexible graphics engine, ahead of the more advanced transform techniques covered in its follow-up note.

## Historical Commentary
**Status:** Partially Superseded

As Part 1 of the SVG coordinate system series, this note lays out the foundational SVG viewport/viewBox model and the translate/scale transform values, concepts that remain accurate as general SVG/web knowledge today.

However, the specific application context — 4D's own SVG rendering engine used to draw picture-object charts and graphics inside classic Design Mode forms — is a legacy delivery mechanism now that 4D applications more commonly embed standards-based SVG/HTML5 content via web areas rather than 4D's proprietary SVG component.
