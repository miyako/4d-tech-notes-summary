# Tech Note: A different way to display data

- **Asset ID:** 29726
- **Tech Note #:** 03-30
- **Published:** June 26, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=29726
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_26-30_(JUN)/03-30_DifftWayToDisplayData.hqx

## Overview

Jean-Yves Fock-Hoon (4D Inc. QA Manager) shows how to make data more perceptually meaningful by dynamically color-coding form areas, 4D Chart polygons, and map regions based on computed values, rather than displaying raw figures alone.

## Key Points

- First demo computes per-area sales totals/averages by looping through `[Sales]` records with `ALL RECORDS`/`NEXT RECORD` and building parallel arrays, then maps each result onto a 20-level RGB color gradient (values scaled into a 100-255 range) applied to form areas via `SET RGB COLORS`.
- A second variant of the same demo instead uses 4D 2003's new Quick Report XML export path (`QR New offscreen area`, `QR SET DESTINATION`, `QR SET HTML TEMPLATE` with an inline XML template, `QR RUN`) to produce a `report.xml` file that is then parsed back into the same arrays.
- A phone-queue-load example applies the same color-scaling technique but with a fixed, hard-coded Green-Yellow-Red scale instead of a dynamically computed one, representing call-queue congestion per line.
- A third example moves the technique into 4D Chart, loading a polygon-shaped map document (`Area.4CT` / `map.4CT`) and coloring individual polygon regions -- something not possible with plain form rectangles -- based on computed or hard-coded values.
- Implements a graph/map-coloring algorithm that stores country adjacency in a `[Borders]` table and ensures no two bordering countries share the same color, comparing a minimal-palette approach against a more colorful randomized-color approach.
- Notes that compiling the database significantly speeds up the manual record-looping computation (Example 1) but has no effect on Quick Report's own execution speed, since the report engine is already compiled internally.

## Featured Technology

- SET RGB COLORS
- Dynamic RGB color-scale computation
- QR SET HTML TEMPLATE (Quick Report XML export)
- 4D Chart polygon coloring
- Graph coloring / map-coloring algorithm

## Historical Commentary

**Status:** Superseded

This note's central insight -- that color and shape communicate data patterns more effectively than raw numbers -- remains as valid today as it was in 2003, and is now a mainstay of contemporary data-visualization and UX practice. The specific mechanics shown here (manually computing RGB values for form rectangles and 4D Chart polygons, hand-rolled map-coloring in 4D code) have been superseded by modern charting: 4D web areas can now embed rich, standards-based JS charting/visualization libraries, and 4D Chart itself has long been a legacy, rarely-used component. The QR SET HTML TEMPLATE-based XML export shown as a secondary technique is likewise a dated way to get report data into a usable form compared to modern JSON-based Quick Report/ORDA data access.

**References to newer/updated information:**
- Modern 4D web areas can embed contemporary JS charting/visualization libraries, offering far richer and more interactive options than the manual RGB-scaling and 4D Chart polygon techniques shown here
- 4D Chart itself is a legacy component rarely used in current 4D application development
