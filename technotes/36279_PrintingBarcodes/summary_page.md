# Tech Note: Printing Barcodes

- **Asset ID:** 36279
- **Tech Note #:** 05-08
- **Published:** February 24, 2005
- **Product / Version:** 4D 2004.1
- **Platform:** Mac & Win
- **Author:** Thomas Maul
- **Page URL:** https://kb.4d.com/assetid=36279
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_05-11_(FEB)/05-08_Printing_Barcodes.hqx

## Overview

Thomas Maul (General Manager, 4D Germany) provides a source-included 4D component for generating barcode pictures across nearly all common 1D symbologies (Industrial/Interleaved 2 of 5, Code 39, Code 128 A/B/C, EAN-8/13, UPC-A/E, and supplements) through a single Barcode_Create command, alongside detailed symbology reference material including the 2005 US/Canada EAN-UPC 'Sunrise' convergence rules.

## Key Points

- Barcode_Create(barcodetype; code; createchecksum; showchecksum; printcode; {chartarea}) → Picture generates a barcode for any of: Industrial 2 of 5, Interleaved 2 of 5, Code39, Code128A/B/C, EAN8, EAN13, UPC-A, UPC-E, Supplemental2, Supplemental5.
- Barcode_Calc_Checksum(barcodetype; code) → Checksum independently computes/validates a checksum, e.g. to detect a mistyped EAN-8 number before printing.
- Detailed per-symbology reference: supported characters, max length, whether a checksum is mandatory/optional, real-world usage (USPS, LOGMARS/US DoD, retail EAN/UPC/ISBN/ISSN/ISMN), and UPC-A ↔ UPC-E lossless conversion rules.
- Covers the January 1, 2005 'Sunrise' rule change requiring US/Canada POS systems to read EAN-8/13 alongside UPC-A/E, plus the GTIN 14-digit leading-zero convention (which the component automatically strips for printing).
- Rendering uses a reusable 4D Chart offscreen area (CT New offscreen area/CT New Document/CT Delete offscreen area) — reuse benchmarked at ~2 seconds for 100 EAN codes vs. ~5.5 seconds when recreating the area each time.
- Improves inkjet print quality by generating the picture 3-4x oversized then converting to a bitmap (picture | picture) and scaling back down (picture * (1/scale)), rather than printing at native 72 dpi vector resolution.
- Six tunable variables control manual sizing/appearance: Barcode_Width, Barcode_Height, Barcode_Add, Barcode_Font, Barcode_FontSize, Barcode_FontOffset — used when Barcode_Width isn't left at 0 (automatic).
- Addendum notes barcode fonts (commercial or free GNU-licensed PostScript Type 1 fonts) as an alternative, with the tradeoff of needing font installation on every client machine.

## Featured Technology

- Barcode_Create component method (Industrial/Interleaved 2 of 5, Code 39, Code 128 A/B/C, EAN-8/13, UPC-A/E, supplements)
- Barcode_Calc_Checksum component method
- 4D component built with 4D Insider 2004.1
- 4D Chart offscreen area for picture generation (CT New offscreen area / CT New Document / CT Delete offscreen area)
- UPC-A to UPC-E conversion and GTIN leading-zero handling
- Bitmap upscaling technique (picture | picture, picture * scale) for inkjet print quality

## Historical Commentary

**Status:** Partially Superseded

Thomas Maul (General Manager, 4D Germany) delivers a genuinely comprehensive component — with source — for generating the full range of common 1D barcode symbologies (Industrial/Interleaved 2 of 5, Code 39, Code 128 A/B/C, EAN-8/13, UPC-A/E and their supplements) as 4D pictures via a single Barcode_Create call, built around a reusable 4D Chart offscreen area and including the then-critical 2005 'Sunrise' EAN/UPC/GTIN convergence rules for US point-of-sale systems. The barcode-generation technique (rendering via an offscreen 4D Chart area, then converting to bitmap for inkjet print quality) is a classic-4D-era workaround; today, developers more commonly rely on dedicated barcode-generation libraries, PDF-generation tools, or 4D Write Pro/print-form integration with barcode fonts or images produced by external services, though the technical/symbology background this note documents is timeless and still accurate.

References to newer/updated information:

- The 4D Chart offscreen-area picture-generation technique is a classic-4D-era approach; many modern 4D projects instead use dedicated barcode plugins/components, barcode fonts, or externally generated barcode images/PDFs
- The barcode symbology and checksum reference information (Code 39/128, EAN/UPC rules, the 2005 Sunrise GTIN convergence) remains accurate today regardless of the 4D-side rendering technique used
