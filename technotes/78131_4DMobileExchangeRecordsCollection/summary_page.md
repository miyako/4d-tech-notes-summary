# Tech Note 18-17: 4D Mobile Exchange Records using Collection

**Author:** Not specified in the available material
**Published:** September 27, 2018 | **Product/Version:** 4D Mobile v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78131
**Download:** https://kb.4d.com/DLTN/TN/2018/18-17_4DMobileSelectionExchange.zip

## Proposition
Only the demo's readme/setup instructions were retrievable for this note (not the full narrative PDF), so this summary is based on that material. It demonstrates exchanging data between 4D and a Wakanda Enterprise-based 4D Mobile backend using ORDA collections converted from entity selections, including locking and timestamp handling.

## Key Points
- **Environment:** requires 4D v17+, Wakanda Enterprise Studio 2.6.0+, and (for 4D Server scenarios) a 4D Mobile Server Expansion license.
- **Entity selection → collection:** `createEntitySelection` and `entitySelectionToCollection` 4D methods show retrieving a collection from an ORDA entity selection.
- **Conversion options/filtering:** `collectionWithOption` and `collectionWithFilter` demonstrate additional collection-conversion capabilities.
- **Old vs. new retrieval styles:** paired JS demos (`getMobileSelection.js` vs. `getCollection.js`) contrast the legacy "Mobile Return Selection" approach with collection-based retrieval.
- **Sending data from Wakanda to 4D:** `sendCompanyCollection.js` / `receiveCompanyCollection` 4D method shows building a selection-compatible array from a collection.
- **Timestamping:** `sendCompanyCollectionWithStamp.js` adds a timestamp to collections sent from 4D Mobile.
- **Entity locking during exchange:** locking a record via the standard input form, then observing behavior when `sendCompanyCollectionLocked.js` attempts to send/modify it.

## Featured Technology
- 4D Mobile (paired with Wakanda Enterprise Studio/Server)
- ORDA entity selections and collections
- Entity locking
- Wakanda Enterprise JavaScript backend scripts

## Context / Positioning
This note is part of a cluster of 2018 Tech Notes teaching developers to build 4D Mobile apps against a Wakanda Enterprise JavaScript backend, specifically showing how ORDA's newer collection data type could carry data between 4D and mobile/web clients more flexibly than older selection-array approaches.

## Historical Commentary
**Status:** Obsolete

Both halves of the technology stack shown here — the "4D Mobile" branded product and its Wakanda Enterprise Studio/Server dependency — have been discontinued; this demo cannot be meaningfully reproduced with current 4D tooling. Full technical detail beyond the readme was unavailable, so this assessment is based on the setup instructions and referenced method/file names rather than a complete reading of the original document.

The underlying idea of converting ORDA entity selections to/from collections for exchange with an external client, and respecting entity locking during that exchange, is still conceptually valid — modern 4D apps do this via the built-in REST server and standard JSON, without any Wakanda dependency. Developers today should look at 4D's current REST/ORDA documentation rather than this note for building mobile or web-facing data exchange.
