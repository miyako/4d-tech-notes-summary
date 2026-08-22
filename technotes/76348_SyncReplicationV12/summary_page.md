# Tech Note 11-18: Introduction to Synchronization and Replication in 4D v12

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** June 3, 2011 | **Product/Version:** 4D v12.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76348
**Download:** https://kb.4d.com/DLTN/TN/2011/11-18_Replication_Introduction.zip

## Proposition
This Tech Note introduces 4D v12's newly integrated synchronization and replication feature, moving data-engine-level replication out of bespoke developer mechanisms (SOAP, 4D Open, manual import/export) into a supported, built-in capability, with mirror and satellite demo databases.

## Key Points
- **Requirements for replication:** connection type, language access, a primary key, enabling replication, and optionally touching existing data.
- **What enabling replication produces:** replication metadata, new virtual fields, and dedicated replication files.
- **How it works:** replication metadata tracks CRUD actions (what), record IDs (where), and stamps (when), shown via a step-by-step record lifecycle.
- **REMOTE vs. LOCAL:** distinguishes these contexts both in code and in overall software architecture.
- **Core commands:** the REPLICATE and SYNCHRONIZE commands and their respective conflict-resolution behavior.
- **Real-world constraints:** ID collisions, invoice numbering with temporary IDs/services, and subtotal recalculation challenges.
- **Demonstrations:** mirror and satellite demo setups, including a sample "MyMeetings" application.

## Featured Technology
- Integrated data-engine REPLICATE and SYNCHRONIZE commands
- Replication metadata (stamps, IDs, CRUD action tracking)
- REMOTE vs. LOCAL data connection contexts

## Context / Positioning
Published in mid-2011 for the newly released 4D v12.2, this note introduced developers to a major new engine-level capability that eliminated the need for the ad hoc SOAP/4D Open/import-export replication schemes many had built themselves in earlier versions.

## Historical Commentary
**Status:** Still Relevant

4D v12's built-in REPLICATE/SYNCHRONIZE data-engine mechanism described here was a significant improvement over prior ad hoc approaches and its core CRUD-metadata-and-conflict-resolution model has remained part of 4D's classic feature set, still usable for offline/mirror/satellite database scenarios today.

That said, modern mobile and distributed-data architectures increasingly favor REST/ORDA-based data access with client-side caching or dedicated sync services rather than 4D's native replication engine for new greenfield projects, making this technique a solid but no-longer-default choice.
