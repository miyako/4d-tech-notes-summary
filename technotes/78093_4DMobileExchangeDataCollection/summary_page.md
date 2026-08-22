# Tech Note 18-13: 4D Mobile Exchange Data using Collection

**Author:** Not specified in the available material
**Published:** July 20, 2018 | **Product/Version:** 4D v16 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78093
**Download:** https://kb.4d.com/DLTN/TN/2018/18-13_4DMobile_Collection.zip

## Proposition
Only the demo's readme/setup instructions were retrievable for this note (not the full narrative PDF), so this summary is based on that material. It's an introductory demo showing basic bidirectional exchange of data as ORDA collections between 4D and a Wakanda Enterprise-based 4D Mobile client, plus array/collection conversion utilities.

## Key Points
- **Environment:** 4D v17 beta+, Wakanda Enterprise Studio 2.6.0+, tested with Safari 11.1.1+/Chrome 67+; requires a 4D Mobile Server Expansion for 4D Server scenarios (or standalone/uncompelled operation).
- **Return collection from 4D:** `returnCollectionFrom4D.js` (Wakanda) demonstrates retrieving a collection generated on the 4D side.
- **Send collection to 4D:** `sendCollectionTo4D.js` (Wakanda) sends a collection from the client into 4D, displayed in JSON form via the "CollectionFromMobile" 4D form.
- **Array-to-collection conversion:** `convertArrayToCollection` 4D method method converts a classic 4D array into a collection, with results shown via alerts.
- **Collection-to-array conversion:** `convertCollectionToArray` 4D method converts a collection back to an array, inspectable in the debugger.

## Featured Technology
- 4D Mobile (paired with Wakanda Enterprise Studio/Server)
- ORDA collections
- 4D array-to-collection / collection-to-array conversion utilities

## Context / Positioning
As one of the earliest notes in 4D's "4D Mobile Exchange ... using Collection" series, this demo served as a basic on-ramp for developers building 4D Mobile/Wakanda Enterprise client apps during the early ORDA-collection era (v16R/v17), before more advanced companion notes (e.g., TN 18-17) layered in entity-selection conversion and locking.

## Historical Commentary
**Status:** Obsolete

Both the "4D Mobile" branded product and its Wakanda Enterprise Studio/Server dependency have been discontinued, so the demo environment described cannot be reproduced with current 4D tooling. Full technical detail beyond the readme was unavailable, so this assessment relies on the setup instructions and referenced file/method names rather than a full reading of the original document.

The narrower technique of converting between classic 4D arrays and ORDA collections (`convertArrayToCollection`/`convertCollectionToArray`-style utilities) remains a routinely used, valid 4D pattern independent of the mobile-specific context here. Developers building mobile/web data exchange today should look to 4D's current REST/ORDA documentation, which achieves the same collection-exchange goal via standard JSON over REST rather than a Wakanda-specific integration.
