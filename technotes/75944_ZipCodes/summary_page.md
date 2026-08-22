# Tech Note 09-42: ZIP Codes in 4D v11 SQL

**Author:** Luis Piñeiros, Technical Services Team Member, 4D Inc.
**Published:** November 12, 2009 | **Product/Version:** 4D v11.4 SQL | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75944
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_41-45_(NOV)/09-42_ZIPCodes.zip

## Proposition
Shows developers two ways to auto-complete City/State on an address form from a ZIP Code — a bundled local ZIP code table, or a free third-party SOAP web service — plus bonus features for reverse lookups and distance calculation.

## Key Points
- **Local ZIP code database**: a bundled table of 80,000+ US ZIP codes (City, State, Area Code, Time Zone, Latitude, Longitude) enables fast, offline lookups but requires ongoing maintenance to stay current.
- **ZIP Code web service**: a free SOAP service at `www.webservicex.net` (`uszip.asmx`, `GetInfoByZIP`) provides always-current data but depends on Internet connectivity and third-party uptime.
- **Sample code** (`proxy_GetInfoByZIP`) builds the SOAP request with `DOM Create XML Ref`/`SET WEB SERVICE PARAMETER`/`CALL WEB SERVICE`, then parses the XML response with `DOM Find XML element` / `DOM GET XML ELEMENT VALUE`.
- **Form UX detail**: the ZIP field should receive cursor focus before City/State, and focus should skip past them automatically once a valid ZIP resolves those fields.
- **Reverse lookups**: the demo also finds all matching ZIP codes for a given City, State, or Area Code, from either data source.
- **Distance calculation**: an approximate distance between two ZIP codes is computed from latitude/longitude using simplified (non-spherical-geometry) math, sufficient for the sample's needs.
- A sample "Clients" database with 50 Fortune-500 demo records demonstrates the full workflow.

## Featured Technology
- Bundled ZIP Code lookup table (80,000+ US ZIP codes)
- SOAP web service call to www.webservicex.net ZIP code service
- Latitude/longitude-based distance approximation
- 4D form field focus/tab-order automation

## Best Practices Highlighted
1. Design address-entry forms so the ZIP Code field is completed first, driving City/State auto-fill and cursor flow.
2. Weigh offline reliability/speed (local table) against data freshness (web service) based on application needs.
3. Use simplified distance math when full spherical-geometry precision isn't required, for performance and simplicity.

## Context / Positioning
Written as a practical, small-scope productivity note for 4D v11 SQL developers building U.S. address-entry forms, illustrating both the local-database and SOAP web-service integration patterns that were standard in 4D applications of this era.

## Historical Commentary
**Status:** Partially Superseded

The core concept — resolving City/State from ZIP to reduce data-entry errors — remains valid today, and a local reference-table approach is timeless in principle, though the specific 2009-era 80,000-row dataset bundled with this note is now stale and would need replacement with a current source. The free SOAP service at webservicex.net that the sample code depends on is very likely defunct or unreliable today, as that generation of ad-hoc free SOAP APIs has largely disappeared.

A modern implementation would instead call a REST/JSON ZIP or geocoding API (e.g. Zippopotam.us, USPS Web Tools, or a commercial geocoding provider) using 4D's native REST request commands (available since v16+) rather than the legacy `CALL WEB SERVICE`/SOAP/DOM-XML approach demonstrated here.
