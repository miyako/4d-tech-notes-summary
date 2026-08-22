# Tech Note 07-35: 4D Ajax Framework Apartment Demo

**Author:** Joe Resuello, Technical Marketing Engineer, 4D Inc.
**Published:** September 5, 2007 | **Product/Version:** 4D Web 2.0 Pack v1.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47446
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_35-38_(SEP)/07-35_4DAF_Apartment_Demo.zip

## Overview
A hands-on, five-section tutorial for building an apartment-listing Web 2.0 application on top of the 4D Ajax Framework (4DAF), combining an Image Matrix photo grid, the Data Filler, and a Google Maps iframe.

## Key Points
- **Section 01 Setup:** install 4DAF into "AptDemo.4DB" and copy provided HTML/image assets into the `dax` folder.
- **Section 02 Login:** add an automatic guest login via the `<body onload>` attribute, matched by a check in the `DAX_DevHook_Login` developer hook so the "Guest"/"Apt" credentials are accepted.
- **Section 03 Image Matrix:** declare a 4DAF `dataMatrix` JavaScript object bound to the `[Listing]` selection, with header/content templates built from field placeholders (e.g. `[Listing]City`, `[Listing]Photo`), embedded into a page `<div>`.
- **Section 04 OnClick:** use `ImageMatrix.onCellClick` plus the 4DAF Data Filler to populate a details area with the clicked record's data.
- **Section 05 OnDblClick:** extend the handler to also load a Google Maps URL (built from the record's address) into an `<iframe>`.
- Each section ships a folder with the completed files so developers can compare/checkpoint their progress.

## Featured Technology
- 4D Ajax Framework (4DAF) / 4D Web 2.0 Pack
- Image Matrix (`dataMatrix`) object
- Data Filler
- Google Maps iframe embedding

## Historical Context
Published in September 2007, near the tail end of the 4D Web 2.0 Pack's active development, shortly before 4D v11 shipped its own SQL engine. The tutorial assumes 4D's classic Design Mode structure and predates Project Mode and ORDA by roughly a decade.

## Historical Commentary
**Status:** Obsolete

The 4D Ajax Framework and 4D Web 2.0 Pack have been fully discontinued, so the specific installation steps, developer hooks, and `dataMatrix`/Data Filler JavaScript objects described here no longer exist in any current 4D product. However, the general application pattern it teaches — a clickable photo grid of listings, a details panel populated on selection, and a map tied to the selected record's address — remains a completely standard web app design, now implemented with modern JS frameworks or 4D's current web/Qodly tooling instead of 4DAF.
