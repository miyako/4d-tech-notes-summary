# Tech Note 06-42: Cleaning Whitespace from XML Values

**Author:** David Adams
**Published:** November 20, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=44743
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_40-43_(NOV)/06-42_Clean_XML_Whitespace.zip

## Overview
This note explains a subtle but common gotcha when reading XML in 4D 2004: DOM and SAX element-reading commands return the *complete* value of an element, including leading/trailing whitespace (tabs, line feeds, carriage returns, spaces) that XML authors typically add only to make source documents human-readable. Since 4D's built-in commands offer no automatic trimming, the note supplies a hand-written, efficient trimming utility.

## Key Points
- XML specifies four whitespace characters: Tab (9), Line feed (10), Carriage return (13), Space (32).
- `DOM GET XML ELEMENT VALUE` and `SAX GET XML ELEMENT VALUE` both return whitespace as part of an element's value — this is correct per the XML spec but often unwanted.
- A naive trim (repeatedly calling `Substring`/`Delete string` one character at a time) risks resizing the string multiple times, which is wasteful.
- The note's `XML_CleanWhitespace` function instead makes exactly two scanning passes (front-to-back, then back-to-front) to locate the first/last non-whitespace character, then extracts the result in a single `Substring` call.
- A companion routine, `XML_InitWhitespaceCharacters`, populates an interprocess array of the four whitespace characters so the trimming logic can test characters generically via `Find in array` instead of hard-coded `Case of` comparisons — making the whitespace definition easy to extend later.
- Edge cases (all-whitespace or empty source strings) are explicitly handled to return an empty result.
- Full 4D code listings for both routines are included, along with a sample database.

## Featured Technology
- 4D DOM XML commands
- 4D SAX XML commands
- 4D procedural language string functions (`Substring`, `Find in array`, `Length`)

## Historical Context
Written for 4D 2004, well before 4D's own SQL engine (introduced in v11, 2007), Project Mode (v17, 2018), or ORDA (2018+). The DOM/SAX XML command families discussed here are legacy procedural-language APIs that still exist in modern 4D but are less central given today's prevalence of JSON for data interchange. The core algorithmic idea — single-pass, two-pointer string trimming with a configurable character set — remains a textbook-sound technique regardless of platform.

## Historical Commentary
**Status:** Superseded

The specific problem (no built-in whitespace trimming for DOM/SAX XML values) and its 2006-era solution are tied to 4D's legacy XML command set from before native SQL, Project Mode, or ORDA existed. 4D's language has since gained broader native string utilities, and much day-to-day data interchange has shifted toward JSON, reducing the frequency with which developers hand-roll this kind of XML whitespace cleanup. The underlying trimming algorithm remains a reasonable, still-instructive pattern, but the note's specific command references are dated.
