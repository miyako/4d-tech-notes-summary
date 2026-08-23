# Tech Note: Building Interactive Graphic Interfaces with 4D Draw, Part II

- **Asset ID:** 11878
- **Tech Note #:** 99-47
- **Published:** November 1, 1999
- **Product / Version:** 4D Draw 6.5
- **Platform:** Mac & Win
- **Author:** Tim Tonooka
- **Page URL:** https://kb.4d.com/assetid=11878
- **Download:** https://kb.4d.com/DLTN/TN/1999/MacOS/TN_1999_47-50_(NOV)/99-47_Graphic_Interfaces_2.hqx

## Overview

Tim Tonooka (ACI Technical Support) continues a 4D Draw interactive-graphics series with Part II, digging into the "v65Trace" example database's BMP Picture Properties feature and, specifically, how the database thoroughly validates a user-selected BMP file's header before trusting and reading it.

## Key Points

- `DRW_BMPInfoWindow` uses the "start-if-not-running" pattern: when called with no parameters (from the menu), it starts a new named process via `New process(...; *)`, whose asterisk parameter reuses an already-running process of the same name instead of starting a duplicate, then calls `BRING TO FRONT` to surface it.
- `DRW_BMPReadF` shows a standard Open File dialog restricted to BMP files via the ACI_Pack `AP Select document` command, using a platform check (`IFC_PlatformIsWindowsF`) to supply a 3-letter ("BMP") vs. 4-letter ("BMP ") type code array as required by Windows vs. Macintosh.
- Before reading the file, `DRW_BMPFileValidateF` opens it with `Open document` (not `DOCUMENT TO BLOB`) specifically to avoid an out-of-memory risk if the file turns out to be much larger than expected, then reads only the first 34 bytes via `RECEIVE PACKET` into a text variable.
- That header text is converted into a BLOB with `TEXT TO BLOB` so each byte can be indexed numerically (avoiding slower `Substring`/`Ascii` calls on a text variable), then validated in a cascading chain of checks: the two-byte "BM" signature, whether the header's stated file size (`BLB_GetBMPFileSizeF`) matches the actual size from `Get document size`, the header-size field equaling 40 (Windows 3.x/NT BMP), 8 bits-per-pixel (`BLB_GetBMPBitsPerPixelF`), a compression code of 0 (uncompressed, also ruling out Windows NT BMP), and positive image width/height values, plus a final check that the computed needed file size fits within a longint (MAXLONG).
- A custom `BLB_GetDWordF` helper method is deliberately written to read 32-bit values in either byte order, since Windows uses little-endian and Macintosh uses big-endian — making it reusable across other projects needing cross-platform binary parsing.
- Only after every validation test passes does the code call the ACI_Pack `AP Get picture type` command (checking for return value 5, the BMP type code) and then `AP Read picture BLOB` to convert the validated BMP BLOB into a displayable 4D picture variable.
- The note emphasizes that this layered validation is thorough enough that a non-BMP or malformed file is extremely unlikely to pass all tests, and even in the worst case would only produce an unattractive picture rather than a fatal error.

## Featured Technology

- New process for a background BMP Picture Properties window
- AP Select document / AP Get picture type / AP Read picture BLOB (ACI_Pack plug-in)
- RECEIVE PACKET for reading a document header without loading the whole file
- TEXT TO BLOB for fast byte-level header inspection
- BLB_GetDWordF cross-platform (little/big-endian) DWord reader
- Manual BMP header validation (signature, file size, version, bits-per-pixel, compression, dimensions)

## Historical Commentary

**Status:** Obsolete

The second installment in a three-part 4D Draw series, this note focuses entirely on defensively validating a user-selected BMP file before trusting it: checking its OS type code, reading just the first 34 bytes with RECEIVE PACKET to avoid loading an oversized file into memory, and manually decoding the BMP header's "BM" signature, stated vs. actual file size, version, bits-per-pixel, compression flag, and image dimensions using a hand-written, byte-order-aware BLB_GetDWordF helper. 4D Draw itself was discontinued long ago, so the specific plug-in commands (ACI_Pack's AP Select document, AP Get picture type, AP Read picture BLOB) are gone, but the underlying discipline of validating an untrusted file's header before parsing it (reading a small chunk, checking magic bytes, cross-checking stated vs. actual size) remains sound defensive-programming practice, even though modern 4D provides built-in, cross-platform picture-handling commands that make manual BMP header parsing unnecessary for ordinary image loading.

**References to newer/updated information:**
- 4D Draw was discontinued and removed from the 4D product line, along with the ACI_Pack plug-in commands (AP Select document, AP Get picture type, AP Read picture BLOB) used in this note
- Modern 4D provides built-in picture-variable and BLOB commands that handle standard image formats natively, without needing hand-rolled BMP header validation as shown here
- The defensive pattern of reading a small header chunk first and validating magic bytes/size/version before trusting a file remains good general practice, independent of 4D Draw
