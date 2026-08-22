# Tech Note 10-29: Image Manipulation with SVG

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** September 24, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76184
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_28-31_(SEP)/10-29_Image_Manipulation_with_SVG.zip

## Proposition
Tom Fitch's Tech Note explores an under-the-radar use of SVG in 4D v12: rather than just generating original vector graphics, SVG documents can embed existing raster pictures via the <image> element and then have arbitrary SVG transforms/effects applied to that embedded image.

## Key Points
- SVG's <image> element can embed existing raster pictures for further manipulation
- Demonstrates three effects: resizing, reflection, and a fade effect
- Contrasts SVG-based manipulation with native commands like TRANSFORM PICTURE and PHP libraries
- Provides a sample database implementing all three techniques
- Frames these three styles as reusable building blocks for further custom effects

## Featured Technology
- SVG (Scalable Vector Graphics)
- embedding pictures in SVG
- SVG-based reflections and fades
- 4D picture variables

## Best Practices Highlighted
- Choose the manipulation style matching the desired effect (resize/reflect/fade) as a template for new effects

## Context/Positioning
Published as 4D promoted its SVG picture support as a flexible, code-driven alternative to native picture commands for producing polished, dynamic UI imagery.

## Historical Commentary
**Status:** Still Relevant

This note's technique of embedding bitmap pictures inside SVG documents to achieve resizing, reflection, and fade effects reflects 4D's early-2010s SVG support, which remains functional in current 4D versions thanks to backward compatibility. However, modern 4D applications more often achieve these visual effects with native picture handling, CSS-based styling in forms (available since ~v18), or web-based front-ends, making the specific SVG-manipulation techniques here a still-usable but increasingly niche approach rather than the first choice for new development.
