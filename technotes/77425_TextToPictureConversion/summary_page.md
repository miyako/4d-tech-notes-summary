# Tech Note 15-23: Text to Picture Conversion

**Author:** Jean-Pierre Ribreau (JPR) – 4D Trainer and Consultant
**Published:** December 7, 2015 | **Product/Version:** 4D v14.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77425
**Download:** https://kb.4d.com/DLTN/TN/2015/15-23_Text2PictConversion.zip

## Proposition
This note updates a 15-year-old (year-2000) Text2Pict method that used dying QuickDraw/PICT technology, rebuilding it with SVG commands to draw text into a picture, and separately champions passing function parameters via a single 4D Object rather than many positional parameters.

## Key Points
- **Historical continuity:** documents the original 2000-era Text2Pict method and why it needed updating as QuickDraw/PICT declined.
- **SVG-based redraw:** text-to-picture conversion is rebuilt entirely on SVG commands instead of QuickDraw/BLOB/PICT assembly.
- **Feature parity preserved:** font, size, style(s), text color, background color, rotation, alignment, and opacity are all still configurable.
- **Object-based parameter passing ("the lazy way"):** a single JSON-type 4D Object carries named parameters instead of a long positional parameter list.
- **Contrast of classic vs. modern styles:** the note explicitly compares the classic multi-parameter approach against the newer object-based approach.
- **Example database included** demonstrating usage of both the SVG drawing logic and the object-parameter calling convention.

## Featured Technology
- SVG (Scalable Vector Graphics) commands in 4D
- 4D Object / JSON-type parameters
- Legacy QuickDraw/PICT technology (context only)

## Best Practices Highlighted
1. Prefer SVG-based picture generation over legacy QuickDraw/PICT-based approaches.
2. Pass grouped, named parameters via a 4D Object rather than long positional parameter lists for more maintainable method signatures.

## Context / Positioning
This Tech Note was published in 2015, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

This note aged unusually well: its core recommendation to replace QuickDraw/PICT with SVG for text-to-picture rendering remains exactly the correct modern approach in current 4D, and its advocacy for object-based (JSON-type) parameter passing anticipated a coding style that became mainstream 4D practice, later reinforced by 4D's own class-based object features. Aside from minor syntax modernization, the techniques shown are still directly usable today.
