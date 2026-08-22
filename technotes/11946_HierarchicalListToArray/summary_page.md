# Tech Note: The Hierarchical LIST TO ARRAY Command

**Author:** Not specified in source document
**Published:** January 1, 2000 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11946
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a workaround technique that copies an entire hierarchical list, including all nested levels, into a string array — something the built-in LIST TO ARRAY command could not do on its own.

## Key Points
- Specifically, LIST TO ARRAY would only copy the first-level (top) items from a hierarchical list into an array, silently dropping any nested child items, while ARRAY TO LIST could only construct a flat, non-hierarchical list rather than rebuilding a full hierarchy from array data.
- The note's proposition is to supply a custom method that copies an entire hierarchical list — including every nested level, not just the top — into a string array, effectively recursively flattening the tree structure into a linear representation while still preserving enough information (presumably indentation level or parent/child markers) to reconstruct or at least meaningfully print the original hierarchy.
- An accompanying example demonstrates printing the resulting flattened array, giving developers a concrete illustration of how the technique can be applied to output a full hierarchical list to a report or list view.
- Featured technology is squarely 4D's hierarchical list command set (LIST TO ARRAY, ARRAY TO LIST, and the broader hierarchical list command family referenced but not detailed in the surviving teaser) alongside a custom recursive-walk technique implemented in classic 4D code.
- This kind of note exemplifies how the 4D Technical Notes series regularly supplied targeted workarounds for specific command-level gaps soon after a major new feature (hierarchical lists) shipped in a given version, helping developers work around a known limitation before (or in case) the underlying commands were later improved.
- It pairs naturally with the companion introductory note on hierarchical list basics from the same era, together forming a small but complete practical guide to 4D v6's hierarchical list feature.

## Featured Technology
- Hierarchical lists
- LIST TO ARRAY / ARRAY TO LIST commands
- List Editor
- Custom list-flattening technique

## Historical Context
This note documents a workaround for a specific limitation in 4D v6's hierarchical list commands: LIST TO ARRAY only captured the first level of a hierarchical list and ARRAY TO LIST could only rebuild a flat list, so the note supplies custom code to fully flatten a multi-level hierarchical list into a string array (with a printing example). This exact gap has very likely been addressed by improvements to 4D's hierarchical list commands in the many releases since v6, making the specific workaround largely of historical interest, though the general technique of recursively walking a hierarchical structure into a flat representation remains a broadly useful programming pattern. Related updates since: 4D's hierarchical list command set has been extended and improved across many releases since v6, likely closing much of the specific LIST TO ARRAY/ARRAY TO LIST limitation described here; The general recursive-flattening technique for nested/tree data remains a standard programming pattern applicable well beyond this specific 4D command limitation. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
