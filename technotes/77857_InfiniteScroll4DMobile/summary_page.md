# Tech Note 17-18: Build Infinite Scroll of records with 4D Mobile

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** September 26, 2017 | **Product/Version:** 4D Mobile v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77857
**Download:** https://kb.4d.com/DLTN/TN/2017/17-18_4DMobileInfiniteScroll.zip

## Proposition
This Tech Note explains 4D Mobile's paginated REST entity collections ($top/$skip, nextPage()/prevPage()/more()) and demonstrates implementing infinite-scroll record lists using both the Angular-Wakanda framework and plain jQuery/Ajax.

## Key Points
- **Default pagination:** 4D Mobile REST returns 40 records per call by default via $top/$skip parameters.
- **Entity collection JSON:** responses include metadata (__ENTITYSET, __COUNT, __SENT, __FIRST) alongside the actual entity data.
- **Lazy-loading helpers:** nextPage(), prevPage(), and more() methods fetch additional pages on demand.
- **Angular-Wakanda implementation:** shows building an infinite-scroll-ready UI and wiring scroll detection to pagination calls.
- **jQuery/Ajax implementation:** a framework-agnostic alternative for non-Angular web clients.
- **Performance rationale:** avoids unnecessary network traffic by fetching only what's needed as the user scrolls.

## Featured Technology
- 4D Mobile / Wakanda REST API
- Angular-Wakanda framework
- jQuery and Ajax
- Entity and entity collection JSON model

## Context / Positioning
Published in 2017 during the 4D Mobile / Wakanda era (v16), before 4D discontinued the Wakanda-based mobile stack. This is squarely "classic era" 4D web/mobile development, predating both Project Mode and the ORDA-first REST approach that came later.

## Historical Commentary
**Status:** Obsolete

4D Mobile and its underlying Wakanda framework (including Angular-Wakanda) have been discontinued; 4D's current web/mobile strategy centers on ORDA-exposed REST APIs consumable by any modern frontend, and more recently on the Qodly low-code platform. The pagination concept itself (lazy-loading large collections via $top/$skip) remains a valid pattern conceptually and lives on in ORDA's entity selection paging, but the specific APIs, framework, and code shown in this note no longer apply to current 4D development.
