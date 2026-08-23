# Tech Note: The 4D Web Auction Example Database

- **Asset ID:** 18207
- **Tech Note #:** 01-44
- **Published:** September 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Cha Yang, 4D, Inc. Technical Support Engineer
- **Page URL:** https://kb.4d.com/assetid=18207
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/macos/TN_2001_41-45_(SEP)/01-44_Exploring_Auction_DB.hqx

## Overview

Cha Yang, a 4D, Inc. Technical Support Engineer, tours the 4D Web Auction example database, showing how 4D's tag-based HTML parsing (4DHTMLVAR, 4DVAR, 4DLOOP, 4DIF) drives a real-time, non-contextual bidding interface, plus a SET HTTP HEADER technique for defeating browser/proxy caching of dynamic auction data.

## Key Points

- On Web Connection sends index.htm (a static link page) in contextual mode; clicking through calls the W_GenItemTable method (via a slash-free relative 4DACTION link, contrasted in the note with absolute links that start with a leading '/').
- items.shtm uses <!--4DHTMLVAR vtBidResponse--> to show a status message, <!--4DLOOP [Item]--> to iterate the [Item] table's current selection (populated by ALL RECORDS in W_GenItemTable), and a <!--4DIF--> test on record parity to alternate row background color between two blues for readability.
- Clicking an Item ID link calls W_ViewItem, which queries [Item] for that record and sends bid.shtm -- a form with a hidden Item ID field plus enterable name/amount inputs that posts to W_SubmitBid.
- W_SubmitBid creates a [Bid] record, compares the submitted amount to [Item]Highest Bid, updates the item and sets a congratulatory or a red-highlighted rejection vtBidResponse message accordingly, then re-sends items.shtm with the refreshed selection.
- SetNoCacheHeaders builds fieldArray/valueArray pairs (Pragma: no-cache, Cache-Control: no-cache, Expires: a past date) and calls SET HTTP HEADER before every dynamic page send, which only has effect in non-contextual web mode, to stop browsers/proxies from showing stale bid data.
- Form-submitted values are declared for interpreted/compiled compatibility in the Compiler_Web special method; the note also references GET WEB FORM VARIABLES as an alternative that avoids needing such declarations.

## Featured Technology

- 4D HTML tags: <!--4DHTMLVAR-->, <!--4DVAR-->, <!--4DLOOP-->/<!--4DENDLOOP-->, <!--4DIF-->/<!--4DELSE-->/<!--4DENDIF-->
- Non-contextual web mode with relative vs. absolute 4DACTION links
- SET HTTP HEADER for Pragma/Cache-Control/Expires no-cache headers
- Alternating row-color rendering via 4DIF on record parity
- Real-time bid comparison and record update (QUERY/SAVE RECORD)

## Historical Commentary

**Status:** Obsolete

This note walks through the 4D Web Auction demo (originally by Ruffin Scott, updated for 6.7 by Eric Saltzen), showing how 4D's tag-based HTML parsing (4DHTMLVAR, 4DVAR, 4DLOOP, 4DIF) drives a non-contextual bidding interface with real-time highest-bid comparisons, plus a SET HTTP HEADER-based trick to defeat browser/proxy caching of dynamic pages. Tag-based HTML parsing for dynamic pages is a legacy 4D web-publishing pattern that has been superseded by REST/ORDA APIs paired with modern JS front ends, so the specific approach here is now mainly of historical interest, though the underlying no-cache HTTP header technique is still valid and commonly needed today.

References to newer/updated information:
- 4D's web publishing model has moved from embedded-tag (.shtm) HTML parsing to REST/ORDA APIs consumed by JS front ends
- SET HTTP HEADER itself remains part of the current 4D language and no-cache headers are still set the same way for dynamic pages
