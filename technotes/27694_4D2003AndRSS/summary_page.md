# Tech Note: 4D 2003 and RSS

- **Asset ID:** 27694
- **Tech Note #:** 03-20
- **Published:** April 16, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Gou Yang, 4D Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=27694
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_16-20_(APR)/03-20_4D_2003_and_RSS.hqx

## Overview

Gou Yang demonstrates using 4D 2003's brand-new native XML-parsing commands to retrieve and republish RSS feeds, since RSS is itself an XML dialect. The note covers three RSS versions -- 0.91, 1.0, and 2.0 -- with working sample methods for each, storing parsed items into an `[RSS]` table and republishing them via a generated HTML page.

## Key Points

- Explains that RSS is XML, and that this note builds on the general XML-parsing techniques from the earlier Tech Note #03-6, "Parsing XML Documents."
- Covers RSS versions 0.91, 1.0, and 2.0 out of seven total historical versions, explicitly noting the other four (0.90, 0.92, 0.93, 0.94) as obsolete, while observing that 0.91 remained popular even after being technically superseded by 2.0.
- The `RSS_1` method (credited to Justin Leavens of Lizeric Inc., modified by Yang) parses 0.91/2.0 feeds: `Parse XML source`, optional `GET XML ATTRIBUTE BY NAME` for the version, then nested `Get First XML element`/`Get Next XML element` loops to locate `Item` tags and extract `Title`, `Link`, `Description` values.
- Parsed items are upserted into an `[RSS]` table: queried by `Headline`, and if absent, a new record is created using a `[Counter]` table to generate a sequential `RSS_ID`; if found, the existing record's fields are simply updated.
- `CLOSE XML($XMLSource)` is called at the end of parsing to release memory allocated for the XML document, explicitly flagged as necessary to avoid a memory leak.
- RSS 1.0 requires a different method (`RSS_2`) because its `<Item>` tags sit at the same hierarchy level as `<Channel>` rather than nested inside it, so the traversal logic switches on `$SName="Item"` versus `$SName="Channel"`/`"image"` at the top loop level instead of drilling one level deeper.
- Presents a five-step breakdown of the parsing technique: (1) get the source reference, (2) locate the `Item` tag by looping `Get First/Next XML element`, (3) extract Title/Link/Description within an Item, (4) store values into `[RSS]` fields and save the record, (5) clean up memory with `CLOSE XML`.
- The front-end lets a user pick a feed source (4DToday's live RSS 0.91 feed, or xml.com's public sample feeds for 0.91/1.0/2.0), dispatching to `RSS_1` or `RSS_2` accordingly, then calls `SEND HTML FILE("RSS.html")` to publish the parsed, ID-ordered results as a web page.

## Featured Technology

- RSS 0.91 / 1.0 / 2.0 feed parsing
- Parse XML source command (4D 2003)
- Get First XML element / Get Next XML element commands
- CLOSE XML command (memory cleanup)
- GET XML ATTRIBUTE BY NAME command
- SEND HTML FILE for publishing parsed feed content

## Historical Commentary

**Status:** Partially superseded

Gou Yang shows how to use 4D 2003's brand-new native XML parsing commands to retrieve, parse, and republish RSS feeds (versions 0.91, 1.0, and 2.0), including the key structural gotcha that RSS 1.0 places its Item elements at the same hierarchy level as Channel rather than nested inside it. The specific low-level, tag-by-tag traversal technique shown (Parse XML source / Get First XML element / Get Next XML element / CLOSE XML) still exists in 4D and would still function, but RSS itself has faded significantly as a syndication format since its 2000s peak, and current 4D development would more likely use 4D's higher-level XML-to-object/collection conversion commands or JSON-based feeds/APIs instead of this manual element-walking approach. The note is best read today as a snapshot of early, foundational XML support in 4D rather than a recommended pattern for new feed-parsing code.

References to newer/updated information:
- 4D has since added higher-level XML handling (e.g., converting XML directly to 4D objects/collections) that avoids the manual Get First/Next XML element tag-walking shown here
- RSS adoption has declined substantially since the 2000s in favor of other syndication and API mechanisms (JSON feeds, platform-specific APIs), though RSS 2.0 feeds are still produced by many sites and remain parseable with the general approach shown here
- The core commands used (Parse XML source, Get First/Next XML element, CLOSE XML) remain part of current 4D, so the code in this note would still largely function unmodified
