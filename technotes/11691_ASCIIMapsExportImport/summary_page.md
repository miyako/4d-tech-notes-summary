# Tech Note 96-09: Using ASCII Maps to Export and Import Data on the Windows Platform

**Author:** Jeff Browning
**Published:** February 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Win
**Page:** https://kb.4d.com/assetid=11691
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_06-10_(FEB)/96-09_ASCII_Map.exe

## Overview
Because 4D always stores and processes text using the **Macintosh ASCII character set internally**, even when running under Windows, exporting or importing data between 4D and Windows text files runs into a translation problem for high-order (128-255) diacritical/symbol characters, which are encoded completely differently across the Macintosh and the many regional Windows ASCII character sets. This Tech Note explains 4D's built-in **ASCII Map** feature, which solves this via a 256-character translation table.

## Key Points
- Low-order ASCII (0-127) is identical across platforms; high-order ASCII (128-255) differs between Macintosh and Windows, and even between different regional Windows code pages.
- An ASCII Map is a 256-character string where **position = character code** and **value = the translated character**; **input maps** (for reading from disk/serial: `IMPORT TEXT`/`DIF`/`SYLK`, `RECEIVE PACKET`) and **output maps** (for writing: `EXPORT TEXT`/`DIF`/`SYLK`, `SEND PACKET`) are mirror images of each other.
- Custom Windows ASCII maps can be built by exploiting the **Altura Mac2Win** porting layer's automatic character translation during copy-and-paste between 4D and Notepad, producing matched `input.4fi`/`output.4fi` documents for any target Windows character set.
- The example database includes a `[Dialogs];"ASCIIMap"` layout and Open/Save scripts (using `RECEIVE PACKET`/`SEND PACKET` on a `.4fi` document) for capturing and saving map data.
- A `[Test]` file plus `PopASCII`/export/import round-trip demonstrates that the maps correctly translate high-order characters both directions.
- In code, maps are activated with `USE ASCII MAP ("mapname"; 0)` for output or `1` for input, guarded by `GET PLATFORM INFO` to apply the maps only when the client is running on Windows ("Wintel").

## Featured Technology
- 4D ASCII Maps (input/output character translation tables)
- `USE ASCII MAP` command
- Altura Mac2Win porting layer (automatic copy-paste character translation)
- `IMPORT`/`EXPORT TEXT`, `DIF`, `SYLK`; `RECEIVE`/`SEND PACKET`

## Historical Context
Published February 1996 for 4D v3.x, this note reflects a genuinely thorny cross-platform text encoding problem of the pre-Unicode era: with no shared universal character encoding standard in wide use yet, and dozens of incompatible national Windows character sets in circulation, 4D's internal commitment to the Macintosh character set (even on Windows, via the Altura Mac2Win layer) made explicit translation tables a practical necessity for any data interchange with the Windows world.

## Historical Commentary
**Status:** Obsolete

This entire class of problem — reconciling the Macintosh ASCII character set with assorted regional Windows ASCII character sets — has been obsolete for a long time, since modern 4D and virtually all contemporary software use Unicode (UTF-8/UTF-16) universally, eliminating platform-specific high-order character mismatches entirely. The Altura Mac2Win porting layer this note leans on for building custom maps, and the ASCII Map feature/`USE ASCII MAP` command itself, are relics of a pre-Unicode 4D architecture no longer central to current 4D development.

