# Tech Note 10-23: Editing SVG Pictures in 4D v12

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** July 26, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76140
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_21-24_(JUL)/10-23_Editing_SVG_Pictures.zip

## Proposition
Tom Fitch's Tech Note details a major upgrade to 4D's SVG support introduced in v12: the ability to adjust SVG images on the fly by directly manipulating the underlying SVG document's elements, rather than the older workflow of regenerating and re-rendering an entire SVG document as a static image whenever something changed.

## Key Points
- 4D v12 introduces commands to edit a live SVG document rather than regenerate a static SVG image
- Clarifies the distinction between an SVG Image (rendered) and an SVG Document (editable structure)
- Demonstrates organizing SVG content with groups and element IDs for targeted manipulation
- Covers resizing, hiding/showing, moving, and changing text of individual SVG elements
- Shows wiring SVG images to respond to user events for interactivity

## Featured Technology
- 4D v12 SVG commands
- SVG groups and element IDs
- dynamic SVG element manipulation (resize, hide/show, move, text)
- SVG image vs SVG document

## Best Practices Highlighted
- Assign explicit element IDs to SVG parts you intend to manipulate programmatically
- Edit the live SVG document in place instead of regenerating the whole document for incremental changes

## Context/Positioning
Published as 4D v12 significantly extended its SVG capabilities, giving developers a much more efficient way to build dynamic, interactive vector graphics than the prior regenerate-and-redraw approach.

## Historical Commentary
**Status:** Still Relevant

This note showcases 4D v12's new ability to modify a live SVG document in place (rather than re-rendering a static SVG image), using SVG groups, element IDs, and per-element attribute manipulation for resizing, showing/hiding, moving, and text changes. This SVG-editing API remains functional in current 4D thanks to backward compatibility and is still a valid technique for building dynamic vector UIs, though for many new projects a modern 4D form with CSS styling or a web/Qodly front-end would now be a more idiomatic first choice for similarly dynamic interfaces.
