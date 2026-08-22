# Tech Note 08-44: Mashups with 4D v11 SQL Web Area

## Proposition
Demonstrate how the new 4D v11 SQL Web Area can power "Mashups" — combining 4D application data with external web content like maps, tracking, and generated documents — updating the older 4D Live Window-based Mashup concept from TN 07-07.

## Key Points
- Web Area (WebKit on Mac, ActiveX on Windows) is now built into 4D v11 SQL Release 2, removing the need for the 4D Live Window plug-in.
- A Google Map is displayed by constructing a maps.google.com URL from the client's address and loading it with WA OPEN URL.
- A client's own website and product pages are shown simply by loading their stored URL.
- Shipment tracking is shown by building a FedEx URL from a stored tracking number.
- A "Build Correspondence" feature assembles an HTML letter (with header graphics, CSS styling, salutation, and body text) as a temporary file and displays/prints it via the Web Area's contextual menu.

## Featured Technology
- 4D Web Area (WebKit / ActiveX)
- WA OPEN URL
- Google Maps URL-based embedding
- FedEx tracking URL embedding
- Dynamically generated HTML via string concatenation + PROCESS HTML TAGS
- "Mashup" / Web 2.0 concept

## Best Practices Highlighted
- Encapsulate URL-building logic in dedicated project methods (e.g., WA_Mashup_GetGoogleMapURL).
- Use the Web Area's native contextual menu (Print/Save) rather than building custom print logic.
- Keep locale/zoom parameters (e.g., map language, zoom level) as adjustable defaults.

## Context/Positioning
Published at the height of the "Web 2.0 Mashup" trend, this note showed 4D developers how the newly built-in Web Area control could deliver on that trend without needing external plug-ins, reinforcing 4D's positioning as keeping pace with contemporary web integration patterns.

## Historical Commentary
The core idea — blending internal business data with external web services inside the application — remains a valid and common pattern, but the specific implementation here is dated: directly embedding Google Maps and FedEx tracking via bare, unauthenticated URLs in an embedded browser control no longer works reliably, since both providers now require API keys/authenticated REST calls and have changed their URL schemas. A modern equivalent would call the Google Maps or FedEx REST/JSON APIs directly from 4D (via native HTTP request commands) and render results in a modern, CSS-styled form rather than hand-concatenating HTML strings. This note is best read today as a historical snapshot of the Web 2.0 "Mashup" era rather than as usable implementation guidance.
