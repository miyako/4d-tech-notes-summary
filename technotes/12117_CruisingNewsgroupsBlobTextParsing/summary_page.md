# Tech Note: Cruising Newsgroups: Accelerated Text Parsing with BLOBs

- **Asset ID:** 12117
- **Tech Note #:** 01-06
- **Published:** February 28, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Tim Tonooka
- **Page URL:** https://kb.4d.com/assetid=12117
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_06-10_(FEB)/01-06_Cruising_Newsgroups.hqx

## Overview

Tim Tonooka, a 4D Solution Partner, presents the 4D Internet Commands-based '4D News Jockey' Usenet newsreader and uses its uudecode-based binary attachment handling to demonstrate that BLOB variables are not inherently faster than text, but that avoiding repeated BLOB-to-text/text-to-BLOB conversions inside a parsing loop — by operating directly on BLOB bytes with custom methods — yields large real-world performance gains.

## Key Points

- 4D News Jockey uses the 4D Internet Commands plug-in to speak NNTP directly: HELP, LIST ACTIVE, GROUP, ARTICLE/HEAD/BODY, XOVER (batch overview), and QUIT commands are sent and their text replies parsed, similar to how DEFAULT TABLE sets NNTP's implicit newsgroup context via GROUP.
- HIGHLIGHT RECORDS, BOOLEAN ARRAY FROM SET, and LONGINT ARRAY FROM SELECTION (new in 4D v6.5) let the newsreader manage a persistent multi-article selection in a list while preserving sort order across deletions and re-selections.
- A controlled benchmark (filling a 32,000-character text block vs. a 32,000-byte BLOB) showed the BLOB approach was 105% slower on Windows and 180% slower on Mac OS in compiled code, disproving the assumption that BLOBs are inherently faster than text.
- The real performance cost identified is calling BLOB to text and TEXT TO BLOB repeatedly inside a parsing loop; the note's revised code keeps encoded/decoded lines in BLOB variables ($oEncodedLine/$oDecodedLine, sized with SET BLOB SIZE) throughout the loop instead of round-tripping through text each iteration.
- Custom BLOB-native helper methods (e.g., BLB_PositionF) replicate string functions like Position but operate directly on BLOB bytes, avoiding the need to copy substrings out to text variables just to search or compare them.
- The technique is applied to uudecode binary attachment decoding, a task well suited to BLOBs since decoded uuencoded data (images, files) can exceed 4D's 32,000-character text-field limit.

## Featured Technology

- 4D Internet Commands plug-in (NNTP)
- BLOB-native text parsing (avoiding repeated BLOB to text/TEXT TO BLOB conversion)
- Custom BLB_PositionF-style BLOB search methods
- uudecode binary decoding from newsgroup articles
- HIGHLIGHT RECORDS / BOOLEAN ARRAY FROM SET / LONGINT ARRAY FROM SELECTION

## Historical Commentary

**Status:** Historical Interest Only

Written by Tim Tonooka, a 4D Solution Partner, this note documents the '4D News Jockey' Usenet newsreader he built using the 4D Internet Commands plug-in's NNTP support, and uses it as a vehicle to teach a real performance lesson: BLOB variables are not inherently faster than text for string operations, but repeatedly converting between BLOB and text inside a parsing loop (via BLOB to text/TEXT TO BLOB) is extremely costly, so high-volume text parsing (like decoding uuencoded binaries from thousands of newsgroup articles) should be done with custom methods operating directly on the BLOB's bytes. The core lesson about minimizing data-type conversions in hot loops remains valid 4D performance guidance today, but NNTP/Usenet itself is now a niche, largely obsolete protocol, and 4D has since added native JSON, text, and BLOB-adjacent APIs that reduce the need for this specific hand-rolled BLOB-parsing technique for most modern text-processing tasks.

**References to newer/updated information:**
- Usenet/NNTP has become a niche protocol with little contemporary relevance, so the specific 4D News Jockey newsreader application is of historical interest only
- The underlying performance principle — avoid repeated BLOB-to-text/text-to-BLOB conversions inside hot parsing loops — remains valid general 4D performance guidance today
