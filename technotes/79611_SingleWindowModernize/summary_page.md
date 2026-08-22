# Tech Note 24-14: Single Window App – Modernize your application

**Author:** Thomas Maul, 4D Germany.
**Published:** December 23, 2024 | **Product/Version:** 4D v20 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79611
**Download:** https://kb.4d.com/DLTN/TN/2024/24-14_SingleWindowModernize.pdf

## Proposition
Classic 4D applications that open a new process/window on every double-click impose heavy network and server load, especially over slow or remote connections. This note shows how to modernize such an application — using the 20-year-old 4D Invoice demo as a real example — into a modern, single-window, Outlook-style UI with minimal rewriting, while measurably reducing network traffic.

## Key Points
- **Resizable, customizable ribbon toolbar:** The cs.Toolbar/cs.Toolbar_Button classes automatically shrink buttons (full → icon-only → stacked) as window width changes, with a Setup dialog letting end users drag/reposition/hide buttons, persisted in Buttons.json/Default.json/User.json.
- **Generic ORDA list box:** The ORDA_Listbox class dynamically binds table and column expressions at runtime, letting users add/remove/reorder/resize columns and includes aliases and computed attributes, not just real fields.
- **Preview pane replaces double-click windows:** A click (not double-click) shows record details inline via a sub form, driven by an On Selection Change handler that checks touchedAttributes() on the previously selected entity before switching.
- **Optimistic locking conflict handling:** save(dk auto merge) status codes (automerge failed, locked) drive user prompts to retry, wait, or cancel when another user modified the record concurrently.
- **Generic-with-override pattern:** Class functions like useAll() or quickSearch() are checked for existence per table (`If ($class.useAll#Null)`) so default logic applies unless a table defines its own override — avoiding large case-of blocks.
- **EXECUTE METHOD IN SUBFORM for correct context:** Preview pane initialization code must run via EXECUTE METHOD IN SUBFORM to execute in the sub form's own context.
- **Measured ORDA network efficiency:** A logged comparison shows classic double-click browsing using 124 packets (11KB out/14KB in) versus the single-window ORDA approach using only 50 packets (92KB out/6KB in) due to ORDA's upfront data batching/caching.
- **"local" function keyword for further optimization:** Prefixing a class function with "local" avoids a server round-trip entirely when all needed data is already available client-side.

## Featured Technology
- **4D Classes (Toolbar, Toolbar_Button)** — reusable, resizable ribbon toolbar with button/subform/search-box support.
- **ORDA_Listbox class** — generic dynamic list box binding to any ORDA dataclass/entity selection.
- **ORDA EntitySelection / DataClass** — underlying data access layer for list and preview binding.
- **Sub forms & EXECUTE METHOD IN SUBFORM** — used for the dynamic toolbar and preview area panels.
- **ORDA REST request logging (ORDARequests.json / 4DRequestsLogServer)** — used to analyze and optimize network traffic.

## Best Practices Highlighted
1. Use the generic-with-override class function pattern (e.g., useAll/quickSearch) instead of large per-table case statements.
2. Always run sub form initialization code via EXECUTE METHOD IN SUBFORM to ensure correct form context.
3. Mark class functions "local" when they don't need server-side data, to eliminate unnecessary REST round-trips.
4. Migrate only the frequently used workflows to ORDA/single-window first, leaving rarely used classic-mode features unchanged to limit rewrite scope.

## Context / Positioning
Published as 4D continued pushing ORDA and class-based architecture as the modern default (post-20 R2–R5 language features), this note exemplifies 4D's broader "modernize incrementally" narrative — encouraging developers to retrofit decades-old classic-mode applications with contemporary, network-efficient, Outlook-like UX patterns rather than requiring a full rewrite.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
