# Tech Note 11-17: Grid Layout with SVG

**Author:** Jesse Piña, Technical Services Team Member, 4D Inc.
**Published:** May 27, 2011 | **Product/Version:** 4D v12.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76343
**Download:** https://kb.4d.com/DLTN/TN/2011/11-17_Grid_Layout_with_SVG.zip

## Proposition
This Tech Note introduces a dedicated Grid Layout component, built on 4D's SVG engine, that lets developers display data in a tiled grid arrangement rather than the traditional row-based list, driven entirely by array inputs and rendered to a picture object.

## Key Points
- **What grid layouts are:** an alternative to row-based output, defined and motivated with typical use cases.
- **Component API:** documents GL_Attribute_Get, GL_Attribute_Set, GL_DrawGrid_Image, GL_DrawGrid_Text, GL_Error_Get, GL_Initialize, GL_Template_Create, GL_Template_Delete, and GL_Template_GetNames.
- **Array-driven design:** inputs are arrays (including an ID array with attributes); output is a single rendered picture.
- **Usage mechanics:** installation, picture object sizing/scaling, picture format options, and context menu behavior.
- **Five worked demos:** text, images, interactive events, attributes, and templates.
- **Suggested extensions:** pagination, mixed text/image grids, and per-piece text styling as next steps.

## Featured Technology
- 4D SVG-based Grid Layout component (GL_ command set)
- Array-driven grid templates for text and image display
- Picture-object-based grid rendering with context menus

## Context / Positioning
Published in mid-2011 for 4D v12.2, this note showcased a creative use of the (then actively promoted) 4D SVG component to deliver a modern, visually distinctive grid-tile UI pattern that was not otherwise available out of the box in 4D at the time.

## Historical Commentary
**Status:** Obsolete

The grid-layout-as-alternative-to-rows concept remains a valid UI pattern, but this note's implementation is entirely built on the now-legacy 4D SVG component and its GL_ custom component API, rendering output into a static picture object rather than any modern interactive layout mechanism.

Building a grid layout in 4D today would be done far more simply using a list box in grid/tile mode, CSS Grid/Flexbox inside a web area, or 4D View Pro, making the specific component and technique here obsolete despite the underlying UX idea staying sound.
