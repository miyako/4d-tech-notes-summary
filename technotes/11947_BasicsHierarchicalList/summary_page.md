# Tech Note: The Basics of Creating a Hierarchical List

**Author:** Not specified in source document
**Published:** February 1, 2000 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11947
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers an introduction to hierarchical lists, a v6+ enhancement to 4D's classic list feature that supports parent/child/sibling relationships between string items.

## Key Points
- Where a classic list simply held a series of strings, hierarchical lists let those strings relate to one another as parent, child, or sibling — described using the example of "Waffles" being a child of "Breakfast" and a sibling of "Pancakes" — mirroring the kind of indented, expandable outline structure everyone is familiar with from file-system browsers like the Mac OS Finder or Windows Explorer.
- The note's proposition is a straightforward feature introduction: explaining the conceptual model of parent/child/sibling relationships within a single list object, and noting that this structure can be displayed to users either as a dedicated hierarchical list form object or as a hierarchical pop-up menu form object, giving developers flexibility in how the outline data is surfaced in the interface.
- Featured technology centers on 4D's hierarchical list data type and its supporting form objects, positioning this note as foundational reading before diving into more advanced hierarchical-list topics (such as the companion note in this same era covering the LIST TO ARRAY command's limitations with hierarchical data).
- Because only the brief teaser text survives in this archive, deeper implementation details (specific commands for building and editing hierarchical lists programmatically) are not preserved here, but the introductory framing and analogy to familiar file-browser interfaces make the core concept clear.
- This kind of structured, self-relating list object was a meaningful interface capability for 4D applications needing to present categorized or nested data — such as product catalogs, organizational charts, or navigation trees — directly through the forms engine rather than requiring custom-built outline widgets.

## Featured Technology
- Hierarchical lists (v6+)
- List Editor
- Hierarchical list form objects
- Hierarchical pop-up menus

## Historical Context
This note introduces hierarchical lists, a 4D v6 enhancement to the classic list object that let string items form parent/child/sibling relationships (like a file-system outline view), displayable as a hierarchical list form object or hierarchical pop-up menu. The hierarchical list feature and its associated commands remain part of the current 4D language essentially unchanged in concept, so this note's fundamentals are still directly applicable, though modern UI patterns increasingly favor list boxes, tree-style list box components, or web-based tree views for equivalent outline-style presentation. Related updates since: Hierarchical lists and their associated commands remain part of the current 4D language, largely unchanged in concept since v6; List box objects (including tree-structured list box display) and web-based UI have become common modern alternatives to hierarchical list form objects for outline-style presentation. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
