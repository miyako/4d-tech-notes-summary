# Tech Note 09-30: Geocoding Using Public Data

**Author:** Thomas Maul, 4D Germany
**Published:** July 30, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75857
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_27-30_(JUL)/09-30_OpenGeocoding.zip

## Proposition
This Tech Note shows how to perform geocoding and reverse geocoding in 4D using free, Creative Commons-licensed public data sources — Geonames.org and OpenStreetMap — as an alternative to commercial services like the Google Maps API covered in the prior Tech Note (09-29).

## Key Points
- Geonames.org (Creative Commons Attribution license) offers a free XML web service and full data downloads covering over 8 million geographical names worldwide, all in WGS84 coordinates.
- Simple browser-testable GET requests to `ws.geonames.org/search` support parameters like `name`, `country`, `lang` (translated place names), `featureClass`/`featureCode` (villages vs. mountains vs. streams, etc.), and `style` (short/medium/long/full response detail).
- The sample database's 9 form pages cover: name/country search, zip/country lookup, reverse-zip, reverse-place, US-only reverse street address, reverse-nearby search, geo-tagged Wikipedia article search (by zip or coordinates), and OpenStreetMap node search.
- OpenStreetMap is described as a Wikipedia-like community-edited map dataset (XML nodes with attributes) under a Share-Alike license, usable for geocoding as well as mapping.
- Implementation reuses the `HTTP_Download` method from TN 05-31 to fetch raw XML, then a generic `GN_ExtractSearchResult` method (using DOM XML commands) extracts whichever fields are listed in a `tLBArrayList` array into result arrays bound to a list box.
- Notes important licensing distinctions: Geonames' Attribution license just requires credit (even commercially), while OpenStreetMap's Share-Alike license requires derived works to be republished under the same license — the note suggests consulting a lawyer for compliance.

## Featured Technology
- Geonames.org web services (search, postal code, reverse geocoding)
- OpenStreetMap Name Finder / node search
- Creative Commons-licensed open geographic data
- `HTTP_Download` helper method (from TN 05-31)
- DOM XML parsing commands

## Best Practices Highlighted
1. Check the specific open-data license (Attribution vs. Share-Alike) before embedding third-party geographic data in a commercial application.
2. Build a generic, parameter-driven XML extraction method (`GN_ExtractSearchResult`) rather than one-off parsing code per query type.
3. Consider downloading a full offline dataset for single-user/no-internet scenarios rather than always hitting the live web service.

## Context/Positioning
Published as a companion to TN 09-29's Google Maps integration, this note broadened the geocoding conversation to free/open alternatives — relevant to developers wanting to avoid commercial API costs or terms for basic geocoding needs in 2009.

## Historical Commentary
**Status:** Obsolete

This note's specific integrations — the `ws.geonames.org` XML endpoints and the original OpenStreetMap Name Finder as accessed circa 2009 — have largely been superseded; geonames.org's API now requires a registered username/API key rather than the anonymous requests shown here, and OSM's modern geocoding entry point is Nominatim, not the original wiki-based Name Finder tool referenced in this note.

The general concept — geocoding against free, openly-licensed data as an alternative to commercial map APIs — remains entirely valid and popular, but a modern implementation would use JSON REST responses parsed with 4D's native JSON commands (or a call to Google Maps Geocoding API, Mapbox, or Nominatim) rather than raw `HTTP_Download` + DOM XML parsing against these now-outdated endpoints.
