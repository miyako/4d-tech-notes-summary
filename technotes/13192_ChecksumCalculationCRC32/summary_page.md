# Tech Note: Checksum Calculation – CRC32

- **Asset ID:** 13192
- **Tech Note #:** 01-17
- **Published:** April 30, 2001
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Thomas Maul
- **Page URL:** https://kb.4d.com/assetid=13192
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_16-20_(APR)/01-17_CRC32_Checksum.hqx

## Overview

Thomas Maul (4D Germany) delivers a plug-and-play CRC32 checksum implementation for 4D, intended to simplify a concept previously covered more theoretically by Ruffin Scott in TN 99-11. Rather than requiring developers to understand the CRC math, the note supplies two ready-made project methods that let any database verify the integrity of Blobs and exported/imported documents against corruption from disk/RAM failures, CD-ROM read errors, transfer errors, or human error.

## Key Points

- 4D already checksums every database record internally, alerting the user with "Record is bad..." if a checksum error is detected, but Blobs (introduced in 4D v6) and documents exchanged outside 4D Open (e.g. via FTP/e-mail for Distributed Systems synchronization) are not automatically checked.
- CRC32 (Cyclic Redundancy Check, 32-bit form) is based on the generator polynomial G(x) = x32+x26+x23+x22+x16+x12+x11+x10+x8+x7+x5+x4+x2+x+1, using a precomputed lookup-table approach fast enough for large files in interpreted mode.
- `CRC_CreateTable` builds a 256-element `ARRAY LONGINT(CRC_Table;255)` using nested loops with bitwise AND/XOR and right-shift (`$c:=0xEDB88320 ^| ($c >> 1)`), and only needs to run once since the table never changes.
- `CRC_Calculate` takes a pointer to a BLOB, initializes `$value:=0xFFFFFFFF`, and iterates every byte with `$value:=($value >> 8) ^| CRC_Table{($1->{$i}) ^| ($value & 0x00FF)}`, returning the final 32-bit checksum.
- Benchmarks on a 900 MHz AMD machine: table creation takes about 3 ticks interpreted (too fast to measure compiled); calculating the checksum for a 100 KB file takes ~130 ticks interpreted vs. 5 ticks compiled, and for a 3 MB file, ~4,155 ticks interpreted vs. 145 ticks compiled.
- A practical verification trick: append the computed checksum as 4 bytes directly after the document using `LONGINT TO BLOB`; recomputing the checksum over the entire file (data + appended checksum) yields exactly zero if nothing was corrupted, and the last 4 bytes must be stripped before using the file.

## Featured Technology

- CRC32 checksum algorithm
- CRC_CreateTable / CRC_Calculate project methods
- BLOB bitwise operators (AND, OR, XOR, bit shift)
- DOCUMENT TO BLOB / LONGINT TO BLOB
- File integrity verification for Blobs and exported documents

## Historical Commentary

**Status:** Partially superseded

Thomas Maul's note provides a ready-to-use 4D implementation of the CRC32 checksum algorithm, explicitly aiming to make the technique (previously explained more theoretically by Ruffin Scott in TN 99-11) approachable via two drop-in methods, CRC_CreateTable and CRC_Calculate, without requiring the reader to understand the underlying CRC math. The CRC32 algorithm and its 4D implementation remain functionally valid today, but 4D has since added built-in digest/hash commands that make hand-rolling CRC32 largely unnecessary for new development, and CRC32 itself is a much weaker integrity check than the SHA-family hashes now considered standard for verifying file integrity.

**References to newer/updated information:**
- 4D has since added built-in commands for generating cryptographic digests/hashes, reducing the need to hand-implement checksum algorithms like CRC32 in application code
- Modern file-integrity workflows more commonly rely on standard hash algorithms (SHA-256, etc.) exposed via built-in commands rather than a hand-rolled CRC32 routine
