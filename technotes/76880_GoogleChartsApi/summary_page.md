# Tech Note 13-10: 4D and Google Charts API

**Author:** Jean-Jacques BLEU, 4D Developer
**Published:** September 9, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76880
**Download:** https://kb.4d.com/DLTN/TN/2013/13-10_4DandGoogleChartAPI.zip

## Proposition
Part one of a two-part series that lays the technical groundwork for integrating Google's free Charts API into a 4D web application, teaching AJAX requests, hand-built JSON responses, and Google's `DataTable`-based chart rendering through a hosted demonstration site.

## Key Points
- Google Charts is built on HTML5/SVG, making it broadly cross-browser/cross-device, and is centered on the `DataTable` class.
- The demonstration site is served by 4D Web Server (`START WEB SERVER` / `OPEN WEB URL`), with a modified version of 4D's default auto-generated web server homepage.
- Step-by-step walkthrough: build an AJAX request in JavaScript → receive/process it in a 4D method → hand-build a JSON response text variable → send it via `WEB SEND RAW DATA` → parse/consume it in the browser.
- JSON responses are constructed manually in 4D by string-concatenating pieces (`json_return:=json_return+"..."`) rather than via structured JSON commands.
- Debugging uses the Firebug Firefox extension's console/DOM inspector to compare 4D's JSON output against a reference object copied from Google's own documentation.
- The note is intentionally slow-paced/educational, aimed at developers with only basic JavaScript familiarity, and explicitly defers rendering real 4D data and Web-Area-hosted charts to Part 2.

## Featured Technology
- Google Charts API / Visualization `DataTable`
- 4D Web Server hosting a small demo website
- Hand-built JSON responses sent via `WEB SEND RAW DATA`
- Firebug console/DOM inspector for JavaScript/JSON debugging

## Best Practices Highlighted
1. Validate hand-built JSON responses against the exact structure a target JavaScript library expects, using browser dev tools to compare objects directly.
2. Load third-party JS chart libraries (JSAPI, Google Visualization) only once and trigger drawing via an `onLoadCallback`, not ad hoc timing.
3. Separate the AJAX/JSON plumbing from the chart-drawing logic so each piece can be tested independently.

## Context/Positioning
Published for 4D v13.3, this note met a common developer request — attractive, interactive data visualization — by walking through free, widely-used third-party JavaScript charting technology paired with 4D's web server.

## Historical Commentary
**Status:** Partially superseded

Integrating third-party JavaScript charting libraries with 4D-sourced data via AJAX/JSON remains a completely valid general pattern, and Google Charts itself is still available today. However, the specific 4D-side implementation shown here — manually concatenating JSON text piece by piece and using 4D Web Server's basic request-handling model to build the response by hand — has been substantially superseded by 4D's later native JSON commands (`JSON Stringify`/`JSON Parse`) and, more broadly, by 4D's built-in REST server (built on ORDA), which now provides structured JSON data endpoints without hand-rolled AJAX plumbing. The Firebug-based debugging workflow is also obsolete, since Firebug was discontinued years ago in favor of built-in browser developer tools.
