# Tech Note: Architecture of Variables in Blobs (TN 00-58)

**Author:** Not specified in source document
**Published:** December 1, 2000 | **Product/Version:** 4D v | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11943
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/Windows/TN_2000_56-60_(DEC)/00-58_4D_Variables_in_BLOBs.exe

## Overview
This Tech Note covers a description of the internal byte-level architecture 4D uses to store variables inside a BLOB.

## Key Points
- Its proposition is essentially documentation of an internal format: rather than teaching a development technique or feature usage pattern, it aims to demystify exactly how different variable types (strings, numbers, dates, and so on) get encoded into the raw bytes of a BLOB, information that would be essential for any developer needing to manually construct or parse BLOB data outside of 4D's own automatic VARIABLE TO BLOB/BLOB TO VARIABLE-style conversion commands — for instance, when interoperating with external systems, other applications, or custom file formats that need to read or write 4D-compatible BLOB-encoded variable data.
- Because the download link points to a legacy Windows self-extracting .exe archive that cannot be extracted in this environment, only the short teaser sentence survives here, so the specific byte-layout details, type-by-type encoding rules, and any accompanying example code are not preserved in this archive.
- Featured technology is squarely 4D's internal BLOB serialization format and the variable-to-BLOB conversion mechanism as it existed in the 4D v6.5-era engine.
- This kind of low-level internals note served a narrower, more advanced audience than most Technical Notes — developers doing byte-level data interchange, file format work, or debugging serialization issues — rather than the broader audience targeted by feature tutorials or UI technique notes.
- As an internal-format reference tied to a specific historical version of the 4D engine, its precise byte-layout details should not be assumed to still hold in current 4D releases, even though the general concept of variables being serializable into a compact binary representation remains valid.

## Featured Technology
- BLOB storage format
- Variable serialization
- Memory/byte-layout internals

## Historical Context
This note describes the internal, byte-level layout 4D used to serialize variables into a BLOB in the classic v6.5 era, useful for developers needing to manually parse or construct BLOB-encoded variable data (for interchange, storage, or interoperability purposes). Such low-level internal serialization formats are inherently implementation-specific and subject to change across 4D versions, so while the note is a useful historical reference for that specific era's BLOB variable layout, it should not be assumed to reflect current internal formats; modern 4D applications favor higher-level serialization approaches (e.g., JSON, objects/collections) over manually parsing BLOB byte layouts. Related updates since: 4D has since added higher-level, more portable serialization options (objects, collections, JSON) that are generally preferred over manually parsing raw BLOB byte layouts; Internal BLOB/variable byte-layout details are implementation-specific and have likely changed across the many 4D versions released since 2000. The full Tech Note PDF/text could not be recovered for this archive entry because the linked archive was an old Windows self-extracting .exe installer that could not be extracted without a Windows environment; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
