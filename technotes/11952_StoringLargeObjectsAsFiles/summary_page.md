# Tech Note: Storing Large Objects as Separate Files on the Hard Drive

**Author:** Not specified in source document
**Published:** April 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11952
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a design pattern for storing large objects (such as pictures or documents) as separate external files rather than inside the 4D data file, tracked via a database table.

## Key Points
- It opens by reminding readers that 4D's core value proposition is its database engine — the software that manages data storage and retrieval — and then makes the case that once a database needs to handle many large objects, it can make more sense to store those objects as separate files on the hard drive rather than embedding them directly inside the 4D data file.
- The proposed pattern uses a dedicated table in the database to track each external file, with each record holding metadata (such as a file path or identifier) describing and locating the corresponding file on disk.
- This design keeps the core data file leaner and can improve performance and manageability, since large binary blobs stored inline can bloat the data file, slow down backups, and complicate compaction and maintenance operations.
- Featured technology is 4D's classic database engine and file-system interaction commands used to read, write, and track external files alongside a metadata table — essentially a manual, developer-implemented precursor to the more automated large-object/document management features 4D added in later versions.
- Because only the brief teaser text survives in this archive, the specific commands and implementation code used for file creation, referencing, and retrieval are not preserved here, but the architectural rationale is clearly and concisely stated.
- This pattern — separating large object storage from the primary data store while tracking it relationally — is a durable database design principle that remains applicable well beyond the specific 4D version this note was written for.

## Featured Technology
- BLOB/large object handling
- External file storage strategy
- Database engine design

## Historical Context
This note describes a still-conceptually-valid database design pattern: keeping large binary objects outside the core data file and tracking them via a reference table, reducing data-file bloat and the operational costs that come with it. The specific mechanics for external file storage in classic 4D (pre-BLOB-field and pre-modern document/folder management commands) are dated, but the underlying architectural principle — separating large object storage from the primary data store, tracked by metadata records — remains a widely used and relevant pattern in database design generally, including in modern 4D applications that store large files outside the current .4DD/.4DIndx data structure. Related updates since: 4D has since added more capable BLOB, picture, and document/folder-management commands making external large-object storage easier to implement than in 2000; The core architectural pattern (external file storage plus a tracking table) remains a standard technique in current 4D and general database application design. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
