# Tech Note: 4D for Keynote

- **Asset ID:** 27688
- **Tech Note #:** 03-15
- **Published:** March 31, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Cha Yang
- **Page URL:** https://kb.4d.com/assetid=27688
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_11-15_(MAR)/03-15_4D_for_Keynote.hqx

## Overview

This Tech Note by Cha Yang of 4D Inc. Technical Support describes "4D for Keynote," a 4D 2003 database that reads the XML-based "presentation.apxl" file inside an Apple Keynote package, extracts the chart data it contains, and lets a 4D user view and modify that data before writing a rebuilt presentation.apxl file back into the Keynote package. Because Keynote regenerates its slides from presentation.apxl every time a presentation is opened, editing that file's chart-data section is enough to change the charts a user sees, without 4D needing to understand Keynote's full rendering model. To cope with 4D's 32,000-character text limit and the file's large size (100+ pages of XML for an 8-slide deck), the note introduces a generic chunked-read method, KN_Import_Gen, that pulls the file in 10,000-character blocks, locates key markers such as <slide-list> and <plugin:data>, and stores the surrounding non-chart sections as opaque BLOBs while isolating just the chart-data XML for parsing with 4D 2003's new XML parser commands. The isolated chart data is parsed into XML_TreeName/XML_TreeValue/XML_TreeDepth arrays, and depth-1 boundaries are used to split the data into 4D records (one per chart column), linked back to their original slide and template via TemplateID and Slide_ID fields. On export, KN_Write_XML walks the stored template sections and modified chart records in original order to reconstruct a valid presentation.apxl, which then replaces the file inside the Keynote package. The note is a compact demonstration of streaming large external XML documents into 4D and selectively editing only the portion of interest while preserving the rest of a foreign file format byte-for-byte.

## Key Points

- Keynote stores presentation data in an XML file, `presentation.apxl`, inside the Keynote package; because Keynote regenerates its slides from this file every time it opens, rewriting only the chart-data section is enough to change what the user sees.
- 4D's 32,000-character text limit is worked around with the generic `KN_Import_Gen` method, which reads the file in 10,000-character chunks via `RECEIVE PACKET`, searching each buffer for a target marker string (e.g. `<slide-list`) while being careful not to split a word across chunk boundaries.
- The isolated chart-data XML fragment is exported to a temp document and parsed with 4D 2003's new XML parser commands (`ParseXMLDoc`), producing `XML_TreeName` / `XML_TreeValue` / `XML_TreeDepth` arrays that are then walked in `KN_Find_Slide` to split the data into 4D records by depth level.
- Each chart's data is stored in a `KN_TemPlate` table keyed by `TemplateID` (per imported Keynote file) and `Slide_ID` (per chart's position in the presentation), with header rows split off into a separate `Header` table.
- On export, `KN_Write_XML` walks the stored sections and modified chart records in `Slide_ID` order via `RELATE MANY`/sets, reconstructing a new `presentation.apxl` document and using `DELETE DOCUMENT` + `MOVE DOCUMENT` to replace the original file inside the Keynote package.

## Featured Technology

- Apple Keynote "presentation.apxl" XML file format
- 4D 2003 XML parser commands (Parse XML Doc, Get First/Next XML Element)
- Generic chunked document reader (KN_Import_Gen, 10,000-char buffering)
- BLOB-based storage of unparsed XML sections
- XML depth-based record decomposition (KN_Find_Slide)
- Document reassembly and export (KN_Write_XML, KN_Export)

## Historical Commentary

**Status:** Obsolete

This note is a clever, resourceful piece of engineering for its time: buffering a huge external XML file in 10 KB chunks to work around 4D 2003's 32 KB text limit, and rewriting only the chart-data fragment of a foreign file format to keep the rest byte-identical. Apple's Keynote file format has changed multiple times since 2003 (it soon moved to a zipped-bundle format with different internal XML/plist schemas, and modern Keynote files are quite different from the 2003 "presentation.apxl" structure), so the specific tag names and structure described here no longer apply to current Keynote files. The general technique — chunked reading plus 4D's native XML parser commands — remains valid today, but current 4D (with far larger text/BLOB limits and richer XML/JSON tooling) would not need the same manual chunking workaround.

References to newer/updated information:
- Apple's Keynote file format has been revised multiple times since 2003 (moving to a bundle-based format with different internal XML/plist schemas), making the specific tags in this note obsolete for current Keynote files
- 4D has since removed the 32,000-character text size limitation that necessitated this note's chunked-read technique, and offers richer native XML/JSON parsing
