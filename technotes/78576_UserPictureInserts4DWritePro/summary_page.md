# Tech Note 20-19: Handling User Picture Inserts Into 4D Write Pro

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** October 26, 2020 | **Product/Version:** 4D Write Pro v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78576
**Download:** https://kb.4d.com/DLTN/TN/2020/20-19_4DWPUserPict.zip

## Proposition
By default, 4D Write Pro always inserts a user-dragged or pasted image as an in-line picture, with no way to ask whether the user wants a background or anchored image instead. This Tech Note explains 4D Write Pro's three picture types and demonstrates how to intercept drag-and-drop and paste actions to give the developer full control over how a user-inserted image is placed.

## Key Points
- **Background pictures**: document-level attributes (`wk background image`, `wk background repeat`, etc.) set/read via `WP SET ATTRIBUTES`/`WP GET ATTRIBUTES`.
- **In-line pictures**: behave like a text character, inserted with `WP INSERT PICTURE` on a Write Pro range/cursor position.
- **Anchored pictures**: the most flexible type, positioned absolutely with `WP Add picture` and attributes like `wk anchor origin`, `wk anchor horizontal align`, and `wk anchor layout` (for text-relative stacking order).
- **Custom drop handling**: set the Write Pro area's "Droppable" property to Custom and enable `On Drop` to inspect pasteboard contents via the Pasteboard command theme before deciding how to insert an image.
- **No native paste event**: paste must be detected via `On Before Keystroke`, checking for the Cmd+V/Ctrl+V shortcut with modifier-key detection plus `Keystroke`.
- **Contextual menu paste is the hardest case**: since the built-in right-click menu isn't customizable, the workaround uses `On After Edit` to detect and replace an automatically-inserted picture.
- **Source-dependent pasteboard structure**: images copied from Word, a browser, or a file each populate the pasteboard differently, requiring source-aware handling.

## Featured Technology
- 4D Write Pro picture model (background / in-line / anchored)
- WP SET ATTRIBUTES / WP GET ATTRIBUTES
- WP INSERT PICTURE / WP Add picture
- On Drop, On Before Keystroke, On After Edit form events
- Pasteboard command theme

## Best Practices Highlighted
1. Disable automatic drop handling ("Droppable" = Custom) whenever the app needs non-default image placement behavior.
2. Inspect pasteboard contents before committing to an insertion strategy, since different source applications populate the pasteboard differently.
3. Prefer an explicit user dialog for ambiguous cases (background vs. anchored vs. in-line) rather than guessing intent.

## Context / Positioning
This note is part of 4D's ongoing investment in 4D Write Pro as its modern, HTML/CSS-based word-processing engine (the successor to classic 4D Write), showing developers how to build polished, Word-like document editing experiences — including nuanced image handling — entirely within a 4D Write Pro area, reinforcing 4D Write Pro's suitability for building rich document-generation and editing features natively in 4D applications.

## Historical Commentary
**Status:** Still relevant

4D Write Pro remains 4D's current, actively developed word-processing technology (having long since superseded classic 4D Write), so the picture model and attribute-based commands (`WP SET ATTRIBUTES`, `WP INSERT PICTURE`, `WP Add picture`) documented here are still accurate and in active use today. The workaround nature of the paste-handling technique — using `On Before Keystroke` because there is no native "on paste" event, and the more convoluted `On After Edit` trick for contextual-menu pastes — appears to still reflect a real gap in the 4D Write Pro area's event model; developers should verify against current documentation whether a dedicated paste event has since been added, but absent that, this technique remains a valid and commonly used approach.
