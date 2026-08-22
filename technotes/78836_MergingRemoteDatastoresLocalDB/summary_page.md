# Tech Note 21-22: Merging Data from Remote Datastores into a Local Database

**Author:** Mehdi AARAB, Technical Services Engineer, 4D Morocco.
**Published:** December 20, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78836
**Download:** https://kb.4d.com/DLTN/TN/2021/21-22_MergeDataFromRemoteDS.zip

## Proposition
Demonstrates using ORDA's remote datastore feature (Open datastore over 4D's REST server) to pull data from multiple independently-hosted 4D Server databases into one local database, then reports on the merged dataset with 4D View Pro.

## Key Points
- **Remote datastore**: an ORDA datastore hosted on a separate 4D Server, accessed via the `Open datastore` command using a connection string (type 4D Server, hostname/port) plus an alias.
- **Requirements**: 4D v18+ for remote datastores, a 4D REST license per remote connection, and 4D Server licenses to host each remote datastore.
- **REST exposure prerequisites**: 'Expose as REST resource' must be enabled at the database and table level on each remote server, with the HTTP Server running.
- **Merge pattern**: `.all()` on the remote datastore's DataClass, `.new()`/field copy/`.save()` on the local datastore's equivalent DataClass, executed per remote source.
- **Use case**: consolidating region-specific databases (Spain, France) into one combined database (Europe) with an extra 'Country' attribute to track provenance.
- **4D View Pro reporting**: used to chart and compare sales data (e.g., pre/post-Covid) across the merged multi-source dataset.

## Featured Technology
- ORDA Remote Datastore (Open datastore)
- 4D REST server
- 4D View Pro reporting
- Entity/EntitySelection .all()/.new()/.save()

## Best Practices Highlighted
1. Enable REST exposure only on the specific tables/fields that need to be remotely accessible, for security.
2. Use distinct HTTP ports per 4D Server instance when running multiple remote datastores for testing on one machine.
3. Explicitly copy/map fields when merging entities across datastores rather than assuming identical structures line up automatically.

## Context / Positioning
This note reflects 4D's ORDA/REST architecture maturing into practical multi-site/multi-tenant data consolidation scenarios, a use case made newly urgent by pandemic-driven distributed work, and reinforces REST+ORDA as 4D's standard modern data-access layer over older, heavier integration approaches.

## Historical Commentary
**Status:** Still Relevant

This remains a valid and current technique: ORDA remote datastores and the Open datastore command are unchanged core 4D features, and multi-datastore merge patterns like this are still commonly used for consolidating distributed 4D deployments. 4D View Pro is also still the current reporting/spreadsheet component (having replaced classic 4D View years earlier). Nothing here is deprecated; a developer today would implement this almost identically, perhaps with minor ORDA syntax refinements in newer 4D versions.
