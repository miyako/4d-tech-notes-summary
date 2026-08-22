# Tech Note 07-07: Creating Mashups with 4D Live Window

**Author:** Joseph Resuello, Technical Support Engineer, 4D Inc.
**Published:** February 22, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45570
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_05-09_(FEB)/07-07_4DLW_Mashups.zip

## Overview
This Tech Note introduces "Mashups" — the then-emerging Web 2.0 practice of combining content from multiple web sources into a single custom experience — and shows how 4D developers can bring this pattern into their own databases using the 4D Live Window plug-in, part of the 4D Web 2.0 Pack. 4D Live Window embeds a real internet browser as a plug-in area on a 4D form, and its URL can be programmatically driven using data from the current record.

## Key Points
- Explains the concept of a "Mashup" (citing Wikipedia) as reusing/recombining existing web content and APIs (Google, eBay, Yahoo, Amazon, etc.) in custom ways.
- Documents the six 4D Live Window plug-in commands: `Web_SetURL`, `Web_GetURL`, `Web_Back`, `Web_Forward`, `Web_GetContent`, `Web_SetPreferences`, with full parameter/type/error-code tables.
- Focuses on `Web_SetURL` as the core command, typically called from a form's "On Load" event once a data-driven URL string has been assembled.
- **Example 1 – Google Maps:** a `GetGoogleMapsURL` method builds a Google Maps search URL from `[Customers]Address/City/State/Country`, handling zoom level, language code, and space-to-"+" encoding.
- **Example 2 – FedEx tracking:** a `GetFedexURL` method appends `[Inventory]TrackingNo` to a FedEx tracking URL template.
- **Example 3 – UPC lookup:** a `GetUpcURL` method appends `[Inventory]UPC` to a UPCDatabase.com query URL.
- Notes platform-specific caveats: on Mac OS, resizing the plug-in area can crash sites like Google Maps unless the area is fixed-size or resize is explicitly enabled via `Web_SetPreferences`; file paths differ between Mac (HFS/Unix-style, URL-encoded) and Windows (native paths accepted).
- Notes that `SET VISIBLE` alone does not fully hide the browser area — `Web_SetPreferences` must also be used.

## Featured Technology
- 4D Live Window plug-in (4D Web 2.0 Pack)
- `Web_SetURL` and related plug-in commands
- Google Maps, FedEx tracking, UPCDatabase.com (as example external data sources)

## Historical Context
Published in February 2007, this note predates 4D v11's SQL engine and reflects the classic Design-Mode-only, procedural 4D era. The 4D Web 2.0 Pack and its 4D Live Window plug-in have long been discontinued, and the specific Google Maps/FedEx/UPCDatabase URL formats shown are outdated (these services have since moved to versioned REST/JS APIs). However, the core idea — embedding a live web browser control in a form and driving its content from record data — remains a standard integration pattern, now typically implemented with 4D's native Web Area form object rather than a third-party plug-in.

## Status
**Obsolete** — the specific plug-in, product pack, and example URL schemes are all discontinued/outdated, though the general integration pattern is still conceptually used today via native Web Area objects.
