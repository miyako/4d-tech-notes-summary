# Tech Note 07-40: SVG Charts in 4D v11 SQL

**Author:** Christopher Visaya, Technical Support Engineer, 4D Inc.
**Published:** October 12, 2007 | **Product/Version:** 4D Developer v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47733
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_39-42_(OCT)/07-40_SVG_Charts.zip

## Overview
This note documents 4D v11 SQL's new native support for Scalable Vector Graphics (SVG), a vector-based, XML image format, and demonstrates using the `GRAPH` and `GRAPH SETTINGS` commands to render statistical charts through the new SVG engine instead of the older 4D Chart plug-in.

## Key Points
- SVG explained as XML-based, vector (geometric-shape) rather than pixel-based, giving scaling advantages over JPEG/GIF.
- `GRAPH` command engine selection depends on its first parameter's type: a 4D Chart area/graph reference uses the legacy 4D Chart plug-in; a Picture variable invokes the new native SVG engine.
- `GRAPH SETTINGS` configures axis min/max (0 = default), proportional/gridline display booleans, and legend titles, matched to the `GRAPH` call's graph parameter.
- Sample database tracks daily exercise time (Wii, gym, basketball) across a 31-day month, aggregated with `Sum()` into arrays and rendered via `GRAPH(vGraphPict;1;times;wii_time;gym_time;bas_time)`.
- Graph style parameter supports values 1 through 8 for different chart types (e.g. style 1 = column/bar chart).
- Three sample graphs are included: activity totals, activity averages, and per-day activity breakdowns, all using the same SVG mechanism.
- The older 4D Chart plug-in remains available as a fallback for developers who prefer its visual style.
- Additional coverage of contextual menu behavior and exporting the resulting chart as an SVG file to disk.

## Featured Technology
- Native SVG rendering engine (new in 4D v11 SQL)
- `GRAPH` / `GRAPH SETTINGS` commands
- 4D Chart plug-in (legacy alternative engine)
- SVG file export

## Historical Context
Published in October 2007 as part of the 4D v11 SQL release wave, this note reflects 4D's broader move toward adopting open, XML-based standards (alongside the era's new SQL engine and regex support) rather than relying purely on proprietary plug-ins like 4D Chart for core functionality such as data visualization.

## Historical Commentary
**Status:** Superseded

SVG remains a current, actively used web graphics standard, and the `GRAPH`/`GRAPH SETTINGS` commands described here continued to work in 4D for many years after this note was published, so the core mechanism is not obsolete outright. However, 4D's charting and reporting capabilities have expanded considerably since 2007, and the 4D Chart plug-in referenced as a fallback in this note is a legacy component from that era, making this note's specific code examples and comparisons dated relative to current charting practice in 4D.
