# Tech Note: DataGrid/EDM Overview - Beta 1

**Author:** Not specified in source document
**Published:** June 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11966
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers an early overview of the Beta 1 DataGrid application and its Enterprise Data Module (EDM) architecture for editing data across multiple back-end server types.

## Key Points
- It describes the Enterprise Data Module (EDM), an abstraction layer intended to let DataGrid talk to a local 4D Server database (no plug-in required), remote 4D servers via 4D Open, ODBC-compliant servers via 4D ODBC, and Oracle servers via 4D for Oracle.
- The proposition is essentially a unified front end for heterogeneous back-end data sources, letting a single application present and edit records regardless of where they physically live.
- As only the first entry in a series, the note is deliberately high-level, promising future notes that would dig into how EDM handles each specific back end (4D, 4D Open, ODBC, Oracle) in more detail.
- The featured technology is squarely EDM/DataGrid itself, alongside the enabling connectivity plug-ins of the era: 4D Open for 4D-to-4D remote access, 4D ODBC for generic database connectivity, and 4D for Oracle for direct Oracle access.
- Notably, the source text itself states plainly that "This Tech Note is no longer available," suggesting the DataGrid/EDM initiative was discontinued or superseded before the series (or the product) matured.
- As only a teaser/overview survives in this archive, no concrete implementation details, sample code, or screenshots are available to describe further.

## Featured Technology
- DataGrid (Enterprise Data Module)
- 4D Open
- 4D ODBC
- 4D for Oracle
- 4D Server

## Historical Context
This note previews DataGrid, an ambitious ACI/4D project meant to let a 4D front end edit data uniformly across 4D Server, 4D Open, ODBC, and Oracle sources via an Enterprise Data Module abstraction layer. The product itself never became a mainstream part of the 4D lineup and the note explicitly states it is no longer available, making it a historical curiosity about a road not taken. The underlying idea of a unified data-access abstraction across heterogeneous back ends foreshadows concepts 4D later solved differently through ODBC/SQL connectivity and, much later, ORDA's data-model abstraction. Related updates since: The DataGrid/EDM product line was discontinued and superseded long ago; 4D's own SQL engine (v11 SQL, ~2007) and later ORDA (v17+, 2018) provide modern, unified approaches to multi-source and remote data access that DataGrid attempted to solve in 2000. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
