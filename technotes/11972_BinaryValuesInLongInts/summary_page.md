# Tech Note: Storing Binary Values in Long Integers

## Overview
- **Technical Note (number unavailable)**
- **Author:** Unknown / not specified
- **Published:** February 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note presents a compact, space-efficient technique for storing multiple boolean or small-enumeration values inside a single Longint field rather than dedicating a separate field to each flag. It starts from the basic fact that a Longint field is coded in 32 bits, giving it a numeric range of roughly -2,147,483,648 to +2,147,483,648, and observes that those same 32 bits can instead be treated as 32 independent boolean values — the kind of Yes/No, True/False, or Male/Female data that would typically be represented with checkboxes or radio buttons on a form. The note extends this idea further, showing how grouping more than one bit together lets a single Longint field represent multiple-choice data (more than two possible states) as well, rather than being limited to strictly binary flags. It comes with a preliminary caution: the accompanying example database is designed to run in compiled mode, and developers are warned that running it interpreted will seriously impair its performance, reflecting the significant interpreted-versus-compiled performance gap typical of 4D applications in this era. The featured technology is bitwise flag-packing into 4D's native Longint field type, a foundational low-level data-modeling technique. Because only the teaser abstract for this note survives (its kb.4d.com page had no working download link at all), the full example code demonstrating the bit-packing and unpacking logic could not be recovered here.

## Featured Technology
- Longint bit-packing
- Boolean/multi-choice bit flags
- Compiled mode performance

## Historical Context
This note explains how to pack up to 32 individual boolean flags (or multi-bit multiple-choice values) into the bits of a single 32-bit Longint field, a space-efficient technique for representing many yes/no or small-enumeration values without dedicating a separate field to each one. Bitwise packing of flags into integer fields is a general low-level programming technique that remains just as valid in current 4D (Longint/bitwise operators are unchanged), so unlike most other notes in this batch, this one is still directly usable guidance today, though the note's specific warning about needing compiled mode for acceptable performance is less critical on modern hardware.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- 4D's Longint type and bitwise operators used for this technique remain unchanged and fully supported in current 4D versions
- Modern hardware and the current 4D compiler/interpreter performance profile make the note's original compiled-mode-only performance warning less critical than in 2000, though compiled mode still performs better for bit-heavy loops

