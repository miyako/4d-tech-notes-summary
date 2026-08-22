# Tech Note 11-14: Reusable SVG — The Power of <defs>

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** April 29, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76326
**Download:** https://kb.4d.com/DLTN/TN/2011/11-14_Reusable_SVG.zip

## Proposition
This note explores how 4D's native SVG support can leverage the SVG standard's <defs> element to predefine reusable graphical objects and attributes — such as shapes, gradients, patterns, and style sheets — that are referenced rather than duplicated throughout an SVG document displayed in a 4D form. Through a series of progressively more sophisticated demos (building a warehouse rack-and-package diagram), the author shows how definitions reduce document size, simplify maintenance, and speed up modification of complex 4D SVG graphics. The note covers defining and using basic shape templates, applying quick global changes via shared definitions, defining and linking external style sheets, and defining reusable patterns. It's aimed at 4D developers building custom vector graphics inside their applications who want more efficient, maintainable SVG structures.

## Key Points
- Two SVG document zones: the `<defs>` block (never directly rendered) holds reusable templates, while everything else is the presentation layer that references them.
- Progressive demo series: from a a plain, repetitive rack-and-package SVG image to versions using defined rectangles/patterns referenced via URIs, showing dramatic simplification.
- Quick global changes: because presentation elements reference shared definitions, changing one definition updates every instance that references it.
- External and embedded style sheets: shows how to define, include, and apply a CSS-like style sheet within the 4D SVG document.
- Pattern definitions: demonstrates defining and using a repeating SVG pattern as a fill for shapes.
- Sample database included with all seven demos for hands-on exploration.

## Featured Technology
- 4D SVG area (SVG_New_rect, SVG_New_line, SVG_Use, SVG_New_symbol commands)
- SVG <defs> element (definitions vs. presentation layers)
- SVG patterns, style sheets, and symbol reuse

## Best Practices Highlighted
- Place all reusable graphical templates inside `<defs>` rather than duplicating markup inline
- Use symbolic/pattern references to keep SVG documents compact and easier to update
- Favor style sheets over inline attributes when many objects share the same visual styling

## Context / Positioning
Published in 2011 for 4D v12.1, at a time when 4D had recently added native SVG rendering areas to forms, and this series of Tech Notes was building out best practices for developers producing custom vector graphics without external drawing tools.

## Historical Commentary
**Status:** Still Relevant

4D's SVG area and its SVG_* command set (including SVG_New_rect, SVG_Use, and pattern/definition support) are still present in current 4D and the underlying SVG <defs>/reuse technique described here remains valid, so this note is still directly usable as a reference for building efficient SVG graphics in 4D forms. It predates 4D's later investment in richer built-in charting/data-visualization tools and picture-variable based UI approaches, which now offer alternative, lower-code ways to achieve similar visual results for many common cases.
