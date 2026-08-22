# Tech Note 16-04: Working With Audio Files in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** May 12, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77526
**Download:** https://kb.4d.com/DLTN/TN/2016/16-04_WorkingWithAudioFiles.zip

## Proposition
This note documents the binary structure of WAV and MP3/ID3 audio files and shows how to read and modify their headers, tags, and sample data directly at the byte level using 4D BLOB manipulation, since 4D has no native high-level audio metadata commands.

## Key Points
- **WAV structure:** chunk-based layout, big-endian vs. little-endian field ordering, and raw audio sample data location.
- **MP3/MPEG structure:** file layout plus ID3v1 (fixed trailer) and ID3v2 (frame-based header) metadata tag formats.
- **Byte-level parsing via BLOB:** the 4D implementation reads/writes specific byte offsets rather than relying on any built-in audio command.
- **Endian-aware conversion utilities:** Util_BitConvert and Util_Base10Convert/Revert handle the numeric base and byte-order conversions parsing requires.
- **Information getters and setters** are provided for both WAV and MP3 metadata.
- **Sample database** demonstrates reading and modifying real audio files end to end.

## Featured Technology
- 4D BLOB commands
- Binary/bitwise manipulation in 4D
- WAV file format
- MP3/MPEG Audio Layer & ID3v1/ID3v2 tags

## Best Practices Highlighted
1. Always account for endianness explicitly when parsing multi-byte binary fields.
2. Build small reusable bit/base conversion utilities rather than repeating byte-math inline.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

WAV and MP3/ID3 are stable, well-documented legacy formats that have not meaningfully changed since this note was written, so the format knowledge and byte-level BLOB manipulation techniques described remain directly applicable in current 4D versions. Some of the custom conversion utility methods might be replaceable by newer built-in 4D commands added since 2016, but nothing here has been deprecated or broken by the classic Design Mode-to-Project Mode transition.
