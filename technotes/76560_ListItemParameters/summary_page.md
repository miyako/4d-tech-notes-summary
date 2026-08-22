# Tech Note 12-09: Practical Uses for List Item Parameters

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** April 29, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76560
**Download:** https://kb.4d.com/DLTN/TN/2012/12-09_ListItemParameters.zip

## Proposition
This Tech Note introduces and demonstrates 4D v13's new GET LIST ITEM PARAMETER ARRAYS command, which lets developers enumerate and retrieve all metadata parameters attached to a hierarchical list item in one call.

## Key Points
- List items have carried String/Boolean/Long Integer "parameters" (metadata) since 4D v11 SQL via SET/GET LIST ITEM PARAMETER, but names had to be known in advance to retrieve values.
- The new GET LIST ITEM PARAMETER ARRAYS command retrieves all parameter names (and optionally values) for a list item in a single call.
- Documents the command's five-parameter syntax, including the object-name-vs-reference selector and output arrays.
- Sample database demonstrates the command across a List Editor, Countries demo, Countries Maps demo, Countries Smart Searches demo, Settings demo, Test Routines, and Web Searches demo.
- Emphasizes practical, varied use cases for parameter-driven metadata on hierarchical list items.

## Featured Technology
- GET LIST ITEM PARAMETER ARRAYS (new command)
- SET LIST ITEM PARAMETER / GET LIST ITEM PARAMETER
- 4D hierarchical lists
- Typed list item metadata (String, Boolean, Long Integer)

## Best Practices Highlighted
1. Use list item parameters to attach lightweight, typed metadata to hierarchical list entries rather than maintaining parallel lookup structures.
2. Enumerate parameter names dynamically with the new array command instead of hard-coding known parameter names.
3. Build reusable list editors that can introspect and display arbitrary item parameters.

## Context/Positioning
Published for 4D v13.0 in 2012, this note documents a small but practical API improvement that removed friction from an existing but underused 4D list feature.

## Historical Commentary
4D hierarchical lists and their parameter API remain part of the current classic language and this command still works as documented, so the technique is directly still relevant for applications already using hierarchical lists. That said, many modern 4D applications now store richer per-item metadata in objects/collections rather than typed list-item parameters, and data-driven lists more often pull from ORDA entity selections, making this approach somewhat less central to new development than it was in 2012.

**Status:** Still relevant
