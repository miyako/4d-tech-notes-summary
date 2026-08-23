# Tech Note: XML based Export/Import for Archiving Data

- **Asset ID:** 18206
- **Tech Note #:** 01-43
- **Published:** September 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Thomas Maul, 4D Germany
- **Page URL:** https://kb.4d.com/assetid=18206
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_41-45_(SEP)/01-43_Archiving_Data_in_XML.hqx

## Overview

Thomas Maul (4D Germany) presents a generic TMXML_ 4D component for exporting and reimporting an entire database as XML, intended for long-term legal archiving, database defragmentation, controlled repair of suspect files, and clean drop-field/drop-table structural migrations.

## Key Points

- Motivations covered: multi-year legal archival requirements (e.g., 7-10 years for German invoice data), database defragmentation via full export/reimport, controlled repair that reports exactly which records/tables are damaged (unlike 4D Tools' silent tag-based repair), major-version/structure migrations, and drop-field/drop-table cleanup that 4D's live structure doesn't otherwise support.
- TMXML_Init/TMXML_ExportAll/TMXML_ImportAll are the three core calls; ExportAll opens a Select Folder dialog and writes one XML file per table (named by table name, or optionally by table number via UseTableNumbers for 8.3-compatible ISO CD filenames), skipping invisible tables/fields if AvoidInvisible is set.
- TMXML_AddSubTable/TMXML_AddSubField register one level of 4D subtables for export/import (nested subtables, possible pre-v3, are explicitly unsupported); TMXML_AddPictToConvert/TMXML_AddBlobToRTF opt individual picture and 4D Write blob fields into JPG and RTF conversion respectively for long-term external readability, writing at most 1,000 files per output subfolder.
- TMXML_AddFieldSortingOrder lets a developer control per-table export sort order so records land on disk in the order they're usually queried (mirroring 4D Tools' "Order on disk"), speeding later Query/Order-without-index operations.
- Character encoding: field/table names with diacritical characters are underscore-substituted for XML compatibility, and non-ASCII content is converted to ISO-8859-1 entities for broad readability by tools like early MS Internet Explorer.
- The code is distributed and should be used strictly as an installed 4D Component (via 4D Insider's Install/Update), not copied inline, so a single canonical implementation can be updated across many databases without behavioral drift; sample export timings for a 450MB/50-table database ranged 40-120 minutes across period hardware.

## Featured Technology

- TMXML_ 4D Component (TMXML_Init/TMXML_ExportAll/TMXML_ImportAll)
- Generic table/field enumeration for XML export
- Subtable handling via TMXML_AddSubTable/TMXML_AddSubField
- Picture-to-JPG and 4D Write-to-RTF conversion for future readability
- Field-sort-order control for defragmentation (TMXML_AddFieldSortingOrder)
- 4D Insider component install/update workflow

## Historical Commentary

**Status:** Still Relevant

Thomas Maul (4D Germany) presents a generic, component-packaged XML export/import scheme (the TMXML_ methods) intended for long-term legal data archiving, database defragmentation, controlled repair of damaged files, and structural migrations such as dropping fields or tables -- with explicit guidance to write archives to ISO 8.3 CD-Rs, convert pictures to JPG and 4D Write documents to RTF for long-term legibility, and refresh media every five years. XML import/export commands remain part of 4D's classic language and the archiving/defragmentation/migration use cases described are still genuinely faced by 4D developers today, but many modern projects would now reach for native JSON (added circa 4D v15-16) or ORDA-based data transfer instead of hand-rolled XML tooling for these same needs.

References to newer/updated information:
- 4D added native JSON parsing/serialization (circa 4D v15-16), now often preferred over hand-built XML export/import for data interchange and archiving
- ORDA provides additional entity-based mechanisms for migrating and reorganizing data between structures that can substitute for parts of this component's role
