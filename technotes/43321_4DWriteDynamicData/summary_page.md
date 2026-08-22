# Tech Note 06-23: 4D Write: Dynamic Data

**Author:** Daniel Do, Technical Support Engineer, 4D Inc.
**Published:** June 9, 2006 | **Product/Version:** 4D Write v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43321
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_22-26_(JUN)/06-23_4D_Write_Dynamic_Data.pdf

## Overview
This note covers using dynamic data in 4D Write 2004 — the word-processing/document-management plug-in for 4D — explaining how to insert and refresh live database fields and expressions inside documents, plus how to build tables in a 4D Write area.

## Key Points
- 4D Write documents can be attached to any database record and merge live data from that record into reports and letters.
- Getting started requires installing the 4D Write plug-in and adding a 4D Write area to an input form in Design mode; the "Goto Full Menu" button expands the working area.
- Fields/expressions are inserted via the Insert menu's "4D Expression…" command (or the equivalent contextual menu), presenting a hierarchical table/field picker plus applicable display formats.
- Inserted content can display either as a reference (grey background, surrounded by `<< >>`) or as a computed value.
- Reference values only refresh when "Compute References Now" is run from the 4D Write Tools menu, or when the document is reopened — they don't auto-update live as the record changes.
- Standard dynamic references (date/time, page number) compute at the moment of insertion; database-driven references (4D fields/expressions) reflect the current record and go blank if there's no current record.
- Supports arbitrary 4D expressions (not just plain fields), e.g. computing and inserting a calculated annual salary.
- The note also covers creating tables within a 4D Write area (part of the broader dynamic-content treatment).

## Featured Technology
- 4D Write plug-in area (classic word processor for 4D)
- Dynamic field/expression references
- COMPUTE REFERENCES NOW (4D Write Tools menu command)
- 4D Write tables and mail-merge style documents

## Historical Context
Published in 2006 for the original 4D Write 2004 plug-in, this note documents a document-merge capability years before 4D Write Pro existed, and long before Project Mode or ORDA. 4D Write, 4D View, and other companion products were still separate add-on components at this time.

## Historical Commentary
**Status:** Superseded

Classic 4D Write (the plug-in-based word processor described here) was superseded by 4D Write Pro, introduced in 2016, which handles data merging into rich text documents differently. The specific Insert-menu workflow, reference display model, and Compute References Now command described in this note apply only to the original 4D Write product, though the general mail-merge concept of embedding live database data into documents remains a relevant capability in 4D Write Pro today.
