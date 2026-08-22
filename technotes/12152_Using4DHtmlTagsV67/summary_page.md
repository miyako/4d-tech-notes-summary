# Tech Note 01-01: Using 4D HTML Tags in Version 6.7

**Author:** Not specified in source document
**Published:** January 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12152
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_01-05_(JAN)/01-01_4D6.7_HTML_Tags.exe

## Overview
A comparison of v6.7's new web server features for implementing semi-dynamic pages against the older v6.5 technique described in TN 36-00. This technical note describes an approach to implementing semi-dynamic web pages that takes advantage of new web server features introduced in 4D v6.7.

## Key Points
- To make the improvement concrete, it explicitly compares the v6.7 technique against the older approach used in v6.5, which had been described in an earlier Tech Note (36-00), highlighting the added convenience the new version's features bring to embedding dynamic content within otherwise static HTML pages.
- The featured technology is 4D's classic HTML-tag-based web serving mechanism (predecessor to later 4DACTION/4DTAGS conventions), aimed at developers who wanted pages that were mostly static but needed a handful of dynamically generated values or sections without committing to a fully Contextual Mode session-driven page.

## Featured Technology
- 4D HTML tags (4DACTION/4DVAR-style)
- 4D Web Server (semi-dynamic page generation)
- Comparison with v6.5 technique (TN 36-00)

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Obsolete

This note describes implementing semi-dynamic web pages using 4D v6.7's then-new web server tag features, explicitly contrasting the improved v6.7 convenience against the older v6.5-era technique from TN 36-00. This entire generation of 4D-tag-based, HTML-embedded server-side page generation has been superseded by 4D's later shift to REST APIs built on ORDA, paired with modern client-side JavaScript frameworks or low-code tools like Qodly, making the specific mechanism in this note obsolete for current web development even though semi-dynamic page generation as a general goal remains common.

**Related updates since:**
- 4D's web publishing strategy has moved decisively from embedded HTML tag/4DACTION-style page generation to REST APIs built on ORDA consumed by modern JavaScript front-ends
- 4D Qodly Studio now offers a low-code alternative for building dynamic web interfaces, further superseding hand-coded 4D HTML tag techniques

