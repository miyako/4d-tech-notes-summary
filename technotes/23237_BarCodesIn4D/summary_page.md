# Tech Note: Bar Codes

- **Asset ID:** 23237
- **Tech Note #:** 02-20
- **Published:** May 15, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Eric Juhel, 4D Developer
- **Page URL:** https://kb.4d.com/assetid=23237
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_20-24_(MAY)/02-20_Bar_Codes.hqx

## Overview

Eric Juhel demonstrates a from-scratch technique for creating, displaying, and printing bar codes in 4D that match real-world standards -- Code 39 (EAN 39), Code 128 (EAN 128), UPC, and EAN-13 -- using nothing more than the 4D picture library, choice lists, and array/string commands, with no plug-in required.

## Key Points

- The whole technique hinges on storing two 1x1 pixel pictures in the picture library (one black, one white); characters are built by concatenating these tiny pixel pictures side by side, then vertically resizing the assembled strip (e.g. `$picture:=$picture*/60`) to the correct bar-code height.
- Code 39 (EAN 39) encodes 43 characters (0-9, A-Z, and symbols like `_ . * / % $ +`) with each character represented by 9 elements (5 bars on even ranks, 4 spaces on odd ranks); wide elements are simulated by tripling the pixel width (`$pixel:=$pixel*+3`).
- A documented printing-width formula for Code 39 accounts for margins (M1/M2, at least 6mm or 10x narrow-element width), the number of characters N, and the narrow-element width W and wide-ratio R.
- The `EAN_EditBarcode_39` project method loops through the input string, uses `Find in array` against a `Characters_Set_39` choice list (keyed by ASCII code via `LIST TO ARRAY`) to fetch each character's 9-element pattern, and optionally appends a modulo-43 checksum control character.
- Code 128 (EAN 128) encodes 103 ASCII characters using three encoding modes -- Code A (uppercase only), Code B (mixed case), Code C (paired digits) -- with an 11-element bar/space pattern per character and a mandatory modulo-103 weighted checksum; the `EAN_Edit_Barcode_128` method builds the encoded string with `Char(135)` (start) and `Char(138)` (stop) framing characters.
- UPC and EAN-13 are also covered as numeric-only, fixed-length codes (UPC-A: 12 digits, UPC-E: 6 digits, EAN-13: 13 digits, EAN-8: 8 digits) using the same black/white pixel-concatenation principle.
- Error handling throughout uses `ALERT` for missing choice lists, missing library pictures, or empty input strings, returning a numeric `$error` code from each function.

## Featured Technology

- Code 39 (EAN 39) bar code encoding
- Code 128 (EAN 128) bar code encoding
- UPC and EAN-13 bar code encoding
- 1x1 pixel picture library resizing technique
- GET PICTURE FROM LIBRARY / LIST TO ARRAY choice-list lookups
- Modulo checksum calculation for control characters

## Historical Commentary

**Status:** Superseded

Eric Juhel's note shows a clever, low-level technique for generating scannable bar codes purely from 4D's picture library and array/string manipulation: a single black and a single white 1x1 pixel picture are horizontally concatenated and vertically stretched to build Code 39, Code 128, UPC, and EAN-13 symbols entirely without a plug-in. Bar codes and this general automatic-identification use case remain extremely common today, so the topic itself is still directly relevant, but 4D has long since gained plug-ins, bar code fonts, and later native rendering/PDF capabilities that make this manual pixel-concatenation approach unnecessary; most modern 4D bar code needs are met with a bar code font or a dedicated component instead of hand-rolled picture math.

References to newer/updated information:
- Modern 4D applications typically generate bar codes with dedicated bar code fonts or components rather than hand-building them pixel-by-pixel from the picture library as shown here
- Bar codes remain in widespread real-world use (alongside QR codes and RFID), so the underlying need this note addresses is still relevant even though the implementation technique is dated
