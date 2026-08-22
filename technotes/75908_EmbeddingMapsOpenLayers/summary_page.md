# Tech Note 09-36: Embedding Maps in 4D using Open Layers

**Author:** Thomas Maul, 4D Germany.
**Published:** September 10, 2009 | **Product/Version:** 4D 11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75908
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_36-39_(SEP)/09-36_OpenLayers.zip

## Proposition
This Tech Note, the third in a mapping series, shows how to embed OpenStreetMap-based maps in a 4D form's Web Area using the OpenLayers JavaScript framework, as a license-friendlier and more data-rich alternative to the Google Maps API covered in an earlier note.

## Key Points
- Motivation: Google Maps' terms of service restrict some use cases (e.g. printed mass mailings), and its map data can lack points of interest, minor streets, or smaller countries — OpenStreetMap (CC-BY-SA licensed) fills these gaps.
- Simplest approach: load the OpenStreetMap website directly into a Web Area via a constructed URL (`?lat=...&lon=...&zoom=...`) using `WA OPEN URL`.
- `WA Execute JavaScript` is used to inject custom JavaScript into the loaded page — both to hide unwanted UI chrome (sidebar, navigation) and to call OpenLayers' own JS API (e.g. placing a marker via `OpenLayers.LonLat`).
- For full control, a helper method `Geo_OpenLayerOSM` uses `PROCESS HTML TAGS` to substitute `#4DVAR` placeholders in an HTML template (longitude, latitude, zoom, object name) and writes the resulting HTML to the temporary folder before loading it into the Web Area — avoiding write-protected application folders and enabling multiple simultaneous map instances.
- Later sections cover adding multiple/Google Maps layers within OpenLayers, handling click events, and exporting a rendered map as an image.
- Licensing: OpenStreetMap data is CC-BY-SA; applications using the API without shipping the map data are generally not bound by the license, but printed/shipped map output may be.

## Featured Technology
- OpenLayers JavaScript mapping framework (legacy v2-era)
- OpenStreetMap tile/data source
- 4D Web Area (WA OPEN URL, WA Execute JavaScript)
- PROCESS HTML TAGS / #4DVAR template substitution
- Google Maps layers (via OpenLayers)

## Best Practices Highlighted
1. Write generated HTML/templates to the temporary folder rather than the application folder, since the latter may be write-protected and multiple simultaneous map windows need distinct files.
2. Use a template + placeholder-substitution pattern (`PROCESS HTML TAGS`) rather than string-concatenating full HTML documents.
3. Consult a lawyer regarding CC-BY-SA obligations before shipping map data directly with an application.

## Context / Positioning
Completing a three-part 2009 mapping series (Google Maps, geocoding, then OpenLayers/OpenStreetMap), this note gave 4D v11.4 developers a non-Google option for embedding interactive maps at a time when 4D had no native mapping commands and the Web Area was the primary vehicle for rich embedded content.

## Historical Commentary
**Status:** Partially Superseded

The specific OpenLayers version and JavaScript API used here are from the OpenLayers 2 era, which has since undergone multiple major rewrites (OpenLayers 3 replaced the entire architecture, and the library is now well past version 9); the code samples in this note would need to be substantially rewritten to run against a current OpenLayers release, and Leaflet.js has since emerged as a popular lighter-weight alternative for exactly this kind of embed.

The broader pattern — building a local HTML template, injecting variables, and loading/controlling it inside a 4D Web Area via JavaScript injection — remains valid in 4D's Web Area today, and the Web Area's underlying browser engine has been modernized since 2009, but a developer starting this project now would pick a current mapping library rather than follow this note's code verbatim.
