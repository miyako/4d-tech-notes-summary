# Tech Note: Introduction to 4D Open

## Overview
- **Technical Note 00-50**
- **Author:** Unknown / not specified
- **Published:** October 1, 2000
- **Product:** 4D Open
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note is a companion, data-focused introduction to 4D Open, 4D's client API for communicating with 4D Server, covering how to enter and delete data, search and sort data, and work with Blobs and Sets through the 4D Open interface. Its central proposition is that 4D Open enables a genuinely 'thin' client architecture: the note points out that the 4dopen.dll library weighs in at only 264KB, compared to a full 4D Client installation at 8.6MB, making 4D Open attractive for lightweight or embedded integration scenarios where deploying a full 4D Client would be overkill. This complements a companion note (also archived here, asset 11984) that covers 4D Open's structure-access side; together they formed a two-part introduction to the API aimed at developers building custom clients against 4D Server. The featured technology is 4D Open itself, 4D's precursor concept to today's REST/ORDA-based external access APIs. Because only the teaser abstract survives for this specific note (its original download was an old Windows self-extracting installer that could not be extracted here), the detailed data-access code samples could not be recovered.

## Featured Technology
- 4D Open
- Thin client architecture (4dopen.dll)
- Blobs and Sets

## Historical Context
This note covers 4D Open's data-manipulation side (entering/deleting/searching/sorting data, handling Blobs and Sets) and highlights one of 4D Open's genuine selling points at the time: a thin-client footprint (a 264KB DLL versus an 8.6MB full 4D client). 4D Open, the C/C++/Java API precursor to modern client-server access technologies, has been discontinued for many years; developers building thin, programmatic clients against 4D data today use 4D's REST/ORDA web data server instead, which did not exist at the time this note was written.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- 4D Open has been discontinued; there is no direct modern successor product by that name
- 4D's REST/ORDA data server now provides the modern equivalent of thin, programmatic, cross-platform access to 4D Server data that 4D Open aimed to provide in 2000

