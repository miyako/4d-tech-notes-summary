# Tech Note 11-28: Interactive Charting with 4D SVG

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** December 9, 2011 | **Product/Version:** 4D v12.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76438
**Download:** https://kb.4d.com/DLTN/TN/2011/11-28_InteractiveChartingWithSVG.zip

## Proposition
This Tech Note demonstrates how to use the 4D SVG component to produce a wide variety of interactive chart types — bar, column, line, pie, stacked, step, XY line, and stock-tracker charts — as an alternative to the static output of the legacy 4D Chart plugin or the more limited native 4D Graph commands.

## Key Points
- **Core SVG charting API:** SC_NewChart, SC_SET_Background, SC_SET_Dimensions, SC_SET_Chart_Attributes, SC_SET_Atts_and_Values, SC_SET_Legend_Attributes, SC_Chart_Display, SC_SVG_Ref.
- **Chart library:** ready-made examples of bar, column, line, pie, stacked bar, stacked column, step, XY line, and stock-tracker charts.
- **True interactivity:** shows how to add user interaction to SVG charts via Object method callbacks, beyond the static images of 4D Chart.
- **Efficient SVG techniques:** dash line, marker, and symbol definitions for cleaner, more reusable chart code.
- **Demo database:** packages all chart types and interaction patterns for direct reuse.
- **Positioning vs. alternatives:** contrasts 4D SVG against the dated-looking 4D Chart plugin and the more limited native 4D Graph commands.

## Featured Technology
- 4D SVG component (SC_ command set)
- 4D Graph commands (SVG-based charting)
- Object method callbacks for chart interactivity

## Context / Positioning
Published in late 2011 for 4D v12.3, this note showcased the 4D SVG component as the modern, flexible charting path at a time when 4D's other charting tools (the older 4D Chart plugin, the more constrained 4D Graph commands) left visual and interactive gaps developers wanted filled.

## Historical Commentary
**Status:** Obsolete

The 4D SVG component and its SC_ command family described here were retired as 4D moved toward web-standard charting; modern 4D applications typically render interactive charts using embedded HTML/JavaScript charting libraries rather than 4D's own SVG rendering engine.

The underlying SVG concepts (viewBox, transforms) remain valid general web knowledge, but the specific 4D SC_ API and object-method-callback interaction model documented here are now legacy techniques superseded by web-area-based JS charting and 4D View Pro.
