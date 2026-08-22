# Tech Note 06-05: Rich Internet Clients – First Steps with AJAX

**Author:** Thomas Maul, General Manager, 4D Germany.
**Published:** February 3, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41677
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_05-08_(FEB)/06-05_Rich_Internet_Clients.zip

## Overview
4D's first Tech Note introducing Ajax (Asynchronous JavaScript and XML) to 4D developers, teaching the basic building blocks (JavaScript/DOM, XMLHttpRequest) and showing how to combine them with a 4D Web server backend to build responsive, desktop-like web UIs.

## Key Points
- Motivates Ajax with contemporary examples (Google Mail, Google Suggest, Flickr) and defines it per Wikipedia's XHTML/CSS + DOM + XMLHttpRequest formulation.
- Demo database (based on "Video Library" sample) showcases a Type Ahead actor-search autocomplete and a scrollable "Live Grid," both updating without full page reloads or URL changes; recommends Firefox's "Live HTTP Headers" extension for observing traffic.
- A JavaScript primer covers DOM element IDs and `onChange` handlers, explicitly comparing them to 4D's "On Data Change" object-method event.
- Covers XMLHttpRequest's browser history (Microsoft ActiveX origin, then native implementations in Mozilla, Safari, Opera) and shows a cross-browser detection snippet.
- The "Simple Ajax" example wires a JavaScript `ContentLoader` object to a 4D `/4DAction/` method that reads `$1` and replies via `SEND HTML TEXT`.
- Identifies a real gotcha: browser caching can return stale Ajax responses; shows two fixes — POSTing as an HTML form (read with `GET WEB FORM VARIABLES`) or setting HTTP cache-expiry headers.
- Begins a deeper walkthrough of a "Double Combo Box" example to illustrate reusable, generic Ajax client-side code.

## Featured Technology
- Ajax (Asynchronous JavaScript and XML)
- XMLHttpRequest object
- 4D Web Server and `4DAction` URL routing
- `GET WEB FORM VARIABLES` / `SEND HTML TEXT` 4D language commands
- JavaScript DOM manipulation
- Type Ahead and Live Grid UI patterns

## Historical Context
Written in February 2006, this note captures the very beginning of the Ajax/"Web 2.0" wave for 4D developers, a year before 4D's own native SQL engine (v11, 2007) and well over a decade before Project Mode or ORDA. The core Ajax concept (asynchronous XMLHttpRequest-driven DOM updates) remains foundational to how the web works today, but the specific implementation patterns shown — hand-rolled cross-browser XHR detection, raw `4DAction` URL dispatch, and manual cache-busting tricks — were later abstracted away by native `fetch`/XHR wrappers, modern JavaScript frameworks, and 4D's own subsequent Ajax framework (4DAF/A4D), itself since superseded by more modern 4D web tooling.

## Status
**Superseded** — the Ajax concept endures, but the specific techniques and tooling shown have been replaced by modern JS frameworks and later 4D web technologies.
