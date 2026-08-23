# Tech Note: Introduction to 4D Open

- **Asset ID:** 11987
- **Tech Note #:** 00-50
- **Published:** October 1, 2000
- **Product / Version:** 4D Open
- **Platform:** Mac & Win
- **Author:** Aziz Elghomari
- **Page URL:** https://kb.4d.com/assetid=11987
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_46-50_(OCT)/00-50_Intro_to_4D_Open.hqx

## Overview

Aziz Elghomari (4D S.A. Technical Support) covers the data-manipulation half of the 4D Open C API — creating/deleting records, searching, sorting, sets, and Blobs — as the second installment in a series introducing 4D Open, 4D's client library for connecting external C/Java programs to a 4D Server.

## Key Points

- Records are created/deleted by first clearing existing data with `_4D_SelectAllRecords`/`_4D_DeleteSelectedRecords`, then building field values into a `DataRec` union (covering Alpha, Text, Real, Integer, Long Integer, Date, Time, Boolean, Picture, Blob types) via `_4D_CreateBuffer` and `_4D_AddToBuffer(CIDH, Buffer, FieldNumber, *Field)`.
- Searching uses `_4D_Search(CIDH, SearchRecordPtr, *RecordsFound)` against a `SearchRecord`/`SearchLine` structure specifying the target file, field number, search operator (SOP, e.g. Equal), value, and logical operator (LOP) — demonstrated searching field 4 of file 1 for the value 999.
- Sorting uses the analogous `SortRecord`/`SortLine` structures (`TargetFile`, `Field_Number`, `Ascent` flag) to define a single-level ascending or descending sort.
- Set-handling routines — `_4D_CreateEmptySet`, `_4D_CreateSet` (captures the current selection), `_4D_AddToSet`, `_4D_RecordsInSet`, and `_4D_ClearSet` — are used to build two named sets (MySet1 for the current record, MySet2 for search results) and report their element counts.
- Blob length is retrieved by selecting/positioning records (`_4D_SelectAllRecords`, `_4D_GotoSelectedRecord`), fetching field data with `_4D_GetFields`/`_4D_GetNthField` into a `DataRec`, and reading `data.u.blob.BlobLen`.
- The accompanying sample ships as Code Warrior 5 (Mac OS) and Visual C++ (Windows) projects, linking against the 4D Open `.Lib`/`.PPC.Lib` (recompiling) or `4D Open.dll` (running the prebuilt executable), and requires a 4D Server v6.5.x database over TCP/IP (`KNC = NC_TCPIP`).
- The note closes by emphasizing 4D Open's thin-client footprint: a 264 KB `4dopen.dll` versus an 8.6 MB full 4D client.

## Featured Technology

- 4D Open C API record/data routines (_4D_CreateBuffer, _4D_AddToBuffer, _4D_GetFields, _4D_GetNthField)
- 4D Open search (_4D_Search / SearchRecord / SearchLine structures)
- 4D Open sort (SortRecord / SortLine structures)
- 4D Open set handling (_4D_CreateSet, _4D_CreateEmptySet, _4D_AddToSet, _4D_RecordsInSet, _4D_ClearSet)
- 4D Open Blob handling (DataRec union, BlobLen)
- 4dopen.dll thin-client architecture

## Historical Commentary

**Status:** Obsolete

The second in a 4D Open technical note series, this note covers the C API side of 4D Open's data manipulation: creating/deleting records via buffer routines, searching and sorting with the SearchRecord/SortRecord structures, handling named sets, and reading Blob data, all compiled against sample Code Warrior (Mac) and Visual C++ (Windows) projects linked to a 4D Open .Lib/.dll. Its highlighted selling point, a 264 KB 4dopen.dll thin client versus an 8.6 MB full 4D client, was a genuine differentiator at the time. 4D Open has been discontinued for many years; developers building thin, programmatic clients against 4D Server data today use 4D's REST/ORDA web data server instead, which offers a modern, language-agnostic equivalent of the thin-client goal this note pursued through a native C library.

**References to newer/updated information:**
- 4D Open has been discontinued; there is no direct modern successor product by that name
- 4D's REST/ORDA data server now provides the modern equivalent of thin, programmatic, cross-platform access to 4D Server data that 4D Open aimed to provide in 2000
