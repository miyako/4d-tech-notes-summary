# Tech Note 15-13: Map Integration with Data Cluster Display

**Author:** Thomas Maul, VP of Strategy – 4D Product Line, 4D Germany
**Published:** July 8, 2015 | **Product/Version:** 4D v15 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77329
**Download:** https://kb.4d.com/DLTN/TN/2015/15-13_MapWithDataCluster.zip

## Proposition
Rather than plotting a single location on a map, this note shows how to build a richer data visualization: clustering many customer records on a map by proximity, and encoding a secondary metric such as revenue into marker color and size — using the open-source Leaflet.js library instead of a commercially licensed mapping API.

## Key Points
- **License-motivated tooling choice:** explicitly moves away from Google Maps due to tightening commercial licensing terms, adopting Leaflet.js with OpenStreetMap data instead.
- **Progressive feature showcase:** single-customer map embedding, interactive multi-customer clustering, zoom-driven marker reveal, and cluster-highlighting synced with a listbox.
- **Metric-encoded markers:** marker color/size reflects revenue range; overlapping customers at one location show a revenue ratio.
- **Alternative aggregate views:** cluster-level totals (e.g., total regional revenue) as an alternative to per-customer detail.
- **Geo_Geocoding helper routine:** a reusable geocoding component included with the sample, adaptable for other applications.
- **Version note:** demo requires 4D v15 for its geo-information handling, though the underlying approach can be adapted back to v14.
- **Integration guidance:** dedicated section on installation requirements and steps for displaying single or multiple customers on a map, plus marker customization.

## Featured Technology
- Leaflet.js (JavaScript mapping library)
- OpenStreetMap (community-driven map data)
- 4D web/HTML area (for embedding the JS map)
- Geo_Geocoding routine (custom geocoding helper)

## Best Practices Highlighted
1. Prefer open-source, permissively licensed mapping libraries (Leaflet + OpenStreetMap) over commercial APIs for internal/embedded applications to avoid licensing risk.
2. Encode secondary business metrics (like revenue) visually into map markers rather than relying solely on location.
3. Use marker clustering to keep dense datasets readable at low zoom levels, revealing detail only as the user zooms in.

## Context / Positioning
Published in the classic Design Mode era (v15, 2015), this note reflects the standard technique of the time for adding rich web-based visualizations to 4D: embedding an external JavaScript library inside a 4D web/HTML area, well before ORDA or Project Mode existed. The licensing rationale (avoiding Google Maps' 2015 commercial terms change) is a nice snapshot of period-specific industry context.

## Historical Commentary
**Status:** Still relevant

Leaflet.js remains a leading, actively maintained open-source mapping library today, and embedding it in a 4D web/HTML area is still a standard, recommended approach for map visualizations in current 4D applications — this note's technology choice held up unusually well over a decade. The specific v15-era 4D-side plumbing (classic web area embedding, the included Geo_Geocoding helper) is dated compared to what ORDA-based data delivery would look like today, but the core architecture and library recommendation remain sound and directly reusable.
