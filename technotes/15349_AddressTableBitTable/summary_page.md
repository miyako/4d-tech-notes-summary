# Tech Note: At the Core of the Data: The Address Table and Bit Table

- **Asset ID:** 15349
- **Tech Note #:** 01-30
- **Published:** June 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Olivier Deschanels
- **Page URL:** https://kb.4d.com/assetid=15349
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_26-30_(JUN)/01-30_At_the_Core_of_the_Data_The_Address_Table_and_Bit_Table.hqx

## Overview

Olivier Deschanels (4D, S.A.) continues the internal data-file architecture series begun in TN 01-29, explaining how 4D's classic engine actually locates records within its 128-byte-block data file — via record "tags" encoding platform/version, and a two-level Primary/Secondary Address Table structure — plus how free space is tracked via a bit-table.

## Key Points

- Every record begins with a 4-byte "tag" encoding the 4D version and the originating platform (Mac vs. Windows), because those platforms order integer/longint bytes differently; the tag lets 4D's engine decide whether byte swapping is required when reading a record (see Appendices A/B in the original PDF for the exact tag values).
- In client/server deployments, the server's platform determines the tag written for a record, and 4D Server performs byte swapping transparently before sending records to clients running on a different platform.
- Explains why the engine designers stored the origin platform in the tag rather than standardizing on one byte order: doing so avoids a constant byte-swap performance penalty for whichever platform wasn't chosen.
- Scanning the raw data file for tag markers to find record boundaries is unreliable (arbitrary field data can coincidentally match a tag's hex pattern, e.g., "DGE" → `$444745`), so it's used only as a last-resort recovery mechanism (4D Tools' "Recover by Tag").
- Instead, 4D maintains an **Address Table** per table: a **Primary Address Table (PAT)** of 4096 rows, each pointing to a **Secondary Address Table (SAT)** of up to 4096 record addresses+sizes, letting the engine find any of up to 16,777,216 records via `(n/4096)+1` rather than a linear file scan; addresses are 32-bit, with 7 bits reserved to encode the record's data segment number (up to 128 segments, 256 GB total).
- A parallel **bit-table** (one bit per 128-byte block, addressed via a **Bit-table-address-table / BTAT**) tracks free vs. occupied blocks for allocation; the "Completely Deleted" table option controls whether deleted records are zero-tagged and their blocks freed in the bit-table immediately (safer but slower) or left recoverable in place (faster but risks resurfacing sensitive deleted data after a crash).
- Recommends using `SELECT ALL([Table])` followed by `APPLY TO SELECTION([Table]field:=[Table]field)` to force records to be re-saved in the deployment platform's native byte order after transporting a data file between Mac and Windows, avoiding ongoing byte-swap overhead.

## Featured Technology

- 4D record 'tag' (version + platform origin marker)
- Byte swapping between Mac and Windows integer/longint storage
- Primary Address Table (PAT) / Secondary Address Table (SAT)
- Bit-table allocation map / Bit-table-address-table (BTAT)
- APPLY TO SELECTION for forcing platform re-save
- 128-byte block-based data file architecture

## Historical Commentary

**Status:** Obsolete

This note offers a genuinely deep look at 4D's classic .4DD/.data storage engine internals — tags, address tables, and bit-tables — that would have helped developers diagnose performance and data-recovery issues in 4D 6.x/2001-era databases. That storage engine was subsequently replaced by 4D's SQL/CoreData-based engine (starting around 4D v11 SQL, 2007), which uses a different internal architecture, so the specific address-table and bit-table mechanics described no longer describe how current 4D databases work. The note remains valuable purely as historical/archival documentation for anyone still working with legacy pre-v11 4D data files.

**References to newer/updated information:**
- 4D replaced its classic data-file engine with the 4D SQL/CoreData storage engine starting around 4D v11 SQL (2007), changing the internal record/address/bit-table structures described here
- Developers working with legacy pre-v11 .4DD/.data files for recovery purposes may still find this architecture description useful as historical reference
- APPLY TO SELECTION remains a valid current 4D command, though its use here (forcing platform-native record re-save) is no longer a relevant optimization on the current engine
