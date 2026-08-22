# Tech Note 09-29: Embedding Maps in 4D using Google Maps

**Author:** Thomas Maul, 4D Germany
**Published:** July 23, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75854
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_27-30_(JUL)/09-29_GoogleMaps.zip

## Proposition
This note shows how to embed maps based on the Google Maps API into a 4D v11 SQL form using the Web Area object, covering simple URL-based embedding, the full JavaScript API with markers, geocoding/reverse-geocoding, and two-way integration with Google Earth.

## Key Points
- **Simple map:** a Web Area whose URL variable is set to a constructed Google Maps search URL (`Geo_ConvertAddressToGoogleMapsURL`) — quick but shows unwanted Google chrome/ads around the map.
- **Full Google Maps API:** requires a free API key and gives control over zoom, layers, and markers, via a locally generated HTML/JS document.
- **Geocoding/Reverse geocoding:** `Geo_GoogleMapsGeoCoding` converts an address to coordinates via a direct HTTP request; reverse geocoding needs a JavaScript round-trip captured through the Web Area's On URL Filtering event and `Geo_GoogleMapsReverseFilter`.
- **Markers with tips:** `Geo_MarkersGoogleMapsURL` builds a map with multiple markers, each carrying rich-text/HTML tip content and an optional click URL that can trigger 4D actions via the Web Area Filter mechanism.
- **Google Earth integration:** launching Google Earth with a generated KML document, plus maintaining a live connection for two-way updates.

## Featured Technology
- Web Area (4D v11 SQL)
- Google Maps API (JavaScript, key-based)
- Google Maps Geocoding / Reverse Geocoding
- WA OPEN URL / On URL Filtering (Web Area URL interception)
- Google Earth integration (KML)

## Best Practices Highlighted
1. Use a Web Area's associated URL variable rather than hardcoding pages, so map content can be changed dynamically.
2. Generate map HTML documents on the fly in the temp folder with a unique per-process object name to support multiple simultaneous maps.
3. Use the Web Area Filter/On URL Filtering mechanism to safely intercept JavaScript-triggered navigation and hand control back to 4D.

## Context / Positioning
Published when mashing up business applications with consumer mapping services was a novel differentiator, this note gave 4D developers a concrete toolkit (reusable "Geo_" methods) for adding location features without needing deep JavaScript expertise, at a time when Web Area was one of the few ways to embed rich web content in a 4D form.

## Historical Commentary
**Status:** Partially Superseded

This note showed how to embed Google Maps into a 4D v11 SQL form via the classic Web Area object, using URL-based tricks and JavaScript callbacks routed through On URL Filtering to bridge 4D and the browser-hosted map. That general Web Area + JS bridge pattern is still functionally valid, but the specific Google Maps JavaScript API v2 techniques shown are long deprecated by Google, and modern 4D development would typically use native HTTP/JSON commands to call Google's REST Geocoding API directly rather than scraping results from an embedded page.

Google has since retired and replaced the Maps JavaScript API used here multiple times (now requiring billing-linked keys), and 4D's own HTTP/JSON support has matured considerably, making a direct REST-based integration more idiomatic today than the Web Area/JavaScript relay approach described in this note.
