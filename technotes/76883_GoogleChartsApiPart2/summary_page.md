# Tech Note 13-11: 4D and Google Charts API - Part 2

**Author:** Jean-Jacques BLEU, 4D Developer
**Published:** September 23, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76883
**Download:** https://kb.4d.com/DLTN/TN/2013/13-11_4DandGoogleChartAPI2.zip

## Proposition
Building on Part 1, this concluding note shows how to draw Google Charts using live data from a 4D database, and — more significantly — how to render those charts directly inside a 4D Web Area object using `PROCESS 4D TAGS`, entirely without requiring 4D Web Server.

## Key Points
- Demonstrates a pie chart of European country populations sourced from a `[Series_value]` table, switchable between top-5, top-10, and full-list views.
- AJAX requests can carry parameters so the 4D side returns exactly the data slice the user selected.
- Introduces rendering Google Charts inside a **4D Web Area** object rather than requiring a browser + 4D Web Server, broadening which applications can use rich charting.
- Uses the classic `PROCESS 4D TAGS` command with `#4DHTML`, `#4DTEXT`, and `#4DIF` template tags to inject 4D-computed JSON, chart type, title, and 3D/table display options into a cached HTML template.
- JavaScript side loads three Google libraries (JSAPI, core Visualization, and a chart-type-specific package like `corechart`, `gauge`, or `table`) and triggers drawing via `google.setOnLoadCallback`.
- Caching the HTML template avoids rebuilding it on every chart redraw.
- Concludes the two-part series by summarizing the complete stack: HTML, JavaScript, 4D Web Server, AJAX/JSON, Web Area objects, and `PROCESS 4D TAGS`.

## Featured Technology
- Google Charts API / Visualization library (`corechart`, `gauge`, `table` packages)
- 4D Web Area object for in-app chart rendering without a Web Server
- `PROCESS 4D TAGS` with `#4DHTML`/`#4DTEXT`/`#4DIF` template tags
- Cached HTML templates for efficient repeated rendering

## Best Practices Highlighted
1. Parameterize AJAX requests so the same chart infrastructure can serve multiple views (top-5/top-10/full list) of the same underlying data.
2. Cache HTML/JS templates that only need their data payload refreshed, rather than regenerating markup on every draw.
3. Prefer rendering charts inside a Web Area when an application shouldn't require a 4D Web Server license just for data visualization.

## Context/Positioning
Published two weeks after Part 1, this note delivered on the promised practical payoff: real database-driven charts, and a broader deployment story (Web Area, no Web Server needed) for teams without a Web Server license.

## Historical Commentary
**Status:** Partially superseded

The note's central achievement — rendering Google Charts inside a 4D Web Area entirely independent of 4D's own Web Server, driven by real database data — remains a broadly valid architecture today; Web Areas paired with third-party JS charting libraries are still commonly combined this way. The specific mechanism for injecting 4D data into the HTML template, the classic `PROCESS 4D TAGS` command with `#4DHTML`/`#4DTEXT`/`#4DIF` tags, is a legacy templating technique that has been effectively superseded by building JSON payloads with 4D's native JSON commands and injecting them via `WA Evaluate JavaScript` or a lightweight REST/ORDA-backed endpoint — approaches that are more maintainable and less coupled to 4D's older tag-substitution engine.
