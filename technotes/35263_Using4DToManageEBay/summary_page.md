# Tech Note: Using 4D to Manage eBay

- **Asset ID:** 35263
- **Tech Note #:** 04-51
- **Published:** December 22, 2004
- **Product / Version:** 4D 2004
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=35263
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_51_(DEC)/04-51_Manage_eBay_with_4D.hqx

## Overview

Frank Chang, a 4D Evangelist, shows how to integrate a 4D 2004 database with eBay's marketplace via the eBay Developers Program's SOAP API, centered on a bundled 4D - eBay Object Library that provides drag-and-drop buttons for binding table fields to eBay's schema and for adding, downloading, and syncing auction listings.

## Key Points

- Introduces the eBay Developers Program's SOAP Web Services API (the "eBay SOAP API"), describing "Individual Applications" (single-user optimized catalogs) and "Bridge Applications" (integration between an existing product database and eBay's marketplace) as the two typical development scenarios.
- Details the 4D - eBay Object Library's nine objects, highlighting the Bind Tool (maps current table fields to the 14 fields required by eBay's SOAP API via the `Binding_SetBindings` method), Add Item(s) to eBay (calls `eBay_PostAdd`, which builds a SOAP request per selected record via `proxy_AddItem` and calls `AddItem`), Download from eBay (`eBay_PostGetSellerList`), Update eBay, and Update Locally.
- Walks through the setup tutorial: obtaining an eBay developer token via the Auth & Auth tool at developer.ebay.com, then using the Bind Tool's property dialog to map 4D table/fields to eBay fields (a one-time, per-database configuration).
- Shows the generic `AbstractAction_Startup` project method, which every Object Library button calls with a table pointer, current selection, and method name, and which spawns a uniquely-named new process (`New process`) to execute the actual eBay operation (e.g. `eBay_PostAdd`) so multiple actions can run concurrently.
- Documents the `eBay_PostAdd` procedure in detail: constructing the item encapsulation (`eBay_ConstructItem`), initializing the SOAP session (`eBay_Initialize` with token/app ID/version/server/site ID), calling `proxy_AddItem`, and parsing the response with `eBay_isOKResponse`/`eBay_GetItemID`/`eBay_GetError` to save the returned auction item ID back onto the 4D record.
- Notes that most other Object Library objects (Download, Update eBay, Update Locally) follow the same call-AbstractAction_Startup-then-dispatch pattern.

## Featured Technology

- eBay Developers Program SOAP API (sforce-style Web Services)
- 4D - eBay Object Library (Bind Tool, Add Item, Download, Update eBay, Update Locally)
- 4D Web Services Wizard-generated proxy methods (proxy_AddItem)
- eBay Auth & Auth (developer token) authentication
- Generic AbstractAction_Startup dispatch method with New process

## Historical Commentary

**Status:** Obsolete

Frank Chang, a 4D Evangelist, demonstrates a complete eBay marketplace integration built as a 4D 2004 Object Library/Template/Component toolkit, using the eBay Developers Program's SOAP API to add, download, and update auction listings directly from a 4D database via a Bind Tool that maps table fields to eBay's object schema. The note is a period showcase of 4D's 2004 SOAP web-services capability applied to e-commerce, but the specific eBay SOAP API version, the Auth & Auth token flow, and the bundled toolkit are all obsolete -- eBay's API has moved through multiple generations (Trading API, and now the modern eBay REST APIs with OAuth) since 2004, and 4D integrations with such platforms are now typically built with native HTTP Client commands and JSON rather than SOAP/XML and Object Libraries.

**References to newer/updated information:**
- eBay has replaced its 2004-era SOAP Developers Program API with modern REST APIs using OAuth authentication
- 4D's own web-service story has moved from Object Library/SOAP-based toolkits toward native HTTP Client commands and JSON for REST integrations
- The 4D-eBay Object Library and Bind Tool described in this note are specific to the classic Design Mode/4D 2004 architecture and are no longer applicable
