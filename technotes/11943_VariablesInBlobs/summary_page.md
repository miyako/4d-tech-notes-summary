# Tech Note: Architecture of Variables in Blobs

- **Asset ID:** 11943
- **Tech Note #:** 00-58
- **Published:** December 1, 2000
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Thierry Ozil
- **Page URL:** https://kb.4d.com/assetid=11943
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_56-60_(DEC)/00-58_Variables_in_Blobs.hqx

## Overview

Thierry Ozil (4D S.A. Technical Support) documents the exact byte-level format 4D uses to store variables inside a Blob via VARIABLE TO BLOB, covering type codes, byte ordering, padding rules, and per-type field layouts for scalars and arrays.

## Key Points

- Each 4D variable type is encoded with a specific one-byte type code (Alpha=0, Text=2, Number=1, Integer=8, Long integer=9, Date=4, Time=11, Boolean=6, Picture=3, Subtable=7, Blob=30, plus array variants).
- Byte ordering is platform-dependent: Mac OS is big-endian (most significant byte first) while Windows is little-endian (least significant byte first) — demonstrated with a long integer value that decodes to the ASCII bytes "B","L","V","R" on Mac but the reverse order on PC.
- Alpha (fixed-length) strings are stored as classic Pascal strings: one length byte followed directly by the characters, with no terminating delimiter.
- Real numbers use a 10-byte word length on 68K Macintosh (for backward compatibility, via Apple-supplied conversion routines) versus 8 bytes on PowerPC and Windows; the 64-bit format holds up to 15 significant decimal digits in a 19-digit representation, with the last 4 digits effectively random.
- Structures with an odd byte count receive one extra padding byte so data stays aligned on even (or 4-byte, for AltiVec) address boundaries, improving processor efficiency.
- The Blob layout for a stored variable begins with a four-byte native-variable marker ("RVLB" on Mac OS, "BLVR" on Windows), followed by type-specific fields: e.g. Long Integer (4 bytes + 1 padding byte), Real (10 bytes + 1 padding byte), Time (4 bytes + 1 padding byte), Date (3×2 bytes + 1 padding byte), Alpha (2-byte declared length + Pascal string + possible padding), Text (2-byte length + characters + possible padding), and Picture (4-byte size + contents + possible padding).
- Arrays repeat the four-byte marker, then a type byte, a 4-byte element count, a 4-byte current-selected-element index, and packed per-element data sized per type (e.g. Integer: n×2 bytes; Long Integer: n×4 bytes; Alpha: n×(2+1+chars) bytes), each followed by a padding byte.
- Multiple variables can be packed sequentially into one Blob by calling VARIABLE TO BLOB repeatedly with the same Blob — the offset advances each time and must be tracked by the caller to later locate each variable.

## Featured Technology

- VARIABLE TO BLOB byte-level encoding format
- 4D variable type byte codes (Alpha, Text, Real, Integer, Longint, Date, Time, Boolean, Picture, arrays)
- Mac vs. Windows byte ordering (big-endian vs. little-endian)
- Pascal-string encoding for Alpha variables
- 10-byte (68K) vs 8-byte (PPC/PC) real-number word length and Apple conversion routines
- Byte-level Blob addressing and offset management

## Historical Commentary

**Status:** Historical interest only

This note documents, byte by byte, the exact binary layout 4D uses when a variable of any type (Alpha, Text, Real, Integer, Long Integer, Date, Time, Boolean, Picture, and their array forms) is written into a Blob via VARIABLE TO BLOB, including the four-byte "RVLB"/"BLVR" native-variable marker, per-type field widths, alignment padding rules, and the platform-dependent big-endian (Mac) vs. little-endian (Windows) byte ordering. This is genuinely low-level reference material for anyone parsing or generating 4D Blobs from outside 4D (or across mixed old-format databases), and while VARIABLE TO BLOB/BLOB TO VARIABLE remain in the 4D language, most day-to-day Blob work in modern 4D is now done through higher-level, type-safe object/collection and JSON serialization commands, making this exact byte-format knowledge mostly a historical-interest reference rather than an everyday necessity.

**References to newer/updated information:**
- VARIABLE TO BLOB and BLOB TO VARIABLE remain part of the current 4D language, but modern 4D development favors object/collection types and JSON-based serialization over manual Blob byte-layout parsing for most use cases
- The 68K Mac real-number word-length and byte-ordering discussion is now purely historical, as 4D no longer supports 68K Macintosh hardware
