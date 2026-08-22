# Tech Note 99-53: Building Interactive Graphic Interfaces with 4D Draw, Part III

**Author:** Tim Tonooka, ACI Technical Support
**Published:** December 1, 1999 | **Product/Version:** 4D Draw v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11862
**Download:** https://kb.4d.com/DLTN/TN/1999/Windows/TN_1999_51-55_(DEC)/99-53_Graphic_Interfaces_3.exe

## Overview
Part III of the interactive graphic interfaces series focuses on reading pixel data from BMP images displayed in 4D Draw areas. It provides detailed code walkthroughs of the "Image Data" page of the "BMP Picture Properties" window in the v65Trace example database, where users can click on any pixel to view its coordinate and color information.

## Key Points
- **4D Draw area configuration:** Uses DR EXPERT COMMAND to disable drawing tools while keeping zoom controls, DR SET HANDLE STATE to hide selection handles, and DR EVENT FILTER for Ctrl/Cmd-click event detection
- **Pixel click detection:** DR LAST CLICK returns coordinates relative to the origin point, independent of zoom level or scroll position
- **Cursor management:** A custom cursor object (dotted rectangle) is drawn over clicked pixels, supporting draw/move/toggle operations with optimized screen updates via DR SET UPDATE MODE
- **BMP pixel data extraction:** Calculates pixel addresses in BLOB storage accounting for BMP row padding, reads color palette entries (RGB values) from the BMP header
- **Lazy page initialization:** Tab control tracks which pages have been displayed, deferring setup code for pages 2 and 3 until first visit
- **Code organization:** Extensive use of local variables with meaningful names, helper methods for reusability (DRW_PointsInBaseUnitF, NUM_RangeRestrictF, DRW_TraceCursorRadiusStdF)
- **Background layer usage:** BMP image placed in background layer to prevent user manipulation while remaining visible and clickable for coordinate detection

## Featured Technology
- 4D Draw (DR EVENT FILTER, DR LAST CLICK, DR EXPERT COMMAND, DR EXPERT MODE, DR SET HANDLE STATE, DR SET UPDATE MODE, DR SCALE, DR MOVE, DR Draw rectangle, DR SET NAME, DR ADD TO BACKGROUND, DR PLACE PICTURE, DR REDRAW, DR SCROLL DOCUMENT, DR SET DISPLAY, DR SET PREFERENCES, DR GET AREA BOUNDARY, DR SET RULER, DR SET LINE ATTRIBUTES, DR SET FILL ATTRIBUTES)
- BLOB operations (BLOB to longint, BLOB size, SET BLOB SIZE)
- ACI_Pack (AP Read picture BLOB)
- BMP file format (pixel addressing, color palette, row padding)
- Multi-page dialog forms with tab controls

## Historical Context
**Status:** Obsolete

4D Draw has been discontinued, along with the ACI_Pack plug-in referenced throughout. The level of manual low-level programming demonstrated—calculating pixel addresses in BMP files via BLOB operations, manually managing cursor objects, configuring expert modes—showcases the ingenuity and complexity required before modern image APIs existed. Today, comparable interactive pixel-inspection functionality would be built using HTML Canvas or WebGL in a 4D Web Area, with image data accessed via standard JavaScript APIs. Despite its obsolescence, Tim Tonooka's meticulous code organization and documentation style remains exemplary.
