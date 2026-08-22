# Tech Note 03-52: Transferring Pictures and Plug-in Documents Using the 4D ODBC Plug-in

**Author:** Not specified in source document
**Published:** December 19, 2003 | **Product/Version:** 4D ODBC v2003 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=30787
**Download:** https://kb.4d.com/DLTN/TN/2003/Windows/TN_2003_52-55_(DEC)/03-52_Xfering_Docs_via_ODBC.exe

## Overview
A practical Tech Note on transferring pictures and plug-in documents through the 4D ODBC plug-in as BLOBs while preserving the original data type integrity of the transferred content.

## Key Points
- Explains why BLOB is the correct generic data type for transferring pictures/documents via ODBC.
- Focuses on preserving the original data type/content when round-tripping binary data through a BLOB.
- Promises coverage of multiple sending/receiving scenarios using the 4D ODBC plug-in.

## Featured Technology
- 4D ODBC Plug-in
- BLOB data type
- ODBC integration

## Historical Context
ODBC was the standard mechanism 4D developers used to integrate with external SQL databases in this pre-4D-SQL-engine era (4D's own SQL engine did not arrive until v11 SQL, around 2007); only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

ODBC remains a supported integration mechanism in current 4D, so the general goal of safely moving binary content through an ODBC connection is still relevant, but 4D's own SQL engine (added in v11 SQL) and modern blob/picture-handling commands have since reduced how often developers need this specific plug-in-era ODBC workaround. The core lesson about preserving binary data fidelity when passing through a generic intermediate format remains a durable engineering principle.
