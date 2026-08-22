# Google Chart API and 4D Live Window Integration

## Overview
The Google Chart API let developers generate chart images simply by encoding data and styling parameters into a specially formatted URL, with Google rendering and returning a PNG chart server-side. This note shows how to construct those parameterized chart URLs and display the resulting images inside a 4D Live Window (an embedded, dynamically-updatable HTML display area), making it easy to add on-the-fly charting to a 4D application's UI without a local charting library.

## Key Points
- Published January 31, 2008 as Technical Note 08-04.
- Targets 4D v11 on Mac & Win.
- Author: Christopher Visaya, Technical Support Engineer, 4D Inc..

## Featured Technology
- Google Chart API (image-based charting)
- 4D Live Window
- URL parameterization for chart generation

## Historical Context
Google officially shut down the Google Chart API's image-chart endpoint years ago (announced deprecation in 2012, later fully retired), so the specific technique in this note no longer functions; the general pattern of embedding externally-rendered visuals in a 4D Live Window remains conceptually valid with other charting services.

**Status:** obsolete

**Related updates:**
- Google deprecated and eventually shut down the classic (image-based) Google Chart API used in this note; the specific URLs/technique no longer work
- Modern charting in 4D applications typically uses JS charting libraries embedded in a Web Area, or 4D's own View Pro charting (introduced 2018) rather than an external image-generation API
