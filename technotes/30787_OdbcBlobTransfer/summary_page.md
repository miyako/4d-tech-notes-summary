# Tech Note: Transferring Pictures and Plug-in Documents Using the 4D ODBC Plug-in

- **Asset ID:** 30787
- **Tech Note #:** 03-52
- **Published:** December 19, 2003
- **Product / Version:** 4D ODBC 2003
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri, Technical Support Engineer, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=30787
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_52-55_(DEC)/03-52_Xfering_Docs_via_ODBC.hqx

## Overview

Jamras Komoncharoensiri (Technical Support Engineer, 4D, Inc.) addresses how to correctly send and receive pictures and plug-in documents through the 4D ODBC plug-in without losing their original data type, by always transporting them as BLOB parameters and using the right conversion command on each end.

## Key Points

- All three scenarios use the same ODBC plumbing: `OC Create cursor`, `OC Set SQL in Cursor` (with `?` placeholders), `OC Bind parameter`/`OC Bind`, `OC Execute cursor`, `OC Load row`, and `OC DROP CURSOR`.
- Scenario 1 (true picture field): sending requires `PICTURE TO BLOB([PictureLibrary]Picture;vBlob;"JPEG")` before binding the blob parameter for INSERT; retrieving requires loading the blob and converting back with `BLOB TO PICTURE(vBlob;[PictureLibrary]Picture)` to preserve the picture's format properties.
- Scenario 2 (a 4D Write plug-in document stored in a picture field): sending requires restoring the document into an offscreen area first — `$area:=WR New offscreen area`, `WR PICTURE TO AREA($area;[DocLibrary]Doc_)`, then `WR Area to blob($area;1)` — before the blob can be inserted; retrieving reverses this with `WR BLOB TO AREA($area;vBlob)` followed by `WR Area to picture($area)` to restore proper document properties before saving to the picture field.
- Scenario 3 (a plug-in document already stored in a BLOB field): the simplest case — the blob is sent and received with zero conversion since it's already a valid document, e.g. `vBlob:=[DocLibrary]Doc_` and `[DocLibrary]Doc_:=vBlob`.
- Explicitly notes that a plug-in document saved into a picture field is not itself a "picture" — 4D encodes it in a plug-in-specific way, so naive transfer without the offscreen-area round trip would corrupt the document.
- Closes by generalizing the lesson: the same blob-based transfer approach applies to any data type that can be represented as a blob, not just pictures and 4D Write documents.

## Featured Technology

- 4D ODBC Plug-in (OC Create cursor / OC Bind parameter / OC Execute cursor)
- BLOB data type as the ODBC transport format
- PICTURE TO BLOB / BLOB TO PICTURE
- 4D Write offscreen areas (WR New offscreen area, WR Area to blob, WR BLOB TO AREA, WR Area to picture)
- SQL INSERT/SELECT parameter binding

## Historical Commentary

**Status:** Partially superseded

This note walks through three concrete scenarios for moving picture and 4D Write plug-in document data between a 4D database and a SQL Server via the 4D ODBC plug-in, showing that a true picture must round-trip through PICTURE TO BLOB/BLOB TO PICTURE, a 4D Write document stored in a picture field must first be restored via an offscreen area (WR Area to blob / WR BLOB TO AREA), and a plug-in document already stored in a BLOB field can be transferred directly with no conversion. ODBC connectivity itself is still supported in current 4D for external database integration, so the core technique remains usable as-is, but 4D's own native SQL engine (added in v11 SQL) has since reduced how often developers need to route through generic ODBC purely to reach a SQL database, and this specific note's focus on the legacy 4D Write plug-in format narrows its relevance to older databases still carrying 4D Write documents.

**References to newer/updated information:**
- 4D introduced its own native SQL engine (v11 SQL, ~2007), reducing reliance on ODBC as the primary way to talk to SQL databases from 4D
- ODBC connectivity itself remains supported in current 4D for external database integration, so the BLOB-transport technique described here is still technically valid
- The 4D Write plug-in referenced for the picture-field document scenarios has been superseded by 4D Write Pro, which uses different document storage/conversion mechanisms than the offscreen-area approach shown here
