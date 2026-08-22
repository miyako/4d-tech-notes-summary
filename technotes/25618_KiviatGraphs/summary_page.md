# Tech Note 03-1: Kiviat Graphs

**Author:** Olivier Deschanels, 4D S.A.
**Published:** January 31, 2003 | **Product/Version:** 4D Chart v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=25618
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_01-05_(JAN)/03-01_kiviat_graphs.exe

## Overview
TN 03-1 explains how to draw Kiviat (radar/spider) graphs — a chart type not natively supported by 4D Chart — by using 4D Chart's basic drawing primitives together with 4D language trigonometry to compute and render the polygon manually.

## Key Points
- 4D Chart (as of 2003) had no built-in Kiviat/radar graph type, requiring a fully custom drawing approach.
- Uses CT DO COMMAND to reset/initialize the 4D Chart area before custom drawing.
- Computes axis endpoints around a circle using trigonometry, based on a defined center point and radius.
- Stores series values and legends in parallel arrays to drive the polygon-drawing loop.
- Demonstrates comparing multiple items (e.g., cameras) by shape rather than raw numbers.

## Featured Technology
- 4D Chart
- CT DO COMMAND
- Custom charting via trigonometric math

## Historical Context
4D Chart was 4D's classic charting plug-in/component bundled with the development environment; custom graph types not in its built-in library had to be hand-drawn using its lower-level primitives, as shown here.

## Historical Commentary
**Status:** Obsolete

4D Chart as described here is a legacy component that has been superseded by more modern charting approaches in current 4D (including web-based charting libraries and later graph area object types), so the specific CT DO COMMAND-based drawing API is largely obsolete for new development. The underlying idea — computing radial/polar coordinates to render a Kiviat-style visualization — remains conceptually valid and is easily portable to any modern drawing or charting library.
