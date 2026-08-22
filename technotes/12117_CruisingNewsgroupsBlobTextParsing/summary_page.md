# Tech Note 01-06: Cruising Newsgroups: Accelerated Text Parsing with BLOBs

**Author:** Not specified in source document
**Published:** February 28, 2001 | **Product/Version:** 4D Internet Commands v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12117
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_06-10_(FEB)/01-06_Cruising_Newsgroups.exe

## Overview
An introduction to the '4D News Jockey' NNTP newsreader example database, showcasing optimized text-parsing techniques in BLOBs to get past 4D's 32,000-character text field limit. This Tech Note introduces the 4D News Jockey example database, a feature-rich Usenet newsgroup reader built by the author as a personal project after finding existing shareware newsreaders lacking.

## Key Points
- Its primary technical focus, however, is on the BLOB-based text-parsing techniques used throughout the application, motivated by the practical limitation that classic 4D text fields cap out at 32,000 characters — a ceiling easily exceeded by, for example, a growing HTML document assembled for web serving.
- The note explains that once that limit becomes a concern, developers need to move their text handling into BLOBs, and that with the right parsing techniques, doing so can also yield substantial performance gains, useful for heavy-duty web serving, document processing, general text parsing, and implementing TCP protocols such as NNTP directly.
- It credits the 4D Internet Commands plug-in v6.7 release with providing the new capabilities that made building a full custom newsreader practical.
- The featured technology is thus BLOB-based text parsing combined with 4D Internet Commands' NNTP support, illustrated through a genuinely substantial example application (with a separate accompanying document providing fuller feature documentation) rather than a narrow single-purpose demo.

## Featured Technology
- 4D Internet Commands (NNTP)
- BLOB-based text parsing
- 4D News Jockey example database
- TCP protocol implementation

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note introduces the '4D News Jockey' example database, a Usenet (NNTP) newsreader built by the author using 4D Internet Commands v6.7, showcasing BLOB-based text-parsing techniques designed to work around the 32,000-character limit of classic 4D text fields — relevant for heavy web serving, document processing, and TCP protocol implementations of the time. Both halves of this note's premise are now obsolete: 4D's text field/variable size limits have been massively expanded in modern versions (removing the original motivation for BLOB-based text workarounds), and Usenet/NNTP newsgroups themselves have become a largely defunct technology in mainstream use, making this note of historical interest primarily as an illustration of period text-processing ingenuity.

**Related updates since:**
- 4D's text field and text variable capacity has been dramatically increased in modern versions, removing the original 32,000-character motivation for BLOB-based text-parsing workarounds
- Usenet/NNTP newsgroups have become a largely obsolete communication medium, diminishing the practical relevance of this note's example application
- 4D Internet Commands' functionality has since been substantially folded into 4D's core language, and modern protocol needs are typically served by HTTP/REST rather than raw TCP/NNTP handling

