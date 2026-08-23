# Tech Note: Exploring the Chord Tool Example Database

- **Asset ID:** 13195
- **Tech Note #:** 01-20
- **Published:** April 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Eric Saltzen
- **Page URL:** https://kb.4d.com/assetid=13195
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_16-20_(APR)/01-20_Exploring_Chord_Tool.hqx

## Overview

Eric Saltzen (4D, Inc. Technical Support) explores the Chord Tool example database, written by Tad Michael Wheeler of DataCraft, which lets users select musical chords and see the corresponding notes displayed as they would be played on an on-screen piano keyboard. The note's central subject is how 4D objects can be conditionally shown or hidden based on individual bits of a Long Integer value, using bitwise operators to assign an offset (Key) and a bit-field definition (Notes/Construct), plus a tangent on the history of Arabic numerals and the words "algebra" and "algorithm."

## Key Points

- Each chord is represented as bits of a single Long Integer (up to 32 bits available), where each bit's position corresponds to a note; `SET VISIBLE` shows or hides the matching "red dot" form object depending on whether that bit is set.
- The `ChordTool_EncodeChord` project method takes a key number and a construct number, looks up the construct's `Note_2` through `Note_7` fields via `QUERY([Constructs];...)`, and uses the bit-set operator `?+` (`$Result:=$Result ?+ $RootNote`, etc.) to accumulate the chord's bit pattern — worked through with a C Major triad example that yields the decimal value 145.
- The `[Chords]` 'Input' form's Key and Construct pop-up menus (`pKey`, `pConstructs`) rely on 4D's convention that an array has an extra, unindexed storage slot used by pop-ups to track the currently selected item, referenced as `pKey{pKey}` in the `On Clicked` case.
- The note recommends bitwise operators over "longhand" decimal/binary computation because they map directly to underlying assembly bit operations and execute faster, and points to third-party decimal/binary calculators (Calc 98, CalcWorks) as helpful tools.
- A historical digression explains that "Arabic numerals" actually originate from Hindu mathematics, transmitted to Europe via Al-Khwarizmi's writings, and that his name and the term "al-jabr" gave us the words "algorithm" and "algebra" respectively.
- Suggested extensions include incorporating the `[Groups]` table into the UI, precomputing and storing bit-fields per record instead of recalculating them on each key/construct change, and using the `PLAY` command to sound the encoded chords (simultaneously or arpeggiated).

## Featured Technology

- Bitwise set-bit operator (?+)
- Long integer bit-flag encoding
- Conditional object visibility (SET VISIBLE)
- Pop-up menu array selection idiom (array without index)
- QUERY-driven record lookups for musical constructs

## Historical Commentary

**Status:** Still relevant

Eric Saltzen's exploration of Tad Michael Wheeler's Chord Tool example database (originally written for 4D v6) shows how a single long integer can encode which notes of a musical chord are active, using the bit-set operator (?+) to build the value and SET VISIBLE/bit tests to light up the corresponding keys on an on-screen piano, alongside a digression on the history of Arabic numerals. Bitwise operators and long-integer bit manipulation remain fully supported in 4D's classic language today, so the core technique still works unchanged, but modern 4D interfaces more often favor discrete boolean variables, object properties, or list box conditional formatting over hand-packed bit flags for readability and maintainability.

**References to newer/updated information:**
- 4D's bitwise operators (including the set-bit operator ?+) remain unchanged in the current classic language
- Contemporary 4D form design more commonly uses discrete boolean/object variables or list box conditional formatting instead of packed bit-flag visibility schemes
