# Tech Note 96-48: Hexadecimal Notation and Bitwise Operators in V6

**Author:** Gordon Muirhead
**Published:** November 1, 1996 | **Product/Version:** 4D v6.0.x (pre-release, "Developer Release 1") | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11724
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_45-50_(NOV)/96-48_Hex_Notation.exe

## Overview
Part of a series previewing the then-unreleased 4D V6, this note explains three related new language features: hexadecimal display formatting, bitwise operators, and the new BLOB data type, illustrated with an interactive example database.

## Key Points
- **Positional numbering primer:** contrasts decimal, binary, and hexadecimal systems to motivate why hex is a concise, computer-friendly notation for humans.
- **Hex display format:** new "&x"/"&$" format codes display a number as hexadecimal (e.g., decimal 26 as 0x1A or $1A).
- **New bitwise operators:** `&` (And), `|` (Or), `^|` (Xor), `??` (Bit Test), `>>` (Shift Right), `<<` (Shift Left) — with bit-diagram worked examples for And/Or/Xor.
- **Pointer symbol change:** V6 changed the pointer symbol to `->`, freeing up `<<`/`>>` for use as shift operators.
- **BLOB data type:** a byte array up to 2GB (memory permitting), addressed via `MyBlob{byteNumber}` (zero-indexed), usable to store any byte-based content (files, sounds, NC programs) in a 4D record.
- **Worked BLOB example:** reading a file into a BLOB with `DOCUMENT TO BLOB`, then using bitwise operators to decode individual status bits within specific bytes.
- **Example database:** two interactive demo screens (hex/bitwise demo; BLOB decode demo reading a sample file), plus appendix methods (`Hex_str_to_dec`, `pAndOrXor`, `RightArrow`, `bBLOBread`, `Byte_to_binary_number`).

## Featured Technology
- Hexadecimal display format (& x / & $)
- Bitwise operators (&, |, ^|, ??, >>, <<)
- BLOB data type
- 4D V6 language (pre-release)

## Historical Context
**Status:** Still relevant

Unlike many 1996-era Tech Notes, most of this note's core technical content has aged well: the bitwise operators, hex display formats, and BLOB byte-array model it previews all became stable, long-lived parts of the 4D language, largely unchanged since V6's official release. What is dated is the note's framing as pre-release "Developer Release 1" documentation for an unreleased product, and the BLOB-centric approach to raw binary decoding, which modern 4D development often supersedes with more structured object (JSON-like) or ORDA-based data handling for many equivalent tasks.
