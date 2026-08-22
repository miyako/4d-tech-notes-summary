# Tech Note 08-21: YouTube API and 4DAF

**Author:** Robert Molina | **Published:** June 4, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.1 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=49987  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_21-24_(JUN)/08-21_4DAF_YouTube.zip

## Proposition
Integrate YouTube video feeds into a 4D Ajax Framework web application by fetching video metadata via the YouTube GData API, storing feed data in 4D BLOB fields, and rendering interactive video grids with playback capabilities using JavaScript and Flash.

## Key Points
- **YouTube API basics:** YouTube provides a GData (Google Data APIs) protocol endpoint at gdata.youtube.com for retrieving standard feeds (top-rated, most-viewed, most-recent, most-discussed, most-linked, most-responded, recently-featured) and custom searches (e.g., by author/channel).
- **Backend feed fetching:** A 4D background process spawned on startup fetches feeds every 3 minutes using 4D Internet Commands to build HTTP GET requests, receive responses, parse out HTTP headers and chunked byte-count markers, and extract the XML feed data.
- **Project method: G_GetYouTubeFeed:** This method constructs the HTTP request string with proper headers, sends it via TCP commands, receives the response into a BLOB, removes HTTP headers and byte-chunk markers, and parses the resulting XML using 4D's XML commands to extract video title, author, thumbnail URL, video embed URL, and description.
- **BLOB storage:** Parsed feed data is stored in arrays and serialized into a BLOB field in a [Feeds] table, with one record per feed type, allowing efficient persistence and retrieval.
- **Developer Created Selections (DCS):** The front-end view is configured with columns for Video Title, Thumbnail, Player Type, Feed Entry, Author, and Content; data is retrieved from the BLOB and passed to the front-end via DAX_Dev_DCS_SetSelection.
- **JavaScript event handling:** The front-end uses 4DAF's Data Grid API (setRowStyle, setColumnStyle, setCellStyle, setGridClass) to manipulate styling; a tab interface allows switching between different feeds; click events on grid cells trigger onCellClickEvent, which embeds the video player if the URL is available.
- **Branding requirements:** The "Powered by YouTube" badge must appear on any page where the YouTube API is used, and it must link back to youtube.com.

## Featured Technology
- YouTube API (GData protocol), now deprecated
- 4D Ajax Framework Data Grid component
- 4D Internet Commands (TCP-level HTTP)
- XML parsing and blob serialization
- JavaScript/4D Data Grid integration
- Flash video embed objects
- Tabbed interface navigation

## Context / Positioning
Published in 2008 for 4D v11 SQL and 4D 2004, this note represents an era when video embedding required direct protocol manipulation and custom JavaScript event handlers. YouTube's GData protocol and 4DAF were both contemporary solutions at the time; the example shows how 4D developers could leverage external web APIs to enhance desktop-to-web application capabilities.

## Historical Commentary
**Status:** Obsolete

YouTube's GData API was deprecated years ago in favor of the YouTube Data API v3, which uses REST and JSON instead of GData and XML. Additionally, the 4D Ajax Framework itself is discontinued and no longer part of 4D's web technology stack, having been replaced by 4D Web Components and the Qodly development environment. Modern 4D applications integrate external APIs using 4D's native HTTP class and modern JavaScript frameworks (React, Vue, Angular) rather than custom AJAX data grids. This note is valuable primarily as a historical reference for understanding the bridge between 4D's database backend and early-2000s web API integration patterns.
