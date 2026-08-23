# Tech Note: Handling Pictures

- **Asset ID:** 37047
- **Tech Note #:** 05-16
- **Published:** April 25, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Gerard Czwiklinski
- **Page URL:** https://kb.4d.com/assetid=37047
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_12-16_(APR)/05-16_Handling_Pictures.hqx

## Overview

Gerard Czwiklinski (4D S.A.) demonstrates direct, byte-level picture manipulation in 4D by converting a picture to an uncompressed 24-bit BMP inside a BLOB via PICTURE TO BLOB, then implementing flips, rotations, cropping, grayscale, negative, and brightness filters as raw pixel operations on that BLOB, with detailed notes on performance and memory tradeoffs.

## Key Points

- Core technique: `PICTURE TO BLOB(picture;blob;"BMPf")` converts any QuickTime-supported picture format to an uncompressed 24-bit BMP inside a BLOB; `PICTURE PROPERTIES` supplies width/height, and bytes-per-line is computed as `(width*3)+(width MOD 4)` to account for BMP's 4-byte row padding; `BLOB TO PICTURE` converts the modified BLOB back to a displayable picture.
- Vertical and horizontal mirror flips are implemented as simple row/pixel byte swaps within the same-sized original BLOB, since dimensions don't change.
- 90-degree left/right rotations and cropping require allocating a new, correctly sized BLOB (width and height swap for non-square images), copying and patching the 54-byte header's width/height fields with `LONGINT TO BLOB` using PC byte ordering (BMP is inherently a Windows format), then moving pixel bytes into their rotated/cropped positions.
- Grayscale conversion is shown in two forms: a naive average `(R+G+B)/3`, then a perceptually corrected weighted formula `0.3×Red + 0.6×Green + 0.1×Blue` that better matches human color sensitivity; negative inverts each channel (`255 - value`); brightness adds an input value between -255 and 255 to each channel.
- A dedicated performance section shows that explicitly typing the BLOB offset variable as a longint (instead of letting 4D default to real) reduced a negative-filter benchmark from 2340 ms to 307 ms, and keeping calculation operands' types consistent shaved off a further ~50 ms — illustrating 4D's automatic type-coercion cost in tight pixel loops.
- A memory-usage walkthrough shows a 44 KB compressed JPEG can balloon to a 2.25 MB uncompressed BMP (50×), and rotation operations needing a second working BLOB can peak memory usage at 5.5–6.75 MB; mitigation options include precomputing the exact required BLOB size, avoiding unnecessary manual memory bumps (unneeded on 4D 2004's revised memory scheme, unlike 4D 2003/OS 9.2), processing on-disk rather than in RAM, or reconverting the result to a compact format like JPEG afterward.

## Featured Technology

- PICTURE TO BLOB / BLOB TO PICTURE
- 24-bit uncompressed BMP byte layout
- QuickTime-based picture format conversion
- Byte-level pixel manipulation (flips, rotation, crop, grayscale, negative, brightness)
- 4D variable data-typing performance tuning
- Memory footprint analysis for image processing

## Historical Commentary

**Status:** Obsolete

This note is a rigorous, hands-on tutorial in byte-level image processing within classic 4D, complete with concrete before/after performance numbers that make a genuinely useful point about 4D data typing in tight loops. Its core mechanism, however, depends entirely on Apple's QuickTime framework for picture format conversion (`PICTURE TO BLOB`/`BLOB TO PICTURE` with the "BMPf" format), and QuickTime was fully discontinued by Apple around 2016 (including QuickTime for Windows years earlier), making this specific conversion path unavailable in modern 4D on current operating systems. 4D has since implemented its own QuickTime-independent picture format handling, so the same PICTURE TO BLOB command still exists today but no longer relies on the deprecated technology this note describes.

**References to newer/updated information:**
- Apple discontinued QuickTime entirely (including QuickTime for Windows, phased out even earlier) around 2016, removing the technology this note's picture format conversion depended on
- 4D introduced native, QuickTime-independent picture format handling following the 64-bit transition and QuickTime's removal from supported OSes, replacing this specific conversion mechanism
- PICTURE TO BLOB remains part of the current 4D language, but its underlying format-conversion engine is no longer QuickTime-based
