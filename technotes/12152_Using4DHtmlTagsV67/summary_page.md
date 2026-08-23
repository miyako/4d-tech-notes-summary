# Tech Note: Using 4D HTML Tags in Version 6.7

- **Asset ID:** 12152
- **Tech Note #:** 01-01
- **Published:** January 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Hugo Fournier
- **Page URL:** https://kb.4d.com/assetid=12152
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_01-05_(JAN)/01-01_4D6.7_HTML_Tags.hqx

## Overview

Hugo Fournier of 4D, Inc. Technical Support shows how 4D v6.7's new HTML tags — 4DLOOP/4DENDLOOP, 4DVAR/4DHTMLVAR, and 4DSCRIPT — let a data-driven web page be published by parsing a static HTML template stored on disk, replacing the far more elaborate manual string-substitution technique used in the earlier TN 00-36 for the identical published content.

## Key Points

- <!--4DLOOP [Chapters]-->...<!--4DENDLOOP--> repeats the enclosed HTML block once per record in the current selection of the named table, eliminating manual duplication of placeholder HTML.
- <!--4DVAR [Chapters]Title--> and <!--4DVAR [Templates]IP_Address--> insert field values directly into the parsed HTML during the loop.
- <!--4DSCRIPT/Set_Space--> executes a 4D method once per loop iteration; the Set_Space method replaces spaces in the chapter title with "%20" so it can be safely embedded in a URL, and the result is exposed via <!--4DHTMLVAR NoSpace-->.
- A similar technique with a NO_CRs method converts a paragraph field's carriage returns into "</p><p>" tags, exposed via <!--4DHTMLVAR NoCRs-->, to preserve paragraph breaks in the rendered page.
- The Welcome method manages selection state (ALL RECORDS/QUERY/ORDER BY/RELATE MANY) depending on whether a chapter parameter ($1) was passed from a clicked link, then calls SEND HTML FILE("static.shtml") to parse the on-disk template using the Web Folder as HTML root.
- Positions the new tags as a direct, much simpler replacement for the fully-dynamic, string-replacement-heavy approach used in TN 00-36 (36-00), while producing identical published output.

## Featured Technology

- 4DLOOP / 4DENDLOOP HTML tags
- 4DHTMLVAR / 4DVAR HTML tags
- 4DSCRIPT HTML tag
- SEND HTML FILE command
- Semi-dynamic .shtm(l) page parsing
- Web Folder as HTML root

## Historical Commentary

**Status:** Obsolete

Written by Hugo Fournier of 4D, Inc. Technical Support, this note contrasts 4D v6.5's fully-dynamic, string-replacement-heavy web publishing technique (from the earlier TN 36-00/00-36) with the new 4DLOOP/4DHTMLVAR/4DSCRIPT tags introduced in 4D v6.7, which let a static HTML template stored on disk be parsed and populated directly from table selections with far less manual string handling. This entire generation of 4D-tag-based, HTML-embedded server-side page generation has since been superseded by 4D's move to REST APIs built on ORDA paired with modern JavaScript front-ends (and more recently Qodly), making the specific tags shown here obsolete for current web development even though the general goal of semi-dynamic, data-driven page generation remains common.

**References to newer/updated information:**
- 4D's web publishing strategy has moved from embedded HTML tags (4DLOOP/4DVAR/4DSCRIPT) to REST APIs built on ORDA consumed by modern JavaScript front-ends
- 4D Qodly Studio now offers a low-code alternative for building dynamic web interfaces, further superseding hand-coded 4D HTML tag techniques
