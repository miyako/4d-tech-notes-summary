# Tech Note 07-08: Creating Mashups in the 4D Ajax Framework Client

**Author:** Jason T. Slack, Technical Support Engineer, 4D Inc.
**Published:** February 27, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45611
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_05-09_(FEB)/07-08_4DAF_Mashups.pdf

## Overview
Framed within the broader Web 2.0 narrative of rich internet applications and public APIs from companies like Google, eBay, and Yahoo, this note walks step-by-step through building a Google Maps "mashup" in the 4D Ajax Framework (4DAF) Client — combining external map data with local 4D address records.

## Key Points
- Does not cover 4DAF installation or general developer docs (pointed to separately at 4D's support documentation site) — focuses purely on the mashup-building steps.
- Builds a new database with an "Address Info" table (Street/City/State/ZipCode fields), generates default forms, and populates sample records with valid addresses.
- After installing and testing the 4D Ajax Framework, logging into the 4DAF Client as Administrator reveals a Portal with a fully functional Selection Window for viewing/editing Address Info records — no 4D code required.
- Introduces the **Developer Defined Window (DDW)**, a 4DAF Settings feature letting developers attach an arbitrary HTML blob or URL to a field, configured via the Settings dialog's DDW Manager and Access Control tabs.
- Creates a "GoogleMaps" DDW (type "New Window – Link") and associates it with the Address Info table's Street field, which then renders as a clickable hyperlink in the Selection Window.
- A short Database Method named "GoogleMaps" powers the DDW: it uses `DAX_Dev_DDW_GetAttributes` to retrieve the current table pointer and selected record numbers, builds a classic Google Maps URL query string (`maps.google.com/maps?f=q&...`) from the record's address fields, and returns it as the DDW's target link.
- Clicking the Street link opens the corresponding Google Maps location — achieved with a handful of lines of code and no custom UI work.

## Featured Technology
- 4D Ajax Framework (4DAF) Client
- 4D Web 2.0 Pack
- Developer Defined Windows (DDW) — Settings, DDW Manager, Access Control
- `DAX_Dev_DDW_GetAttributes`
- Classic Google Maps URL-based mapping API

## Historical Context
This note captures a snapshot of 2007-era "Web 2.0" thinking, built on 4D's now-discontinued Web 2.0 Pack/4DAF product and the classic (pre-JavaScript-API) Google Maps URL-based integration approach. The specific DDW mechanism and `DAX_Dev_DDW_GetAttributes` command no longer exist in current 4D. The general mashup concept — combining an external API/service with local application data — remains a completely standard web/mobile development pattern today, just implemented very differently (e.g., via the modern Google Maps JavaScript API or embed methods, called from a current 4D Web Server or client-side JS framework).

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework, 4D Web 2.0 Pack, and Developer Defined Windows have all been discontinued; modern 4D web/mobile projects would integrate mapping APIs directly via the built-in Web Server, REST/ORDA data access, or a custom web component instead of a DDW.
