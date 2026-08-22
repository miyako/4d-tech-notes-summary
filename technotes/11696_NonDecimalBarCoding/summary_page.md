# Tech Note 96-15: Using Non-Decimal Numbers for Bar Coding and Other Purposes

**Author:** Kent Wilbur
**Published:** March 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11696
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_11-15_(MAR)/96-15_NonDecimal_Numbers.exe

## Overview
This Tech Note addresses converting numbers into non-decimal bases in 4D — motivated chiefly by Code 39 bar code generation, which represents data using a 36-character (base-36) alphabet — since 4D had no built-in support for non-decimal numeric representations at the time.

## Key Points
- Presents two custom methods, `BA_ToDecimal` and `BA_FromDecimal`, converting numbers between decimal and any base from binary (base 2) through base 111, using explicit digit-to-character mapping arrays.
- **Motivating use case:** Code 39 bar codes encode information in base 36 (digits 0-9 plus A-Z); converting a value to base 36 and rendering it with the **Adobe CodeThirtyNine** bar code font produces a scannable bar code from ordinary text output.
- Includes a **speed test** comparing conversion performance across different target bases, giving developers a sense of the runtime cost of encoding larger volumes of values.
- The base-conversion methods are explicitly framed as generically reusable for any application needing non-decimal number representations, not just bar coding.

## Featured Technology
- Custom base-conversion methods (`BA_ToDecimal`, `BA_FromDecimal`)
- Code 39 bar code encoding (base 36)
- Adobe CodeThirtyNine bar code font
- 4D method-based performance/speed testing

## Historical Context
Published March 1996, this note reflects a period when generating bar codes in 4D required a hand-rolled combination of custom numeric-base conversion logic and a specialized bar-code font, since neither 4D nor typical printers offered dedicated, built-in bar code generation support.

## Historical Commentary
**Status:** Historical interest only

The mathematics behind the base-conversion methods (`BA_ToDecimal`/`BA_FromDecimal`) remains entirely correct and could still be used as general-purpose utility code today. However, the overall bar-coding workflow it supports — converting to base 36 and rendering through a specific bar-code font — has been superseded by dedicated bar-code generation plugins, libraries, and printer-native bar-code support, making the specific technique of primarily historical interest rather than a recommended current practice.

