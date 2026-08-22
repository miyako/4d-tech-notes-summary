# Tech Note 11-10: Hierarchical List Boxes

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** April 1, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76295
**Download:** https://kb.4d.com/DLTN/TN/2011/11-10_Hierarchical_List_Boxes.zip

## Proposition
This note comprehensively documents 4D v12's newly introduced hierarchical list box feature, which lets developers group related rows together in a more intuitive, expandable/collapsible tree-like structure instead of a flat data grid. It explains what a hierarchical list box is and its use cases (grouped data values and data usage patterns), then covers two creation paths — via the Form Editor's property list and contextual menu, and entirely programmatically — followed by management topics: sorting hierarchical list boxes, working with hierarchical list box cell position, and expanding/collapsing break levels. A full demo database accompanies the write-up, illustrating every technique covered.

## Key Points
- Introduces 4D v12's hierarchical list box as a new alternative to the traditional flat-grid list box for grouped/nested data display.
- Explains typical data values and data usage patterns suited to hierarchical grouping.
- Shows Form Editor-based creation using the property list and contextual menu.
- Shows fully programmatic creation of hierarchical list boxes.
- Covers sorting behavior specific to hierarchical list boxes.
- Covers cell position management and expanding/collapsing break levels programmatically.
- Includes a complete demo database covering all techniques.

## Featured Technology
- 4D v12 hierarchical list box (new form object type)
- Form Editor property list and contextual menu for list box configuration
- Programmatic creation and management (sorting, break levels, cell position) of hierarchical list boxes

## Best Practices Highlighted
- Choose hierarchical list boxes when data has a natural grouping/break-level structure rather than emulating grouping with flat rows
- Use programmatic creation when list box structure must adapt dynamically at runtime

## Context / Positioning
Published just after 4D v12 introduced hierarchical list boxes as a headline new UI feature, this note served as the definitive early reference for developers adopting the feature for grouped data presentation.

## Historical Commentary
**Status:** Still Relevant

Classic array/object-based hierarchical list boxes described here still exist and function in current 4D, so the note remains a valid reference for that specific form-object type. That said, 4D has since introduced object/collection and entity-selection-based list boxes tied to ORDA, which offer a more modern, less manually-managed way to bind hierarchical/grouped data to list boxes, making some of the manual break-level/sort management described here less necessary for new ORDA-based projects.
